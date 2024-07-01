from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Do not watch the clock. Do what it does. Keep going. - Sam Levenson",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "The best way to predict the future is to invent it. - Alan Kay",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-quote')
def generate_quote():
    quote = random.choice(quotes)
    return jsonify({'quote': quote})

if __name__ == "__main__":
    app.run(debug=True)
