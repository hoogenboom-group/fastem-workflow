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
        
    # Check if MipMaps have already been generated
    # List output dirs and all files for processing
    dir_output = dir_project / stack_name / dir_section.name
    output_dirs = list(os.listdir(dir_output))
    files = list(dir_section.glob('[0-9]*_[0-9]*_0.tiff')) # List all files
    
    # Loop over all output_dirs and find processed files
    processed_files = []
    for output_dir in output_dirs:
        processed_file = dir_section / f'{output_dir}_0.tiff' 
        processed_files.append(processed_file)
        
    # Files to process are files not in processed files list
    files_to_process = [file for file in files if file not in processed_files]  
    
    # If empty, go to next section
    if not files_to_process:
        print(f'Mipmaps for {dir_section.name} already exist, skipping to next section')
                      
    # Loop through tiffs to process in each section
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

