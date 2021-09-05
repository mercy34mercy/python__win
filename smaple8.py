
import spacy
nlp = spacy.load('ja_ginza_electra')
doc = nlp('spaCy はオープンソースの自然言語処理ライブラリです。学習済みの統計モデルと単語ベクトルが付属しています。')

for sent in doc.sents:
    for token in sent:
        print(token.i, token.orth_, token.lemma_, token.pos_, token.tag_, token.dep_, token.head.i)
    print('EOS')
#/home/masakun/.local/lib/python3.8/site-packages/spacy/cli/debug_data.py
