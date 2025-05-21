# app.py
from flask import Flask, request, render_template_string
from recommend import recommend_movies

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<title>Movie Recommender</title>
<h2>AI Movie Recommender</h2>
<form method="POST">
    Enter a Movie Title: <input name="movie">
    <input type="submit" value="Recommend">
</form>
{% if recommendations %}
    <h3>Top Recommendations:</h3>
    <ul>
    {% for movie in recommendations %}
        <li>{{ movie }}</li>
    {% endfor %}
    </ul>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    if request.method == "POST":
        movie = request.form["movie"]
        recommendations = recommend_movies(movie)
    return render_template_string(HTML_TEMPLATE, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
