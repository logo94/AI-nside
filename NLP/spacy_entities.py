import spacy

it_lm = spacy.load("it_core_news_sm")

text = "Dante Alighieri è stato un poeta, scrittore e politico italiano."

tags = it_lm(text)

for ent in tags.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)