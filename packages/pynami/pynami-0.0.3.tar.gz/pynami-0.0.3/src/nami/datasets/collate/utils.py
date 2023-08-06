from nami.registry import COLLATE_ClASSES
from nami.registry import COLLATE_FUNCTIONS
from nami.utils import singleton


@singleton
class BuildCollate:
    def __init__(self, *args, **kwargs):
        self.collate_obj = COLLATE_ClASSES.build(kwargs)


@COLLATE_FUNCTIONS.register_module()
def my_default_collate(data_batch, **kwargs):
    kwargs['type'] = kwargs.pop('collate_class_type')
    align_collate = BuildCollate(**kwargs)
    res = align_collate.collate_obj(data_batch)
    res.update(dict(data_batch=data_batch))

    return res
