from franky.utils.dl_utils import TORCH_VERSION
from franky.utils.version_utils import digit_version
from .averaged_model import BaseAveragedModel, ExponentialMovingAverage, MomentumAnnealingEMA, StochasticWeightAverage
from .base_model import BaseDataPreprocessor, BaseModel, ImgDataPreprocessor
from .base_module import BaseModule, ModuleDict, ModuleList, Sequential
from .test_time_aug import BaseTTAModel
from .utils import convert_sync_batchnorm, detect_anomalous_params, merge_dict, revert_sync_batchnorm, stack_batch
from .weight_init import (BaseInit, Caffe2XavierInit, ConstantInit, KaimingInit, NormalInit, PretrainedInit,
                          TruncNormalInit, UniformInit, XavierInit, bias_init_with_prob, caffe2_xavier_init,
                          constant_init, initialize, kaiming_init, normal_init, trunc_normal_init, uniform_init,
                          update_init_info, xavier_init)
from .wrappers import OPDistributedDataParallel, OPSeparateDistributedDataParallel, is_model_wrapper

if digit_version(TORCH_VERSION) >= digit_version('1.11.0'):
    from .wrappers import OPFullyShardedDataParallel
