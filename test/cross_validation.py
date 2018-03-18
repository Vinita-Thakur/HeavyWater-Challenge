import csv

import test_results
import calculate_accuracy
import inverted_indexing

total_rows = 61159
percentage_test = float(10)
ranges = []
start = 0
per_set_rows = int((percentage_test/100) * float(total_rows)) - 1
accuracy_file = open("CV_Accuracy.csv", "wb")
ac_file_writer = csv.writer(accuracy_file, delimiter=",")

for i in range(start + per_set_rows, total_rows, per_set_rows):
    ranges.append((start, i))
    start += per_set_rows + 1

interval_no = 1
for interval in ranges:
    test_results.generate_output_set_cross_validation(interval[0], interval[1])
    inverted_index = inverted_indexing.create_inverted_index()
    test_results.generate_test_results(inverted_index)
    accuracy = calculate_accuracy.calculate_accuracy("test_actual_last.csv")
    ac_file_writer.writerow(["Set "+str(interval_no), accuracy])
    interval_no += 1

accuracy_file.close()