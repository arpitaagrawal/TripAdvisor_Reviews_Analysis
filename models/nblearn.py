import read_data
import tokenise_data
import NaiveBayes
import sys
import numpy as np

#hotel_reviews_train_data = read_data.read_data()


hotel_reviews_train_data = read_data.read_hotelreviews_selectivefeatures()[:, [0,2]]
train_label_data = read_data.training_data[:,-1]
bow_reviews_list = tokenise_data.tokenise_data(hotel_reviews_train_data, ["space_tokenization"])


#NaiveBayes.load_from_file()
#NaiveBayes2.create_NB_model(bow_reviews_list, hotel_reviews_train_data[:,[2,-1]])

NaiveBayes.create_NB_model(bow_reviews_list, train_label_data.reshape((len(train_label_data),1)))