import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px

fake_x = ['stocks', 'crypto', 'illiquid_assets']
fake_y = [2000, 3000, 10000]


def create_net_worth_graph():
    fig = px.pie(names=fake_x, values=fake_y, template='plotly_dark')
    return fig


net_worth = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is the net worth tab!", className="card-text"),
            dcc.Graph(figure=create_net_worth_graph())
        ]
    ),
    className="mt-3",
)

stocks = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is the stocks tab!", className="card-text"),
        ]
    ),
    className="mt-3",
)

illiquid_assets = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is the illiquid assets tab!", className="card-text"),
        ]
    ),
    className="mt-3",
)

crypto = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is the crypto tab!", className="card-text"),
        ]
    ),
    className="mt-3",
)