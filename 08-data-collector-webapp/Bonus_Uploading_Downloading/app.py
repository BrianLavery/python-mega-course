from flask import Flask, render_template, request, send_file
from send_email import send_email
from werkzeug.utils import secure_filename, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file # Want file to be accessed throughout python script
    if request.method == 'POST':
        file = request.files['file']
         # You save file using same name user submitted - use secure filename to in case hackers point to sever root then have a base file
        file.save(secure_filename("uploaded_" + file.filename))
        # Can modify files
        with open("uploaded_" + file.filename, "a") as f:
            f.write("\n\nThis was added later!")
        # content = file.read() # You can read the content of this object (if desired)
        return render_template("index.html", btn="download.html")

@app.route("/download")
def download():
    return send_file("uploaded_" + file.filename, attachment_filename =  "yourfile.py", as_attachment = True)

if __name__ == '__main__':
    app.debug = True
    app.run() # Can pass in specific port here if want