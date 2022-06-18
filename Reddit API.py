from nltk.corpus import stopwords
import praw
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import os
os.chdir('D:/Random projects/Reddit API')

words = stopwords.words('english')

reddit = praw.Reddit(client_id = 'L4sBRCW2GeFJbdniTnXy2A',
                     client_secret = 'KWKXJsQZelbownBsmu_B1JVSy8lysA',
                     user_agent = 'gh-test1')

print(reddit.read_only)

subreddit = reddit.subreddit('Singapore')

df = []
for post in subreddit.hot(limit = 100):
    df.append(post.title)
    
df = pd.DataFrame(df, columns = ['Title'])
df['Title'] = df['Title'].apply(lambda x: x.lower())
df = df['Title'].apply(lambda x: " ".join(x for x in x.split() if x not in words))
word_count = pd.DataFrame(' '.join(df).split()).value_counts()

words_for_cloud = " ".join(x for x in df)

word_cloud = WordCloud(collocations = False, background_color = 'white', width = 800, height = 400).generate(words_for_cloud)
plt.imshow(word_cloud, interpolation = 'bilinear')
plt.axis('off')
plt.savefig('wordcloud.pdf')
plt.show()
