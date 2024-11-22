import csv, os

LEVEL = 1
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

        for _ in range(n_currencies):
            # read in the lawn
            row = next(csv_reader)
            coins = [int(x) for x in row]



    with open(os.path.join(OUTPUT_DIR, "level{}-{}.out".format(LEVEL, filename[-4])), 'w+') as f:
        for result in results:
            # f.write(result + "\n")
            print(result)
