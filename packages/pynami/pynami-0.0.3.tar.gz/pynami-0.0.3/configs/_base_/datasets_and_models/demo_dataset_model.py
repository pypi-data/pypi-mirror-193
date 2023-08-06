classes = ("O", "B-省", "I-省", "B-区县市", "I-区县市", "B-详细地址", "I-详细地址")
id2label = {idx: cat for idx, cat in enumerate(classes)}
label2id = {cat: idx for idx, cat in enumerate(classes)}
# from_pretrained = './saved_transformers'
from_pretrained = 'bert-base-chinese'
# model settings
model = dict(
    type='MyBertForTokenClassification',
    pretrained=from_pretrained,
    hidden_size1=768,
    id2label=id2label,
    label2id=label2id,
    # loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
    )

# dataset settings
dataset_type = 'MyDataset'
# data_preprocessor = dict(
#     type='NerDataPreprocessor',
# )

train_pipeline = [
    # dict(type='RandomCrop', crop_size=32, padding=4),
    # dict(type='RandomFlip', prob=0.5, direction='horizontal'),
    # dict(type='PackClsInputs'),
]

test_pipeline = [
    # dict(type='PackClsInputs'),
]
collate = dict(
    type='my_default_collate',
    collate_class_type='AlignCollate',
    tokenizer_pretrained=from_pretrained,
    tokenizer_save_dir='./tokenizer',
    tokenizer_config=dict(do_lower_case=True),
    label2id=label2id,
    id2label=id2label
)

train_dataloader = dict(
    batch_size=16,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        ann_file='/home/feiwang/projects/awesome_nlp/nlp_app/address_ner/data/train_data.json',
        test_mode=False,
        pipeline=train_pipeline,
        metainfo=dict(classes=classes),
        ),
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=collate
)

val_dataloader = dict(
    batch_size=16,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        ann_file='/home/feiwang/projects/awesome_nlp/nlp_app/address_ner/data/valid_data.json',
        test_mode=True,
        pipeline=test_pipeline,
        metainfo=dict(classes=classes),
    ),
    sampler=dict(type='DefaultSampler', shuffle=False),
    collate_fn=collate
)
val_evaluator = dict(type='MyMetrics')

test_dataloader = val_dataloader
test_evaluator = val_evaluator
