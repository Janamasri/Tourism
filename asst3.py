import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv("tourism.csv")

# Title for the dashboard
st.title("Tourism Insights Across Lebanese Governorates")

# Sidebar for filtering and dataset display
st.sidebar.title("Navigation")
tab = st.sidebar.radio("Select Tab", ["Filter by Governorate", "View Dataset"])

# If the 'Filter by Governorate' tab is selected
if tab == "Filter by Governorate":
    # Filter by governorate
    governorates = df['refArea'].unique()
    selected_governorate = st.sidebar.selectbox('Choose a Governorate', governorates)

    # Filter the dataset by selected governorate
    filtered_df = df[df['refArea'] == selected_governorate]

    # Group data by 'refArea' and sum 'Total number of restaurants'
    df_grouped = filtered_df.groupby('refArea')['Total number of restaurants'].sum().reset_index()

    # Plot a bar chart with Plotly
    fig = px.bar(df_grouped, x='refArea', y='Total number of restaurants',
                 title='Total Number of Restaurants by Governorate',
                 color='Total number of restaurants',
                 color_continuous_scale='Bluered')

    st.plotly_chart(fig)

    # Scatter plot of restaurants vs cafes
    fig2 = px.scatter(filtered_df, x='Total number of restaurants', y='Total number of cafes',
                     color='refArea', title='Total Number of Restaurants vs Cafes by Governorate',
                     color_continuous_scale='Viridis')

    st.plotly_chart(fig2)

# If the 'View Dataset' tab is selected
elif tab == "View Dataset":
    st.write("Dataset:")
    st.dataframe(df)