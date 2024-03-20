from flask import Flask, redirect, request, render_template, session, url_for
import json


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    if 'logged_in' in session:
        return render_template("success.html")
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "ciao" and password == "123A":
            session['logged_in'] = username
            res = {"res": "Username e password inseriti correttamente"}
    else:
        res = "errore"
    return redirect(url_for("index"))

@app.route('/logout',methods=["POST"])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", ssl_context=('cert.pem', 'key.pem'))
