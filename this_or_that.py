import random

# A dictionary of celebrities with their estimated net worth (in millions)
net_worth = {
    "Elon Musk": 250000,
    "Jeff Bezos": 180000,
    "Bill Gates": 115000,
    "Mark Zuckerberg": 70000,
    "Warren Buffett": 105000,
    "Larry Page": 105000,
    "Sergey Brin": 100000,
    "Steve Jobs": 10000,
    "Oprah Winfrey": 3000,
    "Michael Jordan": 2200,
    "Mukesh Ambani": 83000,
    "Gautam Adani": 60000,
    "Ratan Tata": 1000,
    "Shah Rukh Khan": 750,
    "Amitabh Bachchan": 400,
    "Akshay Kumar": 300,
    "Virat Kohli": 125,
    "Sachin Tendulkar": 170,
    "Deepika Padukone": 50,
    "Priyanka Chopra": 70
}

def get_two_random_celebrities(net_worth_dict):
    return random.sample(list(net_worth_dict.keys()), 2)

def this_or_that_net_worth_game():
    print("Welcome to the Net Worth 'This or That' Game!")
    print("In this game, you'll be presented with two celebrities.")
    print("Your task is to guess who has the higher net worth by typing 'A' or 'B'.")
    print("Type 'quit' at any time to exit the game.\n")
    
    while True:
        celeb1, celeb2 = get_two_random_celebrities(net_worth)
        print(f"Who has a higher net worth?")
        print(f"A: {celeb1}")
        print(f"B: {celeb2}")
        choice = input("Your choice (A/B): ").strip().lower()
        
        if choice == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        
        if choice in ['a', 'b']:
            chosen_celeb = celeb1 if choice == 'a' else celeb2
            other_celeb = celeb2 if choice == 'a' else celeb1
            
            if net_worth[chosen_celeb] >= net_worth[other_celeb]:
                print(f"Correct! {chosen_celeb} has a net worth of ${net_worth[chosen_celeb]:,} million, and {other_celeb} has a net worth of ${net_worth[other_celeb]:,} million.\n")
            else:
                print(f"Wrong! {chosen_celeb} has a net worth of ${net_worth[chosen_celeb]:,} million, but {other_celeb} has a net worth of ${net_worth[other_celeb]:,} million.\n")
                replay_choice = input("Do you want to play again? (yes/no): ").strip().lower()
                if replay_choice == 'yes':
                    print("\nGreat! Let's start again.\n")
                    continue
                else:
                    print("Thanks for playing! Goodbye!")
                    break
        else:
            print("Invalid choice. Please choose 'A' or 'B' or type 'quit' to exit.\n")

if __name__ == "__main__":
    this_or_that_net_worth_game()
