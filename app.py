from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests

app = Flask(__name__)

# Load the recommendation model
file = pickle.load(open('rec.pkl', 'rb'))
df = pd.DataFrame(file)

def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYzE3Njc1MDRiOGIyMTY2MzZlOTMwYzhkNGVmOTlhMyIsIm5iZiI6MTc0NzYwOTEzMC40MTUsInN1YiI6IjY4MmE2NjJhZWVlYzU0MjNkOTBiZDUzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pXD_0czbpVZGC6Le85fCk74_HBVZul_Wiuq3J0BSyj4"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    title = data.get('title', 'N/A')
    poster = "https://image.tmdb.org/t/p/w500" + data.get('poster_path', '')
    return title, poster

@app.route("/", methods=["GET", "POST"])
def index():
    selected_movie = None
    recommendations = []

    if request.method == "POST":
        selected_movie = request.form.get("movie_title")
        if selected_movie:
            indices = df[df['title'] == selected_movie].iloc[0]['recommendations']
            for movie_id in indices[:5]:
                title, poster = get_movie_details(movie_id)
                recommendations.append({"title": title, "poster": poster})

    movie_titles = df['title'].tolist()
    return render_template("index.html", movies=movie_titles, selected=selected_movie, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
