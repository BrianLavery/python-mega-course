# Import the Flask class not the module
from flask import Flask

app = Flask(__name__) # Instantiate the Flask class

# Set the route and then a method to define what happens when go to that route
@app.route('/')
def home():
    return "Website content goes here!"

# When you execute a script then python assigns __name__ == "__main__"
# If a script imported python assigns __name__ == "script1"
# So means this file could be imported into another file
if __name__ == "__main__": 
    app.run(debug = True)

