import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('./data/data_preprocessed.csv')

sum_gross = df.gross_worldwide.sum()

sum_budget = df.budget.sum()

average_runtime = df.runtime.mean()

num_movies = df.shape[0]

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Div([
        html.Div(children=[
            html.Label('GROSS'),
            html.Br(),
            html.P(f"{sum_gross}$")
        ], style={'padding': 10,
                  'flex': 1,
                  'margin': '0 5px',
                  'background-color': '#ffffff',
                  'box-shadow': '-1px 0px 33px -1px rgba(166,166,166,1)'}),

        html.Div(children=[
            html.Label('BUDGET'),
            html.Br(),
            html.P(f"{sum_budget}$")
        ], style={'padding': 10,
                  'flex': 1,
                  'margin': '0 5px',
                  'background-color': '#ffffff',
                  'box-shadow': '-1px 0px 33px -1px rgba(166,166,166,1)'}),
        html.Div(children=[
            html.Label('AVERAGE RUNTIME'),
            html.Br(),
            html.P(f"{average_runtime} minutes")
        ], style={'padding': 10,
                  'flex': 1,
                  'margin': '0 5px',
                  'background-color': '#ffffff',
                  'box-shadow': '-1px 0px 33px -1px rgba(166,166,166,1)'}),
        html.Div(children=[
            html.Label('MOVIES'),
            html.Br(),
            html.P(num_movies)
        ], style={'padding': 10,
                  'flex': 1,
                  'margin': '0 5px',
                  'background-color': '#ffffff',
                  'box-shadow': '-1px 0px 33px -1px rgba(166,166,166,1)'}),
    ], style={'display': 'flex', 'flex-direction': 'row', 'margin': '10px 0', }),
    html.Div(children=[
        html.Div(children=[
            html.Label('Doanh thu theo năm'),
            html.Br(),
            html.P('Biểu đồ')
        ], style={'padding': 10,
                  'flex': 1.75,
                  'margin': '0 5px',
                  'background-color': '#ffffff',
                  'box-shadow': '-1px 0px 33px -1px rgba(166,166,166,1)'}),
        html.Div(children=[
            html.Label('Top phổ biến'),
            html.Br(),
            html.P('Biểu đồ')
        ], style={'padding': 10,
                  'flex': 1,
                  'margin': '0 5px',
                  'background-color': '#ffffff',
                  'box-shadow': '-1px 0px 33px -1px rgba(166,166,166,1)'})
    ], style={'display': 'flex', 'flex-direction': 'row', 'margin': '10px 0'}),
    html.Div(children=[
        html.Div(children=[
            html.Label('Top phim'),
            html.Br(),
            html.P('Biểu đồ')
        ], style={'padding': 10,
                  'flex': 1,
                  'margin': '0 5px',
                  'background-color': '#ffffff',
                  'box-shadow': '-1px 0px 33px -1px rgba(166,166,166,1)'}),
        html.Div(children=[
            html.Label('Gross vs Score'),
            html.Br(),
            html.P('Biểu đồ')
        ], style={'padding': 10,
                  'flex': 1,
                  'margin': '0 5px',
                  'background-color': '#ffffff',
                  'box-shadow': '-1px 0px 33px -1px rgba(166,166,166,1)'}),
        html.Div(children=[
            html.Label('Cat vs Gross'),
            html.Br(),
            html.P('Biểu đồ')
        ], style={'padding': 10,
                  'flex': 1,
                  'margin': '0 5px',
                  'background-color': '#ffffff',
                  'box-shadow': '-1px 0px 33px -1px rgba(166,166,166,1)'})
    ], style={'display': 'flex', 'flex-direction': 'row'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
