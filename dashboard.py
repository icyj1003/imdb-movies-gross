import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from dash.dependencies import Input, Output


def CONTAINER_STYLE(flex=1):
    return {'padding': 20,
            'flex': flex,
            'margin': '0 5px',
            'border-radius': '6px',
            'background-color': '#ffffff',
            'box-shadow': '-1px -1px 10px -1px rgba(166,166,166,1)'}


LABLE_STYLE = {}

df = pd.read_csv('./data/data_preprocessed.csv')

sum_gross = df.gross_worldwide.sum()

sum_budget = df.budget.sum()

average_runtime = df.runtime.mean()

num_movies = df.shape[0]

app = dash.Dash(__name__)

app.title = 'IMDB Movie Dashboard'

app._favicon = ("abc.ico")

server = app.server

url = '0d424d-1f4a57-315260-435a6a-546273-9c92a3-b1a6b8-c6b9cd-cec6df-d6d3f0'


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
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin': '10px 0'}),
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
                         value='A', style={'flex': 1,
                                           'appearance': 'none',
                                           'max-width': '150px',
                                           'padding-right': '20px'
                                           }
                     ),
                 ], style={'display': 'flex',
                           'flex-direction': 'row',
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
                          'justify-content': 'space-between'}),
                dcc.Graph(id='graph-2')
            ], style=CONTAINER_STYLE(1))
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin': '10px 0', 'margin-right': 15}),
        # Row 3
        html.Div(children=[
            # Graph - 3
            html.Div(children=[
                 html.Div(children=[
                     # Graph 1 Label
                     html.H3('Top phim',  style={
                         'flex': 1, 'max-width': '100%'}),

                     # Graph 1 Label
                     dcc.Dropdown(
                         id='graph-3-dropdown',
                         options=[
                            {'label': 'Ascending', 'value': 'A'},
                            {'label': 'Decending', 'value': 'D'},
                         ],
                         clearable=False,
                         value='A', style={'flex': 1,
                                           'appearance': 'none',
                                           'max-width': '150px',
                                           'padding-right': '20px'}
                     ),
                 ], style={'display': 'flex',
                           'flex-direction': 'row',
                           'justify-content': 'space-between',
                           }),
                 dcc.Graph(id='graph-3')
                 ], style=CONTAINER_STYLE(2)),
            ###############################
            html.Div(children=[
                html.H3('Chưa đặt tên'),
                dcc.Graph(id='graph-4')
            ], style=CONTAINER_STYLE(1))
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin': '10px 0', 'margin-right': 15})
    ], style={'flex': 6}),

], style={
    'display': 'flex', 'flex-direction': 'column', })


# Graph-1 callback
@ app.callback(
    Output(component_id='graph-1', component_property='figure'),
    Input(component_id='graph-1-dropdown', component_property='value')
)
def update_fig1(type):
    color_list = ['#' + item for item in url.split('-')]
    temp1 = [color_list[0] for i in range(11)]
    if type == "A":
        graph_1_data = df.groupby('release_date', as_index=False)[
            'gross_worldwide'].mean()
    else:
        graph_1_data = df.groupby('release_date', as_index=False)[
            'gross_worldwide'].sum()

    fig1 = px.area(graph_1_data, x='release_date',
                   y='gross_worldwide', color_discrete_sequence=temp1)

    fig1.update_xaxes(title_text="Year", tickmode='linear')

    fig1.update_yaxes(title_text="Gross")

    fig1.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="White", )

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
        graph_2_data = df.genres.value_counts().head(4)/df.shape[0] * 100
        values = graph_2_data.values
        values = np.append(values, 100-values.sum())
        labels = graph_2_data.index
        labels = np.append(labels, 'Others')
    elif type == 'L':
        graph_2_data = df.languages.value_counts().head(9)/df.shape[0] * 100
        values = graph_2_data.values
        values = np.append(values, 100-values.sum())
        labels = graph_2_data.index
        labels = np.append(labels, 'Others')
    elif type == 'C':
        graph_2_data = df.countries_of_origin.value_counts().head(9) / \
            df.shape[0] * 100
        values = graph_2_data.values
        values = np.append(values, 100-values.sum())
        labels = graph_2_data.index
        labels = np.append(labels, 'Others')

    labels = [label.strip(',').replace(',', ', ') for label in labels]

    fig2 = go.Figure()
    color_list = ['#' + item for item in url.split('-')]
    fig2.add_trace(go.Pie(values=values,
                   labels=labels, marker={'colors': color_list},  hole=.4))

    fig2.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(orientation="h",
                    xanchor="center",
                    x=0.5),
        paper_bgcolor="White",)

    return fig2

# Graph-3 callback


@ app.callback(
    Output(component_id='graph-3', component_property='figure'),
    Input(component_id='graph-3-dropdown', component_property='value')
)
def update_fig2(type):
    color_list = ['#' + item for item in url.split('-')]
    temp = color_list
    temp.reverse()
    if type == 'A':
        graph_3_data = df[['title', 'gross_worldwide']].sort_values(
            'gross_worldwide', ascending=False).head(10)

        graph_3_data = graph_3_data.sort_values('gross_worldwide')
    else:
        graph_3_data = df[['title', 'gross_worldwide']].sort_values(
            'gross_worldwide', ascending=True).head(10)

        # graph_3_data = graph_3_data.sort_values(
        #     'gross_worldwide', ascending=False)

    fig3 = go.Figure()
    labels = graph_3_data['title'].tolist()

    color = {labels[i]: temp[i]
             for i in range(0, len(labels))}

    for i, l, v in zip(range(0, len(labels)), labels, graph_3_data['gross_worldwide'].tolist()):
        fig3.add_trace(go.Bar(y=[l],
                              x=[v],
                              name=l,
                              marker={'color': color[l]}, orientation='h'))
    fig3.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="White",
        showlegend=False

    )
    fig3.update_xaxes(title_text="Gross")
    return fig3

# Graph-4 callback


@ app.callback(
    Output(component_id='graph-4', component_property='figure'),
    Input(component_id='graph-2-dropdown', component_property='value')
)
def update_fig2(type):
    data4 = None
    if type == 'G':
        graph_2_data = df.genres.value_counts().head(5)/df.shape[0] * 100
        labels = graph_2_data.index
        data4 = df[df['genres'].isin(labels)].groupby(
            'genres', as_index=False)['gross_worldwide'].mean()

        labels = [label.strip(',').replace(',', ', ')
                  for label in data4.genres.values.tolist()]

        values = data4['gross_worldwide'].values.tolist()

    elif type == 'L':
        graph_2_data = df.languages.value_counts().head(9)/df.shape[0] * 100
        labels = graph_2_data.index
        data4 = df[df['languages'].isin(labels)].groupby(
            'languages', as_index=False)['gross_worldwide'].mean()

        labels = [label.strip(',').replace(',', ', ')
                  for label in data4.languages.values.tolist()]

        values = data4['gross_worldwide'].values.tolist()

    elif type == 'C':
        graph_2_data = df.countries_of_origin.value_counts().head(9) / \
            df.shape[0] * 100
        labels = graph_2_data.index
        data4 = df[df['countries_of_origin'].isin(labels)].groupby(
            'countries_of_origin', as_index=False)['gross_worldwide'].mean()

        labels = [label.strip(',').replace(',', ', ')
                  for label in data4.countries_of_origin.values.tolist()]

        values = data4['gross_worldwide'].values.tolist()

    fig4 = go.Figure()

    color_list = ['#' + item for item in url.split('-')]
    color = {labels[i]: color_list[i] for i in range(0, len(labels))}

    for i, l, v in zip(range(0, len(labels)), labels, values):
        fig4.add_trace(go.Bar(x=[l],
                              y=[v],
                              name=l,
                              marker={'color': color[l]}))

    fig4.update_xaxes(showticklabels=False)

    fig4.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(orientation="h",
                    xanchor="center",
                    x=0.5),
        paper_bgcolor="White",)

    return fig4


if __name__ == '__main__':
    app.run_server(debug=True)
