import math
from collections import Counter

def entropy(dataset):
    total = len(dataset)
    counts = Counter(movie["Title"] for movie in dataset)

    ent = 0.0
    for count in counts.values():
        p = count / total #prob
        ent -= p * math.log2(p) 
    return ent





def information_gain_binary(movies, attribute, value):
    total_entropy = entropy(movies)

    yes_set = [m for m in movies if m[attribute] == value]
    no_set  = [m for m in movies if m[attribute] != value]

    if not yes_set or not no_set:
        return 0

    total = len(movies)
    weighted_entropy = (
        (len(yes_set) / total) * entropy(yes_set) +
        (len(no_set)  / total) * entropy(no_set)
    )
    return total_entropy - weighted_entropy




def information_gain_numeric(movies, attribute, threshold):
    total_entropy = entropy(movies)

    yes_set = [m for m in movies if int(m[attribute]) >= threshold]
    no_set  = [m for m in movies if int(m[attribute]) < threshold]

    if not yes_set or not no_set:
        return 0

    total = len(movies)
    weighted_entropy = (
        (len(yes_set) / total) * entropy(yes_set) +
        (len(no_set)  / total) * entropy(no_set)
    )
    return total_entropy - weighted_entropy




def select_best_attribute_entropy(movies, attributes):
    best_attr = None
    best_value = None
    best_gain = -1

    for attr in attributes:
        # Numeric split for Release_Year
        if attr == "Release_Year":   
            years = sorted(set(int(m[attr]) for m in movies))
            for y in years:
                gain = information_gain_numeric(movies, attr, y)
                if gain > best_gain:
                    best_gain = gain
                    best_attr = attr
                    best_value = y
        else:
            values = set(m[attr] for m in movies)
            for v in values:
                gain = information_gain_binary(movies, attr, v)
                if gain > best_gain:
                    best_gain = gain
                    best_attr = attr
                    best_value = v

    return best_attr, best_value




# ---- automatic tie-breaker (guarantees ONE movie) ----
def auto_tie_break(movies):
    if len(movies) == 1:
        return movies

    attrs = [k for k in movies[0].keys() if k != "Title"]
    for attr in attrs:
        values = [m[attr] for m in movies]
        freq = Counter(values)
        # use an explicit key function to satisfy type checkers
        rare = min(freq, key=lambda k: freq[k])
        filtered = [m for m in movies if m[attr] == rare]
        if filtered and len(filtered) < len(movies):
            return filtered

    return movies
