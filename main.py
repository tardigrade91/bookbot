def main():
    import string 

    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 

    words = file_contents.split() 
    num_words = len(words)

    print("--- Begin report of books/frankenstein.text ---") 

    print(f"{num_words} words found in the document")

    print(" ") 

    
    # intitalize the alphabet letter dictionary and fill with lower case letters 
    letter_dict = {} 
    alphabet = list(string.ascii_lowercase) 
    for letter in alphabet: 
        letter_dict[letter] = 0
    
    # create a lowercase version of the file 
    lower_case_file_contents = file_contents.lower()

    # count the letters in the text 
    for letter in lower_case_file_contents: 
        if letter in alphabet: 
            letter_dict[letter] += 1 

    # find the rank order of the dictionary 
    value_list = [] 
    for letter in letter_dict:
        value_list.append(letter_dict[letter]) 
    value_list.sort()

    # print out the rank order of the dictionary (this was written by copilot with some prompting from me)
    print("The letters in rank order are:")
    for value in value_list[::-1]:
        for letter in letter_dict:
            if letter_dict[letter] == value: 
                print(f" The letter '{letter}' was found {value} times")
                letter_dict[letter] = -1
                break
    print("--- End report of books/frankenstein.text ---")


main()
