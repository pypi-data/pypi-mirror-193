from typing import Optional

import torch.utils.checkpoint
from franky.model import BaseModel
from torch import nn
from torch.nn import CrossEntropyLoss
from transformers import BertModel, BertPreTrainedModel

from nami.registry import MODELS
from .configuration_bert import MyBertConfig


@MODELS.register_module()
class MyBertForTokenClassification(BertPreTrainedModel, BaseModel):
    config_class = MyBertConfig

    _keys_to_ignore_on_load_unexpected = [r"pooler"]

    def __init__(self, config, *args, **kwargs):
        super().__init__(config, kwargs)
        self.num_labels = config.num_labels

        self.bert = BertModel(config, add_pooling_layer=False)
        classifier_dropout = (
            config.classifier_dropout if config.classifier_dropout is not None else config.hidden_dropout_prob
        )
        self.dropout = nn.Dropout(classifier_dropout)
        self.classifier = nn.Sequential(nn.Linear(config.hidden_size, config.hidden_size1),
                                        nn.Linear(config.hidden_size1, config.num_labels))

        # Initialize weights and apply final processing
        self.post_init()

    def forward(
            self,
            input_ids: Optional[torch.Tensor] = None,
            attention_mask: Optional[torch.Tensor] = None,
            token_type_ids: Optional[torch.Tensor] = None,
            position_ids: Optional[torch.Tensor] = None,
            head_mask: Optional[torch.Tensor] = None,
            inputs_embeds: Optional[torch.Tensor] = None,
            labels: Optional[torch.Tensor] = None,
            output_attentions: Optional[bool] = None,
            output_hidden_states: Optional[bool] = None,
            return_dict: Optional[bool] = None,
            mode: str = 'tensor',
            *args, **kwargs
    ):  # -> Union[Tuple[torch.Tensor], TokenClassifierOutput]:

        # return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        sequence_output = outputs[0]

        sequence_output = self.dropout(sequence_output)
        logits = self.classifier(sequence_output)

        # if mode == 'tensor':
        #     feats = self.extract_feat(inputs)
        #     return self.head(feats) if self.with_head else feats
        # elif mode == 'loss':
        #     return self.loss(inputs, data_samples)
        # elif mode == 'predict':
        #     return self.predict(inputs, data_samples)
        # else:
        #     raise RuntimeError(f'Invalid mode "{mode}".')
        if mode == 'loss':
            loss_fct = CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
            return dict(loss=loss)
        elif mode == 'predict':
            return self.predict(logits, attention_mask)
        else:
            return logits,

    def predict(self, logits, attention_mask):
        id2label = self.config.id2label
        pred_label = []
        for pred, attn_mask in zip(logits.argmax(-1).cpu().numpy(), attention_mask.cpu().numpy()):
            pred_label.append([id2label[p] for p, a in zip(pred, attn_mask) if a == 1])
        return pred_label
