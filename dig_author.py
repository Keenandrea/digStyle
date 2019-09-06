""" program to count unique strings in a text file """
from collections import Counter

filename = "holden.txt"
def word_count(fname):
    with open(fname) as file:
        return Counter(file.read().split())

def main():
    
    print('Author\'s Word Count')
    print('_________ ____ _____')
    print(word_count(filename))
    
if __name__ == '__main__':
    main()