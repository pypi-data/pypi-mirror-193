from nami.apis import Pipeline


model_dir = '/home/feiwang/projects/dl-transformers/saved_transformers'
pipe = Pipeline('my-token-classification', model_dir, device=1, batch_size=2)
res = pipe(['我是张三，我居住在江苏省苏州市', 'asdfasdf'])
print(res)