# Snake Water Gun Game
import random
plays_left = 10
player_pts = 0
comp_pts = 0
while plays_left != 0:
    options = ["S", "W", "G"]
    choice = random.choice(options)
    player = input("Enter your choice:\n S for Snake\n W for Water\n G for Gun\n") 
    plays_left -= 1

    if choice == 'G' and player.lower() == "s":
        comp_pts += 1
        print(f"Computer wins this round. Number of Plays left {plays_left}")
        print(f"Your points:{player_pts}\nComputer points:{comp_pts}\n")

    elif choice == 'S' and player.lower() == "w":
        print(f"Computer wins this round. Number of Plays left {plays_left}")
        comp_pts += 1
        print(f"Your points:{player_pts}\nComputer points:{comp_pts}\n")

    elif choice == 'W' and player.lower() == "g":
        print(f"Computer wins this round. Number of Plays left {plays_left}")
        comp_pts += 1
        print(f"Your points:{player_pts}\nComputer points:{comp_pts}\n")

    elif choice == 'S' and player.lower() == "g":
        print(f"You win this round. Number of Plays left {plays_left}")
        player_pts += 1
        print(f"Your points:{player_pts}\nComputer points:{comp_pts}\n")

    elif choice == 'W' and player.lower() == "s":
        print(f"You win this round. Number of Plays left {plays_left}")
        player_pts += 1
        print(f"Your points:{player_pts}\nComputer points:{comp_pts}\n")

    elif choice == 'G' and player.lower() == "w":
        print(f"You win this round. Number of Plays left {plays_left}")
        player_pts += 1
        print(f"Your points:{player_pts}\nComputer points:{comp_pts}\n")

    elif (choice == 'S' and player.lower() == "s") or (choice == "W" and player.lower() == "w") or \
            (choice == "G" and player.lower() == "g"):
        print(f"Both made same choice.Number of Plays left {plays_left}")
        print(f"Your points:{player_pts}\nComputer points:{comp_pts}\n")

    else:
        print("Invalid choice :(")
        plays_left += 1

print("------------ Game Over ------------")
if player_pts > comp_pts:
    print("Hurrah!! You Won ;)")
elif comp_pts > player_pts:
    print("Computer Wins.Better luck next time! :)")
else:
    print("Game Tied.Well Played!")
