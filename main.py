
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    #print(num_letters)
    print()
    

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_letterrs):
    sorted_list = []
    for ch in num_letterrs:
        sorted_list.append({"char": ch, "num": num_letterrs[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_num_letters(text):
    letters = {}
    for letter in text:
        lowered_text = letter.lower()
        if lowered_text in letters:
            letters[lowered_text] += 1
        else:
           letters[lowered_text] = 1
    return letters


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()