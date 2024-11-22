import csv, os
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations
from math import ceil
from typing import Union, List, Set

LEVEL = 4
INPUT_DIR = os.getcwd() + "\\input\\level{0}".format(LEVEL)
OUTPUT_DIR = os.getcwd() + "\\output\\level{0}".format(LEVEL)

def cheese_solution(coins, amounts):
    N = 2
    max_coin = max(coins)
    optimal_solutions = dict()
    for target in range(1, N*max_coin):
        temp_target = target
        # add logic here
        coins_for_target = {}
        for coin in coins[::-1]:
            if coin > temp_target:
                continue
            how_often = int(temp_target / coin)
            coins_for_target[coin] = how_often
            temp_target = temp_target - (how_often * coin)

        optimal_solutions[target] = coins_for_target

        possible_coins = [c for c in coins if c < target]

        # find better solution
        for n_sol_coin in range(len(coins_for_target)-1, 0, -1):
            for possible_solution in list(combinations_with_replacement(possible_coins, n_sol_coin)):
                if sum(possible_solution) == target:
                    optimal_solutions[target] = Counter(possible_solution)
                    break

    for amount in amounts:
        how_often = ceil((amount-N*max_coin)/max_coin)
        temp_amount = amount - how_often * max_coin
        tmp_solution = optimal_solutions[temp_amount]
        if max_coin in tmp_solution:
            tmp_solution[max_coin] += how_often
        else:
            tmp_solution[max_coin] = how_often
        # results.append(tmp_solution)
        return tmp_solution


listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(INPUT_DIR):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

def amount_coins(coin_tuples):
    return sum([coin_tuple[1] for coin_tuple in coin_tuples])

for filename in listOfFiles:
    if filename.endswith(".out"):
        continue
    print("################ File {} ####################".format(filename))
    results = []
    with open(filename, newline='') as f:
        csv_reader = csv.reader(f, delimiter=' ')

        n_currencies = int(next(csv_reader)[0])
        n_coins = int(next(csv_reader)[0])
        n_amounts = int(next(csv_reader)[0])

        for _ in range(n_currencies):
            row = next(csv_reader)
            coins = [int(x) for x in row]
            row = next(csv_reader)
            amounts = [int(x) for x in row]
            # thomas coide
            # results.append(cheese_solution(coins, amounts))
            # continue

            # lukas code
            optimal_solution = {}
            all_orders_of_coins = list(permutations(coins))
            for target in amounts:
                optimal_solution = None
                for order_of_coin in all_orders_of_coins:
                    temp_target = target
                    # add logic here
                    possible_solution = []
                    for coin in order_of_coin:

                        if coin > temp_target:
                            continue
                        # max_coin_smaller_then_target = max([c for c in coins if c <= temp_target])
                        how_often = int(temp_target / coin)
                        possible_solution += [(coin, how_often)]
                        temp_target = temp_target - (how_often * coin)
                        if temp_target == 0:
                            break
                    if optimal_solution is None or amount_coins(possible_solution) < amount_coins(optimal_solution):
                        optimal_solution = possible_solution
                results.append(optimal_solution)

    with open(os.path.join(OUTPUT_DIR, "level{}-{}.out".format(LEVEL, filename[-4])), 'w+') as f:
        for result in results:
            # print(result)
            f.write(" ".join(["{}x{}".format(b,a) for a,b in result]) + "\n")

