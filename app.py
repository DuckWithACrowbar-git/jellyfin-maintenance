from flask import Flask, render_template
import json
import datetime import datetime


app = Flask(__name__)

scheduled_date = '{"from": "Sep. 4 at 8:00 AM", "to": "Sep. 7 at 5:00 PM"}'
countdown_info = '{"from": "", "to": ""}'
date_data = json.loads(scheduled_date)

# (Year, Month, Day, Hour, Minute, Second)
start_epoch = datetime(2026, 9, 4, 8, 0, 0)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")


def catch_all(path):
  return render_template("index.html", start_date=date_data["from"], end_date=date_data["to"])


if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=9000)
