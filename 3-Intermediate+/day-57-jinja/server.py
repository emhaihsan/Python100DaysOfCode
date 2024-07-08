from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.now().year
    return render_template('index.html', year=year) 

@app.route('/guess/<name>')
def guess(name):
    age_endpoint = 'https://api.agify.io?name={}'.format(name)
    gender_endpoint = 'https://api.genderize.io?name={}'.format(name)
    age = requests.get(age_endpoint).json()['age']
    gender = requests.get(gender_endpoint).json()['gender']
    return render_template('guess.html', name=name.title(),age=age, gender=gender)

@app.route('/blog')
def blog():
    blog_url = "https://www.npoint.io/docs/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template('blog.html', posts=all_posts)
if __name__ == "__main__":
    app.run(debug=True)
