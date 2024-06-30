# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = Dash(__name__)

colors = {
    'background': 'white',
    'text': 'black',
    'graph': 'white',
}

# Load data
df = pd.read_csv('newdata.csv')

# Define options and corresponding dataframes
option_map = {
    'all': df.groupby('date')['sales'].sum().reset_index(),
    'north': df[df['region'] == 'north'],
    'south': df[df['region'] == 'south'],
    'east': df[df['region'] == 'east'],
    'west': df[df['region'] == 'west']
}

@app.callback(
    Output('radio-output', 'children'),
    [Input('radio-buttons', 'value')]
)
def update_output(selected_option):
    df_selected = option_map[selected_option]
    fig = px.line(df_selected, x='date', y='sales', title=f'Sales Data for {selected_option.capitalize()} Region')

    graph = dcc.Graph(
        id='graph',
        figure=fig
    )

    return graph

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sales Data Visualization for Pink Morsel',
        id='header',
        style={
            'textAlign': 'center',
            'color': colors['text']
        },
    ),

    dcc.RadioItems(
        id='radio-buttons',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'},
        ],
        className='radio-class',
        value='all'  # Default selected value
    ),

    html.Div(id='radio-output'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
