import cupy as cp
from cucim.skimage import data, morphology

b = data.binary_blobs(256, n_dim=2)