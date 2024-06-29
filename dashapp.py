# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

colors = {
    'background': 'white',
    'text': 'black',
    'graph': 'white',
}

# import the data
df = pd.read_csv('newdata.csv')

# sum all the sales of a the same day for better datra visualization
df_summed = df.groupby('date')['sales'].sum().reset_index()

fig = px.line(df_summed, x="date", y="sales", title='Sales of Pink Morsel Through Time')


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='A Dash app to visualise the sales data of Pink Morsel',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )

])

if __name__ == '__main__':
    app.run(debug=True)
