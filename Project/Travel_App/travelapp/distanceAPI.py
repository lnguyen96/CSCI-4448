import urllib.request
import json

def getDistance(origin, destination):
    origin = origin.replace(' ', '+')
    destination = destination.replace(' ', '+')
    #endpoint = 'https://maps.googleapis.com/maps/api/directions/json?origin=Boulder&destination=Seattle&key=AIzaSyCD-gN0FQdpkjnD-6yB9EFOf3GypoBaqHk'
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    apiKey = 'AIzaSyCD-gN0FQdpkjnD-6yB9EFOf3GypoBaqHk'
    navRequest = 'origin={}&destination={}&key={}'.format(origin, destination, apiKey)
    request = endpoint + navRequest
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    routes = directions['routes']
    legs = routes[0]['legs']
    miles = legs[0]['distance']['text']
    miles = miles.split()[0]
    miles = miles.replace(',', '')
    return(miles)

def calculateCost(distance, pricePer, milesPer):
    gallons = float(distance)/float(milesPer)
    cost = gallons*float(pricePer)
    cost = float("{0:.2f}".format(cost))
    return (cost)