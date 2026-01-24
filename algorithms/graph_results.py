import matplotlib.pyplot as plt

# Example data (replace with your GA logs)
def get_list() -> list[int]:
    obj = None
    while obj is None:
        try:
            obj = eval(input())
        except:
            obj = None
        if not type(obj) == list:
            obj = None
    return obj
        

best_fitness = get_list()
avg_fitness = get_list()
worst_fitness = get_list()

from math import log, ceil

a=1.1
if len(best_fitness) > 1000:
    def collapse(arr):
        new = []
        i = 1
        while i < len(arr):
            new.append((arr[i]))
            i = ceil(i * a)
        return new
    best_fitness = collapse(best_fitness)
    avg_fitness = collapse(avg_fitness)
    worst_fitness = collapse(worst_fitness)


generations = range(len(best_fitness))

plt.figure()
plt.plot(generations, best_fitness, label="Best Fitness")
plt.plot(generations, avg_fitness, label="Avgerage Fitness")
plt.plot(generations, worst_fitness, label="Worst Fitness")

plt.xlabel("Generation")
plt.ylabel("Fitness (or Tour Length)")
plt.title("Best and Worst Fitness per Generation")
plt.legend()
plt.grid(True)

plt.show()

