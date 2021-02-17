import node
import costFunction
import random
import numpy as np

# +------- PSO Parameters -------+
maxIterator = 1000              #Max number of iterations
nParticles = 50               #Number of particles
particles = []               #Particles array
minNum = 10                  #Min number for randomization
maxNum = -10                 #Max number for randomization
varSize = 2                  #Number of unknown variables

w = 1                           #Inertia Coefficient

coefficient = [1,1]             #Cognitice and social coefficient
globalBest = [[],float('inf')]  #Stores global best particle
                                #globalBest[0] = best position
                                #globalBest[1] = best cost
# +-------Initialize PSO --------+
for i in range(nParticles):
    position = np.array([random.uniform(minNum, maxNum) for i in range(varSize)])
    cost = costFunction.costFunction(position)
    particles.append(node.Node(
        position,            #Sets particles position
        np.array([0 for i in range(varSize)]),   #Sets particles velocity
        cost,                #Evaluates cost of particle
        position,            #Updates personal best position
        cost                 #Update personal best cost
    ))
    if cost < globalBest[1]:
        globalBest = [position,cost]

# +------- PSO Main Loop --------+
for i in range(maxIterator):
    for particle in particles:

        """
            This seperates the particle velocity calculation into two parts
                1: The particles inertia defined as: inertia = w*velocity
                2: The combination of the particles cognitive and social components defined as:
                    cognitive = c1 * r1 * (particle'sBestPosition - position)
                    social    = c2 * r2 * (globalBestPosition - position)
            This was done so we can use np.add(a1,a2) which can only take 2 input arrays. If another method is found it will be updated
            -- Juan Ramirez 2/17/2021
        """
        inertia = w*particle.velocity
        components = np.add(coefficient[0]*random.uniform(minNum, maxNum)* np.subtract(particle.bestPosition, particle.position),
                            coefficient[1]*random.uniform(minNum, maxNum)* np.subtract(globalBest[0],  particle.position))
        
        particle.velocity = np.add(inertia, components)

        particle.position = np.add(particle.position, particle.velocity)
        particle.cost = costFunction.costFunction(particle.position)

        if particle.cost < particle.bestCost:
            particle.bestPosition = particle.position
            particle.bestCost = particle.cost

            if particle.bestCost < globalBest[1]:
                globalBest[0] = particle.bestPosition
                globalBest[1] = particle.bestCost
    print(particle.velocity)
print(globalBest)
