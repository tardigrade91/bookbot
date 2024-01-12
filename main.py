def main():
    import string 
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 

    words = file_contents.split() 
    num_words = len(words)
    print(f"The total number of words in Frankenstein is {num_words}")

    print("---- letter analysis ----") 


    
    # intitalize the alphabet letter dictionary and fill with lower case letters 
    letter_dict = {} 
    alphabet = list(string.ascii_lowercase) 
    for letter in alphabet: 
        letter_dict[letter] = None 

    

    print(letter_dict)
main()
