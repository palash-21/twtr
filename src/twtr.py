import re
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import string
import nltk
from nltk.stem.porter import *
import os
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)

%matplotlib inline

#getting the data
this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "data", "Tweets.csv")
df = pd.read_csv(DATA_PATH)

# remove twitter handles (@user)
def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt  


df['tidy_tweet'] = np.vectorize(remove_pattern)(df['text'], "@[\w]*")

# remove special characters, numbers, punctuations
df['tidy_tweet'] = df['tidy_tweet'].str.replace("[^a-zA-Z#]", " ")

#tolenization
tokenized_tweet = df['tidy_tweet'].apply(lambda x: x.split())

#Stemming
stemmer = PorterStemmer()
tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x]) # stemming

#Adding it to df
for i in range(len(tokenized_tweet)):
    tokenized_tweet[i] = ' '.join(tokenized_tweet[i])

df['tidy_tweet'] = tokenized_tweet

output_df = pd.DataFrame()
output_df['tidy_tweet'] = df['tidy_tweet'].copy()
output_df['tweet_id']=df['tweet_id']

def return_cleaned_tweet():
    return output_df
    
