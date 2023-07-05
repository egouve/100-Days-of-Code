#Criar uma função que modifique o travel_log inserindo novos países

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
#🚨 Do NOT change the code above

def add_new_country(country_name, visit_number, cities_name):

    new_country = {
    'country': country_name,
    'visits': visit_number,
    'cities': cities_name
    }
    travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
