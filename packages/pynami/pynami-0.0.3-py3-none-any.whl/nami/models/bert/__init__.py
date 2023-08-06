from transformers import AutoConfig, AutoModelForTokenClassification

from .configuration_bert import MyBertConfig
from .modeling_bert import MyBertForTokenClassification

AutoConfig.register("mybert", MyBertConfig)
AutoModelForTokenClassification.register(MyBertConfig, MyBertForTokenClassification)
