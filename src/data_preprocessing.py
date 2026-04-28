import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("stopwords")

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    #lowercase
    text = text.lower()

    #tokenize text
    tokens = word_tokenize(text)

    #remove stop words and short words
    tokens = [word for word in tokens if word not in stop_words and len(word) > 1]

    #lemmentization
    tokens = [lemmatizer.lemmatize(word )for word in tokens]
    
    return " ".join(tokens)

