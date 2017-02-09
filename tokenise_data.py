stop_words = set(["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't",
                 "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by",
                 "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
                 "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have",
                 "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him",
                 "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
                 "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor",
                 "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours    ourselves", "out",
                 "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so",
                 "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then",
                 "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those",
                 "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
                 "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which",
                 "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd",
                 "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "Subject:"])
import re
punctuation = re.compile(r'[-.?!,":;()|0-9]')
    
def tokenise_data(data, technique_arr):

    list_bow_rewies = []
    for technique in technique_arr:
        if technique == "space_tokenization":
            list_bow_rewies = tokenise_data_based_on_space(data)
    
    return list_bow_rewies        

            
def tokenise_data_based_on_space(data):
    list_bow_rewies = []
    for review in data:
        list_bow_rewies.append(remove_stop_words(review[1].split(" ")))
    return list_bow_rewies

def remove_stop_words(review):
    updated_review = []
    for word in review:
        if word.lower() not in stop_words:
            word = punctuation.sub("", word)
            updated_review.append(word.lower())
    return updated_review