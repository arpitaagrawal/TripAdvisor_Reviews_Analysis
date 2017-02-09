import utils
import math
import sys
import json
import tokenise_data
import numpy as np
import read_data

dir = '/Users/arpita/Documents/Personal_project/Trip_advisor_data/json-2'
model_filename = dir + "/nbmodel.txt"
hotel_reviews_test_data = []

#test_label_data_filename = "data/new-test-labels.txt"
test_text_filename = sys.argv[1]
test_label_data = []
unique_identifier = []
true_test_labels = []
review_column = 2

def classify_data():
    read_test_data()
    global hotel_reviews_test_data
    global model_filename
    global true_test_labels
    
    with open(model_filename) as inputfile:
        data_dictionary = json.load(inputfile)
    ## For each Class, look at each label, calculate the probability for each label, and calculate max nd give it a label
    label_arr = get_labels_for_class(data_dictionary['class_prior_probability'], data_dictionary['labels_index_dict'], data_dictionary['word_dict'], data_dictionary['wordwiseprob_eachclass'], data_dictionary['unique_labels_each_class_dict'])
    correct_labels(label_arr, true_test_labels)
    write_labels_outputfile(label_arr)
    
    
def correct_labels(label_arr, test_label_data):
    
    num_rows = len(test_label_data)
    correct_count = 0
    for i in range(0,num_rows):
        if label_arr[i][1] == test_label_data[i] :
            correct_count += 1
    print correct_count
     
def get_labels_for_class(class_prior_probability, labels_index_dict, word_dict, wordwiseprob_eachclass, unique_labels_each_class_dict):
    global hotel_reviews_test_data
    
    label_arr = utils.initialise_new_arr(len(unique_labels_each_class_dict) + 1, len(hotel_reviews_test_data), "str")
    
    index = 0
    for review in hotel_reviews_test_data:
        label_arr[index][0] = review[0]
        index += 1
        
    class_count = 1
    classes_list = []
    for key in unique_labels_each_class_dict.keys(): classes_list.append(key)
    classes_list.sort()
    
    for classes in classes_list:
        unique_label_set = unique_labels_each_class_dict[classes]
        review_count = 0
        for review in hotel_reviews_test_data:
            test_bow = tokenise_data.tokenise_data([review], ["space_tokenization"])
            test_bow = test_bow[0]
            ## Max probability between lets say positive & negative
            max_prob = -999999
            max_prob_label = ""
            ## unique_label_set : Set of labels in each class: review type: Set (Positive, negative)
            for label in unique_label_set:
                # final_prob is the combined probability for label say positive
                final_prob = 1
                for word in test_bow:
                    if word in word_dict.keys():
                        word_index = word_dict[word]
                        label_index = labels_index_dict[label]
                        final_prob = final_prob + math.log(wordwiseprob_eachclass[label_index][word_index])
                final_prob = final_prob + math.log(class_prior_probability[label_index])

                if final_prob>max_prob:
                    max_prob = final_prob
                    max_prob_label = label
            label_arr[review_count][class_count] = max_prob_label
            review_count += 1
        class_count += 1
    
    #print label_arr[0:10]   
    return label_arr
   
def read_test_data():
    
    global test_text_filename
    global hotel_reviews_test_data
    global review_column
    global true_test_labels
    test_data = []
    with open(test_text_filename) as data_file:
        test_data = json.load(data_file)
    complete_data = np.array(read_data.parseData(test_data))
    hotel_reviews_test_data = complete_data[:, [0,2]]
    true_test_labels = complete_data[:,-1]
    return hotel_reviews_test_data

def write_labels_outputfile(labels_arr):
    with open("nboutput.txt", "w") as outputfile:
        for item in labels_arr:
            outputfile.write(" ".join(item))
            outputfile.write("\n")

classify_data()