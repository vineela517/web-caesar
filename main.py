from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="POST">
        <label for="rot">Rotate by:</label>
        <input id="rot" type="text" name="rot" value="0"/>
        <br>
        <textarea name="text"></textarea>
        <br>
        <input type="submit" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    Rot = int(request.form['rot'])
    Text = request.form['text']
    result = rotate_string(Text,Rot)
    return "<h1>" + result + "</h1>"

app.run()