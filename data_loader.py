import csv 

def load_movies(csv_file):
    movies = []
    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)
    return movies
