#Jebel Macias
#  11/11/2018
#Lab 4 option(B)

# HashTable class using chaining.
class HashTable:
    def __init__(self, initial_size=26):
        # Hash Table is initialized with 26 indices
        self.table = []
        for i in range(initial_size):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, word):
        # First, get index where the word will go.
        index = (ord(word[:1].lower())-97) % len(self.table)
        list = self.table[index]
        # The word is inserted at the end of the list.
        list.append(word.lower())

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def find(self, word):
        # get the list at index where the word would be.
        index = (ord(word[:1].lower())-97) % len(self.table)
        list = self.table[index]

        # search for the word in the list at the index
        try:
            item_index = list.index(word)

        # if there is no word found return none
        except ValueError as e:
            return None
        return list[item_index]

    def average_number_strings(self):
        sum = 0
        for i in range(len(self.table)):
            sum += len(self.table[i])
        return str(sum/len(self.table))



def read_from_dictionary(file_name):
    """ populates the hashTable"""

    hashTable = HashTable()
    try:
        with open(file_name, 'r') as file:
            for line in file:
                hashTable.insert(line.split()[0])
    except Exception as e:
        print("Failed to load file " + file_name + " in the fucntion read_from_dictionary")
        return
    return hashTable

def max_in_list(list):
    """The funcion max_in_list is used to
    determine the word in any given list
    with the greatest number of anagrams
    The run time of this function is O(n)
    """

    max = list[0] # Takes first item to avoid none error below
    for i in range(1, len(list)):
        if int(list[i].split()[0]) > int(max.split()[0]):
            max = list[i]
    return max

def print_anagrams(dict, count, word, prefix=""):
    """The function print_Anagrams determines
    if a word is in the binary search tree
    """
    if len(word) <= 1:
        str = prefix + word

        #If in tree, print string, and append to counter
        if dict.find(str.lower()) != None:
            print(str)
            count.append(str)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur

            if cur not in before:
                print_anagrams(dict, count, before + after, prefix + cur)


def read_from_file(file_name, dict):
    """The fucntion read_from_file takes any given
    file containing a list of words, and determines
    how many anagarams each word has.
    """

    try:
        most_anagrams = []
        with open(file_name, 'r') as file:
            for line in file:
                count = [] # Stores word and count of angrams
                word = line.split()[0]
                print("---Anagrams for " + word.upper() + "---")
                print_anagrams(dict, count, word)
                most_anagrams.append(str(len(count)) + " " + word) # Appends words, and amount of anagrams
                print("Total Anagrams: " + str(len(count)) +"\n")
            max = max_in_list(most_anagrams) # Which word contains the most anagrams
            print("The word with the most anagrams:" + max.split()[1])
    except Exception as e:
        print("Failed to load file " + file_name + " in read_From_File.")
        return
    return

def begin():
    again = True
    while again:
        dict_name = input("What is the name of the file containing the list of english words?\n") # File containing englishword
        file_name = input("What is the name of the file containing the list of words you want to check for anagrams?\n") # File containing word used to check for anagrams
        hashTable = read_from_dictionary(dict_name)

        print("The average number of strings in the hash table is: " + hashTable.average_number_strings())

        read_from_file(file_name, hashTable)
        again = True if input("Would you like to try a different list of words? Type y or n: ") == "y" else False

begin()
