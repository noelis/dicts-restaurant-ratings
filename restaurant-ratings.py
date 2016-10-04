def process_file(file_name):
    """Parses restaurant name and ratings from file and adds it to a dictionary.
    """
    
    restaurant_ratings = {}
    
    # open file, iterate line by line
    restaurant_file = open(file_name)
    # split by colon, returns a list
    for line in restaurant_file:
        restaurant_name, restaurant_rating = line.rstrip().split(":")
        restaurant_ratings[restaurant_name] = int(restaurant_rating)

    # close file
    restaurant_file.close()
    return restaurant_ratings

def add_restaurant_rating(restaurant_ratings):
    """Prompts user for restaurant & rating, adds to dictionary."""

    user_restaurant = raw_input("Enter a restaurant name: ")
    user_rating = int(raw_input("Enter a restaurant rating between 1-5: "))

    # prompt user for new restaurant and rating, add to dictionary
    restaurant_ratings[user_restaurant] = user_rating

    return restaurant_ratings


def print_restaurant_ratings(restaurant_ratings):
    """Print dictionary."""

    # loop that returns dictionary alphabetized
    for name, rating in sorted(restaurant_ratings.iteritems()):
        print "{} is rated at {}.".format(name, rating)

def give_user_choice(rest_ratings):
    """User chooses which function to call, based on options available."""

    print """
    Welcome to our program! Here's what's on the menu:
    1. Would you like to see all restaurant ratings available?
    2. Adding a new restaurant to the list?
    3. Quitting our program?"""

    user_selection = int(raw_input("Please type a number here (1, 2, or 3): "))

    while user_selection != 3:
        if user_selection == 1:
            print_restaurant_ratings(rest_ratings)
            user_selection = int(raw_input("Please type a number here (1, 2, or 3): "))
        elif user_selection == 2:
            add_restaurant_rating(rest_ratings)
            user_selection = int(raw_input("Please type a number here (1, 2, or 3): "))

    print "Goodbye!"


rest_ratings = process_file("scores.txt")
# rest_ratings_user = add_restaurant_rating(rest_ratings)
# print_restaurant_ratings(rest_ratings_user)
give_user_choice(rest_ratings)
# print_restaurant_ratings(add_restaurant_rating(process_file("scores.txt")))

#####################################################
# Code V1: all in one function

# def get_restaurant_ratings(file_name):
#     """Parses restaurant and ratings from file_name and prints results.

#     Sample line from file_name:
#     Arinell's:4
#     """

#     user_restaurant = raw_input("Enter a restaurant name: ")
#     user_rating = int(raw_input("Enter a restaurant rating between 1-5: "))
#     # create empty ditionary
#     restaurant_ratings = {}
    
#     # open file, iterate line by line
#     restaurant_file = open(file_name)
#     # split by colon, returns a list
#     for line in restaurant_file:
#         restaurant_name, restaurant_rating = line.rstrip().split(":")
#         restaurant_ratings[restaurant_name] = int(restaurant_rating)

#     # close file
#     restaurant_file.close()

#     # prompt user for new restaurant and rating, add to dictionary
#     restaurant_ratings[user_restaurant] = user_rating

#     # loop that returns dictionary alphabetized
#     for name, rating in sorted(restaurant_ratings.iteritems()):
#         print "{} is rated at {}.".format(name, rating)

# # user_restaurant = raw_input("Enter a restaurant name: ")
# # user_rating = int(raw_input("Enter a restaurant rating between 1-5: "))

# # print_restaurant_ratings("scores.txt", user_rating, user_restaurant,)
# get_restaurant_ratings("scores.txt")
