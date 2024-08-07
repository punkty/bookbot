def main():
   path_to_book = "books/frankenstein.txt"
   book_text = get_book_contents(path_to_book)
   print(f"--- Begin report of {path_to_book} ---")
   print(f"{get_word_count(book_text)} words found in the document")
   letter_to_count = letter_count_dictionary(book_text)
   letter_count_list = construct_list_of_dictionaries(letter_to_count)
   letter_count_list.sort(reverse=True, key=sort_on)
   for item in letter_count_list:
      print(f"The {item['letter']} character was found {item['count']} times")
   print("--- End report ---")

def sort_on(dict):
   return dict["count"]

def construct_list_of_dictionaries(dict):
   list_of_dictionaries = []
   for k, v in dict.items():
      if k.isalpha():
         letter_count_pair = {"letter": k, "count": v }
         list_of_dictionaries.append(letter_count_pair)

   return list_of_dictionaries
def letter_count_dictionary(text):
   lowered_text = text.lower()
   letter_to_count = {}
   for character in lowered_text:
      if character not in letter_to_count.keys():
         letter_to_count[character] = 1
      else:
         letter_to_count[character] += 1

   
   return letter_to_count
      

def get_word_count(text):
   word_list = text.split()
   return len(word_list)
	

def get_book_contents(path):
   with open(path) as file:
      return file.read()

main()
