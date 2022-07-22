import os
from datetime import datetime as dt
from flask import Flask, render_template, request, redirect
import flask.cli
import threading
import datetime

flask.cli.show_server_banner = lambda *args: None

app = Flask(__name__, template_folder='Templates')
format = "%B %d, %Y  %H:%M:%S"
datetime = datetime.datetime


@app.route("/")
def home():
    return render_template('home.html', titre="Welcome on the SecureCodeProject !")


@app.route('/date')
def date():
    format = "%B %d, %Y  %H:%M:%S"
    date = request.args.get('formatUser')

    if (date == "help"):
        return render_template('help.html', la_date=date)

    elif (date == "show"):
        todayDate = datetime.now().strftime(format)
        return render_template('date.html', la_date=todayDate)

    elif (date == "reset"):
        format = "%B %d, %Y  %H:%M:%S"
        return render_template('home.html')

    else:
        format = date
        if (format == datetime.now().strftime(format)):
            return render_template('error.html')
        else:
            todayDate = datetime.now().strftime(format)
            return render_template('date.html', la_date=todayDate)


@app.route('/help')
def help():
    return render_template('help.html')


def setDate():
    tmp = input("Please enter the date (YYYY-MM-DD) or the time (HH:MM:SS) :")

    if (datetime):
        timestamp = float(os.popen("date -d " + tmp + " +%s").read())
        return timestamp
    else:
        print("Error in Date")
        setDate()

def main():
    thread_flask = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=3000, use_reloader=False))
    thread_flask.start()

    while True:
        print("Choose what you want to do : ")
        print(" - 'changeDate' to change the date")
        valueInput = input()

        if valueInput == "changeDate":
            timestamp_send = setDate()
            os.system("sudo python3 timeChange.py " + str(timestamp_send))
            pass
        elif valueInput == 'quit':
            exit(0)


if __name__ == '__main__':
    main()
