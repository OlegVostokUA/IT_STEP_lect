import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwerty'


def get_db_connection():
    conn = sqlite3.connect('blog_db.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute("""SELECT * FROM posts""").fetchall()
    conn.close()
    return render_template('index.html', posts_html=posts)


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute("""SELECT * FROM posts WHERE id == ?""",
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/<int:post_id>')
def post_render(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required')
        else:
            conn = get_db_connection()
            conn.execute("""INSERT INTO posts (title, content) VALUES (?,?)""",
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):

    post = get_post(post_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required')
        else:
            conn = get_db_connection()
            conn.execute("""UPDATE posts SET title = ?, content = ? WHERE id = ?""",
                         (title, content, post_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:post_id>/delete', methods=('GET', 'POST'))
def delete(post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        conn = get_db_connection()
        conn.execute("""DELETE FROM posts WHERE id = ?""", (post_id,))
        conn.commit()
        conn.close()
        flash('Post deleted')
        return redirect(url_for('index'))
    return render_template('delete.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)