from transformers import pipeline, AutoTokenizer

from nami import pipelines
from nami import models


class Pipeline:
    def __init__(self, task, model_dir, device=-1, batch_size=1, **kwargs):
        tokenizer = AutoTokenizer.from_pretrained(model_dir)

        self.pipe = pipeline(task, model=model_dir, tokenizer=tokenizer, device=device, batch_size=batch_size)

    def __call__(self, texts):
        return self.pipe(texts)



