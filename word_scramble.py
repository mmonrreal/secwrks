#Assuming the words in the words.txt are english words with only alphabetical entries
#Assuming that the list of words are entered vertically and not horizontally


#reading from a txt file input
file = open('words.txt', 'r')
lines = file.readlines()
print("The following inputs were found: ",lines)



test_word = ""
largest_word = ""
word_only_letters = True

for line in lines:
    if line != '/n':   # checking if single character

        #print(line[len(line) - 1: len(line)])
        if line[len(line) - 1: len(line)] == "\n":
            test_word = line[0:len(line) - 1]

        else:
            test_word = line[0:len(line)]

        for char in test_word:
            if(ord(char) < 65 or ord(char) > 122 or (ord(char) > 90 and ord(char) < 97)):
                word_only_letters = False

        if(word_only_letters == True):
            if(len(test_word) > len(largest_word)):
                largest_word = test_word
               # print(largest_word)

    word_only_letters = True

print()
print("Longest word is: ", largest_word)
print("Longest word backwards: ", largest_word[::-1])

