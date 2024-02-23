#simple Dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list in dictionary
travel_log = {
    "France": ['Paris', "Lille", "Dijon"],
    "India": ["Bangalore", "Chennai", "Hyderabad"]
}

#Nesting dictionary in Dictionary
travel_log = {
    "France": {"city_visited": ["Paris", "Lille", "Dijon"], "Total_visits": 15},
    "India": {"city_visited": ["Bangalore", "Chennai", "Hyderabad"],"Total_visits": 10}
}

for country in travel_log:
    print(country)
    print(travel_log[country])



#Nesting Dictionary in List
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


