from tifffile import TiffWriter

def create_mipmaps(tiff, dir_out, metadata):
    """Create mipmaps from multi-page tiff"""
    # Unpack pages
    for i, page in enumerate(tiff.pages):
        # Grayscale uint16 image
        image = page.asarray()
        # Write tiff
        fp = dir_out / f"{i}.tif"
        with TiffWriter(fp.as_posix()) as tif:
            tif.write(image, metadata=metadata)