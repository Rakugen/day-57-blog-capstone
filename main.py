from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

# Creating list of all posts to be used in home() and blog() functions
post_list = []
response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")

for post in response.json():
    new_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_list.append(new_post)

# TODO: modify home page to show blog names and links
#   then have the links redirect to its individual blog page
@app.route('/')
def home():

    return render_template("index.html", posts=post_list)

# TODO: create get_blog route and render all blog posts from npoint https://api.npoint.io/c790b4d5cab58020d391
@app.route('/blog/<num>')
def get_blog(num):
    # Search post_list for a post with id of num
    found_post = 0
    for current_post in post_list:
        if current_post.post_id == num:
            found_post = current_post

    return render_template("post.html", post=found_post)


if __name__ == "__main__":
    app.run(debug=True)
