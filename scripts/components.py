from mldesigner import command_component
import os
from pathlib import Path

@command_component(display_name='Custom Processing Routine', 
                   environment=dict(
                        conda_file=Path(__file__).parent / "../environment.yml",
                        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04",
                    ),
                   is_deterministic=False
                  )
def processing_routine(result_count: int):
    
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
    import random
    
    ####################### FUNCTIONAL EXECUTION BLOCK #######################
    
    from azure.identity import DefaultAzureCredential
    from azure.keyvault.secrets import SecretClient

    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url="https://<YOUR-KEY-VAULT>.vault.azure.net/", credential=credential)
    
    secret = secret_client.get_secret("test")
    print(secret.value)

    nltk.download('stopwords')
    english_stopwords = stopwords.words('english')
    
    print(english_stopwords)

    results = []

    for i in range(result_count):
        results.append(random.uniform(0,100))

    print(results)
    print()
    print(len(results))

    ##########################################################################
