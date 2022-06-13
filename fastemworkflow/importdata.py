from tifffile import TiffWriter
import os
import re
from tqdm.notebook import tqdm

def create_mipmaps(tiff, dir_out, metadata):
    """Create mipmaps from multi-page tiff
    
    Parameters
    ----------
    tiff : np.array
        Numpy array with EM image data
    dir_out: PosixPath
        Path of directory to save mipmap
    metadata: str
        Metadata of EM image

    Returns
    -------
    Nothing (Image is written to target folder)"""
    
    # Unpack pages
    for i, page in enumerate(tiff.pages):
        # Grayscale uint16 image
        image = page.asarray()
        # Write tiff
        fp = dir_out / f"{i}.tif"
        with TiffWriter(fp.as_posix()) as tif:
            tif.write(image, metadata=metadata)
            
def generate_mipmaps_from_sections(dir_sections, 
                                   stack_name):
    """Generate mipmaps from all section directories

    Parameters
    ----------
    dir_sections : list
        List of PosixPaths to section directories on disk
    stack_name : 
        Name of stack to be processed

    Returns
    -------
    Nothing (folders are generated with the respective mipmaps for every image in every section)"""
    
    # Loop through section directories
    for z, dir_section in tqdm(enumerate(dir_sections),
                           total=len(dir_sections)):

    # Loop through tiffs in each section
        for fp in tqdm(list(dir_section.glob('[0-9]*_[0-9]*_0.tiff'))):

            # Read tiff
            tiff = TiffFile(fp)
            # Extract metadata
            metadata = {tag.name: tag.value for tag in tiff.pages[0].tags}
            # Infer row, col
            row, col = [int(i) for i in re.findall(r'\d+', fp.stem)][:2]

            # Set directory to output mipmaps
            dir_mipmaps = dir_project / stack_name / dir_section.name / f"{row:03d}_{col:03d}"
            dir_mipmaps.mkdir(parents=True, exist_ok=True)
            # Create mipmaps
            create_mipmaps(tiff, dir_mipmaps, metadata)    

