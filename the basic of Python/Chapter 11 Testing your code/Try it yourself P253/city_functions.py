# P253 11-1 City, Country
def City_Country(city, country, population = ''):
    if population:
        City_Country_string = f"{city}, {country}- population {population}"
        return City_Country_string
    else:
        City_Country_string =f"{city}, {country}"
        return City_Country_string

print(City_Country('santiage', 'chile', '5000000'))