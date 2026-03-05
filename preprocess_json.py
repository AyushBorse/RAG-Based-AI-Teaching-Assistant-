import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib


def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )

    data = r.json()

    if "embeddings" not in data:
        print("API Error:", data)
        return []

    return data["embeddings"]


jsons = os.listdir("jsons")   # list all json files
my_dicts = []
chunk_id = 0


for json_file in jsons:

    with open(f"jsons/{json_file}") as f:
        content = json.load(f)

    print(f"Creating Embeddings for {json_file}")

    texts = []
    valid_chunks = []

    # Filter valid chunks
    for c in content['chunks']:

        text = c.get("text", "")

        if text is None:
            continue
        
        if isinstance(text, float):
            continue

        text = str(text).strip()

        if text == "" or text.lower() == "nan":
            continue

        texts.append(text)
        valid_chunks.append(c)

    # Skip file if no valid text
    if len(texts) == 0:
        continue

    embeddings = create_embedding(texts)

    # Safety check
    if len(embeddings) != len(valid_chunks):
        print("Embedding mismatch in", json_file)
        continue

    # Attach embeddings
    for i, chunk in enumerate(valid_chunks):

        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]

        chunk_id += 1
        my_dicts.append(chunk)


# Convert to dataframe
df = pd.DataFrame.from_records(my_dicts)

# Save embeddings
joblib.dump(df, "embeddings.joblib")

print("Embeddings saved successfully")