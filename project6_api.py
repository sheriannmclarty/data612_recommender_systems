from bias_adjusted_model import BiasAdjustedRecommender

from flask import Flask, request, jsonify
import pickle
import pandas as pd
import traceback

# === Load data ===
df = pd.read_csv("filtered_skintone_reviews.csv", low_memory=False, dtype={"product_name_x": str})
df = df.dropna(subset=['author_id', 'product_name_x', 'rating_x'])
df['rating_x'] = pd.to_numeric(df['rating_x'], errors='coerce')
df['user'] = df['author_id'].astype('category').cat.codes
df['item'] = df['product_name_x'].astype('category').cat.codes

# === Load model and metadata ===
with open("project1_model.pkl", "rb") as f:
    loaded = pickle.load(f)
    print("📦 Loaded type:", type(loaded))

if isinstance(loaded, tuple) and hasattr(loaded[0], 'recommend'):
    model, item_to_meta = loaded
else:
    raise ValueError("❌ Model load failed — object is not a valid recommender.")

print("🎯 Model type:", type(model))
print("🎯 Item meta sample:", list(item_to_meta.items())[:1])

# === Flask app ===
app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        user_id = data['user_id']
        top_n = data.get('top_n', 5)

        recommendations = model.recommend(user_id, top_n=top_n)

        for rec in recommendations:
            meta = item_to_meta.get(rec['item'], {})
            rec['product_name'] = meta.get('product_name_x', 'Unknown')
            rec['brand_name'] = meta.get('brand_name_x', 'Unknown')

        return jsonify({"recommendations": recommendations})

    except Exception as e:
        print("🔥 ERROR:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
