from flask import Flask, render_template, request
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uploaded", methods = ['GET', 'POST'])
def uploaded():
    if request.method == 'POST':
        file = request.files['file']
        
        if file.filename[-4:] != ".csv":
            return render_template("index.html", message = "Must upload a .csv file")        

        
        
        file.save(secure_filename("geocoded_" + file.filename))
    else:
        return redirect('/')
    # return render_template("uploaded.html")

if __name__ == '__main__':
    app.debug = True
    app.run()