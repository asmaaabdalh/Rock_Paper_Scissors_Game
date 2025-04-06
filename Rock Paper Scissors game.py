import random
print("Welcome to Rock, Paper, Scissors game: ")
check = input("Press enter to play or type (Help) for rules ").lower()
if check == "help":
    print("""
        *********** RULES ************
        1) you chose and the computer chose
        2) Rock defeats Scissors -> Rock wins
        3) Paper defeats Rock -> Paper wins
        4) Scissors defeats Paper -> Scissors wins
        ......
        
        """)

chose = input("enter your choice Rock, Paper, Scissors: ").lower()
computer = ["rock", "paper", "scissors"]  # Removed space before "paper"
n = random.randint(0, 2)
final = computer[n]

if chose not in computer:
    print("Invalid option")
elif chose == final:
    print(f"""
        You chose: {chose}
        Computer chose: {final}
        
        It's a tie!
    """)
elif (chose == "rock" and final == "scissors") or \
        (chose == "paper" and final == "rock") or \
        (chose == "scissors" and final == "paper"):
    print(f"""
        You chose: {chose}
        Computer chose: {final}
        
        You win!
    """)
else:
    print(f"""
        You chose: {chose}
        Computer chose: {final}
        
        Computer wins
    """)