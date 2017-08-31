#import the Flask class
from flask import Flask, flash, redirect, render_template, request, session, abort

#create an instance of this class
app = Flask(__name__)

#use route() decorator to tell Flask what URL should trigger our function

#first create a page that puts three point on a map

@app.route("/")
def php():
    data = {'key 1': "53.5452368123344,-113.478794038578",
            "key 2": "53.5209960948731,-113.465662036198",
            "key 3": "53.5777594400968,-113.535932328747",
            "key 4": "53.544594580565,-113.497389149595"}
    return render_template('pointsOnMap.html', id_latlon = data)


if __name__ == "__main__":
    app.run(host='162.106.216.28', port = 4000, debug=True)

