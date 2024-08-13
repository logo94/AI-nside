import pprint
import treetaggerwrapper

tagger = treetaggerwrapper.TreeTagger(TAGLANG='it', TAGDIR="/home/usi/Desktop/IA/Tokenizzatori/treetaggerfolder/")

text = "Dante Alighieri è stato un poeta, scrittore e politico italiano."

tags = tagger.tag_text(text)

pprint.pprint(tags)
