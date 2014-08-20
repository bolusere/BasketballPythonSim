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
    StanCente2= bbplayer("Cente2", 84, 250, 40, 25, 99, 99, 99, 99, 50, 40, 90, 90, 50, 90)"""
    print("\n*** Average Joes' attributes: ***")
    StanPoint = generate_player(1)
    StanShoot = generate_player(2)
    StanSmall = generate_player(3)
    StanPower = generate_player(4)
    StanCenter= generate_player(5)
    
    print("\n*** The Not Bads' attributes: ***")
    StanPoin2 = generate_player(1)
    StanShoo2 = generate_player(2)
    StanSmal2 = generate_player(3)
    StanPowe2 = generate_player(4)
    StanCente2= generate_player(5)

    team_A = team("Average Joes", StanPoint, StanShoot, StanSmall, StanPower, StanCenter)
    team_B = team("The Not Bads", StanPoin2, StanShoo2, StanSmal2, StanPowe2, StanCente2)
    playseries(team_A, team_B, 100, 0, 1)
    print("\n")
    team_A.print_team_ratings()
    #print("\n")
    team_B.print_team_ratings()
    #generate_player(5)
