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


def imwrite(filename, image):
    '''Save a NetPBM image to a file.

    Parameters
    ----------
    filename : str
        image file name
    image : numpy.ndarray
        image being saved
    '''
    raise NotImplementedError('Implement this function/method.')
