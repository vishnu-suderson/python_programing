def last_word_length(my_string):
   init_val = 0

   processed_str = my_string.strip()

   for i in range(len(processed_str)):
      if processed_str[i] == " ":
         init_val = 0
      else:
         init_val += 1
   return init_val

my_input = input("enter the string")
print("The string is :")
print(my_input)
print("The length of the last word is :")
print(last_word_length(my_input))