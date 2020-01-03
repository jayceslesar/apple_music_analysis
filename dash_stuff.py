import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


# ! TODO: make scalable -- add more graphs

def dash_test(data):
    type = data.pop('type')
    if type == 'year':
        year = data.pop('year')
        title_text = '<b>Top 5 Songs of ' + year + \
            ' (' + str(data['mins_total']) + ' minutes listened) ' + '<b>'
        images_text = '<b>Plays in ' + year + '<b>'
    if type == 'month':
        year = data.pop('year')
        month = data.pop('month')
        title_text = '<b>Top 5 Songs of ' + month + ' ' + year + \
            ' (' + str(data['mins_total']) + ' minutes listened) ' + '<b>'
        images_text = '<b>Plays in ' + month + ' ' + year + '<b>'
    if type == 'week':
        title_text = '<b>Top 5 Songs of the past week (' + str(
            data['mins_total']) + ' minutes listened)<b>'
        images_text = '<b>Plays in the past week<b>'
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
                        'text': title_text,
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
                            'text': images_text,
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
