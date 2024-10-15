import streamlit as st
import pandas as pd

# Title of the app
st.title('Student Data')

# Pre-loaded dataset for sales information
data = {
    'Major': ['Electrical', 'Mechanical', 'History', 'Physics'],
    'Years Attended': ['>1', '1-3', '3-5', '5+'],
    'Total Credit Hours Required': [150, 155, 120, 150]
}
df = pd.DataFrame(data)

# Convert 'Years Attended' to numeric for better plotting
df['Years Attended'] = df['Years Attended'].replace({
    '>1': 1, '1-3': 2, '3-5': 4, '5+': 6
})

# Display the dataset
st.write("Student Data:")
st.write(df)

# Let the user select columns for the chart
columns = df.columns.tolist()

# Dropdowns for X and Y axes selection
x_axis = st.selectbox('Select column for X-axis', columns)
y_axis = st.selectbox('Select column for Y-axis', columns)

# Choose chart type: Bar Chart or Line Chart
chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])

# Display chart based on user selections
if chart_type == 'Bar Chart':
    st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))
elif chart_type == 'Line Chart':
    st.line_chart(df[[x_axis, y_axis]].set_index(x_axis))
