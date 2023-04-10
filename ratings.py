
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


ratings_dict = read_file('scores.txt')
while True:
    print("Menu")
    print("P - printing all the ratings (in alphabetical order)")
    print("A - Adding a new restaurant (and rating it)")
    print("Q - Quitting")
    user_input = input("Please choose an option: ").lower()

    if user_input == 'q':
        print("Goodbye!")
        break
    elif user_input == 'p':
        print_ratings(ratings_dict)
    elif user_input == 'a':
        ratings_dict = add_new_restaurant(ratings_dict)
    else:
        print("Input not recognized, please try again.")
