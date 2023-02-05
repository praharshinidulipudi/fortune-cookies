import random

def fortune_cookie():
    messages = ["Today will be a lucky day", "You will meet someone new and interesting", "Watch out for obstacles in your path"]
    message = random.choice(messages)
    print(message)

if __name__ == '__main__':
    fortune_cookie()
