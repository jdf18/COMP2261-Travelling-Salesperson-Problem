# Travelling Salesperson Problem

Coursework for COMP2261 - AI Search

## Algorithm notes

### Genetic Algorithm

```python
def genetic_algorithm():
  pop = generate_pop(pop_size)
  while not terminated:
    newPop = []
    for i in range(len(population)):
      x, y = choose_from_pop(pop)
      z = reproduce(x, y)
      if rand() < p:
        mutate(z)
      newPop.append(z)
    pop.extend(newPop)
    pop = pop[:-pop_size]
```

Child reproduction is done via crossover:
 - Split the parents in two and create two children
 - Fix any duplicate cities

Mutation can be done by swapping a pair of cities

Other crossover algorithms to look at from "Genetic Algorithms for the Travelling Salesman Problem":
 - Partially-mapped crossover (PMX)
 - Cycle crossover (CX)
Mutation:
 - Displacement Mutation (DM)
 - Exchange Mutation (EM) classic

