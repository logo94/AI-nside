## TreeTagger

La documentazione in lingua originale è disponibile al link: https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger 

### Requisiti
1. Dowload tree-tagger-package (tree-tagger-linux-3.2.5.tar.gz) [link](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/)
2. Download tagging script [link](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/tagger-scripts.tar.gz)
3. Download script di installazione [link](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/install-tagger.sh)
4. Download file di lingua [link1](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/italian.par.gz), [link2](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/italian2.par.gz)
5. Aprire il terminale in corrispondenza della cartella di download e eseguire il comando
```
sh install-tagger.sh
```
6. Testare la correttezza del download tramite il comando:
```
echo 'Hello world!' | cmd/tree-tagger-italian
```

Per l'utilizzo tramite script Python è necessario installare il wrapper Python, una volta creato e attivato un ambiente virtuale Python installare il wrapper tramite il comando:

```
pip install treetaggerwrapper
```

e il pacchetto `six`:

```
pip install six
```

Per un corretto funzionamento è indispensabile indicare la cartella all'interno della quale TreeTagger è stato installato
```
tagger = treetaggerwrapper.TreeTagger(TAGLANG='it', TAGDIR="path_alla_cartella_treetagger")
```

si consiglia di mantenere la stessa struttura della cartella di questo repository:

```
tagger = treetaggerwrapper.TreeTagger(TAGLANG='it', TAGDIR="treetaggerfolder/")
```


