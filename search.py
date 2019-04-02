# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return startState

    reached = []
    frontier = util.Stack()
    frontier.push([(problem.getStartState(), "Stop", 0)])

    while not frontier.isEmpty():
        path = frontier.pop()
        state = path[len(path) - 1]  # state contains smth like this ((5, 5), 'Stop', 0)
        state = state[0]  # state[0] contain the actual coordinates (5,5)

        if problem.isGoalState(state):
            return [x[1] for x in path][1:]  # return the path in words, north, south, west, west, etc
            # only when goal is found

        if state not in reached:
            reached.append(state)
            for successor in problem.getSuccessors(state):
                if successor[0] not in reached:
                    successorPath = path[:]  # expand the path to a line
                    successorPath.append(successor)  # then add the new path to it
                    frontier.push(successorPath)  # and push the new path to the stack

    return []  # failure

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return startState

    reached = []
    frontier = util.Queue()
    frontier.push([(problem.getStartState(), "Stop", 0)])

    while not frontier.isEmpty():
        path = frontier.pop()
        state = path[len(path) - 1]  # state contains smth like this ((5, 5), 'Stop', 0)
        state = state[0]  # state[0] contain the actual coordinates (5,5)

        if problem.isGoalState(state):
            return [x[1] for x in path][1:]  # return the path in words, north, south, west, west, etc
            # only when goal is found

        if state not in reached:
            reached.append(state)
            for successor in problem.getSuccessors(state):
                if successor[0] not in reached:
                    successorPath = path[:]  # expand the path to a line
                    successorPath.append(successor)  # then add the new path to it
                    frontier.push(successorPath)  # and push the new path to the stack

    return []  # failure
    util.raiseNotDefined()


def uniformCostSearch(problem):
    # Something wrong, will fix later.
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return startState

    reached = []
    frontier = util.PriorityQueue()
    frontier.push([(problem.getStartState(), "Stop", 0)], 0)

    while not frontier.isEmpty():
        path = frontier.pop()
        state = path[len(path) - 1]  # state contains smth like this ((5, 5), 'Stop', 0)
        state = state[0]  # state[0] contain the actual coordinates (5,5)

        if problem.isGoalState(state):
            return [x[1] for x in path][1:]  # return the path in words, north, south, west, west, etc
            # only when goal is found

        if state not in reached:
            reached.append(state)
            for successor in problem.getSuccessors(state):
                if successor[0] not in reached:
                    successorPath = path[:]  # expand the path to a line
                    successorPath.append(successor)  # then add the new path to it
                    frontier.update(successorPath, successor[2])  # and push the new path to the stack
                    frontier.push(successorPath, successor[2])  # and push the new path to the stack

    return []  # failure
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return startState

    reached = []
    costFunction = lambda somePath: problem.getCostOfActions(x[1] for x in somePath) + nullHeuristic(x[1] for x in somePath)
    # inline cost function, takes two values, cost and heuristic, returns A* value
    frontier = util.PriorityQueueWithFunction(costFunction)
    frontier.push([(problem.getStartState(), "Stop", 0)])
    while not frontier.isEmpty():
        path = frontier.pop()
        state = path[len(path) - 1]
        state = state[0]
        if problem.isGoalState(state):
            return [x[1] for x in path][1:]

        if state not in reached:
            reached.append(state)
            for successor in problem.getSuccessors(state):
                if successor[0] not in reached:
                    successorPath = path[:]
                    successorPath.append(successor)
                    frontier.push(successorPath)

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
