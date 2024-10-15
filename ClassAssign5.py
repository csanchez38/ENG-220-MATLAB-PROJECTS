import streamlit as st
import pandas as pd

# Title of the app
st.title('Student Data Dashboard')

# Pre-loaded dataset with cleaner column names and structured data
data = {
    'Major': ['Electrical Engineering', 'Mechanical Engineering', 'History', 'Physics'],
    'Years Attended': ['>1 year', '1-3 years', '3-5 years', '5+ years'],
    'Total Credit Hours Required': [150, 155, 120, 150]
}
df = pd.DataFrame(data)

# Map 'Years Attended' to numerical values for better plotting
df['Years Attended Numeric'] = df['Years Attended'].replace({
    '>1 year': 1, '1-3 years': 2, '3-5 years': 4, '5+ years': 6
})

# Display the clean dataset
st.write("### Student Data Overview")
st.write(df[['Major', 'Years Attended', 'Total Credit Hours Required']])

# Let the user select columns for the chart (excluding the numeric column used for plotting)
columns = ['Major', 'Years Attended', 'Total Credit Hours Required']

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
