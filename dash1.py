import dash
import dash_html_components as html
import dash_core_components as dcc

# app.css.append_css({
# 'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
# })
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets) 
app.layout = html.Div([
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
        



if __name__ == '__main__':
    app.run_server(debug=True)