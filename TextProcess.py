
import io
import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
import re
from nltk import word_tokenize,pos_tag
from nltk.corpus import wordnet as wn
class TextProcess:
    def read_sheet(self,file, sheet):
        return pd.read_excel(file, sheet_name=sheet, header=0)

    def export_df(self,df, file,h):
        return df.to_csv(file, encoding='utf-8-sig', header=h, index=False, sep='\t', mode='a')

    def r_file(self,file):
        f = io.open(file, encoding='utf-8-sig')
        return (f.read())

    def remove_empty_lines(self, text):
        return text.replace("\n"," ")

    def remove_punctuation(self,text):
        list = sent_tokenize(text)
        list_to_text = ''
        for l in list:
            ln = re.sub(r'[^\w\s]', '', l)
            list_to_text += ln+'. '
        list_to_text = list_to_text.replace(".", "")
        return list_to_text

    def remove_stopwords(self,text):
        text = word_tokenize(text)
        en_stopwords = stopwords.words('english')
        res = []
        for t in text:
            if t not in en_stopwords:
                res.append(t)
        res_str = ''
        for r in res:
            res_str += r+' '
        return res_str

    def frequent_words(self, text):
        lst = word_tokenize(self.remove_stopwords(self.remove_punctuation(text.lower())))
        blacklist = ['virus', 'coronavirus', 'covid19', 'covid-19',
                     '2019ncov', 'corona', 'covid']
        filtered = [s for s in lst if not any(xs in s for xs in blacklist)]
        nouns = []
        all_nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
        for f in filtered:
            if f in all_nouns:
                nouns.append(f)
        fdist = FreqDist(nouns)
        return fdist.most_common(50)




