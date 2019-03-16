import os
from maze import *
from turtle import *
from datetime import datetime
''' File Name format student#_Name e.g.) 2015123456_John'''

''' Write a function to escape from a maze with searching algorithm'''
''' You are allowed to use 5 functions (Left, Right, Forward, Backward, isSuccess) with agent actions '''
''' Starting point will be given'''
''' Program will be tested with different maze'''

''' Comment is necessary for code description '''
''' Plagiarism prohibited '''


''' The main idea of this algorithm is to check every possible way to go outside of the maze. '''
''' It remembers the way which it used and tries not to use the same one twice'''
''' In a situation in which it is in a cul-de-sac it comes back to the point in which'''
''' it has another possible way and tried different path'''

# as it was said in assignment everything is included in this function
def escape():

    # returns opposite direction
    def oppositeDirection(direction):
        if direction == 'forward':
            return 'backward'
        if direction == 'backward':
            return 'forward'
        if direction == 'right':
            return 'left'
        if direction == 'left':
            return 'right'
        return 'start'

    # moves depending on argument
    def move(direction):
        if direction == 'forward':
            Forward(agent)
        if direction == 'backward':
            Backward(agent)
        if direction == 'right':
            Right(agent)
        if direction == 'left':
            Left(agent)

    # it represents one point of the path
    class Point:

        # adds opposite direction to given in argument to the list of tried moves
        def __init__(self, direction):
            self.triedDirections = []
            self.triedDirections.append(oppositeDirection(direction))

        # if it hasn't done move in the direction yet it will add it to the list
        def tryStep(self, direction):
            if direction not in self.triedDirections:
                self.triedDirections.append(direction)
                return True
            else:
                return False

        # returns true if the point has already tried to move in every possible direction
        def wereEverywhere(self):
            allDirections = ['left', 'right', 'forward', 'backward']
            if all(elem in self.triedDirections for elem in allDirections):
                return True
            return False

    # Analogical to radius from maze.py but has values from 0 to 2
    zone = 0
    # The path it has already gone through
    path = []
    # Makes starting point and adds it to the path
    startingPoint = Point('start')
    path.append(startingPoint)
    while True:
        if isSuccess():
            return True
        # if we are in zone 0 we cant go backward so it will be assigned to triedDirections list by default
        if zone == 0:
            path[-1].triedDirections.append('backward')

        # if it hasn't tried to go backward than add it to the list of triedDirections and try to move
        if path[-1].tryStep('backward'):
            # if it is possible to go backward than go, decrease zone of 1 and append path of new point
            if Backward(agent):
                zone -=1
                path.append(Point('backward'))

        # if it hasn't tried to go right than add it to the list of triedDirections and try to move
        elif path[-1].tryStep('right'):
            if Right(agent):
                path.append(Point('right'))

        # analogical to backward, but increase zone value
        elif path[-1].tryStep('forward'):
            if Forward(agent):
                zone += 1
                path.append(Point('forward'))

        # analogical to right
        elif path[-1].tryStep('left'):
            if Left(agent):
                path.append(Point('left'))

        # if it already has tried every possible way (it is in the cul-de-sac)
        # it goes back and delete last element from path
        elif path[-1].wereEverywhere():
            move(path[-1].triedDirections[0])
            if path[-1].triedDirections[0] == 'forward':
                zone += 1
            if path[-1].triedDirections[0] == 'backward':
                zone -= 1
            del path[-1]


if __name__ == '__main__':
    # Maze
    screen = Screen()
    sampleMaze()

    # Agent Init
    agent = Turtle()
    init_agent(agent)
    start = datetime.now()
    escape()
    finish = datetime.now()

    # Result
    print(os.path.basename(__file__).split('.')[0])
    print('Result   : Pass') if isSuccess() else print('Result   : Fail')
    print('Duration :', finish-start)

    mainloop()