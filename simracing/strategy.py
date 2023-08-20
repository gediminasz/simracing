import pygad


def predict_strategy(model, race_parameters):
    def _fitness_function(ga_instance, solution, solution_idx):
        stints = _partition_stints(solution)
        return -model.evaluate(stints)  # negate because solution is being maximized

    available_compounds = [c.value for c in race_parameters.available_compounds]

    ga_instance = pygad.GA(
        fitness_func=_fitness_function,
        num_genes=race_parameters.lap_count,
        gene_type=int,
        gene_space=[-1, *available_compounds],
        num_generations=512,
        sol_per_pop=512,
        keep_elitism=64,
        stop_criteria="saturate_128",
        parent_selection_type="rank",
        num_parents_mating=8,
        crossover_type="two_points",
        mutation_type="scramble",
    )
    ga_instance.run()

    ga_instance.plot_fitness()
    best = ga_instance.best_solution()
    stints = _partition_stints(best[0])
    print(len(stints), stints, model.evaluate(stints))


def _partition_stints(strategy):
    stints = [[strategy[0], 1]]
    for compound in strategy[1:]:
        if compound == -1:  # no tyre change
            stints[-1][1] += 1  # one more lap in current stint
        else:
            stints.append([compound, 1])
    return stints


assert _partition_stints([1, -1, -1, -1, -1, 2, -1, -1, -1, -1]) == [[1, 5], [2, 5]]
assert _partition_stints([1, -1, -1, 1, -1, -1, 1, -1, -1]) == [[1, 3], [1, 3], [1, 3]]
assert _partition_stints([1, 2, 3]) == [[1, 1], [2, 1], [3, 1]]
assert _partition_stints([1, -1, -1]) == [[1, 3]]
