import pyfar as pf
import imkar as ik
import numpy as np
import sofar as sf
import os
import mesh2scattering as m2s


def calculate_scattering(folder):
    """read pattern data ``sample.pattern.sofa`` and ``reference.pattern.sofa``
    and calculate and export the scattering coefficient for each incident angle
    to ``project_name.scattering.sofa``, then random incidence scattering
    coefficient is calculated and is saved in
    ``project_name.scattering_rand.sofa``

    Parameters
    ----------
    folder : str, path
        root directory of the project, this folder need to contain the above
        mentioned sofa files.
    """
    project_name = os.path.split(folder)[-1]
    data, source_coordinates, receiver_coorinates = pf.io.read_sofa(
        os.path.join(folder, 'sample.pattern.sofa'))
    data_ref, source_coords_ref, receiver_coords_ref = pf.io.read_sofa(
        os.path.join(folder, 'reference.pattern.sofa'))
    data, source_coordinates_, receiver_coorinates_ = _reshape_data(
        data, source_coordinates, receiver_coorinates)
    data_ref, source_coords_ref_, receiver_coords_ref_ = _reshape_data(
        data_ref, source_coords_ref, receiver_coords_ref)

    s = ik.scattering.coefficient.freefield(
        data, data_ref, receiver_coords_ref_)

    s_rand = ik.scattering.coefficient.random_incidence(
        s, source_coords_ref_)

    xyz = source_coordinates.get_cart()
    index, _ = source_coords_ref_.find_nearest_k(
        xyz[..., 0], xyz[..., 1], xyz[..., 2])
    shape = np.array(list(s.freq.shape[1:]))
    shape[0] *= s.freq.shape[0]
    s.freq = s.freq.reshape(shape)
    s = s[index]
    shape = np.insert(np.array(list(s.freq.shape)), 1, 1)
    s.freq = s.freq.reshape(shape)

    sofa = m2s.utils._get_sofa_object(
        s.freq,
        source_coordinates.get_cart(),
        np.array([0, 0, 0]),
        m2s.__version__,
        frequencies=s.frequencies)

    # write scattering coefficient data to SOFA file
    sf.write_sofa(os.path.join(
        folder, f'{project_name}.scattering.sofa'), sofa)

    sofa = m2s.utils._get_sofa_object(
        s_rand.freq.reshape(1, 1, len(s.frequencies)),
        np.array([0, 0, 0]),
        np.array([0, 0, 0]),
        m2s.__version__,
        frequencies=s.frequencies)

    # write random scattering coefficient data to SOFA file
    sf.write_sofa(os.path.join(
        folder, f'{project_name}.scattering_rand.sofa'), sofa)


def _reshape_data(data, source_coordinates, receiver_coorinates):
    sources_sph = source_coordinates.get_sph(unit='deg')
    source_phi = np.sort(np.array(list(set(np.round(sources_sph[:, 0], 5)))))
    source_theta = np.sort(np.array(list(set(np.round(sources_sph[:, 1], 5)))))
    sources = _angles2coords(
        source_phi, source_theta, np.mean(sources_sph[:, 2]), unit='deg')

    receiver_sph = receiver_coorinates.get_sph(unit='deg')
    receiver_phi = np.sort(
        np.array(list(set(np.round(receiver_sph[:, 0], 5)))))
    receiver_phi = np.append(receiver_phi, 0)
    receiver_theta = np.sort(
        np.array(list(set(np.round(receiver_sph[:, 1], 5)))))
    receiver = _angles2coords(
        receiver_phi, receiver_theta, np.mean(receiver_sph[:, 2]), unit='deg')

    if source_coordinates.cshape != sources.cshape:
        caxe = 2
        data = _reshape_to_az_by_el(data, source_coordinates, sources)
    else:
        caxe = 1
    data = _reshape_to_az_by_el(data, receiver_coorinates, receiver, caxe)

    return data, sources, receiver


def _angles2coords(
        azimuth, colatitude,
        radius: float = 1., unit='rad') -> pf.Coordinates:
    """
    ``data.cshape`` fits the cshape of ```coords``. Data get shifed throght
    the ``coords`` Object around azimuth by ``shift_azimuth``.
    """
    azimuth = np.array(azimuth)
    colatitude = np.array(colatitude)
    if unit == 'deg':
        azimuth = azimuth * np.pi / 180.
        colatitude = colatitude * np.pi / 180.
    elif unit != 'rad':
        raise TypeError("Unknown Unit")
    phi, theta = np.meshgrid(azimuth, colatitude, indexing='ij')
    return pf.Coordinates(
        phi, theta, np.ones(phi.shape)*radius, 'sph')


def _reshape_to_az_by_el(
        data: pf.FrequencyData, coords_in: pf.Coordinates,
        coords_out: pf.Coordinates, cdim: int = 0) -> (pf.FrequencyData):
    if coords_in.cshape == coords_out.cshape:
        return data
    if cdim > 0:
        data.freq = np.moveaxis(data.freq, cdim, 0)
    freq_shape = list(coords_out.cshape)
    if len(data.cshape) > 1:
        for dim in data.cshape[1:]:
            freq_shape.append(dim)
    freq_shape.append(data.n_bins)
    freq = np.zeros(freq_shape, dtype=complex)
    data_in = data.freq
    xyz = coords_out.get_cart()
    index, _ = coords_in.find_nearest_k(xyz[..., 0], xyz[..., 1], xyz[..., 2])
    for iaz in range(coords_out.cshape[0]):
        res_data = data_in[index[iaz, :], ...]
        freq[iaz, ...] = res_data
    if cdim > 0:
        freq = np.moveaxis(freq, 0, cdim+1)
        freq = np.moveaxis(freq, 0, cdim+1)
    data_out = pf.FrequencyData(freq, data.frequencies)
    return data_out
