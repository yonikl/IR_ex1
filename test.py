import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download the WordNet data (only the first time)
nltk.download('wordnet')
nltk.download('punkt_tab')

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    word_list = nltk.word_tokenize(text)
    lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
    return lemmatized_output

# Example usage
text = "you're Pope don't Francis says his thoughts go to those facing wars , especially children who have ‘ forgotten how to smile ’ ."
lemmatized_text = lemmatize_text(text)
print(lemmatized_text)