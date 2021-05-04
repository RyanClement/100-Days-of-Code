"""
Created: May 4, 2021
@author: Ryan Clement
Day #9: Dictionary in List.
"""

travel_log = [
    {
      "country": "France",
      "visits": 12,
      "cities": ["Paris", "Lille", "Dijon"]
    },
    {
      "country": "Germany",
      "visits": 5,
      "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visits, cities):
    dic = {}
    dic["country"] = country
    dic["visits"] = visits
    dic["cities"] = cities
    travel_log.append(dic)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)