import streamlit as st
import os
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # removing special characters
    ans = []
    for i in text:
        if i.isalnum():
            ans.append(i)

    # removing stop words and punctuation
    text = ans[:]
    ans.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            ans.append(i)

    # stemming
    text = ans[:]
    ans.clear()
    for i in text:
        ans.append(ps.stem(i))

    return " ".join(ans)

model = pickle.load(open('model.pickle','rb'))
tfidf = pickle.load(open('vectorizer.pickle','rb'))

st.title("SMS / Email Spam Classifier")

input_sms = st.text_area("Enter Your massage")

if st.button("Predict"):
    #data preprocess
    transformed_sms = transform_text(input_sms)

    #vectorize
    vector_input = tfidf.transform([transformed_sms])

    #predict
    result = model.predict(vector_input)[0]

    #display
    if result == 1:
        st.error("Spam")
    else:
        st.success("Not Spam")

