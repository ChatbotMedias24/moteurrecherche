import pandas as pd
import numpy as np
import json
import os
import uuid


from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
import elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch import helpers

from tqdm.auto import tqdm
tqdm.pandas()

class Tokenizer(object):
    def __init__(self):
        self.model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

    def get_token(self, documents):
        sentences  = [documents]
        sentence_embeddings = self.model.encode(sentences)
        encod_np_array = np.array(sentence_embeddings)
        encod_list = encod_np_array.tolist()
        return encod_list[0]


token_instance = Tokenizer()

ENDPOINT='http://localhost:9200/'
USERNAME='elastic'
PASSWORD='nP-c7JvEobVFgiKxct3r'
es=Elasticsearch(hosts=[ENDPOINT],http_auth=(USERNAME,PASSWORD))
es.ping()
df=pd.read_csv('datafinal.csv')
elk_data=df.to_dict("records")

for x in elk_data:
    if 'lien' in x and 'post_content' in x and 'summary' in x and 'date' in x and 'post_title' in x :
        try:
            _ = {
                "post_title": x.get("post_title", ""),
                "post_content":x.get("post_content",""),
                "lien":x.get("lien",""),
                "summary":x.get("summary",""),
                "date":x.get("date",""),




                
            }
            es.index(index='sea', body=_)
        except Exception as e:
            print(f"Erreur lors de l'indexation : {e}")
    else:
        print("Les clés 'post_title' et 'vectors' ne sont pas présentes dans l'objet elk_data")