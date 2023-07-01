from torch.utils.data import DataLoader

from hezar.data.datasets import TextClassificationDataset, TextClassificationDatasetConfig


config = TextClassificationDatasetConfig(
    name="text_classfication",
    path="hezarai/sentiment_digikala_snappfood",
    text_field="text",
    label_field="label",
    tokenizer_path="hezarai/distilbert-base-fa",
)

dataset = TextClassificationDataset(config, split="train")
print(dataset[0])

loader = DataLoader(dataset, batch_size=16, shuffle=True, collate_fn=dataset.data_collator)
itr = iter(loader)
x = next(itr)
print(x)