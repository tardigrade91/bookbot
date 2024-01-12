def main():
    import string 

    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 

    words = file_contents.split() 
    num_words = len(words)

    print("--- Bein report of books/frankenstein.text ---") 

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
    print(value_list[::-1])
    # print out the letter part of the report
    for i in letter_dict: 
        print(f" The letter '{i}' was found {letter_dict[i]} times")

main()
