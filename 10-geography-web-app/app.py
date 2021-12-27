from flask import Flask, render_template, request, send_file
from werkzeug.utils import redirect, secure_filename
import pandas
from geopy.geocoders import ArcGIS
import datetime

app = Flask(__name__)
nom = ArcGIS()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uploaded", methods = ['GET', 'POST'])
def uploaded():
    global filename
    if request.method == 'POST':
        file = request.files['file']
        
        # Check they uploaded CSV file
        if file.filename[-4:] != ".csv":
            return render_template("index.html", error_message = "Must upload a .csv file")

        # Check that there is an address/ Address column
        df = pandas.read_csv(file)
        if "address" not in (column.lower() for column in df.columns):
            return render_template("index.html", error_message = "File must contain a column named 'Address' or 'address'")
        
        # Replace any columns with "Address" with address
        df.rename(columns={'Address': 'address'}, inplace = True)
        
        # Add a latitude and longitude column to the dataframe
        lats = []
        longs = []

        for index, row in df.iterrows():
            coord = nom.geocode(row["address"], timeout = None)
            lats.append(coord.latitude if coord != None else None)
            longs.append(coord.latitude if coord != None else None)
        
        df['Latitude'] = lats
        df['Longitude'] = longs

        filename = datetime.datetime.now().strftime("uploads/%Y-%m-%d-%H-%M-%S-%f.csv")
        # df.to_csv("./uploads/" + secure_filename("geocoded_" + file.filename))
        df.to_csv(filename, index = None)
        return render_template("uploaded.html", tables=[df.to_html(classes='data', header="true")])
    else:
        return redirect('/')

@app.route("/download")
def download():
    return send_file(filename, attachment_filename =  "geocoded.csv", as_attachment = True)


if __name__ == '__main__':
    app.debug = True
    app.run()