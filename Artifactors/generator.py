import numpy
import numpy.linalg
import scipy.fft

# https://en.wikipedia.org/wiki/Quantization_(image_processing)
QUANTIZATION_MATRIX = \
    numpy.array(
        [
            [16, 11, 10, 16, 24, 40, 51, 61],
            [12, 12, 14, 19, 26, 58, 60, 55],
            [14, 13, 16, 24, 40, 57, 69, 56],
            [14, 17, 22, 29, 51, 87, 80, 62],
            [18, 22, 37, 56, 68, 109, 103, 77],
            [24, 35, 55, 64, 81, 104, 113, 92],
            [49, 64, 78, 87, 103, 121, 120, 101],
            [72, 92, 95, 98, 112, 100, 103, 99]
        ]
    )

def add_artifacts_with_quantization(image: numpy.ndarray, intensity: float) -> numpy.ndarray:
    
    """Add artifacts with quantization matrix

        Parameters:
            - image : an image
            - intensity : number in [0, 100[

        Returns:
            image with artifacts
    """
    artifacts: numpy.ndarray = numpy.zeros(image.shape)

    # Quality of image
    quality: float = 100-intensity
    # Size of block for processing
    block_size: int = QUANTIZATION_MATRIX.shape[0] # 8
    
    ## Source : https://stackoverflow.com/questions/29215879/how-can-i-generalize-the-quantization-matrix-in-jpeg-compression
    # Determine factor S for Quantization Table
    S: float = 5_000/quality if quality < 50 else 200 - 2*quality

    # Define quantization matrix altered
    quantization_table_S: numpy.ndarray = numpy.floor((S*QUANTIZATION_MATRIX+50) / 100)
    # Prevent "divide by 0"
    quantization_table_S[quantization_table_S==0] = 1

    # Block processing 8x8
    for i in range(0, artifacts.shape[0], block_size):
        for j in range(0, artifacts.shape[1], block_size):
            # DCT on 8x8 block
            dct: numpy.ndarray = scipy.fft.dctn(image[i:i+block_size, j:j+block_size])
            # Divide by quantification table/coefs
            dct: numpy.ndarray = numpy.round(dct/quantization_table_S)
            # inverse DCT
            artifacts[i:i+block_size, j:j+block_size] = scipy.fft.idctn(dct)

    return artifacts


def add_artifacts_with_svd(image: numpy.ndarray, epsilon: float) -> numpy.ndarray:

    """Add artifacts with by thresholding singular values 

        Parameters:
            - image : an image
            - epsilon : number in [0, 1] such as we set 0 forall 
            singular value low than `epsilon * value_singular_max`

        Returns:
            image with artifacts
    """
    artifacts: numpy.ndarray = numpy.copy(image)
    u, s, vh = numpy.linalg.svd(artifacts)

    s_diag = numpy.diag(s)
    value_max = numpy.max(s_diag)
    s_diag[s_diag < epsilon*value_max] = 0

    s_threshold = numpy.diag(s_diag)

    artifacts = numpy.dot(u * s_threshold, vh)

    return artifacts
