from data_loader import load_movies
from entropy_selector import (
    select_best_attribute_entropy,
    auto_tie_break
)
from question_generator import generate_entropy_question
from movie_filter import filter_movies_binary
from config import ATTRIBUTES, CSV_FILE


def run_movie_system():
    movies = load_movies(CSV_FILE)
    remaining_movies = movies.copy()
    available_attributes = ATTRIBUTES.copy()

    print("\n THINK OF A MOVIE FROM THE DATASET ")
    print("Answer ONLY with Yes or No.\n")

    # Main entropy-based loop
    while len(remaining_movies) > 1 and available_attributes:

        best_attr, best_value = select_best_attribute_entropy(
            remaining_movies,
            available_attributes
        )

        if best_attr is None:
            break

        print(generate_entropy_question(best_attr, best_value))
        user_answer = input("Your answer: ").strip()

        filtered = filter_movies_binary(
            remaining_movies,
            best_attr,
            best_value,
            user_answer
        )

        # Invalid input
        if filtered is None:
            print(" Invalid input. Type Yes or No.\n")
            continue

        # No reduction or empty branch → skip attribute
        if len(filtered) == 0 or len(filtered) == len(remaining_movies):
            print(f"'{best_attr}' cannot split further. Skipping.\n")
            available_attributes.remove(best_attr)
            if not available_attributes:
                break
            continue

        remaining_movies = filtered
        available_attributes.remove(best_attr)
        print(f"Remaining movies: {len(remaining_movies)}\n")

    # Guaranteed single result
    while len(remaining_movies) > 1:
        remaining_movies = auto_tie_break(remaining_movies)

    print("\n YOUR MOVIE IS:", remaining_movies[0]["Title"])


if __name__ == "__main__":
    run_movie_system()
