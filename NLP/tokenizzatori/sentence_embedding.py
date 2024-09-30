import spacy
import spacy_universal_sentence_encoder

text = "Dante Alighieri è stato un poeta scrittore e politico italiano"

nlp = spacy.load('xx_use_md')

doc_1 = nlp(text)

print(doc_1.vector)
