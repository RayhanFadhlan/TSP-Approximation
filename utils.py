
from haversine import haversine,Unit
import json
import plotly.graph_objects as go


class Country:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_coordinate(self):
        return (self.latitude, self.longitude)
    
    def print_name(self):
        print(self.name)
    
    def print_coordinate(self):
        print(f"({self.latitude}, {self.longitude})")


class Countries:
    def __init__(self):
        self.countries = [] 

    def get_countries(self):
        return self.countries

    def get_country(self, name):
        for country in self.countries:
            if country.name == name:
                return country
        return None

    def get_distance(self, name1, name2):
        country1 = self.get_country(name1)
        country2 = self.get_country(name2)
        return haversine(country1.get_coordinate(), country2.get_coordinate(),unit=Unit.KILOMETERS)

    def get_adj_matrix(self):
        adj_matrix = []
        for country1 in self.countries:
            row = []
            for country2 in self.countries:
                row.append(self.get_distance(country1.name, country2.name))
            adj_matrix.append(row)
        return adj_matrix

    def parse_json_countries(self,n):
        with open('coordinates.json') as json_file:
            data = json.load(json_file)
            count = 0
            for region, countries in data.items():
                for country, coordinate in countries.items():
                    if count < n:
                        self.countries.append(Country(country, coordinate['latitude'], coordinate['longitude']))
                        count += 1  # Increment counter
                    else:
                        break  
                if count >= n:
                    break

    def parse_json_by_region(self,region):
        with open('coordinates.json') as json_file:
            data = json.load(json_file)
            for country, coordinate in data[region].items():
                self.countries.append(Country(country, coordinate['latitude'], coordinate['longitude']))

    def print_countries(self):
        for country in self.countries:
            print(country.name)

    def get_latitudes(self):
        latitudes = []
        for country in self.countries:
            latitudes.append(country.get_latitude())
        return latitudes
    
    def get_longitudes(self):
        longitudes = []
        for country in self.countries:
            longitudes.append(country.get_longitude())
        return longitudes
    
    def print_countries_path(self, path):
        for i in path:
            print(self.countries[i].name, end=" -> ")

    def plot_dots(sellf):
        lat = sellf.get_latitudes()
        lon = sellf.get_longitudes()

        fig = go.Figure(go.Scattermapbox(
        mode = "markers",
        lon = lon,
        lat = lat,
        marker = {'size': 20}))

        fig.update_layout(
            margin ={'l':0,'t':0,'b':0,'r':0},
            mapbox = {
                'center': {'lon': 10, 'lat': 10},
                'style': "open-street-map",
                'center': {'lon': -20, 'lat': -20},
                'zoom': 1})

        fig.show()

    def plot_lines(self, path : list[int]):
        lat = []
        lon = []
        for i in path:
            lat.append(self.countries[i].get_latitude())
            lon.append(self.countries[i].get_longitude())

        fig = go.Figure(go.Scattermapbox(
            mode = "markers+lines",
            lon = lon,
            lat = lat,
            marker = {'size': 20}))

        fig.update_layout(
            margin ={'l':0,'t':0,'b':0,'r':0},
            mapbox = {
                'center': {'lon': 10, 'lat': 10},
                'style': "open-street-map",
                'center': {'lon': -20, 'lat': -20},
                'zoom': 1})

        fig.show()
    

# def main():
#     countries = Countries()
#     countries.parse_json_by_region('Western Europe')
#     countries.plot_dots()
#     # countries.parse_json_countries(5)
#     countries.print_countries()
#     # adj_matrix = countries.get_adj_matrix()
#     # print(adj_matrix)
#     # print(countries.get_countries()[1].get_coordinate())   

# main()
