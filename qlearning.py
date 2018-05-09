import numpy as np
import random
import math

class obj:
	def __init__(self):
		self.x = 0
		self.y = 9

r = np.genfromtxt('DataTugasML3.txt')

q = np.zeros(shape=(10,10))

state = obj()
# print(state.x)
# print(state.y)

finish = False

i=0

learn = 1
count = 0
next = obj()

gamma = 0.8

while (not finish):
	if (state.x==0):
		if (state.y==0):
			arah = random.choices(['bawah','kanan'])
		elif (state.y==9):
			arah = random.choices(['kanan','atas'])
		else:
			arah = random.choices(['bawah','kanan','atas'])
	elif (state.y==0):
		arah = random.choices(['kiri','bawah','kanan'])
	elif (state.y==9 and state.x==9):
		arah = random.choices(['atas','kiri'])
	else:
		arah = random.choices(['kiri','bawah','atas','kanan'])
	# print(arah)
	if (state.x==0):
		if (state.y==0):
			q[state.y][state.x] = r[state.y][state.x] + gamma * max([q[state.y-1][state.x],q[state.y][state.x+1]])
			if (max([q[state.y-1][state.x],q[state.y][state.x+1]])==q[state.y-1][state.x]):
				state.y = state.y-1
			elif (max([q[state.y-1][state.x],q[state.y][state.x+1]])==q[state.y][state.x+1]):
				state.x = state.x+1
		elif (state.y==9):
			q[state.y][state.x] = r[state.y][state.x] + gamma * max([q[state.y-1][state.x],q[state.y][state.x+1]])
			if (max([q[state.y-1][state.x],q[state.y][state.x+1]])==q[state.y-1][state.x]):
				state.y = state.y-1
			else:
				state.x = state.x+1
		else:
			q[state.y][state.x] = r[state.y][state.x] + gamma * max([q[state.y-1][state.x],q[state.y][state.x+1],q[state.y+1][state.x]])
			if (max([q[state.y-1][state.x],q[state.y][state.x+1]])==q[state.y-1][state.x]):
				state.y = state.y-1
			elif (max([q[state.y-1][state.x],q[state.y][state.x+1]])==q[state.y][state.x+1]):
				state.x = state.x+1
			else:
				state.y = state.y+1
	elif (state.y==0):
		q[state.y][state.x] = r[state.y][state.x] + gamma * max([q[state.y][state.x-1],q[state.y][state.x+1],q[state.y+1][state.x]])
		if (max([q[state.y][state.x-1],q[state.y][state.x+1],q[state.y+1][state.x]])==q[state.y][state.x-1]):
			state.x = state.x - 1
		elif (max([q[state.y][state.x-1],q[state.y][state.x+1],q[state.y+1][state.x]])==q[state.y][state.x+1]):
			state.x = state.x + 1
		else:
			state.y = state.y+1
	elif (state.y==9):
		if (state.x==9):
			q[state.y][state.x] = r[state.y][state.x] + gamma * max([q[state.y-1][state.x],q[state.y][state.x-1]])
			if (max([q[state.y-1][state.x],q[state.y][state.x-1]])==q[state.y][state.x-1]):
				state.x = state.x-1
			else:
				state.y = state.y-1
		else:
			q[state.y][state.x] = r[state.y][state.x] + gamma * max([q[state.y-1][state.x],q[state.y][state.x-1],q[state.y][state.x+1]])
			if (max([q[state.y-1][state.x],q[state.y][state.x-1]])==q[state.y][state.x-1]):
				state.x = state.x-1
			elif (max([q[state.y-1][state.x],q[state.y][state.x-1]])==q[state.y][state.x+1]):
				state.x = state.x+1
			else:
				state.y = state.y-1
	elif (state.x==9):
		q[state.y][state.x] = r[state.y][state.x] + gamma * max([q[state.y][state.x-1],q[state.y-1][state.x],q[state.y+1][state.x]])
		if (max([q[state.y][state.x-1],q[state.y-1][state.x],q[state.y+1][state.x]])==q[state.y][state.x-1]):
			state.x = state.x - 1
		elif (max([q[state.y][state.x-1],q[state.y-1][state.x],q[state.y+1][state.x]])==q[state.y-1][state.x]):
			state.x = state.y - 1
		else:
			state.y = state.y+1

	else:
		q[state.y][state.x] = r[state.y][state.x] + gamma * max([q[state.y-1][state.x],q[state.y][state.x+1],q[state.y+1][state.x],q[state.y][state.x-1]])
		if (max([q[state.y-1][state.x],q[state.y][state.x+1],q[state.y+1][state.x],q[state.y][state.x-1]])==q[state.y-1][state.x]):
			state.y = state.y - 1
		elif (max([q[state.y-1][state.x],q[state.y][state.x+1],q[state.y+1][state.x],q[state.y][state.x-1]])==q[state.y][state.x+1]):
			state.x = state.x + 1
		elif (max([q[state.y-1][state.x],q[state.y][state.x+1],q[state.y+1][state.x],q[state.y][state.x-1]])==q[state.y+1][state.x]):
			state.y = state.y + 1
		else:
			state.x = state.x - 1	
	# q[state.y][state.x] = r[state.y][state.x] + gamma * max([])
	print(q)
	print(state.x,state.y)
	learn = learn + 1
	count = count + 1
	if (state.x==9 and state.y==0):
		if (learn>20):
			finish = True
		else:
			state.x = 0
			state.y = 9
			count = 0
	else:
		if (count>100):
			finish = True
