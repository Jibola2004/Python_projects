user_input = input('Enter a Phrase:')
if not user_input.strip():
    raise ValueError('invalid input. Enter a valid phrase.')

result=''
makeup=''
for text in user_input.split():
    result += text[0].upper()


# using a list comprehension    
acronym = ''.join([word[0].upper() for word in user_input.split()])
print(result)    
print(acronym)