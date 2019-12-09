import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


def dash_test(data):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = html.Div(children=[
        html.H1(children=''),
        html.Div(children='''
        '''),
        dcc.Graph(
            id='top_five_songs',
            figure={
                'data': data['graph'],
                'layout': {
                    'title': {
                        'text': '<b>Top 5 Songs of 2019<b>',
                        'y': '5',
                        'x': '0.5',
                        'xanchor': 'center'
                    },
                    'plot_bgcolor': '#ffffff',
                    'paper_bgcolor': '#ffffff',
                    'font': {
                        'family': 'SF Pro',
                        'color': '#000000',
                        'size': '16'
                    },
                    'images': data['imgs'],
                    'yaxis': {
                        'title': {
                            'text': '<b>Plays in 2019<b>',
                            'size': '20'
                        }
                    },
                    'height': '500',
                    'margin': {
                        'l': '150',
                        'r': '50',
                        'b': '100',
                        't': '150',
                        'pad': '4'
                    }
                }
            }
        )
    ])

    app.run_server(debug=True)
