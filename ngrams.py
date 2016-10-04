#! /usr/bin/env python
'''Given a list of words, return the n-grams for given n.

User must supply command line args:

    sentence:   e.g., 'How much wood could a woodchuck chuck if a woodchuck could chuck wood'
    n:          number, e.g., n = 3 returns tri-grams

Note:  For a sentence containing K words, the number of n-grams is K - (n - 1).
'''
import sys


def n_gram(sentence, n):
    '''Returns the n-grams for a supplied sentence.

    Args:
        sentence:   a string with characters and whitespaces
        n:          number of words to group, e.g., n = 3 is a "trigram"

    Returns:
        n_grams:    a list containing the n-grams
    '''
    n_grams = []    # empty list
    n = int(n)      # idiot-proof n to be an int

    wordlist = sentence.split() # split on whitespaces
    # The number of n-grams that can be constructed is ( # words ) - (n - 1)
    for i in range(len(wordlist)-n+1):
        # slice out ith to (i+n)th words, form n-gram by joining with whitespace, append to list
        n_grams.append( ' '.join(wordlist[ i : i+n ] ) )
    return n_grams


def main():
    try:
        sentence = sys.argv[1]
        n = sys.argv[2]
    except:
        sys.exit('\nYou must supply a string (sentence) and an integer n\n')

    n_grams = n_gram( sentence, int(n) )

    print("\nFor the following sentence:"  )
    print("'" + sentence + "'")
    print("\nFor n = {}, the {} n-grams are:".format(int(n), len(n_grams)))
    print( n_grams )


if __name__ == '__main__':
    main()