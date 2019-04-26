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
    return(legs[0]['distance']['text'])