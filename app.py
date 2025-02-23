from flask import Flask, render_template
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why do cows have hooves instead of feet? Because they lactose!",
    "What did one snowman say to the other snowman? It smells like carrots over here!",
    "Why did Beethoven get rid of his chickens? All they ever said was, “Bach, Bach, Bach!",
]

@app.route("/")
def home():
    joke = random.choice(jokes)
    return render_template("index.html", joke=joke)

if __name__ == "__main__":
    app.run(debug=True)
