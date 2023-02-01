import random
from art import logo


def final_result(player_score, computer_score):
    if player_score == 21 and len(player) == 2:
        return "you got a blackjack"
    elif computer_score == 21 and len(computer) == 2:
        return "computer got a blackjack"
    elif player_score > 21:
        return "you went over, you lose"
    elif computer_score > 21:
        return "you win"
    else:
        if player_score < computer_score:
            return "you lose"
        elif player_score == computer_score:
            return "its a draw"
        else:
            return "you win"


def game(s):

    if 11 in player and sum(player) > 21:
        player.remove(11)
        player.append(1)

    print(f"    your cards: {player} ,current score: {s}")
    print(f"    computers first card: {computer}")

    computer.append(random.choice(cards))
    final_score_p = sum(player)
    score = final_score_p

    if sum(computer) < 17:
        computer.append(random.choice(cards))
        if 11 in computer and sum(computer) > 21:
            computer.remove(11)
            computer.append(1)
    final_score_c = sum(computer)
    result = final_result(score, final_score_c)
    print(f"    your final hand is: {player}, final score : {final_score_p}")
    print(f"    your final hand is: {computer}, final score : {final_score_c}")
    print(result)


blackjack = True
while blackjack:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards)]
    score = sum(player)
    play = input("do you want to play blackjack? type 'y' or 'n' : ")
    if play == "y":
        print(logo)
        print(f"    your cards: {player} ,current score: {score}")
        print(f"    computers first card: {computer}")

        next_card = input("type 'y' to get another card, type 'n' tp pass: ")

        if next_card == "y":
            player.append(random.choice(cards))
            game(score)

        else:
            game(score)
    elif play == "n":
        blackjack = False
    else:
        print("invalin input try again")
