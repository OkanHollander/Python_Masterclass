from pprint import pprint

input_filename = "Country_info.txt"
countries = {}

with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip().split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'code': code,
            'code3': code3,
            'dialing': dialing,
            'timezone': timezone,
            'currency': currency
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict

# pprint(countries)
user_input = input("Enter a country name: ").casefold()
match_found = False
for key, value in countries.items():
    if user_input == key:
        print(f"The capital of {user_input} is {value['capital']}")
        match_found = True
        break
if not match_found:
    print(f"Sorry, {user_input} is not a country")
