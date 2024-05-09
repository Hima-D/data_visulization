!pip install matplotlib
!pip install seaborn
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Define the list of available graph types
graph_types = ["Line", "Bar", "Scatter", "Histogram", "Pie"]

# Create a Streamlit app
st.title("Data Visualization App")

# Add a dropdown to select the graph type
graph_type = st.selectbox("Select a graph type", graph_types)

# Get the user's data
data = st.text_area("Enter your data (comma-separated)")

# Parse the data into a list of numbers
data = [float(x) for x in data.split(",")]

# Create the graph based on the selected type
if graph_type == "Line":
    plt.plot(data)
elif graph_type == "Bar":
    plt.bar(range(len(data)), data)
elif graph_type == "Scatter":
    plt.scatter(range(len(data)), data)
elif graph_type == "Histogram":
    plt.hist(data)
elif graph_type == "Pie":
    plt.pie(data)

# Display the graph on Streamlit
st.pyplot()
