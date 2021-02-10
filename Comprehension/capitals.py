countries = input().split(", ")
capitals = input().split(", ")

zipped_cities = zip(countries, capitals)

result_dict = {key: value for key, value in zipped_cities}

for key, value in result_dict.items():
    print(f"{key} -> {value}")