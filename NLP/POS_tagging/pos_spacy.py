import spacy

it_lm = spacy.load("it_core_news_sm")

text = "Dante Alighieri è stato un poeta, scrittore e politico italiano."

tags = it_lm(text)

for tag in tags:
    print(f"{tag.text} [{tag.pos_}]")