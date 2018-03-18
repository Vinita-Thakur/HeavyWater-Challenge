import csv
from test import test_results

encode_dict = {"APPLICATION": 0,
               "BILL": 1, "BILL BINDER": 2, "BINDER": 3, "DECLARATION": 4, "DELETION OF INTEREST": 5,
               "EXPIRATION NOTICE": 6, "INTENT TO CANCEL NOTICE": 7, "NON-RENEWAL NOTICE": 8,
               "POLICY CHANGE": 9, "REINSTATEMENT NOTICE": 10, "RETURNED CHECK": 11, "CANCELLATION NOTICE": 12,
               "CHANGE ENDORSEMENT": 13}


"""This method creates an inverted index - a dictionary with key as word
and value as the list of documents in which the word occurs"""
def create_inverted_index():
    inverse_doc_freq_table = {}
    with open("output.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            hash_values = row[1:len(row)]
            for hash_val in hash_values:
                if hash_val in inverse_doc_freq_table:
                    get_list = inverse_doc_freq_table[hash_val]
                    get_list.append(encode_dict[row[0]])
                    inverse_doc_freq_table[hash_val] = get_list
                else:
                    get_list = [encode_dict[row[0]]]
                    inverse_doc_freq_table[hash_val] = get_list

    return inverse_doc_freq_table


"""This method gets the document label (along with confidence) by calculating the
frequency of words in documents. The document that gets majority of word matches
is returned"""
def get_doc_label(inverted_index, doc_data):
    uniqueness = set()
    max_count = 0
    most_likely_label = "Unknown"
    intersection_list = [0] * 14
    hash_list = doc_data.split(" ")
    list_sum = 0

    for word in hash_list:
        if word not in uniqueness:
            if word in inverted_index:
                get_value = inverted_index[word]
                for value in get_value:
                    intersection_list[value] += 1.0 / len(get_value)
        uniqueness.add(word)

    for i in range(len(intersection_list)):
        list_sum += intersection_list[i]
        if intersection_list[i] > max_count:
            max_count = intersection_list[i]
            most_likely_label = test_results.reverse_encode_dict[i]

    if list_sum!=0:
        return most_likely_label, 100 * (float(max_count)/float(list_sum))
    else:
        return most_likely_label, 0
