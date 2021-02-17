class Node():
    def __init__(self, position, velocity, cost, bestPosition, bestCost):
        self.position       = position
        self.velocity       = velocity
        self.cost           = cost
        self.bestPosition   = bestPosition
        self.bestCost       = bestCost
        
    def display(self):
        print("Particle's Position: {}".format(self.position))
        print("Particle's Velocity: {}".format(self.velocity))
        print("Particle's Cost: {}".format(self.cost))
        print("Particle's Best Position: {}".format(self.bestPosition))
        print("Particle's Best Cost: {}".format(self.bestCost))