import random as random
'''
This file is where you put your solutions.
'''


'''
This function computes the Q-learning update given a new (s,a,r,s') data point.

Input:
q is the current estimated Q-function that you should update in-place
alpha dictates how much of the new Q-value should mix with the current value
gammma is the discount factor
(s,a,r,ss) is the new data point
s was the current state
a was the action taken at s
r is the reward recieved
ss is the next state the MDP has transitioned to

Output:
No output is expected
q should be updated in-place
'''
def ql_update(q, alpha, gamma, s, a, r, ss):
    l=1-alpha
    m=l*q[s][a]
    n=alpha*r
    maxi=-10000000000000000000000000000000
    for t in q[ss]:
    	if(t>maxi):
    		maxi=t
    rt=alpha*gamma*maxi
    we=m+n+rt
    q[s][a]=we
    return q

'''
This function computes the greedy policy associated with the given Q-function

Input:
q is the current estimated Q-function

Output:
A policy which should be represented as a list (as explained in the handout)
The list will give an action for each state
'''
def ql_policy(q):
    l=[]
    for t in q:
    	maxi=-10000000000000000000000000000000
    	tran=0
    	count=0
    	for s in t:
    		if(s>maxi):
    			maxi=s
    			tran=count
    		count=count+1    	
    	l.append(tran)
    return l 
'''
This function performs one step of Q-learning
Given a new data point (s,a,r,ss), it will update the estimated Q-function in-place
Then it will determine the next action to take using an epsilon-greedy policy
You should use 0.3 for alpha and 0.1 for epsilon

Input:
q is the current estimated Q-function
gamma is the discount factor
(s,a,r,ss) is the new data point
s was the current state
a was the action taken at s
r is the reward recieved
ss is the next state the MDP has transitioned to

Output:
A tuple (greedy_a, a) where
greedy_a is the action that the greedy policy says to take for state ss
a is the action that the epsilon-greedy policy would take
You should also update the Q-function q in-place
'''


def ql_iteration(q, gamma, s, a, r, ss):    
    q=ql_update(q, 0.3, gamma, s, a, r, ss)
    l=ql_policy(q)
    y=random.randrange(0,len(q[0]),1)
    z=random.randrange(0,1000,1)
    z=z/1000.0
    if(z>0.9):
    	action=y
    else:
    	action=l[ss]
    return (l[ss],action)

'''
This function performs one step of Q-learning
Given a new data point (s,a,r,ss), it will update the estimated Q-function in-place
Then it will determine the next action to take using an epsilon-greedy policy
It is up to you how you want to set alpha and epsilon to try to learn more quickly

Input:
q is the current estimated Q-function
gamma is the discount factor
(s,a,r,ss) is the new data point
s was the current state
a was the action taken at s
r is the reward recieved
ss is the next state the MDP has transitioned to

Output:
A tuple (greedy_a, a) where
greedy_a is the action that the greedy policy says to take for state ss
a is the action that the epsilon-greedy policy would take
You should also update the Q-function q in-place
'''
def ql_iteration_tuned(i, q, gamma, s, a, r, ss):
	w=1.0/pow(i+1,0.9)
	t=1.0/pow(i+1,0.009)
	q=ql_update(q,t, gamma, s, a, r, ss)
	l=ql_policy(q)
	y=random.randrange(0,len(q[0]),1)
	z=random.randrange(0,100000,1)
	z=z/100000.0
	if(z>(1-w)):
		action=y
	else:
		action=l[ss]
	return (l[ss],action)
    