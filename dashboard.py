import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output


def CONTAINER_STYLE(flex=1):
    return {'padding': 20,
            'flex': flex,
            'margin': '0 5px',
            'background-color': '#ffffff',
            'box-shadow': '-1px -1px 10px -1px rgba(166,166,166,1)'}


LABLE_STYLE = {}

df = pd.read_csv('./data/data_preprocessed.csv')

sum_gross = df.gross_worldwide.sum()

sum_budget = df.budget.sum()

average_runtime = df.runtime.mean()

num_movies = df.shape[0]

app = dash.Dash(__name__)

server = app.server

# Graph 1
fig1 = go.Figure()

graph_1_data = df.groupby('release_date', as_index=False)[
    'gross_worldwide'].sum()

fig1.add_trace(go.Bar(x=graph_1_data['release_date'],
                      y=graph_1_data['gross_worldwide']))

fig1.update_xaxes(title_text="Year", tickmode='linear')

fig1.update_yaxes(title_text="Gross")

fig1.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="White",)

# Main layout
app.layout = html.Div(children=[
    html.Div([
        html.H1('IMDB Movie Dashboard', style={
            'width': '1000',
            'padding': 10
        })
    ], style={
        'flex': 1
    }),
    html.Div(children=[
        # Row 1
        html.Div([
            html.Div(children=[
                html.H3('GROSS'),
                html.P(f"{sum_gross}$")
            ], style=CONTAINER_STYLE()),

            html.Div(children=[
                html.H3('BUDGET'),
                html.P(f"{sum_budget}$")
            ], style=CONTAINER_STYLE()),
            html.Div(children=[
                html.H3('AVERAGE RUNTIME'),
                html.P(f"{average_runtime} minutes")
            ], style=CONTAINER_STYLE()),
            html.Div(children=[
                html.H3('MOVIES'),
                html.P(num_movies)
            ], style=CONTAINER_STYLE()),
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin': '10px 0', }),
        # Row 2
        html.Div(children=[
            # Graph 1
            html.Div(children=[
                 html.Div(children=[
                     # Graph 1 Label
                     html.H3('Doanh thu theo năm',  style={
                         'flex': 1, 'max-width': '100%'}),

                     # Graph 1 Label
                     dcc.Dropdown(
                         id='graph-1-dropdown',
                         options=[
                            {'label': 'Sum', 'value': 'S'},
                            {'label': 'Average', 'value': 'A'},
                         ],
                         clearable=False,
                         value='S', style={'flex': 1,
                                           'appearance': 'none',
                                           'max-width': '150px',
                                           'padding-right': '20px'}
                     ),
                 ], style={'display': 'flex',
                           'flex-direction': 'row',
                           'column-gap': '20px',
                           'justify-content': 'space-between'}),
                 dcc.Graph(id='graph-1')
                 ], style=CONTAINER_STYLE(2)),
            # Graph 2
            html.Div(children=[
                html.Div(children=[
                    # Graph 2 Label
                    html.H3('Top phổ biến',  style={
                        'flex': 1, 'max-width': '100%'}),

                    # Graph 2 Label
                    dcc.Dropdown(
                        id='graph-2-dropdown',
                        options=[
                            {'label': 'Genres', 'value': 'G'},
                            {'label': 'Languages', 'value': 'L'},
                            {'label': 'Country', 'value': 'C'},
                        ],
                        clearable=False,
                        value='G', style={'flex': 1,
                                          'appearance': 'none',
                                          'max-width': '130px',
                                          'padding-right': '20px'}
                    ),
                ], style={'display': 'flex',
                          'flex-direction': 'row',
                          'column-gap': '20px',
                          'justify-content': 'space-between'}),
                dcc.Graph(id='graph-2')
            ], style=CONTAINER_STYLE(1))
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin': '10px 0'}),
        # Row 3
        html.Div(children=[
            html.Div(children=[
                html.H3('Top phim'),
                html.Br(),
                html.P('Biểu đồ')
            ], style=CONTAINER_STYLE()),
            html.Div(children=[
                html.H3('Gross vs Score'),
                html.Br(),
                html.P('Biểu đồ')
            ], style=CONTAINER_STYLE()),
            html.Div(children=[
                html.H3('Cat vs Gross'),
                html.Br(),
                html.P('Biểu đồ')
            ], style=CONTAINER_STYLE())
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin': '10px 0'})
    ], style={'flex': 6}),

], style={
    'display': 'flex', 'flex-direction': 'column'})


# Graph-1 callback
@ app.callback(
    Output(component_id='graph-1', component_property='figure'),
    Input(component_id='graph-1-dropdown', component_property='value')
)
def update_fig1(type):
    if type == "A":
        graph_1_data = df.groupby('release_date', as_index=False)[
            'gross_worldwide'].mean()
    else:
        graph_1_data = df.groupby('release_date', as_index=False)[
            'gross_worldwide'].sum()
    fig1 = go.Figure()

    fig1.add_trace(go.Bar(x=graph_1_data['release_date'],
                          y=graph_1_data['gross_worldwide']))

    fig1.update_xaxes(title_text="Year", tickmode='linear')

    fig1.update_yaxes(title_text="Gross")

    fig1.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="White",)

    return fig1


# Graph-2 callback
@ app.callback(
    Output(component_id='graph-2', component_property='figure'),
    Input(component_id='graph-2-dropdown', component_property='value')
)
def update_fig2(type):
    values = []
    labels = []
    if type == 'G':
        graph_2_data = df.genres.value_counts().head(5)/df.shape[0] * 100
        values = graph_2_data.values
        values = np.append(values, 100-values.sum())
        labels = graph_2_data.index
        labels = np.append(labels, 'Other')
    elif type == 'L':
        graph_2_data = df.languages.value_counts().head(9)/df.shape[0] * 100
        values = graph_2_data.values
        values = np.append(values, 100-values.sum())
        labels = graph_2_data.index
        labels = np.append(labels, 'Other')
    elif type == 'C':
        graph_2_data = df.countries_of_origin.value_counts().head(10) / \
            df.shape[0] * 100
        values = graph_2_data.values
        values = np.append(values, 100-values.sum())
        labels = graph_2_data.index
        labels = np.append(labels, 'Other')

    fig2 = go.Figure()

    fig2.add_trace(go.Pie(values=values,
                   labels=labels))

    fig2.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(orientation="h",
                    xanchor="center",
                    x=0.5),
        paper_bgcolor="White",)

    return fig2


if __name__ == '__main__':
    app.run_server(debug=True)
