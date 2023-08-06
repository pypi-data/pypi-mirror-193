import os.path as osp
from os import PathLike
from typing import Optional, Sequence, Union

from franky.dataset import BaseDataset as _BaseDataset

from nami.registry import DATASETS, TRANSFORMS


def expanduser(path):
    if isinstance(path, (str, PathLike)):
        return osp.expanduser(path)
    else:
        return path


@DATASETS.register_module()
class BaseDataset(_BaseDataset):
    def __init__(self,
                 ann_file: str,
                 metainfo: Optional[dict] = None,
                 data_root: str = '',
                 data_prefix: Union[str, dict] = '',
                 filter_cfg: Optional[dict] = None,
                 indices: Optional[Union[int, Sequence[int]]] = None,
                 serialize_data: bool = True,
                 pipeline: Sequence = (),
                 test_mode: bool = False,
                 lazy_init: bool = False,
                 max_refetch: int = 1000):
        if isinstance(data_prefix, str):
            data_prefix = dict(img_path=expanduser(data_prefix))

        ann_file = expanduser(ann_file)

        transforms = []
        for transform in pipeline:
            if isinstance(transform, dict):
                transforms.append(TRANSFORMS.build(transform))
            else:
                transforms.append(transform)

        super().__init__(
            ann_file=ann_file,
            metainfo=metainfo,
            data_root=data_root,
            data_prefix=data_prefix,
            filter_cfg=filter_cfg,
            indices=indices,
            serialize_data=serialize_data,
            pipeline=transforms,
            test_mode=test_mode,
            lazy_init=lazy_init,
            max_refetch=max_refetch)
