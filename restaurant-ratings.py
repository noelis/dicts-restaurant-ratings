def print_restaurant_ratings(file_name):
    """Parses restaurant and ratings from file_name and prints results.

    Sample line from file_name:
    Arinell's:4
    """
    # create empty ditionary
    restaurant_ratings = {}
    # open file, iterate line by line
    restaurant_file = open(file_name)
    # split by colon, returns a list
    for line in restaurant_file:
        restaurant_name, restaurant_rating = line.rstrip().split(":")
        restaurant_ratings[restaurant_name] = restaurant_rating

    # close file
    restaurant_file.close()

    # either loop or function that returns dictionary alphabetized
    for name, rating in sorted(restaurant_ratings.iteritems()):
        print "{} is rated at {}.".format(name, rating)

print_restaurant_ratings("scores.txt")