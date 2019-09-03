import operator
#1. 
phonebook_dict = { 
  'Alice': '703-493-1834', 
  'Bob': '857-384-1234', 
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])

#2. Nested Dictionaries
ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}

print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])



word = "hello"
letter_tally = {}
for char in word:
    if char not in letter_tally:
        letter_tally[char] = 1
    else:
        letter_tally[char] += 1

print(letter_tally)

sentence = "to be or not to be"
word_tally = {}
word_array = sentence.split()
for word in word_array:
    if word not in word_tally:
        word_tally[word] = 1
    else:
        word_tally[word] += 1

print(word_tally)

most_letter_count = 0
the_dang_letter = ''
for char in letter_tally:
    print(char)
    print(letter_tally[char])
    if letter_tally[char] > most_letter_count:
        the_dang_letter = char

print(the_dang_letter)


phonebook_dict['Bob'] = '430-109-2093'
print(phonebook_dict)

phonebook_complicated = [{"Name":"Bob", "Number":'507-256-7890'}, {"Name":"Alice", "Number":'302-465-3029'}]
new_number = "405-215-9999"

for dictionary in phonebook_complicated:
    if dictionary["Name"] == "Bob":
        dictionary["Number"] = new_number

        
# for user in phonebook_complicated:
#     if phonebook_complicated["Name"] == "Bob":
#         phonebook_complicated["Number"] = new_number

print(phonebook_complicated)
