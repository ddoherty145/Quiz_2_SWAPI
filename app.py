from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    character_data = {}
    if request.method == "POST":
        character_id = request.form.get("character_id")
        if character_id:
            try:
                response = requests.get("https://swapi.py4e.com/api/people/{character_id}/")
                if response.status_code == 200:
                    character_data = response.json()
                else:
                    character_data = {"error": "Character not found"}
            except Exception as e:
                character_data = {"error": str(e)}

    return render_template("index.html", character_data=character_data)

if __name__ == "__main__":
    app.run(debug=True)