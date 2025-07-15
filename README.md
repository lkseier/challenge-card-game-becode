# 🎴 Challenge: Card Game - BeCode
Creating a card game making good use of OOP skills

This project is a simple Object-Oriented Python card game simulation built as part of a coding challenge at [BeCode](https://becode.org). The game demonstrates core OOP principles like class design, inheritance, and project architecture.

---

## 📌 Description

Players are dealt cards from a shuffled 52-card deck. In each turn, all players randomly play a card from their hand. The player with the highest-ranked card wins the round and gains a point. The game continues until all cards are played. The player with the most points at the end wins.

---

## 🧠 Concepts & Learning Goals

- ✅ Object-Oriented Programming (OOP)
- ✅ Class inheritance and encapsulation
- ✅ Clean Python project structure
- ✅ Custom imports and typing
- ✅ Game loop and logic
- ✅ Interactive command-line interface

---

## 🗃️ Project Structure

challenge-card-game-becode/
├── main.py
├── README.md
└── utils/
├── init.py
├── card.py # Card and Symbol classes
├── deck.py # Deck generation, shuffling, and distribution
├── game.py # Board class and main game loop
└── player.py # Player logic and card play


---

## 🧩 How It Works

1. A full deck (52 cards) is created.
2. The deck is shuffled and distributed evenly to all players.
3. Each player plays a card per round.
4. The highest-ranked card wins the round.
5. The game ends when all cards are used.
6. The player with the most points is declared the winner.

---

## 🚀 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/challenge-card-game-becode.git
   cd challenge-card-game-becode

2. (Optional but recommended) Create a virtual environment:
python -m venv env
source env/bin/activate     # On Linux/Mac
.\env\Scripts\activate      # On Windows

3. Run the game:
python main.py

🕹️ Usage
Just run main.py, and you'll be prompted to input how many players will participate. The game will then simulate each round and print round winners and final scores.

💡 Example Output

🎲 Game Start!

--- Turn 1 ---
Alice played: 7♣
Bob played: J♦
🏆 Bob wins Turn 1 with J♦

...

🎉 Game Over!
📊 Final Scores:
Alice: 5 point(s)
Bob: 7 point(s)

🏅 Winner: Bob!

✨ Features
Must-Have ✅
 52 unique cards generated

 Cards distributed among players

 Each player plays one card per turn

 Game runs until all cards are played

Nice-to-Have 💡
 Interactive user prompt

 Score system

 Determine winner(s)

 User chooses cards (WIP)

 Real card games (e.g. War, Blackjack) (Future scope)

🧪 Constraints
No relative imports like from .module import

Typed functions and classes

Docstrings and in-code documentation

Clean and readable code

👨‍💻 Contributors: 
| Name               |    Role      |
| ---------          |    --------- |
| 
| Klebert Tchatchoua |   Developper |

💭 Personal Situation
This project was completed as part of my learning journey at BeCode. It was an excellent challenge to apply OOP principles in a fun and structured way while reinforcing good coding practices and clean architecture.

🏁 Final Note
Thanks for checking out my project. Feel free to fork it, run it, and even build your own version of a card game!



