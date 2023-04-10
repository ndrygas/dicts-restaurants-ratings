
from random import choice 

def read_file(input_file):
    """Restaurant rating lister."""
    ratings_dict = {}
    for line in open(input_file):
        restaurant_name, rating = line.rstrip().split(":")
        ratings_dict[restaurant_name] = rating
    return dict(sorted(ratings_dict.items()))


def print_ratings(dictionary):
    """Prints ratings dictionary"""
    # dictionary = dict(sorted(dictionary.items()))
    for restaurant_name, rating in dictionary.items():
        print(f"{restaurant_name} is rated at {rating}.")
    

def add_new_restaurant(dictionary):
    restaurant_name = input("Please enter a new restaurant name: ")
    while True:
        rating = input("Please enter restaurant's rating: ")
        if rating.isnumeric() == True:
            rating = int(rating)
            if rating >= 1 and rating <= 5:
                break
        print("The rating must be an integer between 1 and 5 (inclusive)")
        
    dictionary[restaurant_name] = rating
    return dict(sorted(dictionary.items()))

def update_random_restaurant(dictionary):
    random_restaurant= choice(list(dictionary.keys()))
    print(f"{random_restaurant} is rated {dictionary[random_restaurant]}.")
    while True:
        new_rating = input("Please enter restaurant's rating: ")
        if new_rating.isnumeric() == True:
            new_rating = int(new_rating)
            if new_rating >= 1 and new_rating <= 5:
                break
        print("The rating must be an integer between 1 and 5 (inclusive)")

    dictionary[random_restaurant] = new_rating    

    return dictionary


def update_chosen_restaurant(dictionary):
    chosen_restaurant= input("Please enter restaurant name you want to update: ")
    if chosen_restaurant in dictionary:
        print(f"{chosen_restaurant} is rated {dictionary[chosen_restaurant]}.")
        while True:
            new_rating = input("Please enter restaurant's rating: ")
            if new_rating.isnumeric() == True:
                new_rating = int(new_rating)
                if new_rating >= 1 and new_rating <= 5:
                    break
            print("The rating must be an integer between 1 and 5 (inclusive)")

        dictionary[chosen_restaurant] = new_rating
    else: 
        print("This restaurant does not exist")
    return dictionary


ratings_dict = read_file('scores.txt')
while True:
    print("Menu")
    print("P - printing all the ratings (in alphabetical order)")
    print("A - Adding a new restaurant (and rating it)")
    print("R - Update a random restaurant’s rating")
    print("C- Update a chosen restaurant’s rating")
    print("Q - Quitting")
    user_input = input("Please choose an option: ").lower()

    if user_input == 'q':
        print("Goodbye!")
        break
    elif user_input == 'p':
        print_ratings(ratings_dict)
    elif user_input == 'a':
        ratings_dict = add_new_restaurant(ratings_dict)
    elif user_input == 'r':
        ratings_dict = update_random_restaurant(ratings_dict)
    elif user_input == 'c':
        ratings_dict = update_chosen_restaurant(ratings_dict)
    else:
        print("Input not recognized, please try again.")
