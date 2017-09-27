# cs329e-netflix Netflix movie rating prediction project
[![Build Status](https://travis-ci.com/SuperYuLu/cs329e-netflix.svg?token=X7jP7aW4CTQYTcpeZ5qW&branch=master)](https://travis-ci.com/SuperYuLu/cs329e-netflix)

# Author
|Name|Github|
|---:|:-----|
|Yu Lu|[SuperYuLu](https://github.com/SuperYuLu)|
|Ruth Mendez|[mendezruth35](https://github.com/mendezruth35)|


# Description
## Specification

Write a program, ideally with a partner, to win the Netflix Prize in Python.

Ignore the qualifying data. It's just there for explanation.

Just use the probe data and produce an RMSE (truncated to two decimal places) of less than 1.00 and a runtime of less than 1 min.

Note: Because the Netflix files are very large, it's impractical to make copies of them to your local machine. Your best bet is to develop the solution on the CS machines.
Data
##Training Data:

    17,770 movies
    480,189 customers
    about 100,000,000 ratings
    about 5,600 ratings per movie
    about 200 ratings per customer

## Qualifying Data:

    2,836,401 ratings, no customers from training data

## Probe Data:

    1,425,333 ratings, all customers from training data

## Files:

    /u/fares/public_html/netflix/README

    /u/fares/public_html/netflix/training_data/* (1.4 GB)
    /u/fares/public_html/netflix/training_data/mv_0002043.txt (162 KB)
    17,770 files total (one per movie)

