
from flask import Flask, jsonify
  
app = Flask(__name__)
@app.route('/')
def cricgfg():
  return "Harshitha Lakruwan"


if __name__ == "__main__":
    app.run(debug=True)
