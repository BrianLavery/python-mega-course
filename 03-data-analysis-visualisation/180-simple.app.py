import justpy as jp # naming convention

# Justpy uses some quasar framework that is built in Javascript
# We create an app function that returns the quasar page
def app():
    # Create the webpage then add elements
    wp = jp.QuasarPage() 
    
    # Add elements and connect to the web page - the order matters
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis")

    # Return page with added elements
    return wp

# Justpy below takes care of executing function
jp.justpy(app)


