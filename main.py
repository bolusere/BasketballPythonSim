#Basketball sim in Python -- probably really badly

import random
#player needs
#GENERAL: height-weight-speed-age
#OFFENSE: inside-midrange-outside-passing-handling
#DEFENSE: steal-block-intd-outd-rebounding
class bbplayer:
    #stats
    stats_pts = 0
    stats_fga = 0
    stats_fgm = 0
    stats_3ga = 0
    stats_3gm = 0
    stats_ass = 0
    stats_reb = 0
    stats_stl = 0
    stats_blk = 0
    
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
    
    def print_box(self):
        print("NAME:   | PTS | FGM/FGA | 3GM/3GA | REB | ASS | STL | BLK |")
        self.pointg.print_boxplayer()
        self.shootg.print_boxplayer()
        self.smallf.print_boxplayer()
        self.powerf.print_boxplayer()
        self.center.print_boxplayer()

def playgame(home, away):
    print(away.name, " @ ", home.name)
    #set possession
    poss = random.random()
    if poss >= 0.5:
        poss_home = 1
        poss_away = 0
        print(home.name, " wins the tip-off!")
    else:
        poss_away = 1
        poss_home = 0
        print(away.name, " wins the tip-off!")
    gametime = 0
    hscore = 0
    ascore = 0
    hspeed = (home.pointg.speed + home.shootg.speed + home.smallf.speed) / 300
    aspeed = (away.pointg.speed + away.shootg.speed + away.smallf.speed) / 300
    while gametime < 2400:
        if poss_home == 1:
            hscore += run_play(home, away)
            poss_away = 1
            poss_home = 0
            gametime += 24 * random.random() / hspeed
            print("Gametime: ", int(gametime), " | ", home.name, ": ", hscore, " ", away.name, ": ", ascore,"\n")
        elif poss_away == 1:
            ascore += run_play(away, home)
            poss_away = 0
            poss_home = 1
            gametime += 24 * random.random() / aspeed
            print("Gametime: ", int(gametime), " | ", home.name, ": ", hscore, " ", away.name, ": ", ascore,"\n")
    #boxscore
    print("HOME ", home.name, ": ", hscore)
    home.print_box()
    print("\n")
    print("AWAY ", away.name, ": ", ascore)
    away.print_box()

def run_play(offense, defense): #take it possession at time yo
    print(offense.name, " have the ball.")
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
                print(who_def.name, " has stolen the ball!")
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
            points = take_shot(who_poss, who_def)
            if points > 0:
                #made it!
                if assister.name == who_poss.name:
                    print(who_poss.name, " made a ", points, "pt shot")
                    return points
                else:
                    assister.stats_ass += 1
                    print(who_poss.name, " made a ", points, "pt shot with an assist from ", assister.name)
                    return points
            else:
                print(who_poss.name, "misses!")
                #rebounding, defenders have 3:1 advantage
                #weighted rebounding advantage calculator, maybe add height adv too l8r
                reb_adv = (defense.center.rebounding - offense.center.rebounding)*2 + (defense.powerf.rebounding - offense.powerf.rebounding)*1.75 + (defense.smallf.rebounding - offense.smallf.rebounding)*1.5 + (defense.shootg.rebounding - offense.shootg.rebounding) + (defense.pointg.rebounding - offense.pointg.rebounding)*0.75
                if (random.random()*100 + reb_adv) > 25: #defensive reb
                    rebounder = find_rebounder(defense)
                    print(rebounder.name," grabs the defensive rebound!")
                    return 0
                else: #offensive reb
                    rebounder = find_rebounder(offense)
                    print(rebounder.name," snatches the offensive rebound!")
                    who_poss = rebounder
   
def find_rebounder(team): #who shall receive the rebounding blessing?
    cenreb = random.random()*team.center.rebounding
    powreb = random.random()*team.powerf.rebounding
    smfreb = random.random()*team.smallf.rebounding
    shgreb = random.random()*team.shootg.rebounding
    ptgreb = random.random()*team.pointg.rebounding
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
    if random.random() < 0.25: #only 25% of passes are "stealable"
        chance = random.random() * (stlr.steal - poss.passing)
        if chance > 15 or random.random() < 0.005:
            #stolen!
            return 1
        else: return 0
    else: return 0

def take_shot(shooter, defender): #return points of shot, 0 if miss
    #block?
    if random.random() * (defender.block + (defender.height - shooter.height)) > 75 or random.random() < 0.005:
        #NOT IN MY HOUSE MOFO
        print(defender.name," has blocked ",shooter.name,"!")
        shooter.stats_fga += 1
        defender.stats_blk += 1
        return 0
    if shooter.out_s * random.random() > 40:
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
            shooter.stats_fga += 1
            shooter.stats_3ga += 1
            return 0
    elif shooter.mid_s * random.random() > 50:
        #midrange jumper
        chance = (shooter.mid_s / defender.out_d) * random.random() * 80
        if chance > 50:
            #made it!
            shooter.stats_pts += 2
            shooter.stats_fga += 1
            shooter.stats_fgm += 1
            return 2
        else: 
            shooter.stats_fga += 1
            return 0
    else:
        #inside layup/dunk/etc
        chance = (shooter.int_s / defender.int_d) * random.random() * 90
        if chance > 50:
            #made it!
            shooter.stats_pts += 2
            shooter.stats_fga += 1
            shooter.stats_fgm += 1
            return 2
        else:
            shooter.stats_fga += 1
            return 0

# ------------------|  NAME  |HGT|WTLB|SPD|AGE|INS|MID|OUT|PSS|HND|STL|BLK|IND|OTD|REB| 
StanPoint = bbplayer("Pointy", 72, 150, 90, 25, 75, 75, 75, 90, 90, 80, 30, 30, 80, 20)
StanShoot = bbplayer("Shooty", 76, 180, 80, 25, 75, 85, 95, 75, 75, 50, 50, 50, 60, 40)
StanSmall = bbplayer("Smally", 80, 200, 80, 25, 80, 85, 80, 70, 75, 75, 70, 75, 80, 75)
StanPower = bbplayer("Powery", 82, 220, 60, 25, 80, 75, 30, 60, 75, 60, 90, 85, 70, 85)
StanCenter= bbplayer("Center", 84, 250, 40, 25, 90, 50, 20, 60, 75, 60, 90, 95, 50, 90)

# ------------------|  NAME  |HGT|WTLB|SPD|AGE|INS|MID|OUT|PSS|HND|STL|BLK|IND|OTD|REB|
GodPoint  = bbplayer("iJesus", 72, 150, 90, 25, 99, 75, 75, 90, 90, 80, 30, 30, 80, 20)

team_A = team("Standards")
team_B = team("Pandas")
playgame(team_A, team_B)











