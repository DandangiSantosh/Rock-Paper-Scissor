import random
i=1
player_wins = 0
computer_wins = 0
draw = 0
print("Welcome to Rock,Paper,Scissor!!\nYou will paly total 10 rounds\nWho score high points\nIf you win more rounds than computer then you are winner😃\nLet's Start the game.....!!")
while i<=10:
    print(f"------ Round-{i} ------")
    choice = input("\nChoices:\nRock(R)\nPaper(P)\nScissor(S)\n\nPick: ")
    your_choice = choice.lower()

    l = ['r','p','s']
    computer_choice = random.choice(l)

    if your_choice not in l:
        print("Invalid Choice!!!!")
        continue
    elif your_choice == computer_choice:
        print(f"Your choice: {your_choice}\nComputer choice: {computer_choice}\nIt's a draw!!😒\n")
        draw += 1
    elif your_choice == 'r' and computer_choice == 's':
        print(f"Your choice: Rock\nComputer choice: Scissor\nYou won!!🎉\n")
        player_wins+=1
    elif your_choice == 's' and computer_choice == 'p':
        print(f"Your choice: Scissor\nComputer choice: Paper\nYou won!!🎉\n")
        player_wins += 1
    elif your_choice == 'p' and computer_choice == 'r':
        print(f"Your choice: Paper\nComputer choice: Rock\nYou won!!🎉\n")
        player_wins += 1
    else:
        if your_choice == 'r':
            your_choice = "Rock"
        elif your_choice == 's':
            your_choice = "Scissor"
        elif your_choice == 'p':
            your_choice = "Paper"
        if computer_choice == 'r':
            computer_choice = "Rock"
        elif computer_choice == 'p':
            computer_choice = "Paper"
        elif computer_choice == 's':
            computer_choice = "Scissor"
        print(f"Your choice: {your_choice}\nComputer choice: {computer_choice}\nComputer won!!😭\n\n")
        computer_wins+= 1
    i+=1

print(f"Your wins: {player_wins}\nComputer wins: {computer_wins}\nDraw: {draw}\n")
if player_wins>computer_wins:
    print("Congratulations!!!! You won the match🎉🎉....\n")
elif player_wins<computer_wins:
    print("Computer won the match...Better luck next time😭\n")
else:
    print("Its a draw Match")

print("Bye..Bye....")
