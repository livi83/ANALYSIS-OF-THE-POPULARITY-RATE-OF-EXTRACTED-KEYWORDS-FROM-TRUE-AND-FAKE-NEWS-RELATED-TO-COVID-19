from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer
from nltk.corpus import wordnet as wn
from rake_nltk import Rake, Metric

class Extractor:
    bert = KeyBERT()
    vectorizer = KeyphraseCountVectorizer()
    def keybert_extractor(self,text, start, stop,top):
        keywords = self.bert.extract_keywords(text, keyphrase_ngram_range=(start, stop), stop_words="english", top_n=top)
        results = []
        blacklist = ['virus', 'coronavirus', 'covid19', 'covid-19',
                     '2019ncov', 'corona', 'covid']
        for scored_keywords in keywords:
            for keyword in scored_keywords:
                if isinstance(keyword, str):
                    if not any(b in keyword for b in blacklist):
                        results.append(keyword)
        nouns = []
        all_nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
        for r in results:
            if r in all_nouns:
                nouns.append(r)
        return nouns
    def vector_keybert_extractor(self,text):
        v_ex = [i for i,j in self.bert.extract_keywords(docs=text, stop_words="english", top_n=10, vectorizer=self.vectorizer)]
        return v_ex





