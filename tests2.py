import dash
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello dash'),

    html.Div(children='''
        Результаты опроса:
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2], 'y': [7, 6], 'type': 'bar', 'name': 'первый фреймворк/библиотека'},
                {'x': [1, 2], 'y': [3, 4], 'type': 'bar', 'name': u'второй фреймворк/библиотека'},
            ],
            'layout': {
                'title': 'Визуализация'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)