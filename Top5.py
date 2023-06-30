import plotly.express as px
import pandas as pd

# Load the dataset
data = pd.read_csv('/kaggle/input/agus-riyanto-analyzed-data/agus_riyanto_analyzed_data.csv')

# Top 5 Popular Genres
# Popular Genres
genre_counts = data['listed_in'].str.split(', ').explode().value_counts()
top_genres = genre_counts.head(5)

fig_genres = px.bar(
    x=top_genres.index,
    y=top_genres.values,
    labels={'x': 'Genre', 'y': 'Count'},
    title='Top 5 Popular Genres'
)

# Apply a template and customize colors
fig_genres.update_layout(
    template='plotly_dark',
    xaxis={'title': 'Genre', 'title_font': {'size': 14, 'color': 'white'}},
    yaxis={'title': 'Count', 'title_font': {'size': 14, 'color': 'white'}},
    title={'font': {'size': 18, 'color': 'white'}}
)
fig_genres.update_traces(marker_color=px.colors.sequential.Blues[::-1])  # Reverse color scale

fig_genres.show()


# Top 5 Release Years
top_years = analyzed_data['release_year'].value_counts().head(5)

fig_years = px.bar(
    x=top_years.index,
    y=top_years.values,
    labels={'x': 'Release Year', 'y': 'Count'},
    title='Top 5 Release Years'
)

# Apply a template and customize colors
fig_years.update_layout(
    template='plotly_dark',
    xaxis={'title': 'Release Year', 'title_font': {'size': 14, 'color': 'white'}},
    yaxis={'title': 'Count', 'title_font': {'size': 14, 'color': 'white'}},
    title={'font': {'size': 18, 'color': 'white'}}
)
fig_years.update_traces(marker_color=px.colors.sequential.Blues[::-1])  # Reverse color scale

fig_years.show()


# Top 5 Countries
top_countries = analyzed_data['country'].value_counts().head(5)

fig_countries = px.bar(
    x=top_countries.index,
    y=top_countries.values,
    labels={'x': 'Country', 'y': 'Count'},
    title='Top 5 Countries'
)

# Apply a template and customize colors
fig_countries.update_layout(
    template='plotly_dark',
    xaxis={'title': 'Country', 'title_font': {'size': 14, 'color': 'white'}},
    yaxis={'title': 'Count', 'title_font': {'size': 14, 'color': 'white'}},
    title={'font': {'size': 18, 'color': 'white'}}
)
fig_countries.update_traces(marker_color=px.colors.sequential.Blues[::-1])  # Reverse color scale

fig_countries.show()
