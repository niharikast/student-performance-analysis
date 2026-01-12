# Student Performance Analysis

## Overview
This project analyzes student academic performance based on **study hours, attendance, and gender**.  
It includes **interactive visualizations** and a **Streamlit web app** to explore the data dynamically.

## Features
- Calculate **total score** and **average score** from individual subjects
- Visualize performance trends:
  - Scatter plots: Study Hours vs Average Score, Attendance vs Average Score
  - Bar chart: Average Score by Gender
  - Correlation heatmap
  - Pair plots for numeric features
  - Boxplots to show distributions and outliers
- **Interactive Streamlit app** for recruiters or users to explore the dataset
- Generate insights from data to understand what affects student performance

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

## Dataset
Includes 10 students with the following fields:
- `gender`
- `study_hours`
- `attendance`
- `math_score`
- `science_score`
- `english_score`

## Key Insights
- Students who study more than **3 hours/day** tend to score higher.
- **Attendance above 80%** strongly correlates with better performance.
- Gender alone does not significantly affect performance.
- Students with low study hours and low attendance perform the worst.

## How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/niharikast/student-performance-analysis.git
