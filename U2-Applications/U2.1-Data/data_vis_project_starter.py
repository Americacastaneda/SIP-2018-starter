'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''
#is meant for the tweets text
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
#is meant for the graph
import numpy as np
#for the frequency of the word
from wordcloud import WordCloud


#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweettext = []
tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet['text']
print(tweetstring)

tweetBlob = TextBlob(tweetstring)
print(tweetBlob.translate(to='es'))

blob_polarity = []
for text in tweettext:
    b = TextBlob(text)
    blob_polarity.append(b.polarity) 

blob_subjectivity = []
for text in tweettext:
     b = TextBlob(text)
     blob_subjectivity.append(b.subjectivity)

word_dict = {}

for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]

print(word_dict)



#tweettext.append(tweet['text'])

# blob_polarity = []
# for text in tweettext:
#     b = TextBlob(text)
#     blob_polarity.append(b.polarity) 

# print("polarity average: ",sum(blob_polarity)/len(blob_polarity))
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# blob_subjectivity = []
# for text in tweettext:
#     b = TextBlob(text)
#     blob_subjectivity.append(b.subjectivity)

# print("subjectivity average: ",sum(blob_subjectivity)/len(blob_subjectivity))
# #~~~~~~~~~~~~~~~~graph~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# plt.hist(blob_polarity, bins=[-1, -0.8, -0.5, 0, 0.5, 0.8, 1])
# plt.xlabel("polarity")
# plt.ylabel("tweets")
# plt.title("Histogram of polarity")
# plt.axis([-1.1, 1.1, 0, 100])
# plt.grid(True)
# plt.show()
# #~~~~~~~~~~~~~~~graph 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# plt.hist(blob_subjectivity, bins=[-1, -0.8, -0.5, 0, 0.5, 0.8, 1])
# plt.xlabel("subjectivity")
# plt.ylabel("tweets")
# plt.title("Histogram of subjectivity")
# plt.axis([-1.1, 1.1, 0, 100])
# plt.grid(True)
# plt.show()
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # s = tweettext
# # ''.join(s)
# # print(s)
# # first = tweettext[10]
# # print (first)
#     #print(tweet.keys())

# # Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.sentiment)


# # # words = tb.words
# # # print(tb.polarity)
# # # print(TextBlob("bad").sentiment)

# # # for word in words:
# # #     print(TextBlob(word).sentiment)