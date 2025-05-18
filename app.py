from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("treatments.json", "r", encoding="utf-8") as f:
    treatments = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    mutation = request.form["mutation"]
    histology = request.form["histology"]

    for regimen in treatments:
        if regimen["mutation"] == mutation and regimen["histology"] == histology:
            return render_template("result.html", regimen=regimen)

    return "該当する治療レジメンが見つかりませんでした"

if __name__ == "__main__":
    app.run(debug=True)