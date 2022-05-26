import dash_bootstrap_components as dbc
from dash import html

footer = dbc.Container([
    html.P(children='Made by Joost van der Putten yo', style={"text-align": "center"}),
])
