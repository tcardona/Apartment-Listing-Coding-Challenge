from FriendTree import FriendTree
import unittest

#this assumes that if the same word is given twice, it will only be recognized as a friend once

#this also assumes that the word will always be in the social network

#this assumes that the words will always be presented in uppercase in the dictionaries


tests=(['LISTY', ''],
    ['LISTY'],
    ['LISTYLISTYLISTYLISTY', 'LISTY'],
    ['LISTY', 'LISTY', 'RUSTY', 'JACK', 'BEEEEES', 'HELLO'],
    ['LISTY', 'LISTY', 'HISTY', 'HISTY', 'HUSTY', 'HUSKY', 'RIP'],
    ['LIS', 'L', 'I', 'LIST', 'LISTY'],
    ['23456', 'LISTY', 'LIST'],
    ['LISTY', 'LISTY', 'LISTY', 'LISTY'],
    ['LISTY', 'FINE', 'HI', 'HEY', 'HELLO'],
    ['LISTY', 'FISTY', 'FUSTY', 'RUSTY', 'CRUSTY', 'HUSTY'],
    ['LISTY', 'FISTY', 'KISTY', 'MISTY', 'LISTE', 'LASTY', 'LATTY'])

test_answers=(1, 1, 1, 1, 4, 3, 2, 1, 1, 6)

def check_correct(A, ans):
    word='LISTY'
    guess_size=FriendTree(word).findSocialNetwork(word, A)
    print('')
    print('Your Output for the social network size: ' + str(guess_size))
    print('The actual size of the social network: '+str(ans))
    return guess_size==ans

class TestSocialNetowrk(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check_correct(tests[0], test_answers[0]))

    def test_02(self):
        self.assertTrue(check_correct(tests[1], test_answers[1]))

    def test_03(self):
        self.assertTrue(check_correct(tests[2], test_answers[2]))

    def test_04(self):
        self.assertTrue(check_correct(tests[3], test_answers[3]))
       
    def test_05(self):
        self.assertTrue(check_correct(tests[4], test_answers[4]))

    def test_06(self):
        self.assertTrue(check_correct(tests[5], test_answers[5]))

    def test_07(self):
        self.assertTrue(check_correct(tests[5], test_answers[5]))

    def test_08(self):
        self.assertTrue(check_correct(tests[5], test_answers[5]))

    def test_09(self):
        self.assertTrue(check_correct(tests[5], test_answers[5]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)