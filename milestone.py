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
        """Creates a blank picobot instruction file
        """
        self.rules = {}
    
    def __repr__(self):
        """Returns the string representation of the picobot instruction
        """
        unsortedKeys = list(self.rules.keys())
        sortedKeys = sorted(unsortedKeys)
        s = ''
        for key in sortedKeys:
            s += " ".join([str(key[0]), str(key[1]), "->", str(self.rules[key][0]), str(self.rules[key][1])]) + "\n"
        return s

    def randomize(self):
        """Creates a random set of picobot instructions
        """
        for state in range(NUMSTATES):
            for surr in POSSIBLE_SURROUNDINGS:
                dirs = "".join([s for s in 'NEWS' if s not in surr])
                self.rules[(state, surr)] = (random.choice(dirs), random.randrange(0, NUMSTATES))
    
    def getMove(self, state, surroundings):
        """Returns the move of picobot based on the state and surroundings
        """
        return self.rules[(state, surroundings)]
    
    def mutate(self):
        """Returns the picobot instructions with one move changed
        """
        key = random.choice(list(self.rules.keys()))
        surr = key[1]
        dirs = "".join([s for s in 'NEWS' if s not in surr])
        self.rules[key] = (random.choice(dirs), random.randrange(0, NUMSTATES))
    
    def crossover(self, other):
        """Crosses over moves from two parents by states
        """
        new = {}
        for state in range(NUMSTATES):
            parent = random.choice([self, other])
            for surr in POSSIBLE_SURROUNDINGS:
                new[(state, surr)] = parent[(state, surr)]
        return new
    
    def __gt__(self, other):
        """idk
        """
        return random.choice([True, False])

    def __lt__(self, other):
        """idk
        """
        return random.choice([True, False])

class World:
    def __init__(self, initial_row, initial_col, program):
        self.row = initial_row
        self.col = initial_col
        self.state = 0
        self.program = program
        self.room = [[' ']*WIDTH for row in range(HEIGHT)]
        for col in range(WIDTH):
            self.room[0][col] = '+'
            self.room[HEIGHT][col] = '+'
        for row in range(HEIGHT):
            self.room[row][0] = '+'
            self.room[row][WIDTH] = '+'
    
    def __repr__(self):


    def getCurrentSoundings(self):
        s = ''
        if self.room[self.row-1][]


    def step(self):


    def run(self, steps):


    def fractionVisitedCells(self):