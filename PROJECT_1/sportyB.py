import random
import string

# Constants
COUNTRIES = [
    'USA', 'UK', 'Germany', 'France', 'Spain', 'Italy',
    'Netherlands', 'Brazil', 'Argentina', 'Australia'
]

# Functions
def generate_player_name(length=5):
    """Generate a random player name consisting of uppercase letters."""
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def generate_player_country():
    """Randomly select a player's country from a predefined list."""
    return random.choice(COUNTRIES)

def generate_virtual_game_info():
    """Generate virtual game information for a player."""
    player_name = generate_player_name()
    player_country = generate_player_country()
    player_credits = random.randint(1000, 10000)
    return player_name, player_country, player_credits

# Main execution
if __name__ == "__main__":
    player_name, player_country, player_credits = generate_virtual_game_info()
    print(f"Player Name: {player_name}")
    print(f"Player Country: {player_country}")
    print(f"Player Credits: {player_credits}")

