# Surfs_up,
Exploring Weather Data by the use of SQLAlchemy to connect to and query a SQLite database, analyzing data with Python (Pandas functions and methods), plotting graphs with Matplotlib comprehensive library and building a Climate App using Flask.

## Results : 

The purpose of this project  was to create a strong business plan which will rely on our Weather Data Analysis as key information to potential Inverstors for "Surf and Shake" shop in Oahu, Hawaii serving surfboards and ice cream to locals, tourists and you reading this github repository.

Specifically, for this analysis, we want to focus on temperature trend data for the months of June and December in Oahu, in order to determine if the "Surf and Shake" shop business is sustainable year-round.

 [Analysis stages :](https://github.com/MilosPopov007/Surfs_up/blob/main/SurfsUp_Challenge.ipynb)
* Import dependencies and set up a Python SQL toolkit and Object Relational Mapper
* Write a query that filters the date column from the Measurement table to retrieve all the temperatures for the month of June and December
* Convert the temperatures to a list
* Create a DataFrame from the list of temperatures
* Generate the summary statistics for the June and December temperatures DataFrame

![This is an image](https://github.com/MilosPopov007/Surfs_up/blob/main/June_Temps.png) ![This is an image](https://github.com/MilosPopov007/Surfs_up/blob/main/December_Temps.png)

Weather Data Analysis major points :
* Looking at data summary statistic we can conclude that average temperatures for the  month of  June are slightly higher than average temperatures for the month of December
* Standard deviation (measure of how dispersed the data is in relation to the mean) for two data sets is almost similar
* Focusing on 75 % summary statistics data from both data sets we can conclude that temperature disparity between month of  June and the month of  December won't have a negative impact on our business decisions

To present our data to potential investors, we created a [Climate App](https://github.com/MilosPopov007/Surfs_up/blob/main/app.py) using the Flask application with set out rout for each segment of our analysis: Precipitation, Stations, Monthly Temperature, and Statistics, as well as a welcome route associated with the webpage.

### Summary : 

![This is an image](https://github.com/MilosPopov007/Surfs_up/blob/main/June_precipitation.png) ![This is an image](https://github.com/MilosPopov007/Surfs_up/blob/main/Decemeber_precipitation.png)

In order to back up our business plan we performed additional  analyses on our data set to get information on precipitation data for the month of June and December.
Based on summary statistic we can definitely conclude that month of December has more precipitation than the month of June, taking that into account December is one of  the wettest month on Oahu, with the mean of 0.22  inches per hour it is still considered moderate rainfall, according to meteorological standards (rain is classified as light, meaning rain falling at a rate between a trace and 0.10 inches per hour; moderate, 0.11 to 0.30 inches per hour; heavy, more than 0.30 inches per hour).
We included [Data sample](https://github.com/MilosPopov007/Surfs_up/blob/main/climate_analysis.ipynb) in the graphical analysis for more comprehensive results.
Our data is backing up our project as safe to go venture.



