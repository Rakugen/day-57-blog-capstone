from flask import Flask, render_template
from post import Post
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# TODO: create get_blog route and render all blog posts from npoint https://api.npoint.io/c790b4d5cab58020d391
@app.route('/blog')
def get_blog():
    post_list = []
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    for post in posts:
        new_post = Post()
        post_list.append(new_post)

    pass


if __name__ == "__main__":
    app.run(debug=True)
