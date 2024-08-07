def main():
   path_to_book = "books/frankenstein.txt"
   book_text = get_book_contents(path_to_book)
   print(book_text)
   print(f"word count: {get_word_count(book_text)}")

def get_word_count(text):
   word_list = text.split()
   return len(word_list)
	

def get_book_contents(path):
   with open(path) as file:
      return file.read()

main()
