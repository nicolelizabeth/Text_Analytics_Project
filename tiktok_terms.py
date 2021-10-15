#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 21:10:59 2021

@author: nicolehanrahan
"""

# This code is currently set up to run for the pre covid time period
# Need to change lines 51, 81 and 103 for post covid data sets

import re
import pandas as pd
from operator import itemgetter
import nltk
nltk.download('punkt')
import string

scores = pd.read_csv('/Users/nicolehanrahan/Documents/MSA/3. Fall/AA502/Text Analytics/scored_reviews.csv')
postcovid = scores[scores.posted_date.str.startswith('2021') | scores.posted_date.str.startswith('2020')].copy()
precovid = scores[scores.posted_date.str.startswith('2019') | scores.posted_date.str.startswith('2018')].copy()
postcovid_sample = postcovid.sample(frac=0.01, replace=False, random_state=77)
precovid_sample = precovid.sample(frac=0.01, replace=False, random_state=77)
reviews_only_post = postcovid_sample[['review_text']].copy()
reviews_only_pre = precovid_sample[['review_text']].copy()
review_list_post = reviews_only_post['review_text'].tolist()
review_list_pre = reviews_only_pre['review_text'].tolist()
review_string_post = ' '.join(str(e) for e in review_list_post)
review_string_pre = ' '.join(str(e) for e in review_list_pre)

#                                    Character Frequency

def print_dict( d ):
    """Print frequency dictionary. Key is 'representation', v
    frequency of representation.

    Args:
      d (dict): Dictionary of (rep,freq) pairs
    """

    keys = list( d.keys() )
    keys.sort()

    for k in keys:
        print( f'{k}: {d[ k ]}; ', end='' )
    print( '' )

# Character representation, both w/ and w/o punctuation

# Convert to lower case, use regex to create a version with no punctuation

t = review_string_pre.lower()
t_no_punc = re.sub( r'[^\w\s]', '', t )

# Create punc, no punc dictionaries to hold character frequencies

char_dict = { }
char_dict_no_punc = { }

# Count characters in text w/punctuation

for c in t:
    char_dict[ c ] = ( 1 if c not in char_dict else char_dict[ c ] + 1 )

# Print results

print( 'Character frequency' )
print( char_dict )

for c in t_no_punc:
    char_dict_no_punc[ c ] = ( 1 if c not in char_dict_no_punc else char_dict_no_punc[ c ] + 1 )

print( 'Character frequency w/o punctuation' )
print( char_dict_no_punc )

#                                    Term Frequency Pat 1

# Term frequencies

# Convert text to lower-case term tokens

t = re.sub( r'[^\w\s]', '', review_string_pre )
tok = t.lower().split()

# Count term frequencies

d = { }
for term in tok:
    d[ term ] = ( 1 if term not in d else d[ term ] + 1 )

# Print results

print( 'Top 20 term frequencies' )
res = dict(sorted(d.items(), key = itemgetter(1), reverse = True)[:20])
print(res)

#                               NLTK Term Vectors

# Remove punctuation, then tokenize documents

punc = re.compile( '[%s]' % re.escape( string.punctuation ) )
term_vec = [ ]

for d in review_list_pre:
    d = d.lower()
    d = punc.sub( '', d )
    term_vec.append( nltk.word_tokenize( d ) )

#                               NLTK Stop Words

# Remove stop words from term vectors

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words( 'english' )

for i in range( 0, len( term_vec ) ):
    term_list = [ ]

    for term in term_vec[ i ]:
        if term not in stop_words:
            term_list.append( term )

    term_vec[ i ] = term_list
    
#                             Term Frequency Part 2

# Term frequencies

# Create flatList

flatList = [ item for elem in term_vec for item in elem]

# Count term frequencies

d = { }
for term in flatList:
    d[ term ] = ( 1 if term not in d else d[ term ] + 1 )

# Print results

print( 'Top 20 Term frequencies - No Stop Words' )
res = dict(sorted(d.items(), key = itemgetter(1), reverse = True)[:20])
print(res)