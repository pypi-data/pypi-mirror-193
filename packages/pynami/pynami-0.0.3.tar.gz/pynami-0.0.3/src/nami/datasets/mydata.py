import json
from typing import Optional

import franky.dist as dist

from nami.registry import DATASETS
from .base_dataset import BaseDataset



@DATASETS.register_module()
class MyDataset(BaseDataset):
    def __init__(self,
                 ann_file: str,
                 test_mode: bool,
                 metainfo: Optional[dict] = None,
                 data_root: str = '',
                 **kwargs):
        super().__init__(
            ann_file=ann_file,
            metainfo=metainfo,
            data_root=data_root,
            test_mode=test_mode,
            **kwargs)

    def load_data_list(self):
        file = self.ann_file

        dist.barrier()

        texts, gt_labels = [], []
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                item = json.loads(line)
                text = item['content']  # .replace('"', '')
                label = item['annotation']
                if label is None:
                    label = []
                else:
                    label = [[temp['points'][0]['start'], temp['points'][0]['end'],
                              temp['label'][0]] for temp in label]
                    label.sort(key=lambda x: x[1])
                texts.append(text)
                gt_labels.append(label)

        data_list = []
        for text, gt_label in zip(texts, gt_labels):
            info = {'text': text, 'gt_label': gt_label}
            data_list.append(info)
        return data_list
