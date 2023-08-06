"""Enums used in the project."""

import enum

from .country_codes import ALL_COUNTRY_CODES


class Device(enum.Enum):
    """The compute device to use for the evaluation.

    Attributes:
        CPU:
            CPU device.
        MPS:
            MPS GPU, used in M-series MacBooks.
        CUDA:
            CUDA GPU, used with NVIDIA GPUs.
    """

    CPU = "cpu"
    MPS = "mps"
    CUDA = "cuda"


class Modality(enum.Enum):
    """The modality of the input data.

    Attributes:
        AUDIO:
            Input data is audio.
        TEXT:
            Input data is text.
    """

    AUDIO = "audio"
    TEXT = "text"


class Framework(enum.Enum):
    """The framework of a model.

    Attributes:
        PYTORCH:
            PyTorch framework.
        JAX:
            JAX framework.
        SPACY:
            spaCy framework.
    """

    PYTORCH = "pytorch"
    JAX = "jax"
    SPACY = "spacy"


country_code_enum_list = [
    (country_code, country_code.upper()) for country_code in ALL_COUNTRY_CODES
]
country_code_enum_list += [("EMPTY", "")]
CountryCode = enum.Enum("CountryCode", country_code_enum_list)  # type: ignore[misc]
