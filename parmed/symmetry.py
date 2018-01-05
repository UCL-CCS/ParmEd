import numpy as np

class Symmetry(object):
    """Symmetry operations

    Parameters
    ----------
    tensor : np.array, shape=(3*n_symmetry, 4)
    """
    def __init__(self, tensor):
        self.data = np.asarray(tensor, dtype='f8')
        if self.data.ndim != 2 or self.data.shape[1] != 4:
            raise ValueError('Tensor shape must be (3*n_symmetry, 4)')


class BioTransform(Symmetry):
    """Biological unit transform

    Parameters
    ----------

    """
    def __init__(self, matrix):
        self.data = np.asarray(matrix, np.float)
        if ((self.data.ndim != 2) or (self.data.shape[0] != 3) or (self.data.shape[1] != 4)):
            raise ValueError('Matrix must be (3, 4)')

    def transform_coords(self, coords):

        coords4 = np.ones((len(coords), 4), dtype=np.float)
        coords4[:, 0:3] = coords

        return coords4.dot(self.data.T)


class BioUnit(object):
    """Biological unit information

    Parameters
    ----------

    """

    def __init__(self, **kwargs):

        self.source = kwargs.get('source', "")
        self.chains = kwargs.get('chains', [])
        self.nmer = kwargs.get('nmer', "")
        self.transforms = kwargs.get('transforms', [])
