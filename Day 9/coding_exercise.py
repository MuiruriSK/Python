travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Nice"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Munich", "Frankfurt"],
        "total_visits": 5,
    },
    {
        "country": "Italy",
        "cities_visited": ["Rome", "Milan", "Venice"],
        "total_visits": 7,
    },
]

# Write a function to add a new entry to the travel log
def add_new_country(country, total_visits, cities_visited):
    new_entry = {
        "country": country,
        "cities_visited": cities_visited,
        "total_visits": total_visits,
    }
    travel_log.append(new_entry)

add_new_country("Spain", 3, ["Madrid", "Barcelona", "Valencia"])
print(travel_log)


