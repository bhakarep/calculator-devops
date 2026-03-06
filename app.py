# app.py
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
   return "Hello Janu! Docker is running on port 5000 🚀"


if __name__ == "__main__":
   # Important: host=0.0.0.0 so container can expose it outside
   app.run(host="0.0.0.0", port=5000)
