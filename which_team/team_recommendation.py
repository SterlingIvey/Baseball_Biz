import pandas as pd

def get_team_recommendation(): 
    print("Welcome User! Which baseball team should you root for?")
    
    # Questions and scoring logic
    
    questions = [{"question": "What region of the country do you live in? (East Coast, Midwest, West Coast, South)", "weight": "region"}
                 {"question": "Are you a history buff? (Yes/No)", "weight": "history"}, 
                 {"question": "Are you passionate about other sports? (Yes/No)", "weight": "passionate"},
                 {"question": "Did you grow up playing baseball? (Yes/No)", "weight": "iq"},
                 {"question": "Do you want to be able to own a piece of your team? (Yes/No)", "weight": "public"}
                ]
                
    # Team data and weightings
    
    teams_data = {         "New York Mets": {"history": 2, "passionate": 1, "iq": 1, "public": 2}, 
                           "Atlanta Braves": {"history": 1, "passionate": 1, "iq": 2, "public": 1}, 
                           "Miami Marlins": {"history": 2, "passionate": 2, "iq": 2, "public": 2}, 
                           "Philadelphia Phillies": {"history": 1, "passionate": 1, "iq": 2, "public": 2}, 
                           "Washington Nationals": {"history": 2, "passionate": 2, "iq": 2, "public": 2}, 
                           "Chicago Cubs": {"history": 1, "passionate": 1, "iq": 1, "public": 2}, 
                           "Cincinnati Reds": {"history": 1, "passionate": 2, "iq": 2, "public": 2}, 
                           "Milwaukee Brewers": {"history": 1, "passionate": 2, "iq": 2, "public": 2},
                           "Pittsburgh Pirates": {"history": 1, "passionate": 1, "iq": 2, "public": 2}, 
                           "St Louis Cardinals": {"history": 1, "passionate": 1, "iq": 1, "public": 2}, 
                           "Arizona Diamondbacks": {"history": 2, "passionate": 2, "iq": 2, "public": 2},
                           "Colorado Rockies": {"history": 2, "passionate": 2, "iq": 2, "public": 2},
                           "San Diego Padres": {"history": 2, "passionate": 2, "iq": 2, "public": 2}, 
                           "San Francisco Giants": {"history": 1, "passionate": 1, "iq": 1, "public": 2}, 
                           "Baltimore Orioles": {"history": 1, "passionate": 1, "iq": 1, "public": 2},
                           "New York Yankees": {"history": 1, "passionate": 1, "iq": 1, "public": 2}, 
                           "Tampa Bay Rays": {"history": 2, "passionate": 2, "iq": 1, "public": 2}, 
                           "Boston Red Sox": {"history": 1, "passionate": 1, "iq": 1, "public": 2}, 
                           "Toronto Blue Jays": {"history": 2, "passionate": 2, "iq": 2, "public": 1},
                           "Chicago White Sox": {"history": 1, "passionate": 2, "iq": 2, "public": 2},
                           "Cleveland Guardians": {"history": 1, "passionate": 2, "iq": 2, "public": 2},
                           "Detroit Tigers": {"history": 1, "passionate": 2, "iq": 2, "public": 2},
                           "Kansas City Royals": {"history": 2, "passionate": 2, "iq": 2, "public": 2},
                           "Minnesota Twins": {"history": 1, "passionate": 2, "iq": 2, "public": 2}
                        }
                        
    # Convert to Data Frame for easier manipulation
    
    df_teams = pd.DataFrame.from_dict(teams_data, orient='index')
    
    # Initialize scores
    
    scores = {team: 0 for team in teams_data}
    
    # Process each question
    
    for question in questions: 
        answer = input(question["question"] + " ").strip().lower()
        if answer not in ['yes', 'no', 'y', 'n', 'Yes', 'No', 'Y', 'N']:  # Validate input
            print("Invalid answer. Please answer some form of 'Yes' or 'No'.")
            return None
        
        # Update scores based on the user's answers
    
        for team in scores:
            if answer == 'yes' or answer == 'y' or answer == 'Yes' or answer == 'Y':
                scores[team] += df_teams.at[team, question["weight"]]
            else:
                scores[team] += df_teams.at[team, question["weight"]] * 0
# No points if no
        
    # Determine recommended team
    
    recommended_team = max(scores, key=scores.get)
    return recommended_team
    
# Run the questionnaire 

team = get_team_recommendation()
print(f"Based on your answers, you might enjoy rooting for the {team}!")
                        
