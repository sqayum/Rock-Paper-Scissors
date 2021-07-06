from Player import Player
from Computer import Computer
from RPSDecisionMaker import RPSDecisionMaker

def rock_paper_scissors(max_rounds: int) -> None:
    dm = RPSDecisionMaker()
    player = Player()
    computer = Computer()

    move_names = {'R': "Rock".upper(), 'P': "Paper".upper(), 'S': "Scissors".upper()}

    current_round = 0
    while current_round < max_rounds:
        print(f"\n\n--------------------------- Round {current_round + 1} ----------------------------")
        print(f"\t(Player Score: {player.score} | Computer Score: {computer.score})")

        player_move = str(input("\n\tChoose your move [r/p/s]: "))
        computer_move = computer.play()

        outcome = dm.decide_outcome(player_move.upper() + computer_move.upper())
        if outcome[0] == -1:
            print(f'''\n\tYour move "{player_move}"" is invalid. You have lost a point.''')
        else:
            player_move_name = move_names[player_move.upper()]
            computer_move_name = move_names[computer_move]

            print(f"\n\t[Player >>> {player_move_name} | {computer_move_name} <<< Computer]")

            if outcome[0]:
                print(f"\n\t{player_move_name} beats {computer_move_name}. You win the round!")
            elif outcome[1]:
                print(f"\n\t{computer_move_name} beats {player_move_name}. Computer wins the round!")
            else:
                print(f"\n\tBoth participants threw {player_move_name}. Round is a draw.")

        print("----------------------------------------------------------------")

        player.change_score(outcome[0])
        computer.change_score(outcome[1])

        current_round += 1

        if abs(player.score - computer.score) > (max_rounds - current_round):
            break

    print(f"\n\n------------------------ Match Results -------------------------")
    print(f"\t(Player Score: {player.score} | Computer Score: {computer.score})")

    if player.score == computer.score:
        print("\n\t\t*** MATCH DRAWN ***")
    else:
        if player.score > computer.score:
            winner = "Player"
        else:
            winner = "Computer"

        print(f"\n\tMATCH WINNER [best of {max_rounds} round(s)]: *** {winner} ***")

    print("----------------------------------------------------------------\n")
