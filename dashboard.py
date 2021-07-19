# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import model_frequency 
import dash_table

frequency_df = model_frequency.frequency_sim()


# def create_dash_application(flask_app):
#     dash_app = dash.Dash(server = flask_app, name ="Dashboard",suppress_callback_exceptions=True ,url_base_pathname='/dashboard/')
#     dash_app.layout = html.Div(children=[
#         html.H1(children='Document Simalarity'),

#         html.Div(children='''
#             Correlation: Frequency based! data Correlation.
#         '''),

#         dcc.Graph(
#             id='heatmap-plot',
#             figure = px.imshow(frequency_df)
#         )
#     ])

#     return dash_app

def create_dash_application(flask_app):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    dash_app = dash.Dash(server = flask_app, name ="Dashboard",suppress_callback_exceptions=True ,url_base_pathname='/dashboard/',external_stylesheets=external_stylesheets)
    data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
    df = pd.read_csv(data_url)
    dash_app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3('Document Simalarity Heatmap',style={'align': 'center'}),
            dcc.Graph(id='g1', figure = px.imshow(frequency_df))
        ], className="six columns"),

            html.Label('Radio Items'),
                dcc.RadioItems(
                options=[
                    {'label': 'Frequency', 'value': 'NYC'},
                    {'label': 'Lecxical', 'value': 'MTL'},
                    {'label': 'Simantic', 'value': 'SF'}
                ],
                value='MTL'
                ),

        html.Div([html.H3('Document Simalarity Index'),
            html.H6('(List of most similar files)'),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} 
                        for i in frequency_df.reset_index().columns],
                data=frequency_df.reset_index().to_dict('records'),
                style_cell=dict(textAlign='left'),
                style_header=dict(backgroundColor="paleturquoise"),
                style_data=dict(backgroundColor="lavender"))
        ], className="six columns"),
    ], className="row") ,
    ])

    # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    # flask_app.layout = dash_table.DataTable(
    # id='table',
    # columns=[{"name": i, "id": i} for i in df.columns],
    # data=df.to_dict('records'),
    # )
    return dash_app
