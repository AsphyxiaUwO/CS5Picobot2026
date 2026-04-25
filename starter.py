# Austin Kim, Saanvi Sakthivel, & Yuna Jung
# CS5 Final Project: Picobot
# 4/24/2026

import random

HEIGHT = 25
WIDTH = 25
NUMSTATES = 5

POSSIBLE_SURROUNDINGS = ['xxxx','Nxxx','NExx','NxWx','xxxS','xExS','xxWS','xExx','xxWx']

class Program:
    def __init__(self):
        '''Constructs a blank picobot file with no instructions
        '''
        self.rules = {}
    
    def __repr__(self):
        '''Returns the string representation of the picobot instructions
        '''
        unsortedKeys = list(self.rules.keys())
        sortedKeys = sorted(unsortedKeys)
        s = ''
        for key in sortedKeys:
            s += " ".join([str(key[0]), str(key[1]), "->", str(self.rules[key][0]), str(self.rules[key][1])]) + "\n"
        return s

    def randomize(self):
        '''Creates a random set of picobot instructions
        '''
        for state in range(NUMSTATES):
            for surr in POSSIBLE_SURROUNDINGS:
                dirs = "".join([s for s in 'NEWS' if s not in surr])
                self.rules[(state, surr)] = (random.choice(dirs), random.randrange(0, NUMSTATES))