from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME")
    env = os.getenv("ENV")
    return f"{app_name} running in {env} mode"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




