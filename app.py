from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# 治療レジメンデータを読み込む
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
    port = int(os.environ.get("PORT", 5000))  # Renderが使う環境変数PORTを利用
    app.run(host="0.0.0.0", port=port)
