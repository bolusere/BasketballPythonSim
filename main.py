#Basketball sim in Python -- probably really badly
import random
from scripts import *
from classes import *
if __name__ == "__main__":
    """
    # ------------------|  NAME  |HGT|WTLB|SPD|AGE|INS|MID|OUT|PSS|HND|STL|BLK|IND|OTD|REB| 
    StanPoint = bbplayer("Pointy", 72, 150, 90, 25, 75, 75, 75, 99, 90, 80, 30, 30, 80, 20)
    StanShoot = bbplayer("Shooty", 76, 180, 80, 25, 75, 85, 95, 75, 75, 50, 50, 50, 75, 40)
    StanSmall = bbplayer("Smally", 80, 200, 80, 25, 80, 85, 80, 70, 75, 85, 70, 75, 80, 75)
    StanPower = bbplayer("Powery", 82, 220, 60, 25, 80, 75, 30, 60, 75, 60, 90, 85, 70, 85)
    StanCenter= bbplayer("iBeast", 84, 250, 40, 25, 95, 50, 20, 40, 50, 40, 90, 90, 50, 90)

    # ------------------|  NAME  |HGT|WTLB|SPD|AGE|INS|MID|OUT|PSS|HND|STL|BLK|IND|OTD|REB|
    StanPoin2 = bbplayer("iJesus", 72, 150, 90, 25, 99, 99, 99, 99, 90, 80, 30, 30, 80, 20)
    StanShoo2 = bbplayer("3Shoot", 76, 180, 80, 25, 99, 99, 99, 99, 75, 50, 50, 50, 75, 40)
    StanSmal2 = bbplayer("Onlydf", 80, 200, 80, 25, 99, 99, 99, 99, 75, 85, 70, 75, 80, 75)
    StanPowe2 = bbplayer("Power2", 82, 220, 60, 25, 99, 99, 99, 99, 75, 60, 90, 85, 70, 85)
    StanCente2= bbplayer("Cente2", 84, 250, 40, 25, 99, 99, 99, 99, 50, 40, 90, 90, 50, 90)

    max_overall = 0
    min_overall = 2000
    overall_1 = 0
    overall_2 = 0
    overall_3 = 0
    overall_4 = 0
    overall_5 = 0
    gen_num = 2000
    for i in range(gen_num):
        ov = generate_player(1, 0).overall
        overall_1 += ov
        if ov > max_overall:
            max_overall = ov
        if ov < min_overall:
            min_overall = ov
    for i in range(gen_num):
        ov = generate_player(2, 0).overall
        overall_2 += ov
        if ov > max_overall:
            max_overall = ov
        if ov < min_overall:
            min_overall = ov
    for i in range(gen_num):
        ov = generate_player(3, 0).overall
        overall_3 += ov
        if ov > max_overall:
            max_overall = ov
        if ov < min_overall:
            min_overall = ov
    for i in range(gen_num):
        ov = generate_player(4, 0).overall
        overall_4 += ov
        if ov > max_overall:
            max_overall = ov
        if ov < min_overall:
            min_overall = ov
    for i in range(gen_num):
        ov = generate_player(5, 0).overall
        overall_5 += ov
        if ov > max_overall:
            max_overall = ov
        if ov < min_overall:
            min_overall = ov
    
    print("  Point Guard Average:", overall_1/gen_num)
    print("  Shoot Guard Average:", overall_2/gen_num)
    print("Small Forward Average:", overall_3/gen_num)
    print("Point Forward Average:", overall_4/gen_num)
    print("       Center Average:", overall_5/gen_num)
    print("          Max Overall:", max_overall)
    print("          Min Overall:", min_overall)
    
    """
    while True:
        try:
            league_size = int(input("Enter total number of teams in league: "))
            if league_size <= 0:
                print("pick a positive integer idiot")
            else:
                break
        except ValueError:
            print("pick a positive integer idiot")
            
    while True:
        try:
            draft_pos = int(input("What pick do you want in the draft? (1-{max}) ".format(max=league_size)))
            if draft_pos < 1 or draft_pos > league_size:
                print("Has to be between 1 and the total number of teams in league.")
            else:
                break
        except ValueError:
            print("Has to be between 1 and the total number of teams in league.")
            
    draft_list = draft_generate(league_size * 5 + 10)
    player_team, opponents_teams = draft_start(draft_list, league_size - 1, draft_pos)
    #TEAM MANAGEMENT:
    name = input("Input team name: ")
    player_team.name = name
    while True:
        player_team.print_team()
        glhf = input("Make your selection: ")
        if glhf == "b":
            break
        glhf = glhf.replace(" ", "")
        partitioned_tuple = glhf.partition(",")

        player_team.swap_players(int(partitioned_tuple[0]), int(partitioned_tuple[2]))

    #play season fool
    league = []
    for ai in opponents_teams:
        league.append(ai)
    league.append(player_team)
    playseason(league)
    
    input("\nPress Enter to continue to the playoffs...")
    
    teamwins = []
    for team in league:
        teamwins.append(team.wins)
    teamwins.sort()
    backup_league = league
    playoff_teams = []
    while len(playoff_teams) < 8:
        for team in league:
            if len(teamwins) > 0:
                if team.wins == teamwins[len(teamwins) - 1]: #most wins
                    playoff_teams.append(team)
                    teamwins.remove(team.wins)
    
    finals_winner = playoffs(playoff_teams)
    print("\n",finals_winner.name,"HAVE WON THE NBA FINALS!!")
    """
    
    """
    print("\n*** Average Joes' attributes: ***")
    StanPoint = generate_player(1, 0)
    StanShoot = generate_player(2, 0)
    StanSmall = generate_player(3, 0)
    StanPower = generate_player(4, 0)
    StanCenter= generate_player(5, 0)
    
    print("\n*** The Not Bads' attributes: ***")
    StanPoin2 = generate_player(1, 0)
    StanShoo2 = generate_player(2, 0)
    StanSmal2 = generate_player(3, 0)
    StanPowe2 = generate_player(4, 0)
    StanCente2= generate_player(5, 0)


    team_A = team("Average Joes", StanPoint, StanShoot, StanSmall, StanPower, StanCenter)
    team_B = team("The Not Bads", StanPoin2, StanShoo2, StanSmal2, StanPowe2, StanCente2)
    """
    #team_A = player_team
    #team_B = opponents_list[0].ai_team
    #playseries(team_A, team_B, 7, 0, 1)
    #print("\n")
    #team_A.print_team_ratings()
    #print("\n")
    #team_B.print_team_ratings()
    #print("\nJoes Mismatches:")
    #detect_mismatch(team_A, team_B, 1)
    #print("\nBads Mismatches:")
    #detect_mismatch(team_B, team_A, 1)


    #gonna play season fool
    while True:
        try:
            league_size = int(input("Input number of teams: "))
            if league_size < 2:
                print("Pick a positive integer greater than 1, idiot.")
            else:
                break
        except ValueError:
            print("Pick a positive integer greater than 1, idiot.")
            
    league = generate_league(league_size)
    playseason(league)
    """
