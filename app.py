from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema Clothes4Happiness rodando com CI/CD e Docker 🚀"

@app.route("/status")
def status():
    return {"status": "online", "sistema": "Clothes4Happiness"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

print("POC DevOps funcionando")