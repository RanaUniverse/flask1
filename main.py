"""
This is for my practise of flask a little
"""

from flask import Flask, request


app = Flask(__name__)

from flask import url_for


@app.route("/")
def index():
    abc_data = request.args
    print("abc data is", abc_data)
    return f"<h1>This is index page<br>{abc_data}</h1>"


@app.route("/user/<username>")
def profile(username: str):
    return f"{username}'s profile"


def process_login():
    username = request.form.get("username")
    password = request.form.get("password")
    return f"""
    <h1>Login Successful</h1>
    <p>Username: {username}</p>
    <p>Password: {password}</p>
    <a href="/login">Go back</a>
    """


def render_login_form():
    return """
    <form method="post">
        <input type="text" id="username" name="username" required>
        <label for="username">Username:</label>
        <br>
        <input type="password" id="password" name="password" required>
        <label for="password">Password:</label>
        <br>
        <button type="submit">Login</button>
        
    </form>
    """


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return process_login()

    else:
        return render_login_form()


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="John Doe"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)