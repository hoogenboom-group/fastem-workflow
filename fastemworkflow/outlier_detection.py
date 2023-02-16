import numpy as np
from tifffile import TiffFile


def get_med(fps, pct=1):
    """Get median value of given percentile of select images"""
    # Collect percentile values
    ps = []
    # Loop through tiffs
    for fp in fps:
        # Read tiff and extract lowest resolution page from pyramid
        tiff = TiffFile(fp.as_posix())
        image = tiff.pages[-1].asarray()
        # Compute percentile
        p1 = np.percentile(image, pct)
        ps.append(p1)
    # Compute median
    med = np.median(ps)
    return med


def get_mad(fps, med, pct=1):
    """Get median absolute deviation from given percentile of select images

    References
    ----------
    [1] https://en.wikipedia.org/wiki/Median_absolute_deviation
    """
    # Collect absolute deviations
    ads = []
    # Loop through tiffs
    for fp in fps:
        # Read tiff and extract lowest resolution page from pyramid
        tiff = TiffFile(fp.as_posix())
        image = tiff.pages[-1].asarray()
        # Compute absolute deviation
        p1 = np.percentile(image, pct)
        ad = np.abs(p1 - med)
        ads.append(ad)
    # Compute median absolute deviation
    mad = np.median(ads)
    return mad


def has_artefact(image, med, mad, pct=1, a=3):
    """Determine if image contains an artefact based on intensity percentiles

    Parameters
    ----------
    image : array-like
        Input image
    med : float
        Median `pct`-percentile value of megafield
    mad : float
        Median absolute deviation from `pct`-percentile across megafield
    pct : float
        Percentile
    a : float
        Scaling factor for thresholding the deviation from the median
        Increasing `a` will allow for larger deviations

    Returns
    -------
    corrupted : bool
        Whether image has been corrupted by an artefact
    """
    p1 = np.percentile(image, pct)
    corrupted = ((p1 < med - a*mad) | (p1 > med + a*mad))
    return corrupted
