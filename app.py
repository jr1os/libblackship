from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\project_python\\libblackship\\foo.db'"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)


@app.route("/")
def index():
    posts = Post.query.order_by(Post.fecha.desc()).all()
    return render_template("index.html", posts=posts)

@app.route("/agregar")
def agregar():
    return render_template("agregar.html")