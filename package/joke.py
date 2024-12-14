# import pyjokes

# joke = pyjokes.get_jokes()
# print(joke[0])


import pyjokes

# Function to get a joke based on theme
def get_joke(category):
    if category == "neutral":
        joke = pyjokes.get_joke(category='neutral')
    elif category == "chuck":
        joke = pyjokes.get_joke(category='chuck')
    else:
        joke = "Sorry, I can only tell 'neutral' or 'chuck' jokes for now."
    return joke

# User input for joke type
category = input("Enter the type of joke you want (neutral/chuck): ").strip().lower()
print(get_joke(category))
