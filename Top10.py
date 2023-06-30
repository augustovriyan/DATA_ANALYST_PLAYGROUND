import plotly.express as px
import pandas as pd

# Load the dataset
analyzed_data = pd.read_csv('/kaggle/input/agus-riyanto-analyzed-data/agus_riyanto_analyzed_data.csv')

fig_genres = px.pie(
    names=analyzed_data['listed_in'].value_counts().head(10).index,
    values=analyzed_data['listed_in'].value_counts().head(10).values,
    title='Top 10 Popular Genres'
)

# Apply a template and customize colors
fig_genres.update_layout(
    template='plotly_dark',
    title={'font': {'size': 18, 'color': 'white'}}
)
fig_genres.update_traces(marker=dict(colors=px.colors.sequential.Blues[::-1]))  # Reverse color scale

fig_genres.show()


fig_years = px.line(
    x=analyzed_data['release_year'].value_counts().head(10).index,
    y=analyzed_data['release_year'].value_counts().head(10).values,
    labels={'x': 'Release Year', 'y': 'Count'},
    title='Top 10 Release Years'
)

# Apply a template and customize colors
fig_years.update_layout(
    template='plotly_dark',
    xaxis={'title': 'Release Year', 'title_font': {'size': 14, 'color': 'white'}},
    yaxis={'title': 'Count', 'title_font': {'size': 14, 'color': 'white'}},
    title={'font': {'size': 18, 'color': 'white'}}
)
fig_years.update_traces(line_color='blue')

fig_years.show()


fig_countries = px.scatter(
    x=analyzed_data['country'].value_counts().head(10).index,
    y=analyzed_data['country'].value_counts().head(10).values,
    labels={'x': 'Country', 'y': 'Count'},
    title='Top 10 Countries'
)

# Apply a template and customize colors
fig_countries.update_layout(
    template='plotly_dark',
    xaxis={'title': 'Country', 'title_font': {'size': 14, 'color': 'white'}},
    yaxis={'title': 'Count', 'title_font': {'size': 14, 'color': 'white'}},
    title={'font': {'size': 18, 'color': 'white'}}
)
fig_countries.update_traces(marker_color='blue', mode='markers', marker_size=12)

fig_countries.show()
