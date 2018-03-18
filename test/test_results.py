import csv

reverse_encode_dict = {0: "APPLICATION",
                       1: "BILL", 2: "BILL BINDER", 3: "BINDER", 4: "DECLARATION", 5: "DELETION OF INTEREST",
                       6: "EXPIRATION NOTICE", 7: "INTENT TO CANCEL NOTICE", 8: "NON-RENEWAL NOTICE",
                       9: "POLICY CHANGE", 10: "REINSTATEMENT NOTICE", 11: "RETURNED CHECK", 12: "CANCELLATION NOTICE",
                       13: "CHANGE ENDORSEMENT"}


"""This method is used to generate test results for a test document
Used at the time of cross validation"""
def generate_test_results(inverted_index):
    test_output_generated = open("test_actual_last.csv", "wb")
    csvwriter1 = csv.writer(test_output_generated, delimiter=",")
    with open("test_data.csv", "r") as test_file:
        test_csv_reader = csv.reader(test_file, delimiter=",")
        for row in test_csv_reader:
            uniqueness = set()
            max_count = 0
            most_likely_label = "Unknown"
            intersection_list = [0] * 14
            hash_list = row[0].split(" ")

            for word in hash_list:
                if word not in uniqueness:
                    if word in inverted_index:
                        get_value = inverted_index[word]
                        for value in get_value:
                            intersection_list[value] += 1.0/len(get_value)
                uniqueness.add(word)

            for i in range(len(intersection_list)):
                if intersection_list[i] > max_count:
                    max_count = intersection_list[i]
                    most_likely_label = reverse_encode_dict[i]

            csvwriter1.writerow([most_likely_label])

    test_output_generated.close()


"""This method generates a file called output.csv that contains
various documents along with a set of words in them. Used during cross-
validation. Separates the test data, does not include it during training"""
def generate_output_set_cross_validation(test_data_start, test_data_end):
    test_expected = open("test_expected.txt", "w")
    test_data = open("test_data.csv", "wb")
    test_data_writer = csv.writer(test_data, delimiter=",")

    op_file = open("output.csv", "wb")
    csvriter = csv.writer(op_file, delimiter=",")
    dump_dict = {}

    with open("shuffled_clean.csv", "rb") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        row_no = 0
        for row in csvreader:
            hash_values = row[1].split(" ")
            if row_no >= test_data_start and row_no <= test_data_end:
                test_data_writer.writerow([row[1]])
                test_expected.write(row[0]+"\n")
                row_no+=1
                continue
            retrieved_set = set()
            if row[0] in dump_dict:
                retrieved_set = dump_dict[row[0]]

            for word in hash_values:
                retrieved_set.add(word)

            dump_dict[row[0]] = retrieved_set
            row_no += 1

    for key in dump_dict:
        write_row = [key]
        write_row += list(dump_dict[key])
        csvriter.writerow(write_row)

    test_data.close()
    test_expected.close()
    op_file.close()