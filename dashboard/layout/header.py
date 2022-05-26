import dash_bootstrap_components as dbc
from dash import html

header = dbc.Container([
    html.H1('Personal finance app', style={'text-align': 'center'}),
    html.Hr(),
])
