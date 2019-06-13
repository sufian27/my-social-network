from flask import Flask, render_template, request
import requests, json
import sqlite3

conn = sqlite3.connect("posts.sqlite", check_same_thread = False)
c = conn.cursor()
c.execute('''
	CREATE TABLE IF NOT EXISTS posts (
	user_id INTEGER, post_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, body TEXT)''')

app = Flask(__name__)


@app.route("/")
def display_home():
	# for i in range(1, 11):
	# 	r = requests.get("https://jsonplaceholder.typicode.com/posts?userId=" + str(i))
	# 	info = json.loads(r.text)
	# 	for x in info:
	# 		c.execute("INSERT OR IGNORE INTO posts (user_id, title, body) VALUES (?, ?, ?)", (x["userId"], 
	# 			x["title"], x["body"],))
	# 		conn.commit() 
	# c.close()
	c.execute("SELECT * FROM posts")
	rows = c.fetchall()
	return render_template("index.html", rows = rows)

@app.route("/add")
def display_add():
	return render_template("add.html")

@app.route("/success", methods = ["POST"])
def display_success():
	c.execute("INSERT OR IGNORE INTO posts (user_id, title, body) VALUES (?, ?, ?)", 
		(request.form.get("user_id"), request.form.get("title"), request.form.get("body"),))
	conn.commit()
	return render_template("success.html")

@app.route("/remove")
def display_remove():
	return render_template("remove.html")

@app.route("/search")
def display_search():
	return render_template("search.html")