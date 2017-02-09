import json
import numpy as np
import glob, os

RATING_FEATURE = "Ratings"
REVIEWID_FEATURE = "ReviewID"
TITLE_FEATURE = "Title"
CONTENT_FEATURE = "Content"
LOCATION_FEATURE = "Location"

training_data = []


def read_hotelreviews_selectivefeatures():
    review_id_arr = []
    rating_arr = []
    title_arr = []
    content_arr = []
    file_directory = "/Users/arpita/Documents/Personal_project/Trip_advisor_data/json-2"
    formatted_training_data_final = []
    
    os.chdir(file_directory)
    for file in glob.glob("*.json"):
        with open(file_directory+"/"+file) as data_file:
            data = json.load(data_file)
            formatted_training_data = [len(data['Reviews'])]
            for review in data['Reviews']:
                
                if REVIEWID_FEATURE in review: review_id_arr.append(review[REVIEWID_FEATURE])
                else: review_id_arr.append(" ")
                if TITLE_FEATURE in review: title_arr.append(review[TITLE_FEATURE])
                else: title_arr.append(" ")
                if CONTENT_FEATURE in review: content_arr.append(review[CONTENT_FEATURE])
                else: content_arr.append(" ")
                if CONTENT_FEATURE in review: rating_arr.append(review[RATING_FEATURE]['Overall'])
                else: rating_arr.append(object)
            
            formatted_training_data = review_id_arr
            formatted_training_data = np.column_stack((formatted_training_data, title_arr))
            formatted_training_data = np.column_stack((formatted_training_data, content_arr))
            ## Adding labels to the rating arr: if the rating is greater than 2.5, positive review else negative review
            formatted_training_data = np.column_stack((formatted_training_data, np.where(np.array(rating_arr, dtype='f') > 2.5, 'Positive', 'Negative')))
            
            if len(formatted_training_data_final) == 0:
                formatted_training_data_final = formatted_training_data
            
        formatted_training_data_final = np.concatenate((formatted_training_data_final, formatted_training_data), axis=0)
    print "number of reviews ::", len(formatted_training_data_final)
    return formatted_training_data_final
            
training_data = read_hotelreviews_selectivefeatures()
          
            
