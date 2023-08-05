from enum import Enum


class EntityList(Enum):
    """List of templates in cgc-server

    :param Enum: name of template
    :type Enum: str
    """

    DATASCIENCE_JUPYTER = "datascience-jupyter"
    TENSORFLOW_JUPYTER = "tensorflow-jupyter"
    NVIDIA_TENSORFLOW = "nvidia-tensorflow"
    NVIDIA_RAPIDS = "nvidia-rapids"
    NVIDIA_PYTORCH = "nvidia-pytorch"
    NVIDIA_TRITON = "nvidia-triton"

    @classmethod
    def get_list(cls) -> list[str]:
        return [el.value for el in cls]


class GPUsList(Enum):
    """List of templates in cgc-server

    :param Enum: name of template
    :type Enum: str
    """

    A100 = "A100"
    # V100 = "V100"
    A5000 = "A5000"

    @classmethod
    def get_list(cls) -> list[str]:
        return [el.value for el in cls]
