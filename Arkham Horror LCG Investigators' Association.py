# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 23:24:48 2020

@author: min_2
"""

class Investigator:
    def __init__(self):
        self.fullname = input("Enter the first and last name of the new investigator: ")
        self.motto = input("Enter the motto: ")
        self.team = [""]
        self.inv_class = {"Survivor":0,"Seeker":0,"Rogue":0,"Guardian":0,"Mystic":0}
        self.fr_inv_class = max(self.inv_class, key=self.inv_class.get) # Retrieves key w/ the highest value from a dictionary.
        self.persist = {"Panache": 0,"Endeavor": 0,"Radiance":0,"Synergy":0,"Inquisitive":0,"Selfless":0,"Tactics":0}
        self.campaign = [""]
        self.camp_count = 0
        self.experience = 0
        self.rank = "Detective"
        
        print("Welcome aboard investigator!")
        self.report()
    
    def report(self):
        print (
                "========== INVESTIGATOR REPORT ==========" '\n'
                "|| NAME:        [ {} ]".format(self.fullname) + '\n'
                "|| RANK:        [ {} ]".format(self.rank) + '\n'
                "|| F.CLASS:     [ {} ]".format(self.fr_inv_class) + '\n'
                "|| RECENT TEAM: [ {} ]".format(self.team[0]) + '\n'
                "|| R.CAMPAIGN:  [ {} ]".format(self.campaign[0]) + '\n'
                "|| CAMPAIGN #:  {}".format(self.camp_count) + '\n'
                "|| EXPERIENCE:  {}".format(self.experience) + '\n'
                "||" + '\n'
                "|| {}".format(self.motto) + '\n'
                "" +'\n'
                )

    def performance(self):
        grade = ""
        for score in ((self.persist).values()):
            pass
            
        print (
                "===== P.E.R.S.I.S.T =====" + '\n'
                "|| PANACHE     : {}".format(self.persist["Panache"]) + '\n'
                "|| ENDEAVOR    : {}".format(self.persist["Endeavor"]) + '\n'
                "|| RADIANCE    : {}".format(self.persist["Radiance"]) + '\n'
                "|| SYNERGY     : {}".format(self.persist["Synergy"]) + '\n'
                "|| INQUISITIVE : {}".format(self.persist["Inquisitive"]) + '\n'
                "|| SELFLESS    : {}".format(self.persist["Selfless"]) + '\n'
                "|| TACTICS     : {}".format(self.persist["Tactics"]) + '\n'
                "|| PERFORMANCE :[{}]".format(grade)
                )

persist_description = {
                       "Panache":"Evaluates the confidence and arrogance shown by the investigator.",
                       "Endeavor":"Represents the investigator's value in objectivity and determination.",
                       "Radiance":"Shows the investigator's overall optimism and self-satisfaction.",
                       "Synergy":"Evaluates the cooperative ability and contribution to the team's value by th,e investigator.",
                       "Inquisitive":"Represents the investigator's trait of being curious and adventurous.",
                       "Selfless":"Valued at the investigator's altruistic nature for another.",
                       "Tactics":"Shows the investigator's attribute of being strategic and methodical."
                       }

#def describe_persist():
#    number = "d"
#    while number.isnumeric() != True or int(number) < 0 or int(number) > 8:
#       number = input("Please enter a number from the following li1st:")
#       number = int(number)
        
#       if number == 0:
#            for name,description in persist_description.items():
#                print ('\n' + name + ": " + description + '\n')
                
def describe_persist():
    while True:
        try:
            number = int(input(
                                "Please enter a number from the following list:" + '\n'
                                "0 - All Info" + '\n'
                                "1 - Panache" + '\n'
                                "2 - Endeavor" + '\n'
                                "3 - Radiance" + '\n'
                                "4 - Synergy" + '\n'
                                "5 - Inquisitive" + '\n'
                                "6 - Selfless" + '\n'
                                "7 - Tactics" + '\n'
                                ))
            
        except ValueError:
            print("Enter a 'number' from the list.")
            continue
        
        else:
            if 0 <= number < 8:
                break
            else:
                print("Out of range. Please try again.")
                continue    
    
    if number == 0:
        for name,description in persist_description.items():
            print('\n'+name+": "+description+'\n')
    
    elif number == 1:
        print('\n'+"Panache: "+persist_description["Panache"]+'\n')
    elif number == 2:
        print('\n'+"Endeavor: "+persist_description["Endeavor"]+'\n')
    elif number == 3:
        print('\n'+"Radiance: "+persist_description["Radiance"]+'\n')
    elif number == 4:
        print('\n'+"Synergy: "+persist_description["Synergy"]+'\n')
    elif number == 5:
        print('\n'+"Inquisitive: "+persist_description["Inquisitive"]+'\n')
    elif number == 6:
        print('\n'+"Selfless: "+persist_description["Selfless"]+'\n')
    else:
        print('\n'+"Tactics: "+persist_description["Tactics"]+'\n')

class Campaign:
    def __init__(self):
        
        while True:
            self.name = input("What is the abbreviated name for this Arkham Horror LCG campaign title? ")
        
            if self.name.lower() == "tnotz":
                self.name = "The Night of the Zealot"
                self.sc_list = {"SCENARIO 1":"The Gathering",
                                "SCENARIO 2":"The Midnight Masks",
                                "SCENARIO 3":"The Devourer Below"}
                break
                
            elif self.name.lower() == "tfa":
                self.name = "The Forgotten Age"
                self.sc_list = {"SCENARIO 1":"The Untamed Wilds",
                                "SCENARIO 2":"The Doom of Eztli",
                                "SCENARIO 3":"Threads of Fate",
                                "SCENARIO 4":"The Boundary Beyond",
                                "SCENARIO 5":"Heart of the Elders",
                                "SCENARIO 6":"The City of Archives",
                                "SCENARIO 7":"The Depths of Yoth",
                                "SCENARIO 8":"Shattered Aeons"}
                break
            
            else:
                print('\n'+"Campaign name not found. Please try again.")
                continue

        self.team_name = input("Enter the team name: ")
        
        self.camp_inv_list = []
        
        self.inv1 = input("Enter investigator name: ")
        
        (self.camp_inv_list).append(self.inv1)
        
        while True:
            try:
                self.more_inv_response = input("More investigators? y/n ")
                
                if (self.more_inv_response).lower() == "y":
                    
                    self.add_inv = input("Enter additional investigator name: ")
                    
                    (self.camp_inv_list).append(self.add_inv)
                    
                    print(self.camp_inv_list)
                    
                    if len(self.camp_inv_list) == 4:
                        print('\n'+"Maximum investigator reached.")
                        break
                    else:
                        continue
                
                elif (self.more_inv_response).lower() == "n":
                    break
                
            except ValueError:
                print("Answer only with y or n.")
                continue
            else:
                print("Answer only with y or n.")
                continue 
                
        self.info()
        
        self.scenario = self.Scenario()
        
    def info(self):
        print ('\n'+"========== CAMPAIGN INFO =========="+'\n'
               +'\n'+"CAMPAIGN: "+self.name+'\n'
               +'\n'+"TEAM NAME: "+self.team_name+'\n'
               +'\n'+"INVESTIGATORS: "+", ".join(self.camp_inv_list)+"\n")
        
        for scenario,title in (self.sc_list).items():
            print (scenario+": "+title)
        
    class Scenario:
        def __init__(self):
            pass

Clyde = Investigator()
#Clyde.report()
#Clyde.performance()
#describe_persist()

tnotz_1120 = Campaign()




















        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        