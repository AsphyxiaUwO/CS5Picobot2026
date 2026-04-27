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
        child = Program()
        for state in range(NUMSTATES):
            parent = random.choice([self, other])
            for surr in POSSIBLE_SURROUNDINGS:
                child.rules[(state, surr)] = parent.rules[(state, surr)]
        return child
    
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
        """Creates a picbot world with edges
        """
        self.row = initial_row
        self.col = initial_col
        self.state = 0
        self.program = program
        self.room = [[' ']*WIDTH for row in range(HEIGHT)]
        for col in range(WIDTH):
            self.room[0][col] = '+'
            self.room[HEIGHT-1][col] = '+'
        for row in range(HEIGHT):
            self.room[row][0] = '+'
            self.room[row][WIDTH-1] = '+'
        self.room[self.row][self.col] = 'o'
    
    def __repr__(self):
        self.room[self.row][self.col] = 'P'
        s = ''
        for row in range(HEIGHT):
            s += "".join(self.room[row]) + "\n"
        self.room[self.row][self.col] = 'o'
        return s

    def getCurrentSurroundings(self):
        s = ''
        if self.room[self.row-1][self.col] == '+':
            s += 'N'
        else:
            s += 'x'
        if self.room[self.row][self.col+1] == '+':
            s += 'E'
        else:
            s += 'x'
        if self.room[self.row][self.col-1] == '+':
            s += 'W'
        else:
            s += 'x'
        if self.room[self.row+1][self.col] == '+':
            s += 'S'
        else:
            s += 'x'
        return s


    def step(self):
        (nextMove, nextState) = self.program.getMove(self.state, self.getCurrentSurroundings())
        if nextMove == 'N':
            self.row -= 1
        elif nextMove == 'E':
            self.col += 1
        elif nextMove == 'W':
            self.col -= 1
        elif nextMove == 'S':
            self.row += 1
        self.state = nextState
        self.room[self.row][self.col] = 'o'

    def run(self, steps):
        for i in range(steps):
            self.step()

    def fractionVisitedCells(self):
        flat = "".join([item for row in self.room for item in row])
        visited = flat.count('o')
        total = WIDTH*HEIGHT - flat.count('+')
        return visited/total

def evaluateFitness(program, trials, steps):
    print('boop')
    # Saanvi

def GA(popsize, numgens):
    print('boop')
    # Austin, but we'll work on this together
