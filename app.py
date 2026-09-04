from flask import Flask, render_template
import json
from datetime import datetime
import threading as th
import time as t
import math as m


app = Flask(__name__)

#Change these variables for other maintenance times, leave others as is. (Thanks Mateo, you're the GOAT!)
scheduled_start_date = '{"year": "2026", "month": "09", "day": "04", "hour": "17", "minute": "00", "second": "00"}'
scheduled_end_date = '{"year": "2026", "month": "09", "day": "07", "hour": "17", "minute": "00", "second": "00"}'


start_data = json.loads(scheduled_start_date)
start_date_pretty = str(start_data["month"]) + "/" + str(start_data["day"]) + " at " + str(start_data["hour"]) + ":" + str(start_data["minute"])

end_data = json.loads(scheduled_end_date)
end_date_pretty = str(end_data["month"]) + "/" + str(end_data["day"]) + " at " + str(end_data["hour"]) + ":" + str(end_data["minute"])

remaining_epoch = "Calculating..."


def app_run():
  app.run(debug=False, host="0.0.0.0", port=9000)


def update_countdown():
  global remaining_epoch
  end_epoch = datetime(
        year=int(end_data["year"]),
        month=int(end_data["month"]),
        day=int(end_data["day"]),
        hour=int(end_data["hour"]),
        minute=int(end_data["minute"]),
        second=int(end_data["second"])
    ).timestamp()
  while True:
        current_epoch = t.time()
        remaining_epoch = int(end_epoch - current_epoch)
        remaining_epoch = remaining_epoch // 60
        t.sleep(1)




@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")


def catch_all(path):
  return render_template("index.html", start_date=start_date_pretty, end_date=end_date_pretty, remaining_time=remaining_epoch), 200

if __name__ == "__main__":
  print("Thank you so much Mateo for help with the HTML and CSS.")
  print("Your work is appreciated!")
  try:
    th.Thread(target=app_run).start()            #Main website server thingy-ma-bob
    th.Thread(target=update_countdown).start()   #Calculates time between the maintenance start time and end time in mins 
  except KeyboardInterrupt:
     exit()