from franky.registry import DATA_SAMPLERS as Franky_DATA_SAMPLERS
from franky.registry import DATASETS as Franky_DATASETS
from franky.registry import EVALUATOR as Franky_EVALUATOR
from franky.registry import HOOKS as Franky_HOOKS
from franky.registry import LOG_PROCESSORS as Franky_LOG_PROCESSORS
from franky.registry import LOOPS as Franky_LOOPS
from franky.registry import METRICS as Franky_METRICS
from franky.registry import MODEL_WRAPPERS as Franky_MODEL_WRAPPERS
from franky.registry import MODELS as Franky_MODELS
from franky.registry import OPTIM_WRAPPER_CONSTRUCTORS as Franky_OPTIM_WRAPPER_CONSTRUCTORS
from franky.registry import OPTIM_WRAPPERS as Franky_OPTIM_WRAPPERS
from franky.registry import OPTIMIZERS as Franky_OPTIMIZERS
from franky.registry import PARAM_SCHEDULERS as Franky_PARAM_SCHEDULERS
from franky.registry import RUNNER_CONSTRUCTORS as Franky_RUNNER_CONSTRUCTORS
from franky.registry import RUNNERS as Franky_RUNNERS
from franky.registry import TASK_UTILS as Franky_TASK_UTILS
from franky.registry import TRANSFORMS as Franky_TRANSFORMS
from franky.registry import VISBACKENDS as Franky_VISBACKENDS
from franky.registry import VISUALIZERS as Franky_VISUALIZERS
from franky.registry import WEIGHT_INITIALIZERS as Franky_WEIGHT_INITIALIZERS
from franky.registry import Registry
from franky.dataset import COLLATE_FUNCTIONS

COLLATE_ClASSES = Registry('Collate Classes', locations=['nami.datasets'])

#######################################################################
#                            nami.engine                             #
#######################################################################
# Runners like `EpochBasedRunner` and `IterBasedRunner`
RUNNERS = Registry(
    'runner',
    parent=Franky_RUNNERS,
    locations=['nami.engine'],
)
# Runner constructors that define how to initialize runners
RUNNER_CONSTRUCTORS = Registry(
    'runner constructor',
    parent=Franky_RUNNER_CONSTRUCTORS,
    locations=['nami.engine'],
)
# Loops which define the training or test process, like `EpochBasedTrainLoop`
LOOPS = Registry(
    'loop',
    parent=Franky_LOOPS,
    locations=['nami.engine'],
)
# Hooks to add additional functions during running, like `CheckpointHook`
HOOKS = Registry(
    'hook',
    parent=Franky_HOOKS,
    locations=['nami.engine'],
)
# Log processors to process the scalar log data.
LOG_PROCESSORS = Registry(
    'log processor',
    parent=Franky_LOG_PROCESSORS,
    locations=['nami.engine'],
)
# Optimizers to optimize the model weights, like `SGD` and `Adam`.
OPTIMIZERS = Registry(
    'optimizer',
    parent=Franky_OPTIMIZERS,
    locations=['nami.engine'],
)
# Optimizer wrappers to enhance the optimization process.
OPTIM_WRAPPERS = Registry(
    'optimizer_wrapper',
    parent=Franky_OPTIM_WRAPPERS,
    locations=['nami.engine'],
)
# Optimizer constructors to customize the hyperparameters of optimizers.
OPTIM_WRAPPER_CONSTRUCTORS = Registry(
    'optimizer wrapper constructor',
    parent=Franky_OPTIM_WRAPPER_CONSTRUCTORS,
    locations=['nami.engine'],
)
# Parameter schedulers to dynamically adjust optimization parameters.
PARAM_SCHEDULERS = Registry(
    'parameter scheduler',
    parent=Franky_PARAM_SCHEDULERS,
    locations=['nami.engine'],
)

#######################################################################
#                           nami.datasets                             #
#######################################################################

# Datasets like `ImageNet` and `CIFAR10`.
DATASETS = Registry(
    'dataset',
    parent=Franky_DATASETS,
    locations=['nami.datasets'],
)
# Samplers to sample the dataset.
DATA_SAMPLERS = Registry(
    'data sampler',
    parent=Franky_DATA_SAMPLERS,
    locations=['nami.datasets'],
)
# Transforms to process the samples from the dataset.
TRANSFORMS = Registry(
    'transform',
    parent=Franky_TRANSFORMS,
    locations=['nami.datasets'],
)

#######################################################################
#                            nami.models                             #
#######################################################################

# Neural network modules inheriting `nn.Module`.
# MODELS = Registry(
#     'model',
#     parent=Franky_MODELS,
#     locations=['nami.models'],
# )
from franky.utils import ManagerMixin
import inspect

def build_model(cfg, registry, *args, **kwargs):
    args = cfg.copy()
    obj_type = args.pop('type')
    if isinstance(obj_type, str):
        obj_cls = registry.get(obj_type)
        if obj_cls is None:
            raise KeyError(
                f'{obj_type} is not in the {registry.name} registry. '
                f'Please check whether the value of `{obj_type}` is '
                'correct or it was registered as expected. More details '
                'can be found at '
                'https://franky.readthedocs.io/en/latest/advanced_tutorials/config.html#import-the-custom-module'  # noqa: E501
            )
    elif inspect.isclass(obj_type) or inspect.isfunction(obj_type):
        obj_cls = obj_type
    else:
        raise TypeError(
            f'type must be a str or valid type, but got {type(obj_type)}')

    pretrained = args.pop('pretrained')
    if pretrained:
        obj = obj_cls.from_pretrained(pretrained, **args)
    else:
        obj = obj_cls(**args)  # type: ignore

    return obj

MODELS = Registry('model', build_func=build_model, parent=Franky_MODELS, locations=['nami.models'],)
# Model wrappers like 'MMDistributedDataParallel'
MODEL_WRAPPERS = Registry(
    'model_wrapper',
    parent=Franky_MODEL_WRAPPERS,
    locations=['nami.models'],
)
# Weight initialization methods like uniform, xavier.
WEIGHT_INITIALIZERS = Registry(
    'weight initializer',
    parent=Franky_WEIGHT_INITIALIZERS,
    locations=['nami.models'],
)
# Batch augmentations like `Mixup` and `CutMix`.
BATCH_AUGMENTS = Registry(
    'batch augment',
    locations=['nami.models'],
)
# Task-specific modules like anchor generators and box coders
TASK_UTILS = Registry(
    'task util',
    parent=Franky_TASK_UTILS,
    locations=['nami.models'],
)

#######################################################################
#                          nami.evaluation                           #
#######################################################################

# Metrics to evaluate the model prediction results.
METRICS = Registry(
    'metric',
    parent=Franky_METRICS,
    locations=['nami.evaluation'],
)
# Evaluators to define the evaluation process.
EVALUATORS = Registry(
    'evaluator',
    parent=Franky_EVALUATOR,
    locations=['nami.evaluation'],
)

#######################################################################
#                         nami.visualization                         #
#######################################################################

# Visualizers to display task-specific results.
VISUALIZERS = Registry(
    'visualizer',
    parent=Franky_VISUALIZERS,
    locations=['nami.visualization'],
)
# Backends to save the visualization results, like TensorBoard, WandB.
VISBACKENDS = Registry(
    'vis_backend',
    parent=Franky_VISBACKENDS,
    locations=['nami.visualization'],
)
