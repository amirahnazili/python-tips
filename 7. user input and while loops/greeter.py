''' How the input() Function Works '''

print("'''Writing Clear Prompts '''")

# Add a space at the end of your prompts (after the colon in the preceding
# example) to separate the prompt from the user’s response and to make
# it clear to your user where to enter their text.

name = input("Please enter your name: ")
print(f"\nHelo, {name}!")

# write a prompt longer than one line

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")


print("\n''' Using int() to Accept Numerical Input '''")

age = input("How old are you? ")
print(age)      # a string

# use int() function to treat input as a numerical value

age = input("How old are you? ")
age = int(age)
print(age)      # an integer