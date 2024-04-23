import random
from string import ascii_letters
import socket

HOST = '127.0.0.1'
PORT = 4337

words = ["Adam", "Ayna", "Gemi", "Yara", "Ders", "Oyun", "baba", "Anne", "Onay", "bina"]

def main(connection):

    word = random.choice(words)
    word = word.upper()
    
    formatted_word = word[0].upper() + " " + " ".join("*" for _ in range(len(word)-1))
    connection.sendall(f"Kelimeniz : {formatted_word}\nTahmin 1:".encode()) #Give first clue about the word
    #message forward to client (server -> client)
    
    for guess_num in range(2, 7):
        guess = connection.recv(1024).strip().decode().upper() #tahmini kullanıcan al (client -> server)

        result = show_guess(guess, word, connection)
        if guess == word:
            connection.sendall(f"Doğru Tahmin ettiniz, kelimeniz buydu:{word}\nTebrikler".encode())
            break
        if guess_num == 6:
            connection.sendall(f"\nDogru kelime {word} idi\nBitti".encode())
            break
        
        connection.sendall(f"{result}\nTahmin {guess_num}: ".encode())


def show_guess(guess, word, connection):
    feedback = []
    for guess_letter, word_letter in zip(guess, word):
        if guess_letter == word_letter:
            feedback.append(guess_letter.upper())
        elif guess_letter in word:
            feedback.append(guess_letter.lower())
        else:
            feedback.append('*')

    result = " ".join(feedback)
    return result

def start_game(connection):
    main(connection)
    connection.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Sunucu {HOST}:{PORT} adresinde dinleniyor...")

    while True:
        connection, address = server_socket.accept()
        print(f"{address} adresinden bağlantı alındı.")

        start_game(connection)
