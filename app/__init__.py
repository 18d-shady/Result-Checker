from flask import Flask

app = Flask(__name__)
app.secret_key = 'Shady'

from app import route


app.run(debug=True)

