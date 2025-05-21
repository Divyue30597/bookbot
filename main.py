import sys
from stats import num_of_word

def main(): 
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) != 2:
        print("Error: Please provide the path to the book file.")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_of_words = num_of_word(text)
    dict_of_single_word_count = get_word_count(text)
    new_dict = create_new_dictionary(dict_of_single_word_count)
    generate_report(num_of_words, new_dict)
    

def get_word_count(word_from_book):
    dict = {}

    for char in word_from_book:
        c = char.lower()
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
    
    return dict
            
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

# def sorted_dict(dict):
#     # Using dictionary comprehension to create a new dictionary sorted by values
#     sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

#     # Printing the sorted dictionary
#     return sorted_dict

def sort_on(dict):
    return dict["num"]

def create_new_dictionary(dict):
    new_arr = []
    for char in dict:
        new_arr.append({"char": char, "num": dict[char]})
    
    new_arr.sort(reverse=True, key=sort_on)
    return new_arr


def generate_report(num_of_words, arr_with_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document\n")
    
    for item in arr_with_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
            # print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")
    

main()