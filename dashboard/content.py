from dashboard.index import app
from dashboard.layout.header import header
from dashboard.layout.footer import footer
import dashboard.layout.tabs as tabs
import dash_bootstrap_components as dbc


tabs_content = dbc.Tabs(
    id="tabs",
    children=[
        dbc.Tab(tabs.net_worth, label="Net worth", tab_id='net_worth'),
        dbc.Tab(tabs.illiquid_assets, label="Illiquid_assets", tab_id='illiquid_assets'),
        dbc.Tab(tabs.stocks, label="Stocks", tab_id='stocks'),
        dbc.Tab(tabs.crypto, label="Crypto", tab_id='crypto'),
    ],
)

app.layout = dbc.Container(
    [
        header,
        tabs_content,
        footer,
    ]
)
