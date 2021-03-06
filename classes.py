import math
import random

class ai_opponent:
    def __init__(self, name=None, ai_team=None):
        if name == None:
            names_list = ["Sterling", "Cuban", "Rivers", "Riley", "Blatt", "Carlisle", "Gilbert", "Adolf", "Dolan", "Popovich"]
            self.name = random.choice(names_list)
            names_list.remove(self.name)
        else:
            self.name = name
        if ai_team == None:
            self.ai_team = team.empty()
        else:
            self.ai_team = ai_team

    def select_player(self, player_list):
        overalls = []
        for p in player_list:
            overalls.append(p.overall)
        overalls.sort()
        draft_position = 0
        made_selection = False
        top = 1
        while made_selection==False:
            for p in player_list:
                if p.overall == overalls[len(player_list)-top]:
                    if self.ai_team.player_array[p.pref_pos-1] == None:
                        print(self.name, "has selected", p.name, p.pref_pos)
                        made_selection = True
                        return draft_position
                    else: #don't pick top guy since we already have a guy in that position 
                        if top == len(player_list): #no guys in the position we want
                            sec_draft_position = 0
                            for p in player_list:
                                if p.overall == overalls[len(player_list)-1]: #just pick best overall guy
                                    if self.ai_team.player_array[0] == None:
                                        p.pref_pos = 1
                                    elif self.ai_team.player_array[1] == None:
                                        p.pref_pos = 2
                                    elif self.ai_team.player_array[2] == None:
                                        p.pref_pos = 3
                                    elif self.ai_team.player_array[3] == None:
                                        p.pref_pos = 4
                                    elif self.ai_team.player_array[4] == None:
                                        p.pref_pos = 5
                                    
                                    print(self.name, "has selected", p.name, p.pref_pos)
                                    made_selection = True
                                    return sec_draft_position
                                    
                                sec_draft_position += 1
                        top += 1
                draft_position += 1
            draft_position = 0

    def get_team(self):
        return self.ai_team

class bbplayer:
    #stats_array = [[0 for x in range(2)] 0 for x in range(9)]
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
    stats_tot_msm = 0
    
    def __init__(self, name, pref_pos, height, weight, speed, age, int_s, mid_s, out_s, passing, handling, steal, block, int_d, out_d, rebounding):
        self.name       = name
        self.height     = height
        self.pref_pos   = pref_pos
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
    '''
        for x in stats_array:
            x[1] += x[0]
            x[0] = 0
    '''

    def set_stats_zero(self):
        self.stats_gms = 0
        self.stats_tot_pts = 0
        self.stats_tot_fga = 0
        self.stats_tot_fgm = 0
        self.stats_tot_3ga = 0
        self.stats_tot_3gm = 0
        self.stats_tot_ass = 0
        self.stats_tot_reb = 0
        self.stats_tot_stl = 0
        self.stats_tot_blk = 0
        self.stats_tot_msm = 0
    
    @property
    def overall(self):
        return int(self.speed + self.int_s**1.3 + self.mid_s**1.3 + self.out_s**1.3 + self.passing**1.1 + self.handling + self.steal**1.1 + self.block**1.1 + self.int_d**1.2 + self.out_d**1.2 + self.rebounding**1.2)
    @property
    def ppg(self):
        return self.stats_tot_pts/self.stats_gms
    @property
    def fgp(self):
        if self.stats_tot_fga > 0:
            return self.stats_tot_fgm/self.stats_tot_fga
        else: return 0
    @property
    def fp3(self):
        if self.stats_tot_3ga > 0:
            return self.stats_tot_3gm/self.stats_tot_3ga
        else: return 0
    @property
    def rpg(self):
        return self.stats_tot_reb/self.stats_gms
    @property
    def apg(self):
        return self.stats_tot_ass/self.stats_gms
    @property
    def spg(self):
        return self.stats_tot_stl/self.stats_gms
    @property
    def bpg(self):
        return self.stats_tot_blk/self.stats_gms
        
    def print_ratings(self, labels): #labels = 1 if they want headings, 0 if jsut raw stats
        if labels==1:
            print("NAME:        | HT|WGT|AG|SP|IN|MD|OT|PS|HD|ST|BL|ID|OD|RB|")
        
        if self.height>99: disp_height = 99
        else: disp_height = self.height
        
        if self.speed>99: disp_speed = 99
        else: disp_speed = self.speed
        
        if self.int_s>99: disp_int_s = 99
        else: disp_int_s = self.int_s
        
        if self.mid_s>99: disp_mid_s = 99
        else: disp_mid_s = self.mid_s
        
        if self.out_s>99: disp_out_s = 99
        else: disp_out_s = self.out_s
        
        if self.passing>99: disp_passing = 99
        else: disp_passing = self.passing
        
        if self.handling>99: disp_handling = 99
        else: disp_handling = self.handling
        
        if self.steal>99: disp_steal = 99
        else: disp_steal = self.steal
        
        if self.block>99: disp_block = 99
        else: disp_block = self.block
        
        if self.int_d>99: disp_int_d = 99
        else: disp_int_d = self.int_d
        
        if self.out_d>99: disp_out_d = 99
        else: disp_out_d = self.out_d
        
        if self.rebounding>99: disp_rebounding = 99
        else: disp_rebounding = self.rebounding
        
        print("{name:<13}|".format(name=self.name), disp_height, self.weight, self.age, disp_speed, disp_int_s, disp_mid_s, disp_out_s, disp_passing, disp_handling, disp_steal, disp_block, disp_int_d, disp_out_d, disp_rebounding, self.overall, self.pref_pos)
    
    def print_pergame_boxplayer(self):
        print("{name:<13}| {ppg:<4} | {fgp:<4} | {fp3:<4} | {reb:<4} | {ass:<4} | {stl:<4}| {blk:<4}|  {fga:<2} |  {ga3:<2} | {msm:<3} {pos}".format(name=self.name, ppg=int(self.ppg*10)/10, fgp=int(self.fgp*1000)/10, fp3=int(self.fp3*999)/10,
              reb=int(self.rpg*10)/10, ass=int(self.apg*10)/10, stl=int(self.spg*10)/10, blk=int(self.bpg*10)/10, fga=int(self.stats_tot_fga/self.stats_gms), ga3=int(self.stats_tot_3ga/self.stats_gms), msm=int(self.stats_tot_msm/self.stats_gms), pos=self.pref_pos))

    def print_boxplayer(self):
        print("{name:<13}|  {points:<3} | {fgm:<2}/ {fga:<2} | {gm3:<2}/ {ga3:<2} |  {rebounds:<3} |  {assists:<3} |  {steals:<3} |  {blocks:<3}".format(name=self.name, points=self.stats_pts, fgm=self.stats_fgm, 
              fga=self.stats_fga, gm3=self.stats_3gm, ga3=self.stats_3ga, rebounds=self.stats_reb, assists=self.stats_ass, steals=self.stats_stl, blocks=self.stats_blk))

class team:
    def __init__(self, name, pointg, shootg, smallf, powerf, center):
        self.name = name
        self.player_array = [None] * 5
        self.bench_array = []
        self.player_array[0] = pointg
        self.player_array[1] = shootg
        self.player_array[2] = smallf
        self.player_array[3] = powerf
        self.player_array[4] = center
        self.wins = 0
        self.losses = 0

    @classmethod
    def empty(cls):
        team_prefixes = ["Mc", "Un", "Not", "Big", "Tiny", "Giant", "Red", "Blue",
                         "Neon", "Swaggish", "White", "Black", "Last", "Best", "Worst"]
        team_suffixes = ["Armadillos", "Lumberjacks", "Killas", "Dicks", "Diamonds",
                         "Senators", "Warriors", "Heat", "Bulls", "Tech Support",
                         "Ballers", "Rioters", "Mofos", "Nazis", "Klansmen"]
        team_name = team_prefixes[random.randint(0, len(team_prefixes)-1)] + " " + team_suffixes[random.randint(0, len(team_suffixes)-1)]
        return cls(team_name, None, None, None, None, None)
    @property
    def size(self):
        _size = 0
        for player in self.player_array:
            if player != None:
                _size += 1
        for player in self.bench_array:
            if player != None:
                _size += 1
        return _size
    @property
    def pointg(self):
        return self.player_array[0]
    @property
    def shootg(self):
        return self.player_array[1]
    @property
    def smallf(self):
        return self.player_array[2]
    @property
    def powerf(self):
        return self.player_array[3]
    @property
    def center(self):
        return self.player_array[4]

    def add_player(self, player, player_position=None):
        if player_position == None:
            self.bench_array.append(player)
        elif player_position >= 1 and player_position <= 5:
            self.player_array[player_position - 1] = player
        else:
            raise KeyError('Not a valid position')

    def game_reset_tstats(self):
        for player in self.player_array:
            player.game_reset_pstats()

    def set_stats_zero(self):
        for player in self.player_array:
            player.set_stats_zero()

    def print_team(self):
        print(self.name)
        count = 1
        print("NAME:          | HT|WGT|AG|SP|IN|MD|OT|PS|HD|ST|BL|ID|OD|RB|")
        for player in self.player_array:
            print(count, end=" ")
            if player is not None:
                player.print_ratings(0)
            else: print("None")
            count += 1
        for player in self.bench_array:
            print(count, end=" ")
            if player is not None:
                player.print_ratings(0)
            else: print("None")
            count += 1

    def print_team_ratings(self):
        print(self.name)
        print("NAME:        | HT|WGT|AG|SP|IN|MD|OT|PS|HD|ST|BL|ID|OD|RB|")
        for player in self.player_array:
            player.print_ratings(0)
    
    def print_pergame_box(self):
        print("PER GAME AVG | PPG  | FG%  | 3G%  | RPG  | APG  | SPG | BPG | FGA | 3GA | MSM")
        for player in self.player_array:
            player.print_pergame_boxplayer()
        tot_ppg = self.pointg.ppg + self.shootg.ppg + self.smallf.ppg + self.powerf.ppg + self.center.ppg
        tot_fgp = (self.pointg.stats_tot_fgm + self.shootg.stats_tot_fgm+ self.smallf.stats_tot_fgm + self.powerf.stats_tot_fgm +
                   self.center.stats_tot_fgm)/(self.pointg.stats_tot_fga + self.shootg.stats_tot_fga+ self.smallf.stats_tot_fga + self.powerf.stats_tot_fga + self.center.stats_tot_fga)
        tot_3fp = (self.pointg.stats_tot_3gm + self.shootg.stats_tot_3gm+ self.smallf.stats_tot_3gm + self.powerf.stats_tot_3gm + 
                   self.center.stats_tot_3gm)/(self.pointg.stats_tot_3ga + self.shootg.stats_tot_3ga+ self.smallf.stats_tot_3ga + self.powerf.stats_tot_3ga + self.center.stats_tot_3ga + 1) #so no div 0
        tot_rpg = self.pointg.rpg + self.shootg.rpg + self.smallf.rpg + self.powerf.rpg + self.center.rpg
        tot_apg = self.pointg.apg + self.shootg.apg + self.smallf.apg + self.powerf.apg + self.center.apg
        tot_spg = self.pointg.spg + self.shootg.spg + self.smallf.spg + self.powerf.spg + self.center.spg
        tot_bpg = self.pointg.bpg + self.shootg.bpg + self.smallf.bpg + self.powerf.bpg + self.center.bpg
        print("-----------------------------------------------------------")
        print("TOTAL:       | {ppg:<5}| {fgp:<4} | {fp3:<4} | {reb:<4} | {ass:<4} | {stl:<4}| {blk:<4}".format(ppg=int(tot_ppg*10)/10, fgp=int(tot_fgp*1000)/10, fp3=int(tot_3fp*1000)/10, reb=int(tot_rpg*10)/10,
              ass=int(tot_apg*10)/10, stl=int(tot_spg*10)/10, blk=int(tot_bpg*10)/10))
    
    def print_box(self):
        print("NAME:        |  PTS | FGM/FGA| 3GM/3GA| REB  | ASS  | STL  | BLK")
        for player in self.player_array:
            player.print_boxplayer()
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
        print("TOTAL:       |  {points:<3} | {fgm:<2}/ {fga:<2} | {gm3:<2}/ {ga3:<2} |  {rebounds:<3} |  {assists:<3} |  {steals:<3} |  {blocks:<3}".format(points=tot_pts, fgm=tot_fgm, fga=tot_fga,
              gm3=tot_3gm, ga3=tot_3ga, rebounds=tot_reb, assists=tot_ass, steals=tot_stl, blocks=tot_blk))

    def random_assignment(self):
        if self.size >= 5:
            for player in self.player_array:
                if player is None:
                    self.player_array[self.player_array.index(player)] = self.bench_array.pop()
        self.name = "PLAYER TEAM"

    def swap_players(self, pos_1, pos_2):
        if pos_1 <= 10 and pos_2 <= 10 and pos_1 != pos_2:
            player_list = []
            for player in self.player_array:
                player_list.append(player)
            if len(self.bench_array) != 0:
                for player in self.bench_array:
                    player_list.append(player)
            player_1 = player_list[pos_1 - 1]
            player_list[pos_1 - 1] = player_list[pos_2 - 1]
            player_list[pos_2 - 1] = player_1
            for i in range(5):
                self.player_array[i] = player_list[i]
            for i in range(5, len(player_list)):
                self.bench_array[i - 5] = player_list[i]
        else:
            raise KeyError("ur dumb")
