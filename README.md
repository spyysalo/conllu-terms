# CoNLL-U terms

Extract terms from CoNLL-U parses.

Currently implemented as a simple example rather than a serious term
recognition method.

## Quickstart

Parse Finnish example text (from <https://fi.wikipedia.org/wiki/Turku>)
using [Turku Neural Parser](http://turkunlp.org/Turku-neural-parser-pipeline/):

```
python3 requestparse.py examples/wikipedia_Turku.txt > wikipedia_Turku.conllu
```

Get terms candidates from parsed example text:

```
python3 getterms.py examples/wikipedia_Turku.conllu | head
```

Result:

```
1.00	Turku
0.53	Suomi
0.42	kaupunki
0.26	vuosi
0.26	pää#kaupunki
0.16	alue
0.16	historia
0.11	ruotsi
0.11	Varsinais#Suomi
0.11	maa#kunta
```
