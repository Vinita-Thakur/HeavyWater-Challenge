import csv


"""This method generates a file called output.csv that contains
various documents along with a set of words in them"""
def generate_output_set():
    op_file = open("output.csv", "wb")
    csvriter = csv.writer(op_file, delimiter=",")
    dump_dict = {}

    with open("shuffled_clean.csv", "rb") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            hash_values = row[1].split(" ")
            retrieved_set = set()
            if row[0] in dump_dict:
                retrieved_set = dump_dict[row[0]]

            for word in hash_values:
                retrieved_set.add(word)

            dump_dict[row[0]] = retrieved_set

    for key in dump_dict:
        write_row = [key]
        write_row += list(dump_dict[key])
        csvriter.writerow(write_row)

    op_file.close()