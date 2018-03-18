from FriendTree import FriendTree
import unittest

#this file opens the dictionary and returns the size of the social network for the word listy in the whole dictionary

network=open('dictionary.txt').read().split()

word='LISTY'

friend=FriendTree(word)

print(friend.findSocialNetwork(word, network))
