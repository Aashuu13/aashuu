from flask import Flask, render_template_string, request, redirect, session
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "insta_full_project"

UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        username TEXT,
        content TEXT,
        media_type TEXT,
        media_path TEXT,
        likes INTEGER DEFAULT 0,
        time TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY,
        post_id INTEGER,
        username TEXT,
        comment TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS follows (
        id INTEGER PRIMARY KEY,
        follower TEXT,
        following TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS notifications (
        id INTEGER PRIMARY KEY,
        user TEXT,
        message TEXT
    )""")

    conn.commit()
    conn.close()


init_db()


# ---------------- UI ----------------
UI = """
<!DOCTYPE html>
<html>
<head>
<title>Instagram Clone</title>

<style>
body { margin:0; font-family:Arial; background:#fafafa; }

.sidebar {
    width:220px;
    height:100vh;
    background:#111827;
    color:white;
    position:fixed;
    padding:20px;
}

.sidebar h2 { color:#60a5fa; }

.sidebar a {
    display:block;
    color:white;
    padding:10px;
    text-decoration:none;
    margin-top:10px;
}

.sidebar a:hover { background:#374151; }

.main {
    margin-left:240px;
    padding:20px;
}

.card {
    background:white;
    padding:15px;
    margin:15px 0;
    border-radius:10px;
    box-shadow:0 2px 6px rgba(0,0,0,0.1);
}

button {
    background:#3b82f6;
    color:white;
    border:none;
    padding:5px 10px;
    border-radius:5px;
    cursor:pointer;
}

button:hover { background:#2563eb; }

input, select {
    padding:8px;
    margin:5px;
}
</style>
</head>

<body>

<div class="sidebar">
    <h2>📸 InstaClone</h2>
    <a href="/">🏠 Feed</a>
    <a href="/explore">🔍 Explore</a>
    <a href="/reels">🎬 Reels</a>
    <a href="/notifications">🔔 Notifications</a>
    <a href="/logout">🚪 Logout</a>
</div>

<div class="main">

<h1>🔥 Instagram Feed</h1>

{% if session.get('user') %}
<p>Logged in as <b>{{session['user']}}</b></p>
{% else %}
<form method="POST" action="/login">
<input name="username" placeholder="Username">
<input name="password" placeholder="Password">
<button>Login</button>
</form>

<form method="POST" action="/register">
<input name="username" placeholder="New Username">
<input name="password" placeholder="New Password">
<button>Register</button>
</form>
{% endif %}

<hr>

{% if session.get('user') %}
<form method="POST" action="/post" enctype="multipart/form-data">

<input name="content" placeholder="Write caption..." required>

<select name="media_type">
    <option value="text">Text</option>
    <option value="image">Photo 📸</option>
    <option value="video">Reel 🎬</option>
</select>

<input type="file" name="media">

<button>Post</button>
</form>
{% endif %}

<hr>

{% for p in posts %}

<div class="card">

<h3>👤 {{p[1]}}</h3>
<p>{{p[2]}}</p>
<small>{{p[6]}}</small>

{% if p[3] == "image" and p[4] %}
    <img src="{{p[4]}}" width="250">

{% elif p[3] == "video" and p[4] %}
    <video width="250" controls autoplay loop>
        <source src="{{p[4]}}">
    </video>
    <p>🎬 Reel</p>
{% endif %}

<p>❤️ {{p[5]}} likes</p>

<a href="/like/{{p[0]}}"><button>Like</button></a>
<a href="/follow/{{p[1]}}"><button>Follow</button></a>

<form method="POST" action="/comment/{{p[0]}}">
<input name="comment" placeholder="Comment">
<button>Send</button>
</form>

{% for c in comments %}
    {% if c[1] == p[0] %}
        <p>💬 <b>{{c[2]}}</b>: {{c[3]}}</p>
    {% endif %}
{% endfor %}

</div>

{% endfor %}

</div>
</body>
</html>
"""


# ---------------- ROUTES ----------------
@app.route("/")
def home():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    posts = c.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    comments = c.execute("SELECT * FROM comments").fetchall()

    conn.close()

    return render_template_string(UI, posts=posts, comments=comments)


# -------- REGISTER --------
@app.route("/register", methods=["POST"])
def register():
    u = request.form["username"]
    p = request.form["password"]

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users VALUES (NULL,?,?)", (u, p))
    except:
        pass

    conn.commit()
    conn.close()

    return redirect("/")


# -------- LOGIN --------
@app.route("/login", methods=["POST"])
def login():
    session["user"] = request.form["username"]
    return redirect("/")


# -------- LOGOUT --------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# -------- POST --------
@app.route("/post", methods=["POST"])
def post():
    if "user" not in session:
        return redirect("/")

    content = request.form["content"]
    media_type = request.form["media_type"]
    time = str(datetime.now())

    file = request.files.get("media")
    path = None

    if file:
        path = os.path.join("static", file.filename)
        file.save(path)

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""INSERT INTO posts 
        VALUES (NULL,?,?,?,?,0,?)""",
        (session["user"], content, media_type, path, time))

    conn.commit()
    conn.close()

    return redirect("/")


# -------- LIKE --------
@app.route("/like/<int:id>")
def like(id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("UPDATE posts SET likes = likes + 1 WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


# -------- COMMENT --------
@app.route("/comment/<int:id>", methods=["POST"])
def comment(id):
    text = request.form["comment"]

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("INSERT INTO comments VALUES (NULL,?,?,?)",
              (id, session.get("user","Guest"), text))

    conn.commit()
    conn.close()

    return redirect("/")


# -------- FOLLOW --------
@app.route("/follow/<user>")
def follow(user):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("INSERT INTO follows VALUES (NULL,?,?)",
              (session.get("user","Guest"), user))

    c.execute("INSERT INTO notifications VALUES (NULL,?,?)",
              (user, f"{session.get('user')} followed you"))

    conn.commit()
    conn.close()

    return redirect("/")


# -------- EXPLORE --------
@app.route("/explore")
def explore():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    posts = c.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return "<h1>Explore Page</h1>" + str(posts)


# -------- REELS --------
@app.route("/reels")
def reels():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    reels = c.execute("SELECT * FROM posts WHERE media_type='video'").fetchall()
    conn.close()
    return "<h1>Reels 🎬</h1>" + str(reels)


# -------- NOTIFICATIONS --------
@app.route("/notifications")
def notifications():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    notes = c.execute("SELECT message FROM notifications WHERE user=?",
                      (session.get("user","Guest"),)).fetchall()

    conn.close()

    return "<h1>Notifications</h1>" + "<br>".join([n[0] for n in notes])


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)