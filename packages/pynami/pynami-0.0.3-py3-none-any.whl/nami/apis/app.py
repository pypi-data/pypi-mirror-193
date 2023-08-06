import gradio as gr

from nami.apis.pipeline import Pipeline

model_dir = '/home/feiwang/projects/dl-transformers/nami/work_dirs/myconfig/20230131_021320/save_transformer'
pipe = Pipeline('my-token-classification', model_dir, device=1, batch_size=2)


def predict(text):
    return str(pipe(text))


examples = ['我是王飞，我居住在浙江省杭州市']

demo = gr.Interface(
    fn=predict,
    inputs='text',
    outputs='text',
    examples=[examples]
)

demo.launch(share=True)
