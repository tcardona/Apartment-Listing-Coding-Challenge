class FriendTree:

    def __init__(self, word):
        '''
        ----------------------------------------------------------------------------------------------
        Parameters
        ------------------------------------------------------------------------------------------------

        word = word we are checking the size of the social network for

        ------------------------------------------------------------------------------------------------
        Function Info
        -----------------------------------------------------------------------------------------------

        This initializes the class and initializes the set of counted words (makes sure we don't double
        count words in the social network) to an empty set that will be added to. 

        This also initializes a set seen words that will hold all of our permutations of all given words 
        that are currently a part of the social network. 

        This also initializes a dictionary that will hold all the permutations for a given word, with the
        word serving as the key and the set of permutations as the value.

        ------------------------------------------------------------------------------------------------
        '''
        self.seenWords = set()
        self.countedWords = set()
        self.permutes = {}

    def generate_permutations(self, word):
        '''
        -----------------------------------------------------------------------------------------
        Parameters
        -----------------------------------------------------------------------------------------
        
        word = word we are checking the permutations of

        -----------------------------------------------------------------------------------------      
        Function Info
        -----------------------------------------------------------------------------------------

        This function will generate all the possible permutations of a word from one insertion,
        deletion, or substitution operation

        -----------------------------------------------------------------------------------------
        '''

        permutes=set()

        for i in range(len(word)):
            permutes.add(word[:i]+'*'+word[i:])
            permutes.add(word[:i]+'*'+word[i+1:])
            permutes.add(word[:i]+word[i+1:])
            permutes.add(word+'*')
            permutes.add(word)

        return permutes

    def checkFriends(self, word):
        '''
        -----------------------------------------------------------------------------------------
        Parameters
        -----------------------------------------------------------------------------------------
        
        word = word we are checking if is friends with any of the current friends

        -----------------------------------------------------------------------------------------      
        Function Info
        -----------------------------------------------------------------------------------------

        This function will check all the possible permutations of the word and check if they are
        currently in the set of seen words that holds all the possible permutations of words
        currently in the social network.

        If one of the permutations is in the set of seen words, then it adds all the permutations
        and adds that word to the set of counted words.

        If it is not in the set of words, it then simply returns False.

        -----------------------------------------------------------------------------------------
        '''

        for permute in self.permutes[word]:
            if permute in self.seenWords:
                self.seenWords=self.seenWords.union(self.permutes[word])
                self.countedWords.add(word)
                return True

        return False

    def findSocialNetwork(self, word, network):

        '''
        -----------------------------------------------------------------------------------------
        Parameters
        -----------------------------------------------------------------------------------------
        
        word = word we are checking the size of the social network for

        network = list of all the words that could possibly be in the social network for a 
        particular word

        -----------------------------------------------------------------------------------------      
        Function Info
        -----------------------------------------------------------------------------------------

        This function will intialize the seen words variable that holds all possible permutations
        to the permutations of the original word and initialize the words that have been counted
        to the original word we are finding the size of the social network for (to avoid double
        counting). This function will also initialize an amount_added boolean to check if any words
        were added to the social network during this pass through the network. If any were, then we
        have to be sure to repeat the run through the network to make sure we didn't miss any possible
        members of the social network that may match one of the permutations of the new memeber.

        This function then initializes the dictionary that will hold all permutations of every word
        before beginning in order to allow for easy access through a dictionary later on.

        This function then does a while loop to repeat the operation of checking the if any of the 
        input_words (a word in the list of the network) is friends with any of the words in the 
        social network. It first verifies if the word has already been counted with self.countedWords
        so as not to double count words. It then checks if the word is friends with any of the
        words already in the social network if it has not been counted yet, if it is the function
        adds it to the set of counted words and its permutations to the set of seen words.

        The function then sets the amount_added boolean to true so the function knows to repeat the
        operation of going through the list with the updated set of permutations in order to verify
        if any of the words are friends with the newly added words. Once it has not added more words
        on a run through, it ends the while loop and returns the length of the set of counted words.

        -----------------------------------------------------------------------------------------
        '''


        self.seenWords = self.seenWords.union(self.generate_permutations(word))
        self.countedWords.add(word)
        amount_added = True

        for input_word in network:
            self.permutes[input_word] = self.generate_permutations(input_word)

        while amount_added:
            amount_added = False
            for input_word in network:
                if input_word not in self.countedWords:
                    if self.checkFriends(input_word): amount_added=True

        return len(self.countedWords)
