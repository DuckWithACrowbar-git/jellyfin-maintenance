from flask import Flask, render_template
import json

app = Flask(__name__)

scheduled_date = '{"from": "Sep. 5", "to": "Sep. 7"}'
date_data = json.loads(scheduled_date)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")


def catch_all(path):
  return render_template("index.html", start_date=date_data["from"], end_date=date_data["to"])


if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=9000)
