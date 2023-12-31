try:
    from flask import Flask, render_template
    from flask import request
    import numpy as np

    import uuid
    import os
    import json

    from datetime import datetime
    from flask import request

    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
    import elasticsearch
    from elasticsearch import Elasticsearch
    from elasticsearch import helpers

    from tqdm.auto import tqdm

    from dotenv import load_dotenv

    load_dotenv(".env")

except Exception as e:
    print("Error", e)

app = Flask(__name__)


class Tokenizer(object):

    @staticmethod
    def get_token(documents):
        sentences = [documents]
        sentence_embeddings = model.encode(sentences)
        encod_np_array = np.array(sentence_embeddings)
        encod_list = encod_np_array.tolist()
        return encod_list[0]


def create_scroll(raw_response):
    try:
        data = raw_response.get("hits", None).get("hits", None)
        if not data: return None
        data = data[-1]
        score = data.get("_score", 1)
        scroll_id_ = data.get("_id", None)
        unique_scroll_id = "{},{}".format(score, scroll_id_)
        return unique_scroll_id

    except Exception as e:
        return ""


class Search(object):
    def __init__(self, user_query):
        self.user_query = user_query
        self.vector = Tokenizer.get_token(documents=self.user_query)

        self.es = Elasticsearch(hosts="http://localhost:9200/",
                                http_auth=("elastic",
                                           "nP-c7JvEobVFgiKxct3r"
                                           )
                                )

    def get_query(self):
      return {
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "post_title": {
                                "query": self.user_query,
                                "boost": 2.0,
                                "fuzziness": "auto"
                            }
                        }
                    },
                    {
                        "match": {
                            "post_content": {
                                "query": self.user_query,
                                "boost": 1.0,
                                "fuzziness": "auto"
                            }
                        }
                    }
                ]
            }
        },
        "sort": [
            {
                "_score": {
                    "order": "desc"
                }
            },
            {
                "date": {
                    "order": "desc"
                }
            }
        ]
    }

    def search(self, size=50, scroll_id=None):
        if scroll_id is None:
            res = self.es.search(index="sa",
                                 size=size,
                                 body=self.get_query(),
                                 request_timeout=55)

            scroll_id = create_scroll(res)

            return res, scroll_id
        else:
            pass


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/ingest", methods=["GET", "POST"])
def ingest():
    return render_template("ingest.html")


@app.route("/get_results", methods=["GET", "POST"])
def get_results_data():
    try:
        request_data = dict(request.form)
        user_inputs = json.loads(request_data.get("data")).get("user_inputs")

        search_helper = Search(user_query=user_inputs)
        json_data, scroll_id = search_helper.search()

        results = json_data['hits']['hits']
        sorted_results = sorted(results, key=lambda x: x['_source'].get('date'), reverse=True)
        data_cards = []

        for hit in sorted_results:
            json_payload = {}
            for key, value in hit['_source'].items():
                json_payload[key] = value
            json_payload['_score'] = hit['_score']
            data_cards.append(json_payload)

        total_hits = 0

        try:
            total_hits = json_data['hits']['total']['value']
        except Exception as e:
            pass

        return {"data": data_cards, "total_hits": total_hits, "scroll_id": scroll_id}

    except Exception as e:
        print("Error", e)
        return "error"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
