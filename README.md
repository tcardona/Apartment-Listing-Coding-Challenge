# Apartment-Listing-Coding-Challenge
This repository calculates the size of the social network of a word using the framework that Levenshtein distance.
The social network of a word is defined as all the words that are friends with a friend of words or friend of a friend of words and so on so forth. A friend for two words is defined as another word that has a Levenshtein distance of 1 away from the other word.


This repository contains three python files and other txt files:

FriendTree.py
This file contains the class definition of a friend tree that holds the functions that calculate the size of the social network and the main functionality of the program itself

ApartmentListingCodingChallenge.py
This file contains the actual import of the dictionary and the checking of the size of the social network for the word 'LISTY' in that dictionary.

tests.py
This file contains a list of test cases for the FriendTree.py in order to make sure the functionality was working as expected and that it properly counted the size of the social network correctly with some examples

.txt files
These files are the dictionaries of different sizes that were used to test the code on larger datasets. These were provided from Apartment Listing
