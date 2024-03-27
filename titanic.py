import pandas as pd
import plotly.express as px
import streamlit as st

# Read the CSV file
df = pd.read_csv("C:\\datasets\\CSV\\titanic.csv")


def page_overview():
    st.title("Page 1:Titanic Data")
    st.header("Welcome to the Dashboard")
    st.write(df)


def page_chart():
    st.title("Page 2: Visualization")
    st.header("Count Of Passengers")
    count_by_sex = df["Sex"].value_counts()
    fig_bar = px.bar(x=count_by_sex.index, y=count_by_sex, labels={'x': "Sex", 'y': "Count"},
                     title="Count of the passenger by Sex", color=count_by_sex.index)
    st.plotly_chart(fig_bar)


def hist_pie():
    st.title("Page 3: Histogram and Pie Chart")
    st.header("Distribution of Ages")
    fig_hist = px.histogram(df, x="Age", title="Age Distribution", color_discrete_sequence=['indianred'])
    st.plotly_chart(fig_hist)

    st.header("Distribution of Passenger Classes")
    class_count = df['Pclass'].value_counts()
    fig_pie = px.pie(values=class_count.values, names=class_count.index, title="Passenger Class Distribution",
                     color=class_count.index)
    st.plotly_chart(fig_pie)


def page_map_scatter():
    st.title("Page 4: Map and Scatter Plot")

    st.header("Map")
    st.write("This map shows the embarkation points of passengers.")

    # Set color based on Embarked column
    fig_map = px.scatter_geo(df, lat='Embarked', lon='Embarked', color='Embarked', title='Passenger Embarkation Points')

    # Update color scale and legend title
    fig_map.update_traces(marker=dict(size=12), selector=dict(mode='markers'))
    fig_map.update_layout(coloraxis_colorbar=dict(title="Embarked"))

    st.plotly_chart(fig_map)

    st.header("Relation Between Age and Fare.")
    fig_scatter = px.scatter(df, x='Age', y="Fare", title="Age vs Fare")
    st.plotly_chart(fig_scatter)


def main():
    pages = {
        "Page 1: Text and Table": page_overview,
        "Page 2: Visualization": page_chart,
        "Page 3: Histogram and Pie Chart": hist_pie,
        "Page 4: Map and Scatter Plot": page_map_scatter,
    }

    st.sidebar.title("Navigate")
    page_selection = st.sidebar.radio("Go to", list(pages.keys()))
    pages[page_selection]()


if __name__ == "__main__":
    main()
