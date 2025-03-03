# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 11:46:54 2025

@author: subha
"""
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

file = open("ajeebdastaansgooglereviews.txt","r")
content = file.read()
l=[]
for i in range(0,len(content)):
    if content[i:i+6] == "Myaaao":
        j = 1
        print("myaao")
        while (content[i+2+j:i+j+8] != "Myaaao") and (j <= len(content) - i):
            j+=1
        l.append(content[i+7:i+1+j])
l = l[0:len(l)-1]        



# Download required NLTK resource
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()
sentimlist = []
for text in l:
    sentences = text.split("\n")
    
    # Perform sentiment analysis
    sentiment_scores = [sia.polarity_scores(sentence)["compound"] for sentence in sentences if sentence.strip()]
    
    # Categorize sentiment
    positive = sum(1 for score in sentiment_scores if score > 0.05)
    negative = sum(1 for score in sentiment_scores if score < -0.05)
    neutral = sum(1 for score in sentiment_scores if -0.05 <= score <= 0.05)
    sentimlist.append((positive,negative,neutral))
#fin_score = []
#for i in sentimlist:
#    (positive,negative,neutral) = i
#    m =  positive + negative + neutral
#    if positive/m >= 1/3:
##        fin_score.append(0)
#    elif 