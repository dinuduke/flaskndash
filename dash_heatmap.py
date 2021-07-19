import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = px.data.medals_wide(indexed=True)
print(df)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Medals included:"),
    dcc.Checklist(
        id='medals',
        options=[{'label': x, 'value': x} 
                 for x in df.columns],
        value=df.columns.tolist(),
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("medals", "value")])
def filter_heatmap(cols):
    fig = px.imshow(df[cols])
    return fig

app.run_server(debug=True)