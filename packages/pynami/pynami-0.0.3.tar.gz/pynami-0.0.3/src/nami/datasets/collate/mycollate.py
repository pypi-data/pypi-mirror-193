import bisect

import torch
from transformers import AutoTokenizer

from nami.registry import COLLATE_ClASSES


@COLLATE_ClASSES.register_module()
class AlignCollate:
    def __init__(self, max_length=512, ignore_index=-100, **kwargs):
        tokenizer_pretrained = kwargs.pop('tokenizer_pretrained')
        self.label2id = kwargs.pop('label2id')
        self.id2label = kwargs.pop('id2label')
        tokenizer_config = kwargs.pop('tokenizer_config')
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_pretrained, **tokenizer_config)
        self.max_length = max_length
        self.ignore_index = ignore_index
        tokenizer_save_dir = kwargs.pop('tokenizer_save_dir')
        self._save_tokenizer(tokenizer_save_dir)

    def _save_tokenizer(self, dir):
        self.tokenizer.save_pretrained(dir)

    # 构建[b,s]tag特征矩阵：对每个text对应的tag构建[s]特征矩阵，在entity位置置为tag_index，其余为ignore_index
    def _align_label(self, tokens, labels):  # label [begin, end, tag]
        encodings = tokens.encodings
        labels_ = []  # 对每个text对应的tag构建[s]特征矩阵，在entity位置置为tag_index
        labels_seq = []
        for encoding, label in zip(encodings, labels):
            label_ = [0 if v == 1 else self.ignore_index for v in
                      encoding.attention_mask]  # attention_mask中1转为0，0转为ignore_index -> label_
            begins = [offset[0] for offset in encoding.offsets if offset != (0, 0)]  # token位置 -> character位置
            ends = [offset[-1] - 1 for offset in encoding.offsets if offset != (0, 0)]
            length = sum(encoding.attention_mask)  # 句子token实际长度
            for temp in label:
                begin, end, tag = temp[0], temp[1], temp[2]  # 每个实体character位置
                left = bisect.bisect_left(ends, int(begin)) + 1  # 找到每个实体token位置
                right = bisect.bisect_right(begins, int(end))
                if left > right or left >= length:
                    continue
                elif right >= length:
                    right = length - 1

                # elif left
                label_[left] = self.label2id['B-{}'.format(tag)]  # label_在entity位置置为tag_index
                label_[left + 1: right + 1] = [self.label2id['I-{}'.format(tag)]] * (right - left)
            label_seq = [self.id2label[idx] for idx in label_ if idx != self.ignore_index]
            labels_.append(label_)  # [b,s]
            labels_seq.append(label_seq)
        return labels_, labels_seq

    def _align(self, texts, labels):
        tokens = self.tokenizer(texts, padding=True, truncation=True, max_length=self.max_length, return_tensors="pt")

        labels, labels_seq = self._align_label(tokens, labels)
        labels = torch.tensor(labels)  # 转换成tensor

        return tokens, labels, labels_seq

    def __call__(self, data_batch):
        # list of dict to dict of list
        data = {k: [dic[k] for dic in data_batch] for k in data_batch[0]}
        tokens, labels, labels_seq = self._align(data['text'], data['gt_label'])
        tokens['labels'] = labels
        tokens['labels_seq'] = labels_seq

        return tokens
