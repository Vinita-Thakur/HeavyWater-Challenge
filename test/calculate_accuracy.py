import csv


def calculate_accuracy(filename):
    expected_list = []
    expected_file = open("test_expected.txt", "r")
    expected_results = expected_file.read()

    for result in expected_results.split("\n"):
        expected_list.append(result)

    actual_list = []
    actual_results = open(filename, "rb")
    csvreader = csv.reader(actual_results, delimiter=",")

    for row in csvreader:
        actual_list.append(row[0])

    expected_file.close()
    actual_results.close()

    no_correct = 0
    for i in range(len(actual_list)):
        if actual_list[i] == expected_list[i]:
            no_correct += 1

    accuracy = float(no_correct)/len(actual_list)

    return accuracy

