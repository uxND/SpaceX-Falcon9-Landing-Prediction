"""
SpaceX Launch Records Interactive Dashboard
Built with Dash and Plotly to analyze launch site performance and payload outcomes.
"""

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# Load and initialize dataset
# ---------------------------------------------------------
DATA_PATH = "spacex_launch_dash.csv"
spacex_df = pd.read_csv(DATA_PATH)

min_payload = int(spacex_df['Payload Mass (kg)'].min())
max_payload = int(spacex_df['Payload Mass (kg)'].max())

# Launch site options for dropdown filter
launch_sites = [
    {'label': 'All Sites', 'value': 'ALL'},
    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
    {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
]

# ---------------------------------------------------------
# Initialize Dash Application
# ---------------------------------------------------------
app = Dash(__name__)
app.title = "SpaceX Launch Analytics"

# ---------------------------------------------------------
# Application Layout
# ---------------------------------------------------------
app.layout = html.Div(
    children=[
        html.H1(
            'SpaceX Launch Records Dashboard',
            style={
                'textAlign': 'center',
                'color': '#503D36',
                'fontSize': 40,
                'marginBottom': 20
            }
        ),

        # TASK 1: Launch Site Dropdown Input
        html.Div([
            dcc.Dropdown(
                id='site-dropdown',
                options=launch_sites,
                value='ALL',
                placeholder="Select a Launch Site here",
                searchable=True,
                style={'width': '100%', 'padding': '3px', 'fontSize': '18px'}
            )
        ]),
        html.Br(),

        # TASK 2: Launch Success Pie Chart
        html.Div(
            dcc.Graph(id='success-pie-chart')
        ),
        html.Br(),

        # TASK 3: Payload Range Slider Selector
        html.P("Payload range (Kg):", style={'fontWeight': 'bold', 'fontSize': '16px'}),
        dcc.RangeSlider(
            id='payload-slider',
            min=0,
            max=10000,
            step=1000,
            marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
            value=[min_payload, max_payload]
        ),
        html.Br(),

        # TASK 4: Payload vs. Outcome Scatter Plot
        html.Div(
            dcc.Graph(id='success-payload-scatter-chart')
        ),
    ],
    style={'padding': '20px 40px', 'fontFamily': 'Arial, sans-serif'}
)

# ---------------------------------------------------------
# Callback Handlers
# ---------------------------------------------------------

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def render_pie_chart(selected_site):
    """Generates a pie chart of launch success counts based on the chosen launch site."""
    if selected_site == 'ALL':
        figure = px.pie(
            spacex_df,
            values='class',
            names='Launch Site',
            title='Total Success Launches by Site'
        )
    else:
        site_filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        figure = px.pie(
            site_filtered_df,
            names='class',
            title=f'Total Success Launches for site {selected_site}'
        )
    return figure


@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value')
    ]
)
def render_scatter_chart(selected_site, payload_limits):
    """Renders a scatter plot comparing payload mass to launch success within the selected weight range."""
    lower_bound, upper_bound = payload_limits
    payload_mask = (spacex_df['Payload Mass (kg)'] >= lower_bound) & (spacex_df['Payload Mass (kg)'] <= upper_bound)
    filtered_data = spacex_df[payload_mask]

    if selected_site == 'ALL':
        chart_title = 'Payload vs. Outcome for All Sites'
        plot_df = filtered_data
    else:
        chart_title = f'Payload vs. Outcome for site {selected_site}'
        plot_df = filtered_data[filtered_data['Launch Site'] == selected_site]

    scatter_fig = px.scatter(
        plot_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title=chart_title
    )
    return scatter_fig


# ---------------------------------------------------------
# Server Execution
# ---------------------------------------------------------
if __name__ == '__main__':
    app.run_server(port=8060)
