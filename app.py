import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Student Performance Analysis")

# Load the dataset
df = pd.read_csv("student_data.csv")

# Calculate total and average scores
df["total_score"] = df["math_score"] + df["science_score"] + df["english_score"]
df["average_score"] = df["total_score"] / 3

# Show the dataset
st.subheader("Student Dataset")
st.dataframe(df)

# Scatter plot: Study Hours vs Average Score
st.subheader("Study Hours vs Average Score")
fig, ax = plt.subplots()
ax.scatter(df["study_hours"], df["average_score"])
ax.set_xlabel("Study Hours")
ax.set_ylabel("Average Score")
st.pyplot(fig)

# Scatter plot: Attendance vs Average Score
st.subheader("Attendance vs Average Score")
fig, ax = plt.subplots()
ax.scatter(df["attendance"], df["average_score"])
ax.set_xlabel("Attendance")
ax.set_ylabel("Average Score")
st.pyplot(fig)

# Bar chart: Average Score by Gender
st.subheader("Average Score by Gender")
gender_avg = df.groupby("gender")["average_score"].mean()
st.bar_chart(gender_avg)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
