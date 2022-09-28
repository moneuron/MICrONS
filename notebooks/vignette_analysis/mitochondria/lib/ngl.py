IMG_CVPATH = "gs://microns_public_datasets/pinky100_v0/son_of_alignment_v15_rechunked"
SEG_CVPATH = "gs://microns_public_datasets/pinky100_v185/seg"
CLF_CVPATH = "matrix://sseung-archive/pinky100-clefts/mip1_d2_1175k"
MITO_CVPATH = "matrix://sseung-archive/pinky100-mito/seg_191220"
NUC_CVPATH = "matrix://sseung-archive/pinky100-nuclei/seg"

IMG_SOURCE = f"precomputed://{IMG_CVPATH}"
SEG_SOURCE = f"precomputed://{SEG_CVPATH}"
MITO_SOURCE = f"precomputed://{MITO_CVPATH}"
NUC_SOURCE = f"precomputed://{NUC_CVPATH}"
CLF_CVPATH = f"precomputed://{CLF_CVPATH}"
