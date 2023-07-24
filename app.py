import pickle
import streamlit as st

# Function to load the model
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Function to predict spam/ham
def predict_spam(message):
    model = load_model()
    prediction = model.predict([message])[0]
    return prediction

def main():
    st.title('Spam Classification App')
    st.write('Enter a message to classify whether it is spam or not:')

    # Input text box for user to enter the message
    message = st.text_area('Message', 'Enter your message here...')

    # Predict button
    if st.button('Predict'):
        if message.strip() == '':
            st.error('Please enter a message.')
        else:
            # Predict the message
            prediction = predict_spam(message)

            # Display the prediction
            if prediction == 1:
                st.write('The message is classified as spam.')
            else:
                st.write('The message is not spam (ham).')

if __name__ == '__main__':
    main()
