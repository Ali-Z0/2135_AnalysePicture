---
license: apache-2.0
tags:
- vision
- image-classification

datasets:
- imagenet-1k

widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/tiger.jpg
  example_title: Tiger
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/teapot.jpg
  example_title: Teapot
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/palace.jpg
  example_title: Palace

---

# ResNet

ResNet model trained on imagenet-1k. It was introduced in the paper [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) and first released in [this repository](https://github.com/KaimingHe/deep-residual-networks). 

Disclaimer: The team releasing ResNet did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

ResNet introduced residual connections, they allow to train networks with an unseen number of layers (up to 1000). ResNet won the 2015 ILSVRC & COCO competition, one important milestone in deep computer vision.

![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/resnet_architecture.png)

## Intended uses & limitations

You can use the raw model for image classification. See the [model hub](https://huggingface.co/models?search=resnet) to look for
fine-tuned versions on a task that interests you.

### How to use

Here is how to use this model:

```python
>>> from transformers import AutoFeatureExtractor, ResNetForImageClassification
>>> import torch
>>> from datasets import load_dataset

>>> dataset = load_dataset("huggingface/cats-image")
>>> image = dataset["test"]["image"][0]

>>> feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-18")
>>> model = ResNetForImageClassification.from_pretrained("microsoft/resnet-18")

>>> inputs = feature_extractor(image, return_tensors="pt")

>>> with torch.no_grad():
...     logits = model(**inputs).logits

>>> # model predicts one of the 1000 ImageNet classes
>>> predicted_label = logits.argmax(-1).item()
>>> print(model.config.id2label[predicted_label])
tiger cat
```



For more code examples, we refer to the [documentation](https://huggingface.co/docs/transformers/master/en/model_doc/resnet).