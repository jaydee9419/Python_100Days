travel_log = [
    {
        "country": "France", 
        "city_visited": ["Paris", "Lille", "Dijon"], 
        "Total_visits": 15
    },
    {
        "country": "India", 
        "city_visited": ["Bangalore", "Chennai", "Hyderabad"],
        "Total_visits": 10
    }
]


#adding one more county to the exising list
def add_new_counrty(name, cities_visited, Total_visites):
    new_country = {}
    new_country['country'] = name
    new_country['cities_visited'] = cities_visited
    new_country['Total_visites'] = Total_visites
    
    travel_log.append(new_country)
    
add_new_counrty("Italy",["Rome", "Venice", "Florence"], 13)


print(travel_log[2])