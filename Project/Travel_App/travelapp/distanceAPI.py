'''
This file contains methods that are used to calculate/obtain data that we would otherwise not have from
querying our database or from user input
'''

import urllib.request
import json

# Google Directions API
def getDistance(origin, destination):
    origin = origin.replace(' ', '+')
    destination = destination.replace(' ', '+')
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    #apiKey =
    navRequest = 'origin={}&destination={}&key={}'.format(origin, destination, apiKey)
    request = endpoint + navRequest
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    # Extracting information specific to our app
    routes = directions['routes']
    legs = routes[0]['legs']
    miles = legs[0]['distance']['text']
    miles = miles.split()[0]
    miles = miles.replace(',', '')
    return(miles)

# Function takes parameters from queries to calculate cost of trip
def calculateCost(distance, pricePer, milesPer):
    gallons = float(distance)/float(milesPer)
    cost = gallons*float(pricePer)
    cost = float("{0:.2f}".format(cost))
    return (cost)