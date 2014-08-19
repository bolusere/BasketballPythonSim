#Basketball sim in Python -- probably really badly

import random
#player needs
#GENERAL: height-weight-speed-age
#OFFENSE: inside-midrange-outside-passing-handling
#DEFENSE: steal-block-intd-outd-rebounding
class bbplayer:  
    #2manystats
    stats_pts = 0
    stats_fga = 0
    stats_fgm = 0
    stats_3ga = 0
    stats_3gm = 0
    stats_ass = 0
    stats_reb = 0
    stats_stl = 0
    stats_blk = 0
    
    stats_gms = 0
    stats_tot_pts = 0
    stats_tot_fga = 0
    stats_tot_fgm = 0
    stats_tot_3ga = 0
    stats_tot_3gm = 0
    stats_tot_ass = 0
    stats_tot_reb = 0
    stats_tot_stl = 0
    stats_tot_blk = 0
    
    def __init__(self, name, height, weight, speed, age, int_s, mid_s, out_s, passing, handling, steal, block, int_d, out_d, rebounding):
        self.name       = name
        self.height     = height
        self.weight     = weight
        self.speed      = speed
        self.age        = age
        self.int_s      = int_s
        self.mid_s      = mid_s
        self.out_s      = out_s
        self.passing    = passing
        self.handling   = handling
        self.steal      = steal
        self.block      = block
        self.int_d      = int_d
        self.out_d      = out_d
        self.rebounding = rebounding
        self.ovrshoot   = (int_s + mid_s + out_s) / 3
            
    def game_reset_pstats(self):
        self.stats_gms += 1
        self.stats_tot_pts += self.stats_pts
        self.stats_pts = 0
        self.stats_tot_fga += self.stats_fga
        self.stats_fga = 0
        self.stats_tot_fgm += self.stats_fgm
        self.stats_fgm = 0
        self.stats_tot_3ga += self.stats_3ga
        self.stats_3ga = 0
        self.stats_tot_3gm += self.stats_3gm
        self.stats_3gm = 0
        self.stats_tot_ass += self.stats_ass
        self.stats_ass = 0
        self.stats_tot_reb += self.stats_reb
        self.stats_reb = 0
        self.stats_tot_stl += self.stats_stl
        self.stats_stl = 0
        self.stats_tot_blk += self.stats_blk
        self.stats_blk = 0   
    
    def get_ppg(self):
        return self.stats_tot_pts/self.stats_gms
    def get_fgp(self):
        if self.stats_tot_fga > 0:
            return self.stats_tot_fgm/self.stats_tot_fga
        else: return 0
    def get_3fp(self):
        if self.stats_tot_3ga > 0:
            return self.stats_tot_3gm/self.stats_tot_3ga
        else: return 0
    def get_rpg(self):
        return self.stats_tot_reb/self.stats_gms
    def get_apg(self):
        return self.stats_tot_ass/self.stats_gms
    def get_spg(self):
        return self.stats_tot_stl/self.stats_gms
    def get_bpg(self):
        return self.stats_tot_blk/self.stats_gms
    
    def print_pergame_boxplayer(self):
        print(self.name,"      | ",int(self.get_ppg())," | ",int(self.get_fgp()*100)," | ",int(self.get_3fp()*100)," | ",int(self.get_rpg())," | ",int(self.get_apg())," | ",int(self.get_spg())," | ",int(self.get_bpg()))
    def print_boxplayer(self):
        print(self.name," | ",self.stats_pts," | ",self.stats_fgm,"/",self.stats_fga," | ",self.stats_3gm,"/",self.stats_3ga," | ",self.stats_reb," | ",self.stats_ass," | ",self.stats_stl," | ",self.stats_blk)
        
class team:
    def __init__(self, name, pointg, shootg, smallf, powerf, center):
        self.name = name
        self.pointg = pointg
        self.shootg = shootg
        self.smallf = smallf
        self.powerf = powerf
        self.center = center
    
    def game_reset_tstats(self):
        self.pointg.game_reset_pstats()
        self.shootg.game_reset_pstats()
        self.smallf.game_reset_pstats()
        self.powerf.game_reset_pstats()
        self.center.game_reset_pstats()
    
    def print_pergame_box(self):
        print("PER GAME AVG | PPG  | FG%  | 3G%  | RPG | APG | SPG | BPG")
        self.pointg.print_pergame_boxplayer()
        self.shootg.print_pergame_boxplayer()
        self.smallf.print_pergame_boxplayer()
        self.powerf.print_pergame_boxplayer()
        self.center.print_pergame_boxplayer()
        tot_ppg = self.pointg.get_ppg() + self.shootg.get_ppg() + self.smallf.get_ppg() + self.powerf.get_ppg() + self.center.get_ppg()
        tot_fgp = (self.pointg.stats_tot_fgm + self.shootg.stats_tot_fgm+ self.smallf.stats_tot_fgm + self.powerf.stats_tot_fgm + self.center.stats_tot_fgm)/(self.pointg.stats_tot_fga + self.shootg.stats_tot_fga+ self.smallf.stats_tot_fga + self.powerf.stats_tot_fga + self.center.stats_tot_fga)
        tot_3fp = (self.pointg.stats_tot_3gm + self.shootg.stats_tot_3gm+ self.smallf.stats_tot_3gm + self.powerf.stats_tot_3gm + self.center.stats_tot_3gm)/(self.pointg.stats_tot_3ga + self.shootg.stats_tot_3ga+ self.smallf.stats_tot_3ga + self.powerf.stats_tot_3ga + self.center.stats_tot_3ga)
        tot_rpg = self.pointg.get_rpg() + self.shootg.get_rpg() + self.smallf.get_rpg() + self.powerf.get_rpg() + self.center.get_rpg()
        tot_apg = self.pointg.get_apg() + self.shootg.get_apg() + self.smallf.get_apg() + self.powerf.get_apg() + self.center.get_apg()
        tot_spg = self.pointg.get_spg() + self.shootg.get_spg() + self.smallf.get_spg() + self.powerf.get_spg() + self.center.get_spg()
        tot_bpg = self.pointg.get_bpg() + self.shootg.get_bpg() + self.smallf.get_bpg() + self.powerf.get_bpg() + self.center.get_bpg()
        print("--------------------------------------------------------------------")
        print("TOTAL:       | ",int(tot_ppg)," | ",int(tot_fgp*100)," | ",int(tot_3fp*100)," | ",int(tot_rpg),"| ",int(tot_apg),"| ",int(tot_spg)," | ",int(tot_bpg))
    
    def print_box(self):
        print("NAME:   | PTS | FGM/FGA | 3GM/3GA | REB | ASS | STL | BLK")
        self.pointg.print_boxplayer()
        self.shootg.print_boxplayer()
        self.smallf.print_boxplayer()
        self.powerf.print_boxplayer()
        self.center.print_boxplayer()
        tot_pts = self.pointg.stats_pts + self.shootg.stats_pts + self.smallf.stats_pts + self.powerf.stats_pts + self.center.stats_pts
        tot_fgm = self.pointg.stats_fgm + self.shootg.stats_fgm + self.smallf.stats_fgm + self.powerf.stats_fgm + self.center.stats_fgm
        tot_fga = self.pointg.stats_fga + self.shootg.stats_fga + self.smallf.stats_fga + self.powerf.stats_fga + self.center.stats_fga
        tot_3gm = self.pointg.stats_3gm + self.shootg.stats_3gm + self.smallf.stats_3gm + self.powerf.stats_3gm + self.center.stats_3gm
        tot_3ga = self.pointg.stats_3ga + self.shootg.stats_3ga + self.smallf.stats_3ga + self.powerf.stats_3ga + self.center.stats_3ga
        tot_reb = self.pointg.stats_reb + self.shootg.stats_reb + self.smallf.stats_reb + self.powerf.stats_reb + self.center.stats_reb
        tot_ass = self.pointg.stats_ass + self.shootg.stats_ass + self.smallf.stats_ass + self.powerf.stats_ass + self.center.stats_ass
        tot_stl = self.pointg.stats_stl + self.shootg.stats_stl + self.smallf.stats_stl + self.powerf.stats_stl + self.center.stats_stl
        tot_blk = self.pointg.stats_blk + self.shootg.stats_blk + self.smallf.stats_blk + self.powerf.stats_blk + self.center.stats_blk
        print("----------------------------------------------------------")
        print("TOTAL:  | ",tot_pts," | ",tot_fgm,"/",tot_fga," | ",tot_3gm,"/",tot_3ga," | ",tot_reb," | ",tot_ass," | ",tot_stl," | ",tot_blk)

def playseries(team1, team2, numgames, prbox, prend):
    wins1 = 0
    wins2 = 0
    series_games = numgames
    toggle_home = True #have toggle to change arenas every game (maybe home adv l8r implement so this might matter)
    while numgames > 0:
        if toggle_home == True:
            toggle_home = False
            winner = playgame(team1, team2, 0, prbox)
            if winner==team1:
                wins1 += 1
            elif winner==team2: 
                wins2 += 1
        else:
            toggle_home = True
            winner = playgame(team2, team1, 0, prbox)
            if winner==team2:
                wins2 += 1
            elif winner==team1: 
                wins1 += 1
        numgames -= 1
    
    print("\n")
    print("Result of",series_games,"game series:",team1.name,"-",wins1,team2.name,"-",wins2,"\n")
    if prend == 1:
        print(team1.name,"-",wins1,"wins")
        team1.print_pergame_box()
        print("\n")
        print(team2.name,"-",wins2,"wins")
        team2.print_pergame_box()
        

def playgame(home, away, prplay, prbox): #home team, away team, print play-by-play (0 or 1), print box at end (0 or 1)
    if prbox==1: 
        print("\n")
        print(away.name, " @ ", home.name,"\n")
    
    #set possession
    poss_home, poss_away = tip_off(home, away, prplay)
    gametime = 0
    max_gametime = 2400
    hscore = 0
    ascore = 0
    hspeed = (home.pointg.speed + home.shootg.speed + home.smallf.speed) / 300
    aspeed = (away.pointg.speed + away.shootg.speed + away.smallf.speed) / 300
    playing = True
    
    while playing: #40min games
        if poss_home:
            hscore += run_play(home, away, prplay)
            poss_away = 1
            poss_home = 0
            gametime += 24 * random.random() / hspeed
        elif poss_away:
            ascore += run_play(away, home, prplay)
            poss_away = 0
            poss_home = 1
            gametime += 24 * random.random() / aspeed
        if gametime > max_gametime:
            gametime = max_gametime
            if hscore != ascore:
                playing = False
            else:
                if prplay==1: print("\n*** OVERTIME! ***\n")
                poss_home, poss_away = tip_off(home, away, prplay)
                max_gametime += 300
        if prplay==1: print("Gametime: ", int(gametime), " | ", home.name, ":", hscore, " ", away.name, ":", ascore,"\n")
    
    #print boxscore if desired
    if prbox==1:
        print("HOME ", home.name, ": ", hscore)
        home.print_box()
        print("\n")
        print("AWAY ", away.name, ": ", ascore)
        away.print_box()
    
    #do some stats management, like adding player stuff to their career totals
    home.game_reset_tstats()
    away.game_reset_tstats()
    
    #return winner
    if hscore > ascore:
        #home team has won
        return home
    else: return away

def tip_off(home, away, prplay):
    poss = random.random()
    if poss > 0.5:
        poss_home = True
        poss_away = False
        if prplay==1: print(home.name, "wins the tip-off!")
    else:
        poss_away = True
        poss_home = False
        if prplay==1: print(away.name, "wins the tip-off!")
    return poss_home, poss_away

def run_play(offense, defense, prplay): #take it possession at time yo
    if prplay==1: print(offense.name, "have the ball.")
    passes = 0
    off_poss = 1
    who_poss = offense.pointg
    who_def  = defense.pointg
    assister = who_poss
    while off_poss == 1:
        passprob = who_poss.passing / who_poss.ovrshoot
        if random.random() * passprob > 0.2:
            #pass
            ifsteal = pot_steal(who_poss, who_def)
            if ifsteal == 1:
                #stolen
                if prplay==1: print(who_def.name, "has stolen the ball!")
                who_def.stats_stl += 1
                return 0
            pass_to = random.randint(1, 5)
            assister = who_poss
            if pass_to == 1:
                who_poss = offense.pointg
                who_def  = defense.pointg
            if pass_to == 2:
                who_poss = offense.shootg
                who_def  = defense.shootg
            if pass_to == 3:
                who_poss = offense.smallf
                who_def  = defense.smallf
            if pass_to == 4:
                who_poss = offense.powerf
                who_def  = defense.powerf
            if pass_to == 5:
                who_poss = offense.center
                who_def  = defense.center
        else:
            #shoot
            points = take_shot(who_poss, who_def, defense, prplay)
            if points > 0:
                #made it!
                if assister.name == who_poss.name:
                    if prplay==1: print(who_poss.name, "made a", points, "pt shot")
                    return points
                else:
                    assister.stats_ass += 1
                    if prplay==1: print(who_poss.name, "made a", points, "pt shot with an assist from", assister.name)
                    return points
            else:
                #print(who_poss.name, "misses!")
                #rebounding, defenders have 3:1 advantage
                #weighted rebounding advantage calculator, maybe add height adv too l8r
                reb_adv = (defense.center.rebounding - offense.center.rebounding) + (defense.powerf.rebounding - offense.powerf.rebounding)*0.85 + (defense.smallf.rebounding - offense.smallf.rebounding)*0.7 + (defense.shootg.rebounding - offense.shootg.rebounding)*0.5 + (defense.pointg.rebounding - offense.pointg.rebounding)*0.25
                if (random.random()*100 + reb_adv) > 25: #defensive reb
                    rebounder = find_rebounder(defense)
                    if prplay==1: print(rebounder.name,"grabs the defensive rebound!")
                    return 0
                else: #offensive reb
                    rebounder = find_rebounder(offense)
                    if prplay==1: print(rebounder.name,"snatches the offensive rebound!")
                    who_poss = rebounder
   
def find_rebounder(team): #who shall receive the rebounding blessing?
    cenreb = random.random()*team.center.rebounding*1.3
    powreb = random.random()*team.powerf.rebounding*1.15
    smfreb = random.random()*team.smallf.rebounding
    shgreb = random.random()*team.shootg.rebounding*0.8
    ptgreb = random.random()*team.pointg.rebounding*0.65
    listreb = [cenreb, powreb, smfreb, shgreb, ptgreb]
    listreb.sort()
    if listreb[4]==cenreb:
        team.center.stats_reb += 1
        return team.center
    elif listreb[4]==powreb:
        team.powerf.stats_reb += 1
        return team.powerf
    elif listreb[4]==smfreb:
        team.smallf.stats_reb += 1
        return team.smallf   
    elif listreb[4]==shgreb:
        team.shootg.stats_reb += 1
        return team.shootg
    else:
        team.pointg.stats_reb += 1
        return team.pointg
        
def pot_steal(poss, stlr): #see if the pass is stolen, return 1 if it is
    if random.random() < 0.1: #only 10% of passes are "stealable"
        chance = random.random() * (stlr.steal - poss.handling*0.5)
        if chance > 30 or random.random() < 0.1:
            #stolen!
            return 1
        else: return 0
    else: return 0

def take_shot(shooter, defender, defense, prplay): #return points of shot, 0 if miss
    #block?
    if random.random() * (defender.block + (defender.height - shooter.height)) > 75 or random.random() < 0.005:
        #NOT IN MY HOUSE MOFO
        if prplay==1: print(defender.name,"has blocked",shooter.name,"!")
        shooter.stats_fga += 1
        defender.stats_blk += 1
        return 0
    if shooter.out_s * random.random() > 40 or (shooter.out_s > (shooter.int_s + shooter.mid_s) and random.random() > 0.25): #second part is where guy is clearly 3pt specialist, ie 25/50/99
        #3pt shot
        chance = (shooter.out_s / defender.out_d) * random.random() * 70
        if chance > 50:
            #made it!
            shooter.stats_pts += 3
            shooter.stats_fga += 1
            shooter.stats_fgm += 1
            shooter.stats_3ga += 1
            shooter.stats_3gm += 1
            return 3
        else:
            if prplay==1: print(shooter.name, "misses from downtown!")
            shooter.stats_fga += 1
            shooter.stats_3ga += 1
            return 0
    elif shooter.mid_s * random.random() > 50: #50 norm
        #midrange jumper
        chance = (shooter.mid_s / defender.out_d) * random.random() * 80
        if chance > 50:
            #made it!
            shooter.stats_pts += 2
            shooter.stats_fga += 1
            shooter.stats_fgm += 1
            return 2
        else:
            if prplay==1: print(shooter.name, "bricks the midrange jumper!")        
            shooter.stats_fga += 1
            return 0
    else:
        #inside layup/dunk/etc
        chance = ((shooter.int_s / defender.int_d) * random.random() * 90)# - random.random()*((defense.center.int_d + defense.powerf.int_d + defense.smallf.int_d*0.75)/5)
        if chance > 50:
            #made it!
            if random.random() < 0.3:
                if prplay==1: print(shooter.name, "slams it down over", defender.name, "!")
            else:
                if prplay==1: print(shooter.name, "lays it in!")
            shooter.stats_pts += 2
            shooter.stats_fga += 1
            shooter.stats_fgm += 1
            return 2
        else:
            if prplay==1: print(shooter.name, "can't connect on the inside shot!") 
            shooter.stats_fga += 1
            return 0

if __name__ == "__main__":

    # ------------------|  NAME  |HGT|WTLB|SPD|AGE|INS|MID|OUT|PSS|HND|STL|BLK|IND|OTD|REB| 
    StanPoint = bbplayer("Pointy", 72, 150, 90, 25, 75, 75, 75, 90, 90, 80, 30, 30, 80, 20)
    StanShoot = bbplayer("Shooty", 76, 180, 80, 25, 75, 85, 95, 75, 75, 50, 50, 50, 75, 40)
    StanSmall = bbplayer("Smally", 80, 200, 80, 25, 80, 85, 80, 70, 75, 85, 70, 75, 80, 75)
    StanPower = bbplayer("Powery", 82, 220, 60, 25, 80, 75, 30, 60, 75, 60, 90, 85, 70, 85)
    StanCenter= bbplayer("iBeast", 84, 250, 40, 25, 95, 50, 20, 40, 50, 40, 90, 90, 50, 90)

    # ------------------|  NAME  |HGT|WTLB|SPD|AGE|INS|MID|OUT|PSS|HND|STL|BLK|IND|OTD|REB|
    StanPoin2 = bbplayer("iJesus", 72, 150, 90, 25, 75, 75, 75, 90, 90, 80, 30, 30, 80, 20)
    StanShoo2 = bbplayer("3Shoot", 76, 180, 80, 25, 75, 85, 95, 75, 75, 50, 50, 50, 75, 40)
    StanSmal2 = bbplayer("Onlydf", 80, 200, 80, 25, 80, 85, 80, 70, 75, 85, 70, 75, 80, 75)
    StanPowe2 = bbplayer("Power2", 82, 220, 60, 25, 80, 75, 30, 60, 75, 60, 90, 85, 70, 85)
    StanCente2= bbplayer("Cente2", 84, 250, 40, 25, 95, 50, 20, 40, 50, 40, 90, 90, 50, 90)

    
    team_A = team("Average Joes", StanPoint, StanShoot, StanSmall, StanPower, StanCenter)
    team_B = team("The Not Bads", StanPoin2, StanShoo2, StanSmal2, StanPowe2, StanCente2)
    playseries(team_A, team_B, 50, 0, 1)
