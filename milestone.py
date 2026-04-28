# Austin Kim, Saanvi Sakthivel, & Yuna Jung
# CS5 Final Project: Picobot
# 4/27/2026

import random

HEIGHT = 25
WIDTH = 25
NUMSTATES = 5

POSSIBLE_SURROUNDINGS = ['xxxx','Nxxx','NExx','NxWx','xxxS','xExS','xxWS','xExx','xxWx']

class Program:
    ""
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
        return self
    
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
        return self
        
    
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
        """Just makes the greater than operator not break
        """
        return random.choice([True, False])

    def __lt__(self, other):
        """Just makes the less than operator not break
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
        """returns a string of the world where Picobot is shown as 'P' and visited cells as 'o'
        """
        self.room[self.row][self.col] = 'P'
        s = ''
        for row in range(HEIGHT):
            s += "".join(self.room[row]) + "\n"
        self.room[self.row][self.col] = 'o'
        return s

    def getCurrentSurroundings(self):
        """Notes whether there is a wall in the north, east, west, or south to note the surrounding
        """
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
        """looks at the current surroundings and executes Picobot's next move and state based on the current surrounding
        """
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
        """determine how many times to run the program
        """
        for i in range(steps):
            self.step()

    def fractionVisitedCells(self):
        """calculates the fraction of cells that were visited
        """
        flat = "".join([item for row in self.room for item in row])
        visited = flat.count('o')
        total = WIDTH*HEIGHT - flat.count('+')
        return visited/total

def evaluateFitness(program, trials, steps):
    """calculates the fitness of the program using the fractionVisited function 
    """
    fracs = []
    for i in range(trials):
        w = World(random.randrange(1, WIDTH-1), random.randrange(1, HEIGHT-1), program)
        w.run(steps)
        fracs += [w.fractionVisitedCells()]
    return sum(fracs) / len(fracs)

def GA(popsize, numgens):
    """runs the genenic algorithm with the population size and returns the best algorithm with the best fitness after given number of generations
    """
    programs = [Program().randomize() for i in range(popsize)]
    L = [(evaluateFitness(p, 20, 800), p) for p in programs]
    SL = sorted(L)
    for generation in range(numgens):
        bestPrograms = SL[-(popsize//10):]
        nextGen = list(bestPrograms)
        while len(nextGen) < popsize:
            p1 = random.choice(bestPrograms)[1]
            p2 = random.choice(bestPrograms)[1]
            child = p1.crossover(p2)
            if random.random() < 0.5:
                child.mutate()
            nextGen.append((evaluateFitness(child, 20, 800), child))
        L = nextGen
        SL = sorted(L)
        print("Generation " + str(generation))
        print("Average Fitness: " + str(sum(t[0] for t in SL) / len(SL)))
        print("Best Fitness: " + str(SL[-1][0]))
    print("Best Picobot Program")
    return SL[-1][1]

