from flask import Flask, request, jsonify
import pickle

# Copy your class definition here 👇
class BiasAdjustedRecommender:
    def __init__(self, user_biases, item_biases, global_avg, ratings_df):
        self.user_biases = user_biases
        self.item_biases = item_biases
        self.global_avg = global_avg
        self.ratings_df = ratings_df

    def predict(self, user, item):
        return self.global_avg + self.user_biases.get(user, 0) + self.item_biases.get(item, 0)

    def recommend(self, user_id, top_n=5):
        user_rated = self.ratings_df[self.ratings_df['user'] == user_id]['item'].tolist()
        all_items = set(self.ratings_df['item'])
        unseen_items = all_items - set(user_rated)

        predictions = []
        for item in unseen_items:
            score = self.predict(user_id, item)
            predictions.append((item, score))

        predictions.sort(key=lambda x: x[1], reverse=True)
        return [{"item": int(item), "predicted_rating": round(score, 2)} for item, score in predictions[:top_n]]

# --- Flask App Stuff ---
app = Flask(__name__)

with open("project1_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_id = data.get("user_id")
    top_n = data.get("top_n", 5)

    try:
        recommendations = model.recommend(user_id=int(user_id), top_n=top_n)
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
