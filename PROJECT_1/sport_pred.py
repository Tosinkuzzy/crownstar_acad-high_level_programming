import random

# Constants
PREMIER_LEAGUE_TEAMS = [
    'Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton & Hove Albion',
    'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham',
    'Liverpool', 'Luton Town', 'Manchester City', 'Manchester United', 'Newcastle United',
    'Nottingham Forest', 'Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers'
]

# Functions
def predict_match(home_team, away_team):
    """Predict the result of a match between two teams."""
    # goals for home and away teams
    home_goals = random.randint(0, 5)
    away_goals = random.randint(0, 5)
    return home_goals, away_goals

def predict_all_premier_league_matches():
    """Predict matches for all combinations of Premier League teams."""
    match_predictions = {}
    for home_team in PREMIER_LEAGUE_TEAMS:
        for away_team in PREMIER_LEAGUE_TEAMS:
            if home_team != away_team:  # Avoid predicting matches where a team plays against itself
                match_predictions[(home_team, away_team)] = predict_match(home_team, away_team)
    return match_predictions

# Main execution
if __name__ == "__main__":
    all_match_predictions = predict_all_premier_league_matches()
    for teams, prediction in all_match_predictions.items():
        home_team, away_team = teams
        home_goals, away_goals = prediction
        print(f"Match prediction: {home_team} vs {away_team} - {home_goals}:{away_goals}")

