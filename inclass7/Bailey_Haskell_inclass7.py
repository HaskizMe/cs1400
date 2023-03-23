'''
This program reads a file and puts out the the 
unique word count, longest word, and shortest word from the paragraph
'''
import re
import sys

# longest_word function
def longest_word(file_name):
    updated_string = ""

    # Opening file and writing contents to a list
    with open(file_name, 'r') as filedata:
        wordsList = filedata.read().split()

    # Using a for loop to ignore punctuations and updating the list
    for i in range (len(wordsList)):
        updated_string = re.sub(r'[^\w\s]','',wordsList[i]) 
        wordsList[i] = updated_string

    # Finding the longest word in the list
    longest_word_length = len(max(wordsList, key=len))

    # Adding all the longest words to a new list
    result = [textword for textword in wordsList if len(textword) == longest_word_length]

    # Removing duplicates in the list
    result = list(set(result))

    return result
    
# shortest_word function
def shortest_word(file_name):
    updated_string = ""
    
    # Opening file and writing contents to a list
    with open(file_name, 'r') as filedata:
        wordsList = filedata.read().split()

    # Using a for loop to ignore punctuations and updating the list
    for i in range (len(wordsList)):
        updated_string = re.sub(r'[^\w\s]','',wordsList[i]) 
        wordsList[i] = updated_string

    # Finding the shortest word in the list
    longest_word_length = len(min(wordsList, key=len))

    # Adding all the shortest words to a new list
    result = [textword for textword in wordsList if len(textword) == longest_word_length]

    # Removing duplicates in the list
    result = list(set(result))

    return result

# word_count function
def word_count(file_name):
    count = 0
    # Opening file
    with open(file_name, 'r') as filedata:
        # For loop to split words up and put in list and then check size of list
        for line in filedata:
            words = line.split()
            count += len(words)
    return count

# output_to_file function
def output_to_file(file_name):
    # Creating a file to write to 
    file = open('output.txt', 'w')
    # Writing to the file and putting in the results from out helper functions
    file.write("%s: %s\n" %("Longest word(s) in the paragraph", str(longest_word(file_name))))
    file.write("%s: %s\n" %("Shortest word(s) in the paragraph", str(shortest_word(file_name))))
    file.write("%s: %s\n" %("Word count of paragraph", str(word_count(file_name))))
    # Closing file
    file.close()

# Main function
def main():

    # Checking the length of the arguments and printing out messages
    if(len(sys.argv) > 2):
        print("Too many arguments\nOnly a file path argument is needed:")
    elif(len(sys.argv) < 2):
        print("Not enough arguments\nPlease enter a file path to be read:")
    else:
        # Storing sys.argv into a string and putting the string into the functions to be executed
        file_name = str(sys.argv[1])
        output_to_file(file_name)

if __name__ == "__main__":
    # Calling main function
    main()
