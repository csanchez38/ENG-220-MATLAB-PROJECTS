import streamlit as st
import pandas as pd

# Title of the app
st.title('Student Academic Dashboard')

# Pre-loaded dataset with more meaningful and realistic data
data = {
    'Major': ['Electrical Engineering', 'Mechanical Engineering', 'History', 'Physics', 'Computer Science'],
    'Years Attended': ['1 year', '2 years', '3 years', '4 years', '2 years'],
    'Total Credit Hours Completed': [30, 60, 90, 120, 60],
    'GPA': [3.8, 3.2, 3.5, 3.9, 3.4]
}
df = pd.DataFrame(data)

# Convert 'Years Attended' to numeric for proper charting
df['Years Attended Numeric'] = df['Years Attended'].replace({
    '1 year': 1, '2 years': 2, '3 years': 3, '4 years': 4
})

# Display the clean dataset
st.write("### Student Data Overview")
st.write(df[['Major', 'Years Attended', 'Total Credit Hours Completed', 'GPA']])

# Let the user select columns for the chart (excluding the numeric column used for plotting)
columns = ['Major', 'Years Attended', 'Total Credit Hours Completed', 'GPA']

# Dropdowns for X and Y axes selection
x_axis = st.selectbox('Select column for X-axis', columns)
y_axis = st.selectbox('Select column for Y-axis', columns)

# Choose chart type: Bar Chart or Line Chart
chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])

# Handling special case where 'Years Attended' is selected for charting
if x_axis == 'Years Attended':
    x_axis = 'Years Attended Numeric'

if y_axis == 'Years Attended':
    y_axis = 'Years Attended Numeric'

# Display chart based on user selections
st.write(f"### {chart_type} of {x_axis} vs {y_axis}")

# Swap the X and Y axis for the plot
if chart_type == 'Bar Chart':
    st.bar_chart(df[[x_axis, y_axis]].set_index(y_axis))
elif chart_type == 'Line Chart':
    st.line_chart(df[[x_axis, y_axis]].set_index(y_axis))

