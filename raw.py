#Raw Data (overall by genres,relese year,countries)

fig_genres = px.bar(
    x=analyzed_data['listed_in'].value_counts().index,
    y=analyzed_data['listed_in'].value_counts().values,
    labels={'x': 'Genre', 'y': 'Count'},
    title='Popular Genres'
)

# Apply a template and customize colors
fig_genres.update_layout(
    template='seaborn',
    xaxis={'title': 'Genre', 'title_font': {'size': 14, 'color': 'black'}},
    yaxis={'title': 'Count', 'title_font': {'size': 14, 'color': 'black'}},
    title={'font': {'size': 18, 'color': 'black'}}
)

fig_genres.show()


fig_years = px.bar(
    x=analyzed_data['release_year'].value_counts().index,
    y=analyzed_data['release_year'].value_counts().values,
    labels={'x': 'Release Year', 'y': 'Count'},
    title='Release Years'
)

# Apply a template and customize colors
fig_years.update_layout(
    template='seaborn',
    xaxis={'title': 'Release Year', 'title_font': {'size': 14, 'color': 'black'}},
    yaxis={'title': 'Count', 'title_font': {'size': 14, 'color': 'black'}},
    title={'font': {'size': 18, 'color': 'black'}}
)

fig_years.show()


fig_countries = px.bar(
    x=analyzed_data['country'].value_counts().index,
    y=analyzed_data['country'].value_counts().values,
    labels={'x': 'Country', 'y': 'Count'},
    title='Countries'
)

# Apply a template and customize colors
fig_countries.update_layout(
    template='seaborn',
    xaxis={'title': 'Country', 'title_font': {'size': 14, 'color': 'black'}},
    yaxis={'title': 'Count', 'title_font': {'size': 14, 'color': 'black'}},
    title={'font': {'size': 18, 'color': 'black'}}
)

fig_countries.show()
