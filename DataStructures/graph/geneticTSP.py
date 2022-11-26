from random import random, choice, choices


def mutate(sol: list, p: float, evaluate: function):
    if random() < p:
        new_sol = sol.copy()
        i, j = choices(range(len(sol)), 2)
        new_sol[i], new_sol[j] = new_sol[j], new_sol[i]
    if evaluate(sol) < evaluate(new_sol):
        return new_sol
    else:
        return sol


def coss(sol1: list, sol2: list, nb_children: int, evaluate: function):
    def correct_child(child: list, correction_items: list):
        corrected_child = []
        for item in child:
            if item in corrected_child:
                corrected_child.append(correction_items.pop())
            else:
                corrected_child.append(item)
        return corrected_child

    children = [sol1, sol2]
    scores = [evaluate(sol1), evaluate(sol2)]
    for _ in nb_children:
        i =  choice(range(len(sol1)))
        child1 = correct_child(sol1[:i] + sol2[i:], sol2[:i])
        child2 = correct_child(sol2[:i] + sol1[i:], sol1[:i])
        for child in [child1, child2]:
            new_score = evaluate(child)
            if new_score > scores[0] or new_score > scores[1]:
                children = [child, children[max([0, 1], key=lambda x: scores[x])]]
                scores = [new_score, max(scores)]
    
    return children
