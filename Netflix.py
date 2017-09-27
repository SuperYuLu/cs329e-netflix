#!/usr/bin/env python3

# -------
# imports
# -------

from math import sqrt
import pickle
from requests import get
from os import path
from numpy import sqrt, square, mean, subtract




def create_cache(filename):
    """
    filename is the name of the cache file to load
    returns a dictionary after loading the file or pulling the file from the public_html page
    """
    cache = {}
    folder = "/u/fares/public_html/netflix-caches/"
    filePath = "/u/fares/public_html/netflix-caches/" + filename

    if path.isfile(filePath):
        with open(filePath, "rb") as f:
            cache = pickle.load(f)
    else:
        webAddress = "http://www.cs.utexas.edu/users/fares/netflix-caches/" + \
            filename
        bytes = get(webAddress).content
        cache = pickle.loads(bytes)

    return cache



ACTUAL_CUSTOMER_RATING = create_cache("cache-actualCustomerRating.pickle")
AVERAGE_MOVIE_RATING_PRE_YEAR = create_cache("cache-movieAverageByYear.pickle")
YEAR_OF_RATING = create_cache("cache-yearCustomerRatedMovie.pickle")
CUSTOMER_AVERAGE_RATING_YEARLY = create_cache("cache-customerAverageRatingByYear.pickle")

# ------------
# netflix_eval
# ------------

def netflix_eval(reader, writer) :
    predictions = []
    actual = []
    
    # iterate throught the file reader line by line
    i = 0
    for line in reader:
        # need to get rid of the '\n' by the end of the line
        line = line.strip()
        # check if the line ends with a ":", i.e., it's a movie title 
        if line[-1] == ':':
	    # It's a movie
            current_movie = line.rstrip(':')
            writer.write(line)
            writer.write('\n')
        else:
	    # It's a customer
            current_customer = line
            # Get the year when customer rated this movie
            customer_rating_year = YEAR_OF_RATING[(int(current_customer), int(current_movie))]
            # Get the average rating the customer give in the year when he/she rated this movie 
            avg_customer_in_year = CUSTOMER_AVERAGE_RATING_YEARLY[(int(current_customer), customer_rating_year)]
            # Get the average rating this movie got from the same year when this customer give his/her rate 
            avg_movie_in_year = AVERAGE_MOVIE_RATING_PRE_YEAR[(int(current_movie),customer_rating_year)]
            # Give prediction based on the average movie rating and customer rating in the same year
            prediction = avg_movie_in_year * 0.5  + avg_customer_in_year * 0.5 #0.98

            predictions.append(prediction)
            actual.append(ACTUAL_CUSTOMER_RATING[(int(current_customer),int(current_movie))])
            
            writer.write("%.1f" % prediction) 
            writer.write('\n')	
    # calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    writer.write(str(rmse)[:4] + '\n')

