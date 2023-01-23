import numpy as np


def imread(filename):
    '''Load a NetPBM image from a file.

    Parameters
    ----------
    filename : str
        image file name

    Returns
    -------
    numpy.ndarray
        a numpy array with the loaded image

    Raises
    ------
    ValueError
        if the image format is unknown or invalid
    '''
    # Read in the file
    with open(filename, 'rt') as f:
        contents = f.read()
    # Split the file contents into it's constituent tokens.
    tokens = contents.split()
    # checking P2 and P3 formats
    if tokens[0] != ('P2' and 'P3'):
        raise ValueError(f'Unknown format {tokens[0]}')
    # Get the image dimensions.
    width = int(tokens[1])
    height = int(tokens[2])
    maxval = int(tokens[3])
    isP2 = 0 if tokens[0] == "P2" else 3
    # Convert all of the string tokens into integers.
    values = [int(token) for token in tokens[4:]]
    if maxval != 255:
        raise ValueError('Can only support 8-bit images.')
    # Create the numpy array, reshaping it so that it's no longer a linear
    # array.
    image = np.array(values, dtype=np.uint8)
    return np.reshape(image, (height, width, isP2))


"""
def imwrite(filename, image):
    '''Save a NetPBM image to a file.

    Parameters
    ----------
    filename : str
        image file name
    image : numpy.ndarray
        image being saved
    '''
    # Extract the image dimensions and check that it's 8bpc
    if image.ndim == 2:
        height, width = image.shape
        # Convert the image values to strings.
        values = image.astype(str)
        # Construct the file contents.
        rows = [' '.join(row) for row in values]
        header = '\n'.join(['P2', str(width), str(height), "255"])
    elif image.ndim == 3:
        height, width, color = image.shape
        # Convert the image values to strings.
        values = image.astype(str)
        # Construct the file contents.
        rows = [' '.join(row) for row in values]
        header = '\n'.join(['P3', str(width), str(height), "255"])
    if image.dtype != np.uint8:
        raise ValueError('Can only support 8-bit images.')
    data = '\n'.join(rows)
    # Write it to a file.
    with open(filename, 'wt') as f:
        f.write(header)
        f.write('\n')
        f.write(data)
"""


def imwrite(filename, image):
    '''Save a NetPBM image to a file.
    Parameters
    ----------
    filename : str
        image file name
    image : numpy.ndarray
        image being saved
    '''
    # Extract the image dimensions and check that it's 8bpc
    if image.dtype != np.uint8:
        raise ValueError('Can only support 8-bit images.')

    if image.ndim == 2:
        # Monochrome image
        height, width = image.shape
        # Construct the header for PGM format
        header = '\n'.join(['P2', str(width), str(height), "255"])
        # Convert the image values to strings.
        values = image.astype(str)
        # Construct the file contents.
        rows = [' '.join(row) for row in values]
    elif image.ndim == 3:
        # Color image
        height, width, color = image.shape
        # Check if it's RGB
        if color != 3:
            raise ValueError('Only RGB images are supported')
        # Construct the header for PPM format
        header = '\n'.join(['P3', str(width), str(height), "255"])
        # Interleave the channels
        image = image.reshape(height, width * color)
        # Convert the image values to strings.
        values = image.astype(str)
        # Construct the file contents.
        rows = [' '.join(row) for row in values]
    else:
        raise ValueError('Image dimension not supported')

    # Write it to a file.
    with open(filename, 'wt') as f:
        f.write(header)
        f.write('\n')
        for row in rows:
            f.write(row)
            f.write('\n')
