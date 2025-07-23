import requests
import pandas as pd

# Load mapping from CSV
df = pd.read_csv("filtered_skintone_reviews.csv", low_memory=False)
df['author_id'] = df['author_id'].astype(str)
df['user'] = df['author_id'].astype('category').cat.codes

# Lookup encoded user_id
raw_id = "23866342710"
encoded_id = df[df['author_id'] == raw_id]['user'].iloc[0]


# Send request
url = "http://127.0.0.1:5000/recommend"
payload = {
    "user_id": int(encoded_id),
    "top_n": 5
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
try:
    print("Response:", response.json())
except Exception as e:
    print("❌ Error decoding JSON:", e)
    print("Raw text:", response.text)
