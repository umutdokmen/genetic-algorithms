import random
import ast

city_list=[0,1,2,3,4,5,6,7,8,9,10]
population=[]
cost_list=[]
first_pop=[]
def generateFirstPopulation():
    for i in range(1,1000):
        first_pop.append(generatePossiblePath())
print(first_pop)
graph=[[0,29,20,21,16,31,100,12,4,31,18],
       [29,0,15,29,28,40,72,21,29,41,12],
       [20,15,0,15,14,25,81,9,23,27,13],
       [21,29,15,0,4,12,92,12,25,13,25],
       [16,28,14,4,0,16,94,9,20,16,22],
       [31,40,25,12,16,0,95,24,36,3,37],
       [100,72,81,92,94,95,0,90,101,99,84],
       [12,21,9,12,9,24,90,0,15,25,13],
       [4,29,23,25,20,36,101,15,0,35,18],
       [31,41,27,13,16,3,99,25,35,0,38],
       [18,12,13,25,22,37,84,13,18,38,0]]


def cost(path):
    cost=0
    for i in range(len(path)-2):
        cost += graph[path[i]][path[i + 1]]
    cost+=graph[path[len(path)-2]][path[len(path)-1]]
    cost_list.append(cost)
    return cost

def generatePossiblePath():
    path=[]
    for i in range(1,len(city_list)+1):
        randomNum=random.randint(0,10)
        while(numberExistPath(path,randomNum)):
            randomNum = random.randint(0,10)
        path.append(randomNum)
    path.append(path[0])
    print(path)
    if(path not in population):
        population.append(path)
def numberExistPath(path,number):
    for i in path:
        if i==number:
            return True
    return False
print('first population')
generateFirstPopulation()

def distinc_population(population):
    for i in range(1,100):
        print(population[i])


#distinc_population(population)
print("INITIAL POPULATION")
print('distinct 100 individual')
print(population)

for i in range(1,101):
    print(i,". individual:",population[i-1])
    print("Fitness value of",i,". indivual:",cost(population[i-1]))

#d=dict(zip(population,cost_list))


#print(cost_list)

dictionary1= {str(k): v for k, v in zip(population, cost_list)}
print(dictionary1)
print("100 individuals sorted by fitness function")
dictionary2={k: v for k, v in sorted(dictionary1.items(), key=lambda item: item[1])}
print(dictionary2)

sorted_population = []

def sorted_population_individuals(dictionary2):
    keys_list = list(dictionary2)

    for i in range(0,100):
        x = ast.literal_eval(keys_list[i])
        sorted_population.append(x)
    return sorted_population
sorted_population_individuals(dictionary2)

cost_sorted=[]
def sorted_population_costs(dictionary2):
    for key in dictionary2.keys():
        cost_sorted.append(dictionary2[key])
    return cost_sorted

print("Sorted population ascend order according to fitness values")
print(sorted_population)
elite_pop=[]
non_elite_pop=[]
elite_cost=[]
non_elite_cost=[]
def separate_elite_population(sorted_population):
    for i in range(0,10):
        elite_pop.append(sorted_population[i])
    for i in range(10,100):
        non_elite_pop.append(sorted_population[i])
separate_elite_population(sorted_population)

sorted_population_costs(dictionary2)
print(cost_sorted)

def separate_elite_cost(cost_sorted):
    for i in range(0,10):
        elite_cost.append(cost_sorted[i])
    for i in range(10,100):
        non_elite_cost.append(cost_sorted[i])
separate_elite_cost(cost_sorted)

new_population=non_elite_pop.copy()
new_population=[]
for i in range(0,90):
    new_population.append(non_elite_pop[i])

non_elite_pop=[[9, 2, 10, 6, 1, 5, 4, 8, 7, 0, 3, 9], [1, 6, 7, 4, 3, 8, 10, 2, 9, 0, 5, 1], [3, 6, 1, 7, 10, 8, 2, 4, 5, 0, 9, 3], [5, 0, 8, 2, 10, 7, 1, 6, 4, 3, 9, 5], [10, 0, 2, 6, 1, 4, 8, 9, 3, 5, 7, 10], [6, 9, 4, 2, 8, 0, 1, 10, 7, 5, 3, 6], [8, 1, 7, 3, 5, 4, 2, 6, 10, 9, 0, 8], [7, 2, 6, 5, 3, 4, 8, 1, 10, 9, 0, 7], [4, 10, 6, 2, 9, 7, 8, 0, 1, 3, 5, 4], [4, 10, 2, 9, 1, 6, 7, 5, 3, 8, 0, 4], [9, 1, 3, 10, 2, 0, 8, 4, 7, 6, 5, 9], [1, 10, 2, 6, 4, 3, 5, 8, 9, 0, 7, 1], [10, 2, 9, 1, 7, 3, 4, 8, 0, 5, 6, 10], [8, 3, 5, 4, 6, 1, 0, 10, 9, 2, 7, 8], [8, 2, 7, 6, 5, 3, 4, 0, 10, 1, 9, 8], [5, 9, 8, 0, 7, 1, 4, 6, 2, 3, 10, 5], [8, 5, 3, 7, 10, 6, 9, 4, 0, 1, 2, 8], [8, 1, 2, 5, 6, 9, 7, 3, 4, 0, 10, 8], [0, 8, 9, 3, 1, 4, 10, 6, 2, 5, 7, 0], [1, 6, 2, 5, 7, 0, 10, 3, 4, 8, 9, 1], [10, 8, 0, 9, 1, 5, 3, 2, 6, 4, 7, 10], [5, 9, 10, 1, 0, 6, 8, 3, 7, 2, 4, 5], [5, 4, 1, 10, 0, 9, 6, 7, 8, 2, 3, 5], [5, 4, 2, 0, 10, 7, 3, 6, 8, 1, 9, 5], [8, 4, 3, 5, 10, 6, 7, 1, 9, 2, 0, 8], [5, 8, 3, 9, 10, 0, 4, 1, 6, 2, 7, 5], [3, 6, 2, 4, 1, 8, 7, 5, 9, 0, 10, 3], [3, 4, 10, 5, 9, 8, 7, 1, 0, 6, 2, 3], [3, 6, 8, 0, 9, 7, 10, 1, 5, 4, 2, 3], [4, 1, 2, 7, 5, 8, 0, 9, 3, 10, 6, 4], [5, 2, 10, 3, 6, 1, 0, 9, 4, 7, 8, 5], [9, 10, 7, 0, 4, 8, 6, 1, 5, 2, 3, 9], [1, 3, 9, 4, 8, 6, 10, 2, 5, 0, 7, 1], [1, 2, 6, 9, 0, 4, 3, 7, 5, 10, 8, 1], [3, 5, 8, 9, 6, 2, 1, 7, 4, 0, 10, 3], [5, 3, 1, 4, 9, 10, 0, 7, 8, 2, 6, 5], [6, 0, 10, 7, 8, 3, 5, 4, 1, 2, 9, 6], [7, 0, 10, 4, 1, 3, 8, 6, 2, 5, 9, 7], [7, 2, 10, 8, 4, 9, 6, 0, 3, 5, 1, 7], [3, 2, 0, 1, 7, 5, 9, 8, 4, 6, 10, 3], [5, 3, 9, 6, 4, 2, 8, 1, 7, 0, 10, 5], [3, 7, 6, 9, 2, 4, 10, 1, 5, 0, 8, 3], [4, 3, 2, 10, 7, 9, 6, 0, 8, 5, 1, 4], [6, 1, 5, 0, 4, 2, 7, 9, 8, 10, 3, 6], [4, 3, 5, 7, 2, 8, 1, 9, 0, 6, 10, 4], [0, 4, 2, 5, 8, 9, 1, 10, 6, 3, 7, 0], [6, 0, 8, 5, 2, 1, 7, 9, 4, 10, 3, 6], [10, 2, 9, 0, 4, 5, 6, 8, 1, 3, 7, 10], [0, 10, 1, 4, 6, 8, 2, 9, 3, 7, 5, 0], [8, 6, 4, 1, 10, 7, 3, 5, 0, 2, 9, 8], [3, 2, 9, 7, 0, 10, 1, 5, 4, 6, 8, 3], [8, 3, 4, 2, 6, 10, 9, 0, 7, 1, 5, 8], [5, 2, 10, 9, 7, 8, 0, 6, 4, 3, 1, 5], [8, 2, 5, 1, 9, 6, 3, 10, 7, 4, 0, 8], [1, 4, 7, 9, 3, 0, 10, 6, 8, 2, 5, 1], [2, 3, 1, 7, 10, 0, 5, 6, 8, 9, 4, 2], [6, 0, 3, 1, 10, 4, 9, 7, 2, 8, 5, 6], [0, 5, 8, 6, 3, 7, 4, 10, 1, 2, 9, 0], [1, 10, 5, 0, 6, 4, 3, 7, 9, 8, 2, 1], [9, 8, 10, 2, 3, 6, 7, 4, 5, 0, 1, 9], [7, 0, 9, 8, 1, 3, 4, 6, 10, 5, 2, 7], [10, 6, 7, 9, 1, 0, 5, 4, 8, 3, 2, 10], [0, 7, 9, 1, 5, 8, 10, 6, 4, 3, 2, 0], [7, 0, 10, 2, 9, 1, 8, 5, 4, 6, 3, 7], [0, 2, 6, 9, 8, 3, 10, 7, 1, 5, 4, 0], [5, 6, 9, 1, 8, 10, 3, 2, 0, 4, 7, 5], [5, 4, 7, 6, 8, 10, 3, 0, 9, 1, 2, 5], [10, 0, 7, 2, 6, 3, 8, 4, 5, 1, 9, 10], [7, 4, 10, 6, 3, 8, 5, 2, 1, 0, 9, 7], [10, 0, 1, 5, 4, 6, 7, 3, 2, 9, 8, 10], [6, 3, 5, 10, 4, 7, 0, 9, 1, 2, 8, 6], [4, 2, 6, 0, 5, 3, 7, 1, 8, 9, 10, 4], [4, 7, 1, 5, 8, 2, 3, 9, 10, 6, 0, 4], [0, 6, 8, 5, 7, 9, 3, 1, 10, 4, 2, 0], [2, 4, 7, 6, 0, 10, 9, 8, 3, 5, 1, 2], [9, 10, 4, 6, 3, 2, 5, 0, 8, 1, 7, 9], [2, 8, 9, 10, 6, 3, 1, 4, 5, 0, 7, 2], [10, 4, 0, 1, 7, 9, 8, 5, 6, 3, 2, 10], [6, 7, 5, 2, 3, 10, 0, 4, 9, 1, 8, 6], [4, 6, 0, 7, 2, 1, 3, 9, 8, 5, 10, 4], [10, 3, 4, 8, 7, 9, 2, 6, 0, 1, 5, 10], [1, 9, 2, 10, 3, 7, 5, 4, 0, 6, 8, 1], [6, 0, 2, 9, 7, 4, 1, 5, 3, 10, 8, 6], [7, 5, 6, 2, 0, 3, 10, 9, 8, 1, 4, 7], [9, 3, 1, 4, 0, 6, 7, 2, 10, 5, 8, 9], [7, 0, 5, 2, 3, 10, 9, 6, 4, 1, 8, 7], [3, 8, 5, 1, 7, 6, 4, 9, 2, 0, 10, 3], [3, 0, 6, 9, 7, 5, 2, 8, 10, 4, 1, 3], [6, 0, 9, 8, 2, 4, 10, 7, 3, 1, 5, 6], [5, 1, 4, 6, 7, 8, 2, 9, 10, 3, 0, 5]]
new_population=[[9, 2, 10, 6, 1, 5, 4, 8, 7, 0, 3, 9], [1, 6, 7, 4, 3, 8, 10, 2, 9, 0, 5, 1], [3, 6, 1, 7, 10, 8, 2, 4, 5, 0, 9, 3], [5, 0, 8, 2, 10, 7, 1, 6, 4, 3, 9, 5], [10, 0, 2, 6, 1, 4, 8, 9, 3, 5, 7, 10], [6, 9, 4, 2, 8, 0, 1, 10, 7, 5, 3, 6], [8, 1, 7, 3, 5, 4, 2, 6, 10, 9, 0, 8], [7, 2, 6, 5, 3, 4, 8, 1, 10, 9, 0, 7], [4, 10, 6, 2, 9, 7, 8, 0, 1, 3, 5, 4], [4, 10, 2, 9, 1, 6, 7, 5, 3, 8, 0, 4], [9, 1, 3, 10, 2, 0, 8, 4, 7, 6, 5, 9], [1, 10, 2, 6, 4, 3, 5, 8, 9, 0, 7, 1], [10, 2, 9, 1, 7, 3, 4, 8, 0, 5, 6, 10], [8, 3, 5, 4, 6, 1, 0, 10, 9, 2, 7, 8], [8, 2, 7, 6, 5, 3, 4, 0, 10, 1, 9, 8], [5, 9, 8, 0, 7, 1, 4, 6, 2, 3, 10, 5], [8, 5, 3, 7, 10, 6, 9, 4, 0, 1, 2, 8], [8, 1, 2, 5, 6, 9, 7, 3, 4, 0, 10, 8], [0, 8, 9, 3, 1, 4, 10, 6, 2, 5, 7, 0], [1, 6, 2, 5, 7, 0, 10, 3, 4, 8, 9, 1], [10, 8, 0, 9, 1, 5, 3, 2, 6, 4, 7, 10], [5, 9, 10, 1, 0, 6, 8, 3, 7, 2, 4, 5], [5, 4, 1, 10, 0, 9, 6, 7, 8, 2, 3, 5], [5, 4, 2, 0, 10, 7, 3, 6, 8, 1, 9, 5], [8, 4, 3, 5, 10, 6, 7, 1, 9, 2, 0, 8], [5, 8, 3, 9, 10, 0, 4, 1, 6, 2, 7, 5], [3, 6, 2, 4, 1, 8, 7, 5, 9, 0, 10, 3], [3, 4, 10, 5, 9, 8, 7, 1, 0, 6, 2, 3], [3, 6, 8, 0, 9, 7, 10, 1, 5, 4, 2, 3], [4, 1, 2, 7, 5, 8, 0, 9, 3, 10, 6, 4], [5, 2, 10, 3, 6, 1, 0, 9, 4, 7, 8, 5], [9, 10, 7, 0, 4, 8, 6, 1, 5, 2, 3, 9], [1, 3, 9, 4, 8, 6, 10, 2, 5, 0, 7, 1], [1, 2, 6, 9, 0, 4, 3, 7, 5, 10, 8, 1], [3, 5, 8, 9, 6, 2, 1, 7, 4, 0, 10, 3], [5, 3, 1, 4, 9, 10, 0, 7, 8, 2, 6, 5], [6, 0, 10, 7, 8, 3, 5, 4, 1, 2, 9, 6], [7, 0, 10, 4, 1, 3, 8, 6, 2, 5, 9, 7], [7, 2, 10, 8, 4, 9, 6, 0, 3, 5, 1, 7], [3, 2, 0, 1, 7, 5, 9, 8, 4, 6, 10, 3], [5, 3, 9, 6, 4, 2, 8, 1, 7, 0, 10, 5], [3, 7, 6, 9, 2, 4, 10, 1, 5, 0, 8, 3], [4, 3, 2, 10, 7, 9, 6, 0, 8, 5, 1, 4], [6, 1, 5, 0, 4, 2, 7, 9, 8, 10, 3, 6], [4, 3, 5, 7, 2, 8, 1, 9, 0, 6, 10, 4], [0, 4, 2, 5, 8, 9, 1, 10, 6, 3, 7, 0], [6, 0, 8, 5, 2, 1, 7, 9, 4, 10, 3, 6], [10, 2, 9, 0, 4, 5, 6, 8, 1, 3, 7, 10], [0, 10, 1, 4, 6, 8, 2, 9, 3, 7, 5, 0], [8, 6, 4, 1, 10, 7, 3, 5, 0, 2, 9, 8], [3, 2, 9, 7, 0, 10, 1, 5, 4, 6, 8, 3], [8, 3, 4, 2, 6, 10, 9, 0, 7, 1, 5, 8], [5, 2, 10, 9, 7, 8, 0, 6, 4, 3, 1, 5], [8, 2, 5, 1, 9, 6, 3, 10, 7, 4, 0, 8], [1, 4, 7, 9, 3, 0, 10, 6, 8, 2, 5, 1], [2, 3, 1, 7, 10, 0, 5, 6, 8, 9, 4, 2], [6, 0, 3, 1, 10, 4, 9, 7, 2, 8, 5, 6], [0, 5, 8, 6, 3, 7, 4, 10, 1, 2, 9, 0], [1, 10, 5, 0, 6, 4, 3, 7, 9, 8, 2, 1], [9, 8, 10, 2, 3, 6, 7, 4, 5, 0, 1, 9], [7, 0, 9, 8, 1, 3, 4, 6, 10, 5, 2, 7], [10, 6, 7, 9, 1, 0, 5, 4, 8, 3, 2, 10], [0, 7, 9, 1, 5, 8, 10, 6, 4, 3, 2, 0], [7, 0, 10, 2, 9, 1, 8, 5, 4, 6, 3, 7], [0, 2, 6, 9, 8, 3, 10, 7, 1, 5, 4, 0], [5, 6, 9, 1, 8, 10, 3, 2, 0, 4, 7, 5], [5, 4, 7, 6, 8, 10, 3, 0, 9, 1, 2, 5], [10, 0, 7, 2, 6, 3, 8, 4, 5, 1, 9, 10], [7, 4, 10, 6, 3, 8, 5, 2, 1, 0, 9, 7], [10, 0, 1, 5, 4, 6, 7, 3, 2, 9, 8, 10], [6, 3, 5, 10, 4, 7, 0, 9, 1, 2, 8, 6], [4, 2, 6, 0, 5, 3, 7, 1, 8, 9, 10, 4], [4, 7, 1, 5, 8, 2, 3, 9, 10, 6, 0, 4], [0, 6, 8, 5, 7, 9, 3, 1, 10, 4, 2, 0], [2, 4, 7, 6, 0, 10, 9, 8, 3, 5, 1, 2], [9, 10, 4, 6, 3, 2, 5, 0, 8, 1, 7, 9], [2, 8, 9, 10, 6, 3, 1, 4, 5, 0, 7, 2], [10, 4, 0, 1, 7, 9, 8, 5, 6, 3, 2, 10], [6, 7, 5, 2, 3, 10, 0, 4, 9, 1, 8, 6], [4, 6, 0, 7, 2, 1, 3, 9, 8, 5, 10, 4], [10, 3, 4, 8, 7, 9, 2, 6, 0, 1, 5, 10], [1, 9, 2, 10, 3, 7, 5, 4, 0, 6, 8, 1], [6, 0, 2, 9, 7, 4, 1, 5, 3, 10, 8, 6], [7, 5, 6, 2, 0, 3, 10, 9, 8, 1, 4, 7], [9, 3, 1, 4, 0, 6, 7, 2, 10, 5, 8, 9], [7, 0, 5, 2, 3, 10, 9, 6, 4, 1, 8, 7], [3, 8, 5, 1, 7, 6, 4, 9, 2, 0, 10, 3], [3, 0, 6, 9, 7, 5, 2, 8, 10, 4, 1, 3], [6, 0, 9, 8, 2, 4, 10, 7, 3, 1, 5, 6], [5, 1, 4, 6, 7, 8, 2, 9, 10, 3, 0, 5]]
less_cost=[]
random_num_index = []

for i in range(0,90):
    random_num_index.append(random.uniform(0, 1))
print(non_elite_pop,"non elit pop old")
lesscost=[]

def mutation(non_elite_pop,new_population):

    for j in range(0, len(random_num_index)):

        if (random_num_index[j] < 0.85):
            ex_child = non_elite_pop[j]
            #print("EX  child", ex_child)
            #print('cost ex child', cost(ex_child))
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            temp = non_elite_pop[j][x]
            non_elite_pop[j][x] = non_elite_pop[j][y]
            non_elite_pop[j][y] = temp
            new_child = non_elite_pop[j]
            #print("new child", new_child)
            #print('cost new child', cost(new_child))
            #print("--------------------")
            if cost(non_elite_pop[j]) < cost(new_population[j]):
                lesscost.append(non_elite_pop[j])
                new_population[j] = non_elite_pop[j]
    return new_population
mutation(non_elite_pop,new_population)

print("----------------------------------")
#print(random_num_index)
print("non elit ",non_elite_pop)
print("new pop  ",new_population)
#print("less cost",lesscost)

cost_new_pop=[]
non_elite_cost=[]
for i in range(0,len(new_population)):
    cost_new_pop.append(cost(new_population[i]))
for i in range(0,len(non_elite_pop)):
    non_elite_cost.append(cost(non_elite_pop[i]))

print("cost before mutation:",non_elite_cost)
print("cost after mutation :",cost_new_pop)
#print(sorted(cost_new_pop))

dict_mut= {str(k): v for k, v in zip(new_population, cost_new_pop)}

#print(dict_mut)

dict_sorted=dict(sorted(dict_mut.items(), key=lambda item: item[1]))
print(dict_sorted)
print("----------------")
print("Optimum path after mutation")
print(list(dict_sorted)[0])
print("cost of path")
print(list(dict_sorted.values())[0] )
