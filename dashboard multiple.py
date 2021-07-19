# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd



# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

def create_dash_application(flask_app):
    # dash_app = dash.Dash(server = flask_app, name ="Dashboard", url_base_pathname='/dashboard/')

    # dash_app.layout = html.Div(children=[
    #     html.H1(children='Hello Dash'),

    #     html.Div(children='''
    #         Dash: A web application framework for Python.
    #     '''),

    #     dcc.Graph(
    #         id='example-graph',
    #         figure = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    #     )
    # ])

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    # dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets) 
    dash_app = dash.Dash(server = flask_app, name ="Dashboard", url_base_pathname='/dashboard/',external_stylesheets=external_stylesheets)
    dash_app.layout = html.Div([
    html.Div([
    html.Div([
    html.H3('Column 1'),
    dcc.Graph(id='g1', figure={'data': [{'y': [1, 2, 3]}]})
    ], className="six columns"),

        html.Div([
            html.H3('Column 2'),
            dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one-third column"),
        
        html.Div([
            html.H3('Column 3'),
            dcc.Graph(id='g3', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one-third column"),
        
    ], className="row"),
    html.Div([
        html.Div([
            html.H3('Column 1'),
            dcc.Graph(id='g4', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="three columns"),

        html.Div([
            html.H3('Column 2'),
            dcc.Graph(id='g5', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="three columns"),
        
        html.Div([
            html.H3('Column 3'),
            dcc.Graph(id='g6', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="three columns"),

        html.Div([
            html.H3('Column 4'),
            dcc.Graph(id='g7', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="three columns"),
        
    ], className="row"),
    html.Div([
        html.Div([
            html.H3('Column 1'),
            dcc.Graph(id='g8', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="two columns"),

        html.Div([
            html.H3('Column 2'),
            dcc.Graph(id='g9', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="two columns"),
        
        html.Div([
            html.H3('Column 3'),
            dcc.Graph(id='g10', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="two columns"),

        html.Div([
            html.H3('Column 4'),
            dcc.Graph(id='g11', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="two columns"),
        
        html.Div([
            html.H3('Column 5'),
            dcc.Graph(id='g12', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="two columns"),

        html.Div([
            html.H3('Column 6'),
            dcc.Graph(id='g13', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="two columns"),
    ], className="row"),
    html.Div([
        html.Div([
            html.H3('Column 1'),
            dcc.Graph(id='g14', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),

        html.Div([
            html.H3('Column 2'),
            dcc.Graph(id='g15', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),
        
        html.Div([
            html.H3('Column 3'),
            dcc.Graph(id='g16', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),

        html.Div([
            html.H3('Column 4'),
            dcc.Graph(id='g17', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),
        
        html.Div([
            html.H3('Column 5'),
            dcc.Graph(id='g18', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),

        html.Div([
            html.H3('Column 6'),
            dcc.Graph(id='g19', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),
        
        html.Div([
            html.H3('Column 7'),
            dcc.Graph(id='g20', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),

        html.Div([
            html.H3('Column 8'),
            dcc.Graph(id='g21', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),
        
        html.Div([
            html.H3('Column 9'),
            dcc.Graph(id='g22', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),

        html.Div([
            html.H3('Column 10'),
            dcc.Graph(id='g23', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),
        
        html.Div([
            html.H3('Column 11'),
            dcc.Graph(id='g24', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),

        html.Div([
            html.H3('Column 12'),
            dcc.Graph(id='g25', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="one columns"),    
    ], className="row"),
    ])
    return dash_app



# if __name__ == '__main__':
#     app.run_server(debug=True)