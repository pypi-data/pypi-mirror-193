"""
sentinel_values provides methods for converting
a spectral distribution to sentinel responses.
"""

from collections import namedtuple

import colour
import numpy as np

from sentinel_toolkit.colorimetry.illuminants import D65_360_830_1NM_DISTRIBUTION
from sentinel_toolkit.colorimetry.illuminants.d65 import D65_360_830_1NM_VALUES

SpectralData = namedtuple("SpectralData", "wavelengths spectral_responses")


def sd_to_sentinel_colour(spectral_distribution,
                          s2_srf,
                          s2_srf_options,
                          illuminant=None):
    """
    Converts a spectral distribution to Sentinel-2 responses.

    Parameters
    ----------
    spectral_distribution : colour.SpectralDistribution
        The spectral distribution to convert.
    s2_srf : sentinel_toolkit.S2Srf
        The Sentinel-2 spectral response functions.
    s2_srf_options : S2SrfOptions
        The satellite, band names and wavelength range.
        If satellite is missing, satellite 'A' will be used.
        If band names are missing, all band names will be used.
        If wavelength range is missing, (360, 830) will be used.
    illuminant : colour.SpectralDistribution
        The illuminant to apply.
        If missing, default to D65 360-830 nm.

    Returns
    -------
    output : ndarray
        The Sentinel-2 spectral responses.
    """
    bands_responses = s2_srf.get_bands_responses(s2_srf_options)
    return sd_to_sentinel_direct_colour(spectral_distribution, bands_responses, illuminant)


def sd_to_sentinel_direct_colour(spectral_distribution, bands_responses, illuminant=None):
    """
    Converts a spectral distribution to Sentinel-2 responses.

    Parameters
    ----------
    spectral_distribution : colour.SpectralDistribution
        The spectral distribution ro convert.
    bands_responses : ndarray
        The bands_responses functions as a 2D ndarray.
    illuminant : colour.SpectralDistribution
        The illuminant to apply.
        If missing, default to D65 360-830 nm.

    Returns
    -------
    output : ndarray
        The Sentinel-2 spectral responses.
    """
    if illuminant is None:
        shape = spectral_distribution.shape
        illuminant = colour.SpectralDistribution(D65_360_830_1NM_DISTRIBUTION).trim(shape)

    row_sum = np.sum(bands_responses, axis=1)
    # Hack for solving division by zero optimally
    row_sum[row_sum == 0] = 1
    bands_srf = bands_responses / row_sum[:, None]

    sd_i = spectral_distribution.values * illuminant.values

    return np.dot(bands_srf, sd_i)


def sd_to_sentinel_numpy(spectral_data,
                         s2_srf,
                         s2_srf_options,
                         illuminant=None):
    """
    Converts a spectral distribution to Sentinel-2 responses.

    Parameters
    ----------
    spectral_data : SpectralData (tuple) of ndarray
        The spectral distribution.
    s2_srf : sentinel_toolkit.S2Srf
        The Sentinel-2 spectral response functions.
    s2_srf_options : S2SrfOptions
        The satellite, band names and wavelength range.
        If satellite is missing, satellite 'A' will be used.
        If band ids are missing, all band ids will be used.
        If wavelength range is missing, (360, 830) will be used.
    illuminant : colour.SpectralDistribution
        The illuminant to apply.
        If missing, default to D65 360-830 nm.

    Returns
    -------
    output : ndarray
        The Sentinel-2 spectral responses.
    """
    bands_responses = s2_srf.get_bands_responses(s2_srf_options)
    return sd_to_sentinel_direct_numpy(spectral_data, bands_responses, illuminant)


def sd_to_sentinel_direct_numpy(spectral_data, bands_responses, illuminant=None):
    """
    Converts a spectral distribution to Sentinel-2 responses.

    Note that currently there is no reshaping, so all the arrays
    should have valid dimensions.

    Parameters
    ----------
    spectral_data : SpectralData (tuple) of ndarray
        The wavelengths and spectral_responses.
    bands_responses : ndarray
        The bands_responses functions as a 2D ndarray.
    illuminant : ndarray
        The illuminant to apply.
        If missing, default to D65 360-830 nm.

    Returns
    -------
    output : ndarray
        The Sentinel-2 spectral responses.
    """
    min_wavelength = int(spectral_data.wavelengths[0])
    max_wavelength = int(spectral_data.wavelengths[-1])

    if illuminant is None:
        illuminant = D65_360_830_1NM_VALUES[min_wavelength - 360: max_wavelength - 359]

    row_sum = np.sum(bands_responses, axis=1)
    # Hack for solving division by zero optimally
    row_sum[row_sum == 0] = 1
    bands_srf = bands_responses / row_sum[:, None]

    sd_i = spectral_data.spectral_responses * illuminant

    return np.dot(bands_srf, sd_i)


def dn_to_sentinel(raw_band_data, nodata_value, boa_offset, quantification_value, solar_irradiance):
    """
    Converts Sentinel-2 DN values to sentinel responses.

    Parameters
    ----------
    nodata_value : int
        The nodata pixel value.
    raw_band_data : ndarray
        The raw sentinel-2 band(s) pixel values.
    boa_offset : int scalar or ndarray
        The boa offset.
    solar_irradiance : float scalar or ndarray
        The solar irradiance.
    quantification_value : int
        The quantification value.

    Returns
    -------
    output : ndarray
        The band data as sentinel response values.

    """
    raw_band_data_copy = np.copy(raw_band_data)
    nodata_indices = raw_band_data_copy == nodata_value
    raw_band_data_copy += boa_offset
    raw_band_data_copy[nodata_indices] = nodata_value

    sentinel_responses = raw_band_data_copy / quantification_value
    sentinel_responses = sentinel_responses * solar_irradiance
    sentinel_responses = np.clip(sentinel_responses, 0, 1, out=sentinel_responses)

    return sentinel_responses * 100.0
