from franky.utils.dl_utils import TORCH_VERSION
from franky.utils.version_utils import digit_version
from .distributed import OPDistributedDataParallel
from .seperate_distributed import OPSeparateDistributedDataParallel
from .utils import is_model_wrapper

if digit_version(TORCH_VERSION) >= digit_version('1.11.0'):
    from .fully_sharded_distributed import OPFullyShardedDataParallel  # noqa:F401
