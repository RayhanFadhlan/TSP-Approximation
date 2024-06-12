from geopy.geocoders import Nominatim
import json
from time import sleep
countries = {
    'Eastern Europe': [
        "Moscow Russia",
        "Warsaw Poland",
        "Kyiv Ukraine",
        "Bucharest Romania",
        "Prague Czech Republic (Czechia)",
        "Budapest Hungary",
        "Minsk Belarus",
        "Sofia Bulgaria",
        "Bratislava Slovakia",
        "Chișinău Moldova"
    ],
    'Northern Europe': [
        "London United Kingdom",
        "Stockholm Sweden",
        "Copenhagen Denmark",
        "Helsinki Finland",
        "Oslo Norway",
        "Dublin Ireland",
        "Vilnius Lithuania",
        "Riga Latvia",
        "Tallinn Estonia",
        "Reykjavik Iceland"
    ],
    'Southern Europe': [
        "Rome Italy",
        "Madrid Espana",
        "Athens Greece",
        "Lisbon Portugal",
        "Belgrade Serbia",
        "Zagreb Croatia",
        "Sarajevo Bosnia and Herzegovina",
        "Tirana Albania",
        "Ljubljana Slovenia",
        "Skopje North Macedonia",
        "Podgorica Montenegro",
        "Valletta Malta",
        "Andorra la Vella Andorra",
        "San Marino San Marino",
        "Vatican City"
    ],
    'Western Europe': [
        "Berlin Germany",
        "Paris France",
        "Amsterdam Netherlands",
        "Brussels Belgium",
        "Vienna Austria",
        "Bern Switzerland",
        "Luxembourg City Luxembourg",
        "Vaduz Liechtenstein",
        "Monaco Monaco"
    ],
}

geolocator = Nominatim(user_agent="makalah_stima")


def get_coordinates(country):
    location = geolocator.geocode(country)
    if location:
        return (location.latitude, location.longitude)
    else:
        return (None, None)


coordinates = {}

for region, country_list in countries.items():
    coordinates[region] = {}
    for country in country_list:
        lat, lon = get_coordinates(country)
        coordinates[region][country] = {'latitude': lat, 'longitude': lon}
        sleep(0.2)  # To avoid 


with open('coordinates.json', 'w') as json_file:
    json.dump(coordinates, json_file,indent=4)