import streamlit as st
import pandas as pd

grades_dict = {
    'Class': [
        'Advisement', 
        'PE', 
        'Algebra', 
        'Social Studies', 
        'Honors ELA', 
        'Leadership', 
        'Science'
    ],
    'Grade': ['A', 'A', 'A', 'A', 'A', 'A', 'A'],
    'citizenship': ['S','O','O','O','O','O','O']
}

code_to_display = '''
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(0.001),
    metrics=['accuracy']
)

model.fit(x_train, y_train, batch_size=64, epochs=6, shuffle=True, verbose=2)
model.evaluate(x_test, y_test, batch_size=64, verbose=2)

predictions = tf.nn.softmax(model(x_test))
pred05 = predictions[0:5]
labels05 = np.argmax(pred05, axis=1)

print(pred05.numpy())
print(labels05)
'''

df = pd.DataFrame(grades_dict)

st.title("January and February Portfolio")
st.divider()
st.header("School Related Work")
st.divider()
st.write("This section covers all the work I have completed in these two months.")
st.divider()
st.subheader("Grades")
st.divider()
st.write("The months of January and February were good in terms of grades. I got a 4.0 gpa and 6 Os in citzenship and happiness.")
st.dataframe(df)
st.divider()
st.subheader("Tests")
st.divider()
st.write("I took a social studies and 2 math tests (major) in January and February, and I got amazing grades on those tests.")
st.image("Test.jpg", width=500)
st.divider()
st.subheader("Projects")
st.markdown("**Outsiders News Project**")
st.write("The Outsiders News Project was a documentry explaining the adventure of Johnny Cade and Ponyboy Curtuis commiting murder and hiding. The project made us use AI video generation tools and I bunch of stoyrboarding.")
st.markdown("**Renaissance Project**")
st.write("The Renaissance Project focuses on a arguementive essay about a Renaissance innovator and an artwork. I wrote about Issac Newton and his achivements and I made a drawing of a apple tree.")
st.divider()
st.header("Real World Applications and Knowledge")
st.divider()
st.subheader("Machine Learning and Coding")
st.divider()
st.markdown("**Python**")
st.write("Python is a programming language known for its automation and AI abilities. I currently have a intermidate level of knowledge of Python.")
st.write("Example")
st.code("def Adder_and_POW(a,b):\n"
"   return (a + b) ** 2\n\nAdder_and_POW(4,2)", language="python")
st.markdown("**Machine Learning**")
st.write("Machine Learning is the art of teaching models to predict based off of data. I have learned many machine learning concepts like feature engineering and neural networks. I learned my knowledge of machine learning from Google's Developer Program.")
st.image("Neural Network.jpg",width=1000)
st.divider()
st.header("Projects")
st.divider()
st.markdown("**Weather Predictor**")
st.write("I developed a neural network that used three features: Temp, Pressure, and Condition. It predicted next hour's temp, and it had a margin of error of about 1.11C.")
st.markdown("**Number Recognizer**")
st.write("I developed a neural network that trainied on a dataset of images of numbers to guess the number.")
st.code(code_to_display,language="python")
st.divider()

with st.form("weather_form"):
    st.header("Weather Model")
    t = st.slider("Temp (C)", -10, 50, 20)
    p = st.slider("Pressure", 800, 1500, 1013)
    c = st.radio("Condition", ["Sunny", "Cloudy", "Rainy"])
    if st.form_submit_button("Predict"):
        st.balloons()
        st.subheader("Too lazy to import model")
        