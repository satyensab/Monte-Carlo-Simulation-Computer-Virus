#import random library
import random

#counters
total_num_days = 0
total_inf_least_once = 0; 
total_comp_inf = 0


#user input (number of simulations, total number of computers, probability of virus, and number of computers fixed daily)
sim_input = int(input("Simulations: ")) 
n_computers = int(input("What is the total number of computers? ")) 
p = float(input("What is the probability of spreading the virus? "))
n_fix= int(input("What is the number of computers fixed daily? "))

#bernoulli trial
def MyBernoulli(p):
  U = random.uniform(0,1)
  X = None
  if (U < p):
    X = 1
  else:
    X = 0
  return X


for sim in range(sim_input):
  #counters that reset per simulation
  comp_list = [0] * (n_computers)
  comp_list[0] = 1
  days = 0
  comp_ever = [0] * (n_computers)
  comp_ever[0] = 1
  
  while(comp_list.count(1) > 0):
    count_j = n_fix
    #morning 
    before_morning = comp_list.count(1)
    for i in range(n_computers):
      for j in range(n_computers):
        if ((comp_list[i] == 1) and (comp_list[j] == 0)):
          x = MyBernoulli(p)
          if (x == 1):
            comp_list[j] = 2
            comp_ever[j] = 1

    for l in range(n_computers):
      if comp_list[l] == 2:
        comp_list[l] = 1
  
    #afternoon
    if comp_list.count(1) <= n_fix:
        for b in range(n_computers):
          if comp_list[b] == 1:
             comp_list[b] = 0
    else:  
      while(count_j > 0):
        random_index = random.randint(0,n_computers-1)
        if comp_list[random_index] == 1:
            comp_list[random_index] = 0
            count_j = count_j - 1
    total_num_days+=1
    days+=1

  number_ever_infected = sum(comp_ever)
  if number_ever_infected == 20:
    total_inf_least_once+=1
  total_comp_inf+=number_ever_infected
  


#Expected Outputs
#1)
expected_num_days = total_num_days/sim_input
print("Expected number of days to remove virus: " + str(expected_num_days))

#2)
expected_least_once = float(total_inf_least_once/sim_input)
print("Probability of each computer getting infected: " + str(expected_least_once))

#3)
expected_comp_inf = round(total_comp_inf/sim_input,2)
print("Expected number of computers infected: " + str(expected_comp_inf))