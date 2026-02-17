import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🔹 Sample Movie Dataset
data = {
    "title": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Avengers",
        "Titanic",
        "The Notebook",
        "John Wick",
        "The Matrix",
        "Gladiator",
        "The Conjuring"
    ],
    "genre": [
        "sci-fi thriller",
        "sci-fi space drama",
        "action crime thriller",
        "superhero action",
        "romance drama",
        "romance love drama",
        "action crime",
        "sci-fi action",
        "action historical drama",
        "horror supernatural"
    ]
}

df = pd.DataFrame(data)

# 🔹 Convert text data into numerical vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["genre"])

# 🔹 Compute similarity
similarity = cosine_similarity(tfidf_matrix)

print("🎬 Movie Recommendation System Ready!")
print("Type a movie name to get recommendations.")
print("Type 'quit' to exit.\n")

while True:
    movie_name = input("Enter movie name: ").strip()

    if movie_name.lower() == "quit":
        print("Exiting Recommendation System 👋")
        break

    if movie_name not in df["title"].values:
        print("Movie not found in database ❌\n")
        continue

    index = df[df["title"] == movie_name].index[0]
    similarity_scores = list(enumerate(similarity[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:")
    for i in similarity_scores[1:6]:
        print("-", df.iloc[i[0]]["title"])

    print()
