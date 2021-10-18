import pandas as pd
import nltk
nltk.download( 'vader_lexicon' )
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, datetime

reviews = pd.read_csv('C:/Users/jackm/Documents/analytics/fall2/text/tiktok_app_reviews.csv')

sentiment = SentimentIntensityAnalyzer()

reviews['review_text'] = reviews['review_text'].apply(lambda x: str(x))
reviews["Positive"] = 0
reviews["Negative"] = 0
reviews["Neutral"] = 0
reviews["Compound"] = 0
reviews['Positive'] = reviews['review_text'].apply(lambda x: sentiment.polarity_scores(x)['pos'])
reviews['Negative'] = reviews['review_text'].apply(lambda x: sentiment.polarity_scores(x)['neg'])
reviews['Neutral'] = reviews['review_text'].apply(lambda x: sentiment.polarity_scores(x)['neu'])
reviews['Compound'] = reviews['review_text'].apply(lambda x: sentiment.polarity_scores(x)['compound'])

reviews.head()
reviews.to_csv('C:/Users/jackm/Documents/analytics/fall2/text/scored_reviews.csv')