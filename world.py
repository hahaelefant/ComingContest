import csv, os
from typing import Union, List, Set

LEVEL = 2
INPUT_DIR = os.getcwd() + "\\input\\level{0}".format(LEVEL)
OUTPUT_DIR = os.getcwd() + "\\output\\level{0}".format(LEVEL)


listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(INPUT_DIR):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

for filename in listOfFiles:
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
            # min amount not creatable with one coin
            results.append(min([x for x in range(1, max(coins)+2) if x not in coins]))

    with open(os.path.join(OUTPUT_DIR, "level{}-{}.out".format(LEVEL, filename[-4])), 'w+') as f:
        for result in results:
            f.write(str(result) + "\n")
            print(result)

def get_smallest_amount_not_single_coin(coins: List[int]):
    it = 1
    while True:
        if not it in coins:
            return it
        else:
            it = it + 1

