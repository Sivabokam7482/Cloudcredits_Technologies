import random

quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "If you want to achieve greatness stop asking for permission. – Anonymous",
    "All our dreams can come true if we have the courage to pursue them. – Walt Disney",
    "Act as if what you do makes a difference. It does. – William James",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    "It is never too late to be what you might have been. – George Eliot",
    "Happiness depends upon ourselves. – Aristotle",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis"
]

# Select and display a random quote
print("\033[1;33mRandom Quote: \033[0m ")
print("\033[1;34m"+random.choice(quotes)+"\033[0m")
