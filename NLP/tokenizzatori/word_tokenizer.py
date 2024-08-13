from nltk.tokenize import word_tokenize 

text = '''
Dante Alighieri, o Alighiero, battezzato Durante di Alighiero degli Alighieri e anche noto con il solo nome di Dante, della famiglia Alighieri 
(Firenze, tra il 14 maggio e il 13 giugno 1265 – Ravenna, notte tra il 13 e il 14 settembre[1][2][3] 1321), è stato un poeta, scrittore e politico italiano.
'''

splitted_text = word_tokenize(text)

for word in splitted_text:
    print(word)
