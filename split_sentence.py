from nltk.tokenize import sent_tokenize

sentence = '''
Dante Alighieri, o Alighiero, battezzato Durante di Alighiero degli Alighieri e anche noto con il solo nome di Dante, della famiglia Alighieri 
(Firenze, tra il 14 maggio e il 13 giugno 1265 – Ravenna, notte tra il 13 e il 14 settembre[1][2][3] 1321), è stato un poeta, scrittore e politico italiano.

È considerato il padre della lingua italiana; la sua fama è dovuta alla paternità della Comedìa, divenuta celebre come Divina Commedia e 
universalmente considerata la più grande opera scritta in lingua italiana e uno dei maggiori capolavori della letteratura mondiale[4]. 
Espressione della cultura medievale, filtrata attraverso la lirica del Dolce stil novo, la Commedia è anche veicolo allegorico della salvezza 
umana, che si concretizza nel toccare i drammi dei dannati, le pene purgatoriali e le glorie celesti, permettendo a Dante di offrire al 
lettore uno spaccato di morale ed etica.
'''

splitted_sentece = sent_tokenize(sentence)

for single_sentence in splitted_sentece:
    print(single_sentence + '\n\n')