from rock_paper_scissors import rock_paper_scissors

def main():

    print("\n****************************************************************")
    print("\tWelcome to Rock-Paper-Scissors      ")
    print("****************************************************************")
    print("\tCommands:\n\t\t'r' -> Rock\n\t\t'p' -> Paper\n\t\t's' -> Scissors")
    print("****************************************************************")

    num_rounds = int(input("\tEnter number of rounds to be played: "))
    if not isinstance(num_rounds, int):
        raise TypeError("<num_rounds> must be an integer")
    if num_rounds <= 0:
        raise ValueError("<num_rounds> must be >= 0")

    print("****************************************************************")

    rock_paper_scissors(num_rounds)

main()