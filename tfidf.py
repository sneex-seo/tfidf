# -*- coding: utf-8 -*-
import yake
import csv

with open('text.txt', 'r+', encoding='utf-8') as f:
    keywords = [line.strip() for line in f]

def csv_writer(data):
    with open('result.csv', 'a', newline='', encoding='utf-8') as csvfile:
        spamWriter = csv.writer(csvfile)
        spamWriter.writerow(data)

text = " ".join(keywords)

#пишем языковой код языка
language = "ru"
#какие словосочетания выводить, униграммы (1 слово), биграммы (2 слова), 3 слова и т.д
max_ngram_size = 1
deduplication_thresold = 0.9
deduplication_algo = 'se    qm'
windowSize = 1
numOfKeywords = 20


custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size,
dedupLim=deduplication_thresold, dedupFunc=deduplication_algo,
 windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)

for kw in keywords:
    result = [kw[0],kw[1]]
    csv_writer(result)
