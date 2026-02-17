import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
data = {
    "title": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Batman Begins",
        "The Prestige",
        "Titanic",
        "The Notebook",
        "Avengers",
        "Iron Man",
        "Doctor Strange"
    ],
    "genre": [
        "Sci-Fi Thriller",
        "Sci-Fi Drama",
        "Action Crime",
        "Action Adventure",
        "Drama Mystery",
        "Romance Drama",
        "Romance",
        "Action Superhero",
        "Action Superhero",
        "Fantasy Superhero"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["genre"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend(movie_name):
    movie_name = movie_name.strip()

    if movie_name not in df["title"].values:
        print("Movie not found in database.")
        return

    idx = df[df["title"] == movie_name].index[0]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print(f"\nTop 5 recommendations for '{movie_name}':\n")

    count = 0
    for i in similarity_scores:
        if df.iloc[i[0]]["title"] != movie_name:
            print(df.iloc[i[0]]["title"])
            count += 1
        if count == 5:
            break


# 🔁 Continuous loop
while True:
    user_input = input("\nEnter a movie name (or type 'quit' to exit): ")

    if user_input.lower() == "quit":
        print("Exiting recommendation system. Goodbye!")
        break

    recommend(user_input)
