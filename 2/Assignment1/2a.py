import numpy as np
import scipy.misc
from scipy.misc import imsave
import matplotlib.pyplot as plt

mass = np.load('./input/masses.npy')
position = np.load('./input/positions.npy')
velocity = np.load('./input/velocities.npy')
num_particles = mass.shape[0]
acceleration = np.zeros((num_particles,2))
G=667000
threshold=0.1
timestep=0.0001
print(mass.shape[0],position.shape,velocity.shape)

def check_threshold_distance(r,num_particles,threshold):
	min1=1000000
	for i in range(num_particles):
		for j in range(num_particles):
			if i!=j:
				if min1>np.linalg.norm(r[i]-r[j]):
						min1=np.linalg.norm(r[i]-r[j])
				if np.linalg.norm(r[i]-r[j])<threshold:
					#print("mil gya ",i,j)
					return 1
	#print(min1)
	return 0

def get_acceleration(G,num_particles,masses,positions):
	accelerations = np.zeros((num_particles,2))
	#print(num_particles)
	for i in range(num_particles):
		u=0
		v=0
		for j in range(num_particles):
			if i!=j:
				#euc_dist = np.linalg.norm(positions[j]-positions[i])
				euc_dist=pow(pow(positions[j][0]-positions[i][0],2)+pow(positions[j][1]-positions[i][1],2),0.5)
				euc_dist=euc_dist*euc_dist*euc_dist
				u=u+(1)*((masses[j]*(G)*(positions[j][0]-positions[i][0]))/euc_dist)
				v=v+(1)*((masses[j]*(G)*(positions[j][1]-positions[i][1]))/euc_dist)
		accelerations[i][0]=u
		accelerations[i][1]=v
		if i==199:
			print(u,v)
			print(accelerations[99])
	#print(accelerations[99],i)
	return accelerations

def update_positions_and_velocities(positions,velocities,acceleration,timestep,num_particles):
	#for i in range(num_particles):
	positions=positions+velocities*timestep+0.5*acceleration*timestep*timestep
	velocities=velocities+acceleration*timestep
	return positions,velocities

i=0
while i<100000: 
	if check_threshold_distance(position,num_particles,threshold)==1:
		print("threshold crosses at iteration ",i)
		i=100000
		#file = open(“.txt”,”w”) 
		#file.write(“Hello World”) 
		np.save("positions.npy",position)
		np.save("velocities.npy",velocity)

	else:
		acceleration=get_acceleration(G,num_particles,mass,position)
		position,velocity=update_positions_and_velocities(position,velocity,acceleration,timestep,num_particles)
		i=i+1
	#print(i,position[99])