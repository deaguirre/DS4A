"""Docstring de prueba."""
import dash
import dash_bootstrap_components as dbc
import flask

STYLES =[dbc.themes.BOOTSTRAP, "https://www.w3schools.com/w3css/4/w3.css", ]


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=STYLES)
server = app.server





