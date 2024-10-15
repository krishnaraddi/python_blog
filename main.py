from flask import Flask, request, render_template
from post import Post
import requests
import smtplib
MY_EMAIL="dotindia@gmail.com"
MY_PASSWORD="pwmvwehbklkeyybj"

all_posts = requests.get("https://api.npoint.io/ee090630474f77a9b6d7").json()
 
 

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=all_posts)

@app.route('/about')
def get_about():
    return render_template("about.html")

 

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


     
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        message=f'name :  {data["name"] } \n email: { data["email"] }  \n phone : { data["phone"] }  \n message : {data["message"]}'
        # print(data["name"])
        # print(data["email"])
        # print(data["phone"])
        # print(data["message"])
        with smtplib.SMTP("smtp.gmail.com" ) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="krishnaraddi@gmail.com", msg=f"Subject:Email from website : \n\n {message}") 
            return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)