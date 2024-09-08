# WordGuessingGame

WordGuessingGame is a simple client-server application written in Python. It allows players to connect to a server and guess a hidden 4-letter word. The server provides feedback after each guess, helping the player deduce the correct word within a limited number of attempts.

## Features

- The server randomly selects a 4-letter word from a predefined list.
- The word is hidden, with only the first letter revealed to the player.
- After each guess, the server provides feedback:
  - Correct letters in the correct position are shown in uppercase.
  - Correct letters in the wrong position are shown in lowercase.
  - Incorrect letters are shown as '*'.
- Players have a total of 6 attempts to guess the word correctly.
- If the player guesses the word correctly, they win. If they fail after 6 attempts, the game reveals the correct word.

## Requirements

- Python 3.x

## How to Run

### Server Setup

1. Start the server by running the `server.py` file:
   ```bash
   python server.py

This will start the server and begin listening for client connections at 127.0.0.1:4337.

## Client Setup
1. The client connects to the server by running the client.ipynb file in a Jupyter Notebook or converting it into a .py script.
2. Once connected, the client will receive clues from the server and can begin making guesses.

### Example
#### Server
When you run the server, it will wait for clients to connect. Once connected, it will initiate the game by sending the player a word clue (e.g., A ***). After each guess, feedback is provided (e.g., A *n*).

#### Client
When the client connects to the server, they will receive a clue and begin guessing. Each guess must be a 4-letter word. After sending the guess, the client will receive feedback on how close their guess was. The goal is to guess the correct word within 6 attempts.

## Code Structure
### server.py
This script initializes a socket server that listens for incoming connections. Once a client connects, the server selects a random word and initiates the game loop, handling guesses and providing feedback until the player either wins or runs out of attempts.

### client.ipynb
This script acts as the client, connecting to the server and interacting with it by sending guesses and receiving feedback. The client must guess a 4-letter word and receive feedback on each attempt.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
