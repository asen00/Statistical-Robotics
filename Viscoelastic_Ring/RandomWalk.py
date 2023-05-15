import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# class PARTICLE():
#     def __init__(self, time, s):
#         self.x = np.zeros(len(time))
#         self.y = np.zeros(len(time))
#         self.theta = np.random.rand(len(time))*(2*np.pi)

#         for t in time[1:]:
#             self.x[t] = self.x[t-1] + (s * np.cos(self.theta[t]))
#             self.y[t] = self.y[t-1] + (s * np.sin(self.theta[t]))

class PARTICLE():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SIMULATION():
    def __init__(self, numParticles, simTime, s):
        self.numParticles = numParticles
        self.simTime = simTime
        self.time = np.arange(self.simTime)

        x1 = np.zeros(self.simTime)
        y1 = np.zeros(self.simTime)
        x2 = np.zeros(self.simTime)
        y2 = np.zeros(self.simTime)
        for t in self.time:
            x1[t] = 20 - t
            y1[t] = 20 - t
            x2[t] = t
            y2[t] = t

        self.particles = {}
        # for p in range(numParticles):
        #     self.particles[p] = PARTICLE()
        self.particles[0] = PARTICLE(x1, y1)
        self.particles[1] = PARTICLE(x2, y2)

    def dist(self, pos1, pos2):
        return np.sqrt(((pos1[0]-pos2[0])**2)+((pos1[1]-pos2[1])**2))
    
    def check(self):
        for t in self.time[1:self.simTime-1]:
            positions = {}
            coll = {}
            for p in self.particles:
                for q in self.particles:
                    xp = self.particles[p].x[t]
                    yp = self.particles[p].y[t]
                    xq = self.particles[q].x[t]
                    yq = self.particles[q].y[t]
                    if self.dist((xp,yp),(xq,yq)) <= 0.0000001:
                        if (xp,yp) in positions:
                            positions[(xp,yp)].append(p)
                            coll[(p,q)] = True
                        elif (xq,yq) in positions:
                            positions[(xq,yq)].append(q)
                            coll[(p,q)] = True
                        else:
                            positions[(xp,yp)] = [p]
                            positions[(xq,yq)] = [q]
                            coll[(p,q)] = False
            if coll[(p,q)] == True:
                print('Collision at t=', t)
                self.particles[p].x[t+1] = self.particles[q].x[t-1]
                self.particles[p].y[t+1] = self.particles[q].y[t-1]
                self.particles[q].x[t+1] = self.particles[p].x[t-1]
                self.particles[q].y[t+1] = self.particles[p].y[t-1]
        
    def plot(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        for i in range(self.numParticles):
            ax.plot3D(self.particles[i].x, self.particles[i].y, np.arange(self.simTime))
        # plt.savefig('RandomWalk'+str(self.simTime)+str(self.numParticles)+'.png', dpi=600)
        plt.show()

#np.random.seed(0)
simTime = 20
numParticles = 2
sim = SIMULATION(numParticles, simTime, 5)
sim.check()
sim.plot()