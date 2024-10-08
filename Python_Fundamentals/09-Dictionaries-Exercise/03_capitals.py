countries = input().split(", ")
capitals = input().split(", ")

corresponding_countries_cities = dict(zip(countries, capitals))

for country, capital in corresponding_countries_cities.items():
    print(f"{country} -> {capital}")
