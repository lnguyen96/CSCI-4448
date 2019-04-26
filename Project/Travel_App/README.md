# DinoCo
## Members

* Danny Nguyen
* Long Nguyen
* Edwin Chiang

## Project Overview
DinoCo is a flask based framework that allows users to create accounts, log their travel routes, and find out the cost of a trip. When logged in users are able to create new trips that allow them to see the cost of traveling from point a to point b depending on their car’s mpg and current fuel costs which are calculated as soon as the user enters their information.

## Description of files
Starting from the directory **CSCI-4448/Project/Travel_App/travelapp/** (bulk of the code that makes up our project)

The **static** folder contains files that will be used as imports in HTML. The contents of these files should not be changed, we have a .css folder in there for our HTML properties as well as a picture.

The **templates** folder contains all the HTML pages that are linked to their corresponding pages on our webapp.

**distanceAPI\.py** contains methods that translate user input data and database queries into distance and cost through use of Google's Distance API and basic calculations.

**forms\.py** contains classes that deal with user input. These classes validate data queries as well as necessary information when creating an account.

**models\.py** contains classes that identically mimic our tables in our database to be represented within our program. These are then used with SQLAlchemy's ORM to transfer data for various uses.

**routes\.py** contains classes that route data to a specific HTML page. This contains some elements of a REST API as you can query our database here and send the resulting data to be displayed on it's corresponding HTML page. This is also the place to handle user input data to send it to another place to process it into meaningful information.

**site\.db** is our SQLite3 database, we chose this as it is file based and was fairly quick to setup and have consistent among the 3 of us for testing.

The remaining files are just our data sources that we pulled from Kaggle or compiled python that helps speed things up when running our app.

## Instructions to run


We built this program on Python 3.6.3 and assume that you have Python 3 or a later version installed.

First is to download all the files from the **Travel_App** (this should be one level above the directory this README is on) directory and children directory.

Then in a command terminal, run the command to install the necessary packages

```
pip install flask flask-sqlalchemy flask-bcrypt flask-login flask-wtf
```

Navigate to the **Travel_App** directory and in the command terminal run the command

```
python run.py
```

With your command terminal still running, navigate to [http://localhost:5000/](http://localhost:5000/) or [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use our web app.