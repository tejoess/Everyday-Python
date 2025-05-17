import random

def get_closest_player(guesses, avg):
    closest_player = None
    closest_diff = float('inf')
    for player, guess in guesses.items():
        diff = abs(guess - avg)
        if diff < closest_diff:
            closest_diff = diff
            closest_player = player
    return closest_player

def play_game():
    print("🎯 Welcome to the Guess the Average Game!")
    
   
    num_players = int(input("Enter number of players: "))
    players = []
    for i in range(num_players):
        name = input(f"Enter name of player {i+1}: ")
        players.append(name)
    
    target = int(input("Enter target score (must be negative): "))
    if target >= 0:
        print("Target must be a negative number. Exiting...")
        return

   
    scores = {player: 0 for player in players}
    
    round_num = 1
    while True:
        print(f"\n🔁 Round {round_num}")
        
        
        guesses = {player: random.randint(1, 100) for player in players}
        for player, guess in guesses.items():
            print(f"{player} guessed: {guess}")
        
        
        avg = sum(guesses.values()) / num_players
        print(f"📊 Average of guesses: {avg:.2f}")
        
        
        winner = get_closest_player(guesses, avg)
        print(f"🏆 {winner} was closest to the average!")

        
        for player in players:
            if player != winner:
                scores[player] -= 1
        
        
        for player, score in scores.items():
            print(f"{player}'s score: {score}")
        
        
        active_players = [player for player, score in scores.items() if score > target]
        if len(active_players) == 1:
            print(f"\n🎉 {active_players[0]} is the last player standing and wins the game!")
            break
        round_num += 1


if __name__ == "__main__":
    play_game()
