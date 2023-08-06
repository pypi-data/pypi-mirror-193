from transformers import AutoModelForTokenClassification
from transformers.pipelines import PIPELINE_REGISTRY

from .token_classification import MyTokenClassificationPipeline

SUPPORTED_TASKS = {
    "my-token-classification": {
        "pipeline_class": MyTokenClassificationPipeline,
        "pt_model": AutoModelForTokenClassification,
        # "default": {"pt": ("superb/wav2vec2-base-superb-ks", "372e048")},
        "type": "text",  # current support type: text, audio, image, multimodal
    }
}

for task, pipeline in SUPPORTED_TASKS.items():
    PIPELINE_REGISTRY.register_pipeline(task, **pipeline)
