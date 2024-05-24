def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path) 
  num_of_words = get_num_of_words(book_text)
  characters_in_text = count_characters(book_path)
  characters_in_text_sorted = dict(sorted(characters_in_text.items(), key=lambda x:x[1], reverse=True))
  print(f"--- Begin report of {book_path} ---")
  print(f"{num_of_words} words found in the document")
  for character in characters_in_text_sorted:
    if character.isalpha():
      print(f"The '{character}' character was found {characters_in_text[character]} times")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_of_words(text):
  return len(text.split())

def get_character_count(book_text):
  characters_in_book = {}
  word_arr = book_text.split()

def count_characters(path):
  text = get_book_text(path)
  word_arr = text.split()
  characters = {}
  for word in word_arr:
    lowercase_word = word.lower()
    for letter in lowercase_word:
      if letter in characters:
        characters[letter] = int(characters[letter]) + 1
      else:
        characters[letter] = 1
  return characters
  
main()


