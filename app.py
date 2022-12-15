# We need to create a new Python file and import our dependencies to our code environment.
# This will be the file we use to create our Flask application.
import datetime as dt
import numpy as np
import pandas as pd
# The dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database.# 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#  The code to import the dependencies that we need for Flask
from flask import Flask, jsonify
# The create_engine() function allows us to access and query our SQLite database file.
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the database into our classes.
Base = automap_base()
# With the database reflected, we can save our references to each table.
Base.prepare(engine, reflect=True)
# We'll create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station
# Finally, create a session link from Python to our database with the following code
session = Session(engine)
# Set Up Flask
# This will create a Flask application called "app."
app = Flask(__name__)
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
# Notice the __name__ variable in this code. 
# This is a special type of variable in Python. 
# Its value depends on where and how the code is run. 
#  For example, if we wanted to import our app.py file into another Python file named example.py, 
# the variable __name__ would be set to example.

# All of your routes should go after the app = Flask(__name__) line of code. Otherwise, your code may not run properly.
# Now our root, or welcome route, is set up. The next step is to add the routing information for each of the other routes
# For this we'll create a function, and our return statement will have f-strings as a reference to all of the other routes
# When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. 
# This convention signifies that this is version 1 of our application. 
#  This line can be updated to support future versions of the app as well.

# The next route we'll build is for the precipitation analysis. This route will occur separately from the welcome route.
# Every time you create a new route, your code should be aligned to the left in order to avoid errors. We will create the precipitation() function.
# Next, write a query to get the date and precipitation for the previous year. (.\ ) This is used to signify that we want our query to continue on the next line.
# Finally, we'll create a dictionary with the date as the key and the precipitation as the value. To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file.

# JSON files are structured text files with attribute-value pairs and array data types. They have a variety of purposes, especially when downloading information from the internet through API calls.
#  We can also use JSON files for cleaning, filtering, sorting, and visualizing data, among many other tasks. When we are done modifying that data, we can push the data back to a web interface, like Flask.

@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# With our route defined, we'll create a new function called stations()
# We want to start by unraveling our results into a one-dimensional array. To do this, we want to use the function np.ravel(), with results as our parameter.
# Next, we will convert our unraveled results into a list. To convert the results to a list, we will need to use the list function, which is list(), and then convert that array into a list. 
# Then we'll jsonify the list and return it as JSON
# You may notice here that to return our list as JSON, we need to add stations=stations. This formats our list into JSON. 
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# For this route, the goal is to return the temperature observations for the previous year. 
# Now, calculate the date one year ago from the last date in the database
# The next step is to query the primary station for all the temperature observations from the previous year.
# Finally, as before, unravel the results into a one-dimensional array and convert that array into a list. Then jsonify the list and return our results
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Our last route will be to report on the minimum, average, and maximum temperatures. However, this route is different from the previous ones in that we will have to provide both a starting and ending date.
# We need to add parameters to our stats()function: a start parameter and an end parameter.
# With the function declared, we can now create a query to select the minimum, average, and maximum temperatures from our SQLite database. We'll start by just creating a list called sel
# Since we need to determine the starting and ending date, add an if-not statement to our code. This will help us accomplish a few things. We'll need to query our database using the list that we just made.
#  Then, we'll unravel the results into a one-dimensional array and convert them to a list. Finally, we will jsonify our results and return them.
# In the following code, take note of the asterisk in the query next to the sel list. Here the asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures.
# Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. We'll use the sel list, which is simply the data points we need to collect.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
# when we run the script with python app.py, the __name__ variable will be set to __main__. This indicates that we are not using any other file to run this code.
if __name__ == "__main__":
    app.run(debug=True)
