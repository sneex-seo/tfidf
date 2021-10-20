# -*- coding: utf-8 -*-
import yake

with open('text.txt', 'r+', encoding='utf-8') as f:
    keywords = [line.strip() for line in f]


text = " ".join(keywords)

language = "ru"
max_ngram_size = 1 #какие словосочетания выводить, униграммы (1 слово), биграммы (2 слова), 3 слова и т.д
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 20


custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size,
dedupLim=deduplication_thresold, dedupFunc=deduplication_algo,
 windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)

for kw in keywords:
    print(kw)