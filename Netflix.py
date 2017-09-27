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


#AVERAGE_RATING = 3.60428996442
ACTUAL_CUSTOMER_RATING = create_cache("cache-actualCustomerRating.pickle")
#AVERAGE_RATING_CUSTOMER = create_cache("cache-averageCustomerRating.pickle")
#AVERAGE_RATING_MOVIE = create_cache("cache-averageMovieRating.pickle")

AVERAGE_MOVIE_RATING_PRE_YEAR = create_cache("cache-movieAverageByYear.pickle")
YEAR_OF_RATING = create_cache("cache-yearCustomerRatedMovie.pickle")
CUSTOMER_AVERAGE_RATING_YEARLY = create_cache("cache-customerAverageRatingByYear.pickle")

'''
actual_scores_cache ={10040: {2417853: 1, 1207062: 2, 2487973: 3}}
movie_year_cache = {10040: 1990}
decade_avg_cache = {1990: 2.4}
'''
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
            
            #year = [x[1] for x in AVERAGE_MOVIE_RATING_PRE_YEAR.keys() if x[0] ==int( current_movie)]#[0]
            #avg_movie_in_year = AVERAGE_MOVIE_RATING_PRE_YEAR[(int(current_movie),year[0])]
            #avg_movie_overall = AVERAGE_RATING_MOVIE[int(current_movie)]
            writer.write(line)
            writer.write('\n')
        else:
	    # It's a customer
            current_customer = line
            customer_rating_year = YEAR_OF_RATING[(int(current_customer), int(current_movie))]
            avg_customer_in_year = CUSTOMER_AVERAGE_RATING_YEARLY[(int(current_customer), customer_rating_year)]
            #avg_movie_overall = AVERAGE_RATING_MOVIE[int(current_movie)]
            #avg_customer_overall = AVERAGE_RATING_CUSTOMER[int(current_customer)]
            avg_movie_in_year = AVERAGE_MOVIE_RATING_PRE_YEAR[(int(current_movie),customer_rating_year)]
            prediction = avg_movie_in_year * 0.5  + avg_customer_in_year * 0.5 #0.98

            predictions.append(prediction)
            actual.append(ACTUAL_CUSTOMER_RATING[(int(current_customer),int(current_movie))])
            
            writer.write("%.1f" % prediction) 
            writer.write('\n')	
    # calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    writer.write(str(rmse)[:4] + '\n')

