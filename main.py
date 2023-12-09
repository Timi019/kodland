import random
import time


pol_words = ["Cześć", "Pa", "Zadanie", "Program"]
eng_words = ['Hello','Bye','Task', 'Program']
score = 0

mode = input("Wybierz tryb: 0 - dodawaj nowe słowa, 1 - trenuj: \n")
while ((mode != '0') and (mode != '1')):
    mode = input("Nieprawidłowy symbol! Wybierz 0 lub 1. (0 dodaje nowe słowa, a 1 umożliwia naukę) \n")

if mode == "1":
    print("Przetłumacz jak najwięcej słów! Masz 10 prób!")
    for i in range(10):
        number = random.randint(0, len(pol_words)-1)
        print("Jak powinniśmy tłumaczyć: " + pol_words[number])
        if input() == eng_words[number]:
            print("Świetnie!!!")
            score += 1
        else:
            print("Nie, niezupełnie... Właściwe słowo to - " + eng_words[number])
else:
    word = input("Wpisz polskie słowo: ")
    translate = input("Wpisz tłumaczenie tego słowa: ")
    if len(word) > 0 and len(translate) > 0:
        pol_words.append(word)
        eng_words.append(translate)
        print("Słowo zostało pomyślnie dodane!")
