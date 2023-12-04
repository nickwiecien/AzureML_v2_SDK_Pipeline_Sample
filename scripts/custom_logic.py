import pandas as pd
import numpy as np
import nltk
import matplotlib
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pyodbc
import spacy
import re
from pandarallel import pandarallel
import unicodedata
import matplotlib.pyplot as plt
import string
from tkinter.tix import TEXT
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from string import digits
from itertools import combinations

import numpy as np
import pyodbc
import pandas as pd
 
import snowflake.connector
import os

# Parse input arguments
parser = argparse.ArgumentParser("Get arguments relevant for job execution")
parser.add_argument('--result_count', type=int, required=True)

args, _ = parser.parse_known_args()
result_count = args.result_count


####################### FUNCTIONAL EXECUTION BLOCK #######################

nltk.download('stopwords')
english_stopwords = stopwords.words('english')

results = []

for i in range(result_count):
    results.append(random.uniform(0,100))
    
print(results)
print()
print(len(results))

##########################################################################