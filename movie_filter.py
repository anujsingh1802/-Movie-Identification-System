def filter_movies_binary(movies, attribute, value, answer):
    answer = answer.strip().lower()

    if answer not in ("yes", "no"):
        return None

    if attribute == "Release_Year":
        if answer == "yes":
            return [m for m in movies if int(m[attribute]) >= value]
        else:
            return [m for m in movies if int(m[attribute]) < value]

    if answer == "yes":
        return [m for m in movies if m[attribute] == value]
    else:
        return [m for m in movies if m[attribute] != value]



# for "Release_data"
# Inception → 2010 ≥ 2020 
# Dangal → 2016 ≥ 2020 
# Oppenheimer → 2023 ≥ 2020 right


# for cat data
# Inception → Sci-Fi ≠ Drama right
# Dangal → Drama ≠ Drama 
# Oppenheimer → Drama ≠ Drama 


