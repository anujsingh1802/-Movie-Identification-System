# Movie Identification System using Binary Decision Tree

## Assignment Title
Movie Guessing System using Dynamic Binary Decision Tree (Yes/No Questions)

---

## Problem Statement

The objective of this assignment is to design an interactive system that identifies a specific movie by asking a series of **binary (Yes/No) questions**.  
The system should **not use a hardcoded decision tree**, but instead dynamically determine the most effective question at each step based on the remaining dataset.

---

## Project Objective

- To identify a movie selected by the user from a dataset
- To dynamically generate Yes/No questions
- To progressively reduce the search space
- To finally determine **exactly one movie**

---

## Key Concepts Used (As Per Assignment)

- Binary Decision Tree Logic  
- Entropy (to measure uncertainty)  
- Information Gain (to choose the best split)  
- Dynamic Question Generation  
- Dataset Filtering  
- Edge Case Handling  

---

## Dataset Description

The dataset consists of **real Hollywood and Bollywood movies**.  
Each movie is described using the following attributes:

| Attribute | Description |
|--------|------------|
| Title | Name of the movie (final output) |
| Lead_Gender | Male / Female |
| Genre | Action, Drama, Comedy, Thriller, Sci-Fi, Romance |
| Release_Year | Exact year of release |
| Rating_Category | High / Medium / Low |
| Language | English / Hindi |
| Awards_Won | Yes / No |
| Budget_Category | High / Medium / Low |

> Dataset size is **in the minimum requirement**  
> All data is **real and logically consistent**

---

## System Working (Algorithm)

1. The user thinks of a movie from the dataset
2. The system starts with the complete dataset
3. At each step:
   - Entropy is calculated for all possible attributes
   - The attribute providing maximum information gain is selected
   - A binary Yes/No question is generated dynamically
4. Based on the user’s answer:
   - The dataset is filtered
5. Steps 3–4 are repeated until:
   - Only one movie remains, or
   - A tie-breaking mechanism is applied
6. The system outputs the identified movie

---

## Example Interaction

Dataset: 115 movies

Q1: Is the release year >= 2020?
User: Yes
Remaining movies: 30

Q2: Is the language English?
User: Yes
Remaining movies: 18

Q3: Is the genre Drama?
User: Yes
Remaining movies: 6

Q4: Has the movie won awards?
User: Yes

Result: Oppenheimer


---

## Tie-Break Handling

In scenarios where:
- No further effective entropy-based split is possible, and
- More than one movie still remains,

A **deterministic tie-break mechanism** is applied using the rarest attribute values.  
This guarantees that the system always terminates with **exactly one movie**.

---

## Project Structure
>movie_decision_system/
>│
>├── movie.csv # Dataset
>├── main.py # Main program
>├── config.py # Configuration file
>├── data_loader.py # CSV reader
>├── entropy_selector.py # Entropy & information gain logic
>├── question_generator.py # Dynamic question creation
>├── movie_filter.py # Dataset filtering logic
>└── README.md # Project documentation


---

## How to Run the Program

### Requirements
- Python 3.x

### Command
```bash
python main.py
