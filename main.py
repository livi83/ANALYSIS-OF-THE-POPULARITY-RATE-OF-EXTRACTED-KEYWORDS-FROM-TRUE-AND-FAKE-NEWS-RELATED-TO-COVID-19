from TextProcess import TextProcess
from Extractor import Extractor

tp = TextProcess()
ex = Extractor()

dataset = tp.read_sheet("dataset.xlsx", 0)
dataset['title'] = dataset['title'].astype(str)+". "
dataset_t = dataset.loc[dataset['subcategory'] == "true"]
dataset_t = dataset_t[['title', 'text']]

dataset_f = dataset.loc[dataset['subcategory'] == "false news"]
dataset_f = dataset_f[['title', 'text']]

dataset_pf = dataset.loc[dataset['subcategory'] == "partially false"]
dataset_pf = dataset_pf[['title', 'text']]


true_news = tp.remove_empty_lines(tp.r_file("true.txt"))
false_news = tp.remove_empty_lines(tp.r_file("false.txt"))
partially_false_news = tp.remove_empty_lines(tp.r_file("partiallyfalse.txt"))

s_keybert_true = ex.keybert_extractor(true_news, 1, 1, 100)
s_keybert_false = ex.keybert_extractor(false_news, 1, 1, 100)
s_keybert_partially_false = ex.keybert_extractor(partially_false_news, 1, 1, 100)

#keybert_true = ex.keybert_extractor(true_news, 2, 2, 10)
#keybert_false = ex.keybert_extractor(false_news, 2, 2, 10)
#keybert_partially_false = ex.keybert_extractor(partially_false_news, 1, 2, 10)

#v_true = ex.vector_keybert_extractor(true_news)
#v_false = ex.vector_keybert_extractor(false_news)
#v_partially_false = ex.vector_keybert_extractor(partially_false_news)


freq_true = tp.frequent_words(true_news)
freq_false = tp.frequent_words(false_news)
freq_partially_false = tp.frequent_words(partially_false_news)

rake_true = ex.rake_extractor(true_news,1,1)
rake_false = ex.rake_extractor(false_news,1,1)
rake_partially_false = ex.rake_extractor(partially_false_news,1,1)
if __name__ == '__main__':
    print(s_keybert_true)
    print(s_keybert_false)
    print(s_keybert_partially_false)


