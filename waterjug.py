# 3 water jugs capacity -> (x,y,z) where x>y>z
# initial state (0,0)
# final state (2,0)


capacity = (3,4) 
# Maximum capacities of 3 jugs -> x,y,z
x = capacity[0]
y = capacity[1]


# to mark visited states
memory = {}

# store solution path
ans = []

def get_all_states(state):
	# Let the 3 jugs be called a,b,c
	a = state[0]
	b = state[1]


	if(a==0 and b==2):
		ans.append(state)
		return True

	# if current state is already visited earlier
	#if((a,b) in memory):
	#	return False

	memory[(a,b)] = 1

	#empty jug a
	if(a>=0):
		#empty a into b
		if(a+b<=y):
			if( get_all_states((0,a+b)) ):
				ans.append(state)
				return True
		else:
			if( get_all_states((a-(y-b), y)) ):
				ans.append(state)
				return True
		

	#empty jug b
	if(b>=0):
		#empty b into a
		if(a+b<=x):
			if( get_all_states((a+b, 0)) ):
				ans.append(state)
				return True
		else:
			if( get_all_states((x, b-(x-a))) ):
				ans.append(state)
				return True
		

	

	

initial_state = (0,0)
print("Starting work...\n")
get_all_states(initial_state)
ans.reverse()
for i in ans:
	print(i)
