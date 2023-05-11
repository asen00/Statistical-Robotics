import numpy as np
import matplotlib.pyplot as plt

class PARTICLE():
    def __init__(self, time, s):
        self.x = np.zeros(len(time))
        self.y = np.zeros(len(time))
        # self.theta = np.random.rand(len(time))*(2*np.pi)
        theta = [0, np.pi/2, 3*np.pi/2, 2*np.pi]
        self.theta = np.random.choice(theta, size=len(time))

        for t in time[1:]:
            self.x[t] = self.x[t-1] + (s * np.cos(self.theta[t]))
            self.y[t] = self.y[t-1] + (s * np.sin(self.theta[t]))

class SIMULATION():
    def __init__(self, numParticles, time, s):
        self.numParticles = numParticles
        self.time = time
        self.simTime = len(self.time)

        self.particles = {}
        self.Xpositions = np.zeros((self.simTime, self.numParticles))
        self.Ypositions = np.zeros((self.simTime, self.numParticles))

        for p in range(numParticles):
            self.particles[p] = PARTICLE(self.time, s)
        
        for t in self.time:
            for p in self.particles:
                self.Xpositions[t][p] = self.particles[p].x[t]
                self.Ypositions[t][p] = self.particles[p].y[t]

    
    def check_collision(self):
        for t in self.time[1:]:
            for p in self.particles:
                currentX = self.Xpositions[t][p]
                tempArrX = np.delete(self.Xpositions[t], p)
                currentY = self.Ypositions[t][p]
                tempArrY = np.delete(self.Ypositions[t], p)
                
                for x,y in np.nditer([tempArrX, tempArrY]):
                    coll = ((x-0.0000001 < currentX < x+0.0000001) and (y-0.0000001 < currentY < y+0.0000001))

                #coll = (currentX == np.any(tempArrX)) and (currentY == np.any(tempArrY))
                #coll = (collX==True) and (collY==True)
                if coll == True:
                    print('x:', currentX, tempArrX)
                    print('y:', currentY, tempArrY)
                    collidingparticle = np.argwhere(coll == True)
                    print('\ncollidingparticle', collidingparticle, '\n\n\n')
                    
                    self.particles[p].x[t+1] = -self.particles[p].x[t]
                    self.particles[p].y[t+1] = -self.particles[p].y[t]
                    self.particles[collidingparticle].x[t+1] = -self.particles[collidingparticle].x[t]
                    self.particles[collidingparticle].y[t+1] = -self.particles[collidingparticle].y[t]

    def collision(self):
        array = np.zeros((self.simTime, self.numParticles, 2))
        for t in self.time:
            for p in self.particles:
                array[t][p][0] = self.particles[p].x[t]
                array[t][p][1] = self.particles[p].y[t]
        
        for t in self.time[1:]:
            for p in self.particles:
                current = array[t][p]
                compare = np.delete(array[t], p, axis=0)
                print('\n', t, current, compare)
                if np.all(current) == np.all(np.any(compare, axis=0)):
                    print('\nTRUE1')
                    collidingparticle = np.argwhere(np.all(current) == np.all(np.any(compare, axis=0)))
                    if type(collidingparticle) == int:
                        print('\nTRUE2', collidingparticle)
                else:
                    print('\nFALSE1')

np.random.seed(0)
sim = SIMULATION(3, np.arange(10), 5)
sim.collision()
# plt.plot(sim.particles[0].x, sim.particles[0].y, 'b', linestyle='', marker='o', markersize=10)
# plt.plot(sim.particles[1].x, sim.particles[1].y, 'r', linestyle='', marker='o', markersize=8)
# plt.plot(sim.particles[2].x, sim.particles[2].y, 'y', linestyle='', marker='o', markersize=6)
# plt.plot(sim.particles[3].x, sim.particles[3].y, 'm', linestyle='', marker='o', markersize=4)
# plt.plot(sim.particles[4].x, sim.particles[4].y, 'c', linestyle='', marker='o', markersize=2)
# plt.show()

# time = np.arange(100000)
# x = np.zeros(len(time))
# y = np.zeros(len(time))
# theta = np.zeros(len(time))
# s = 5

# for t in time[1:]:
#     theta[t] = np.random.rand()*(2*np.pi)
#     x[t] = x[t-1] + (s * np.cos(theta[t]))
#     y[t] = y[t-1] + (s * np.sin(theta[t]))

# plt.plot(x,y)
# plt.show()

# import numpy as np
# a = np.random.randint(4,8,size=(2,3))
# print(a)
# for x in np.nditer(a, flags = ['external_loop'], order = 'C'):
#     print(x)