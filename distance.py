from geopy.geocoders import Nominatim
from geopy import distance
import geopy.geocoders
#import pandas as pd
import csv

geolocator = Nominatim(user_agent="distance")
geopy.geocoders.options.default_timeout = 20


with open('FILE_NAME') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    addresses = []
    restaurants = []
    dists = []
    
    for row in readCSV:
        restaurant = row[0]
        restaurants.append(restaurant)
        address = row[1]
        addresses.append(address)
    a = len(addresses)
    i = 0

    while i < 34:
        addr = geolocator.geocode(addresses[i])
        try:
            coords = (addr.latitude, addr.longitude)
            #potomac_square_address = geolocator.geocode("ADDRESS")
            #potomac_square = (potomac_square_address.latitude, potomac_square_address.longitude)
            #dist = round(distance.distance(coords, potomac_square).miles,2)
            #print(restaurants[i],': ', dist, ' miles')
            print(restaurants[i],': ',addr.longitude,' ', addr.latitude)
            i += 1
            
    
            
        except AttributeError:
            print("Error: ", restaurants[i])
            dists.append(restaurants[i])
            i += 1

