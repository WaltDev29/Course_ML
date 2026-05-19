import random
import copy
from game import play_game

POPULATION_SIZE = 50  # 개체 집단의 크기
TOURNAMENT_SIZE = 3  # 토너먼트 선택에서 경쟁하는 개체 수
MUTATION_RATE = 0.1  # 돌연 변이 확률
SIZE = 15  # 하나의 염색체에서 유전자 개수
GENERATION = 300  # 세대 수


# 염색체를 클래스로 정의한다.
class Chromosome:
    command_list = [[1, 0], [2, 0], [0, 1], [0, 2], [1, 1]]

    def __init__(self, g=None):
        self.genes = [] if g is None else copy.deepcopy(g)  # 염색체는 리스트로 구현된다.
        self.fitness = 0  # 적합도
        if self.genes.__len__() == 0:  # 염색체가 초기 상태이면 초기화한다.
            for i in range(SIZE):
                self.genes.append(random.choice(Chromosome.command_list))

    def cal_fitness(self):  # 적합도를 계산한다.
        self.fitness = 0;
        self.fitness, self.count = play_game(copy.deepcopy(self.genes))
        return self.fitness

    def __str__(self):
        return self.genes.__str__()


# 염색체와 적합도를 출력한다.
def print_p(pop):
    i = 0
    for x in pop:
        print("염색체 #", i, "=", x, "적합도=", x.fitness, "시도 횟수=", x.count)
        i += 1
    print("")


# 선택 연산
def select(pop):
    tournament = random.sample(pop, TOURNAMENT_SIZE)
    tournament.sort(key=lambda x: x.fitness, reverse=True)
    return tournament[0]


# 교차 연산
def crossover(pop):
    father = select(pop)
    mother = select(pop)

    while mother == father:
        mother = select(pop)

    index = random.randint(1, SIZE - 1)
    child1 = father.genes[:index] + mother.genes[index:]
    child2 = mother.genes[:index] + father.genes[index:]
    return (child1, child2)


# 돌연변이 연산
def mutate(c):
    for i in range(SIZE):
        if random.random() < MUTATION_RATE:
            c.genes[i] = random.choice(Chromosome.command_list)


# 메인 프로그램
population = []

# 초기 염색체를 생성하여 객체 집단에 추가한다.
for i in range(POPULATION_SIZE):
    population.append(Chromosome())

count = 0
population.sort(key=lambda x: x.cal_fitness(), reverse=True)
print("세대 번호=", count)
print_p(population)
count = 1


for i in range(GENERATION):
    new_pop = []

    best = population[0]
    new_pop.append(best)

    # 선택과 교차 연산
    for _ in range((POPULATION_SIZE // 2) - 1):
        c1, c2 = crossover(population)
        new_pop.append(Chromosome(c1))
        new_pop.append(Chromosome(c2))

    # 자식 세대가 부모 세대를 대체한다.
    # 깊은 복사를 수행한다.
    population = new_pop.copy()

    # 돌연변이 연산
    for c in population[1:]: mutate(c)

    # 출력을 위한 정렬
    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    print("세대 번호=", count)
    print_p(population)
    count += 1