# Write a Program to fill in a letter template given below with name and date.
letter = '''Dear <|Name|>,
Greetings from ABC Coding House. I am happy to tell you about your Selection
You Are Selected!
Have a Great Day...
Date: <|DATE|>
'''
name = input("Enter Your Name: ")
date = input("Enter Date: ")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
