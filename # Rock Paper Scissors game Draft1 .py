# Rock Paper Scissors game with dependency injected/deterministic testing.
def test_rps(user_input, user_score, computer_score, computer_input):
 
 if user_input.lower() == computer_input.lower():                                                                                                           # If a draw
        return user_score, computer_score, f" You tied! You have {user_score} points and the Computer has {computer_score} points"
      
 if user_input.lower() == "rock" and computer_input.lower() == "scissors":                                                                                  # All other bases
        user_score += 1
        return user_score, computer_score, f" Congratulations, you win! You have {user_score} points and the Computer has {computer_score} points"
    
 if user_input.lower() == "rock" and computer_input.lower() == "paper":
        computer_score += 1
        return user_score, computer_score, f" Unlucky, you lost! You have {user_score} points and the Computer has {computer_score} points"
    
 if user_input.lower() == "scissors" and computer_input.lower() == "paper":
        user_score += 1
        return user_score, computer_score, f" Congratulations, you win! You have {user_score} points and the Computer has {computer_score} points"
    
 if user_input.lower() == "scissors" and computer_input.lower() == "rock":
        computer_score += 1
        return user_score, computer_score, f" Unlucky, you lost! You have {user_score} points and the Computer has {computer_score} points"
    
 if user_input.lower() == "paper" and computer_input.lower() == "rock":
        user_score += 1
        return user_score, computer_score, f" Congratulations, you win! You have {user_score} points and the Computer has {computer_score} points" 
    
 if user_input.lower() == "paper" and computer_input.lower() == "scissors":
        computer_score += 1
        return user_score, computer_score, f" Unlucky, you lost! You have {user_score} points and the Computer has {computer_score} points" 

import random # For randomising the computers input

def rock_paper_scissors_game(user_score=0, computer_score=0, computer_input=None):                                       # Creating the function

    if computer_input is None:                                                           # If no computer input
        computer_input = random.choice(["rock", "paper", "scissors"])                    # Create a random computer input

    user_input = input("Make your choice: Rock, Paper or Scissors: ")                    # Takes the users choice
    print("\n3, \n2, \n1!")                                                              # Countdown 

    user_score, computer_score, message = test_rps(user_input, user_score, computer_score, computer_input) # Stores the result as 3 different values
    print(message)                                                                                         # Prints only the message

    answer = input("Would you like to play again?: ").lower()                                              # Go again?
    if answer == "yes" or answer == "yeah":                                                                # If yes
     rock_paper_scissors_game(user_score, computer_score, computer_input=None)                             # Use the updated scores and go again.
    
rock_paper_scissors_game()                                                                                 # First function call



   
 
        
    
