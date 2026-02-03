"""
Dash Dashboard: Compare Powers & Coalition Analysis
Module 6: Dashboard Development
"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Load data
try:
    df = pd.read_csv('../../Milestone_2_KPI_Engineering/Module_3_KPI_Engineering/data/processed/military_final_wide.csv')
except:
    df = pd.DataFrame()

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Military Comparison Dashboard"

# Define app layout
app.layout = html.Div([
    html.Div([
        html.H1("🌍 Military Powers Comparison Dashboard", style={'color': '#2c3e50'}),
        html.P("Compare military capabilities across nations and analyze alliances", style={'color': '#7f8c8d'})
    ], style={'textAlign': 'center', 'padding': '2rem', 'backgroundColor': '#ecf0f1'}),
    
    html.Div([
        html.Div([
            html.Label("Select Countries to Compare:"),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': c, 'value': c} for c in sorted(df['country'].unique())] if not df.empty else [],
                value=df['country'].unique()[:5].tolist() if not df.empty and len(df) > 5 else [],
                multi=True,
                placeholder="Select countries..."
            )
        ], style={'width': '48%', 'display': 'inline-block', 'marginRight': '2%'}),
        
        html.Div([
            html.Label("Select Metric:"),
            dcc.Dropdown(
                id='metric-dropdown',
                options=[
                    {'label': 'Military Budget', 'value': 'military_expenditure_usd'},
                    {'label': 'Active Personnel', 'value': 'active_military_personnel'},
                    {'label': 'Total Military', 'value': 'total_military'},
                    {'label': 'Aircraft', 'value': 'aircraft'},
                    {'label': 'Tanks', 'value': 'tanks'},
                    {'label': 'Navy Ships', 'value': 'navy_ships'}
                ],
                value='military_expenditure_usd'
            )
        ], style={'width': '48%', 'display': 'inline-block', 'marginLeft': '2%'})
    ], style={'padding': '2rem', 'backgroundColor': '#fff'}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='comparison-bar-chart')
        ], style={'width': '48%', 'display': 'inline-block', 'marginRight': '2%'}),
        
        html.Div([
            dcc.Graph(id='radar-chart')
        ], style={'width': '48%', 'display': 'inline-block', 'marginLeft': '2%'})
    ], style={'padding': '1rem'}),
    
    html.Div([
        html.H2("Alliance Analysis", style={'color': '#2c3e50'}),
        html.Div(id='alliance-stats')
    ], style={'padding': '2rem', 'backgroundColor': '#ecf0f1'})
], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f8f9fa'})

# Callbacks
@app.callback(
    Output('comparison-bar-chart', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('metric-dropdown', 'value')]
)
def update_comparison_chart(selected_countries, metric):
    if not selected_countries or df.empty:
        return {}
    
    filtered_df = df[df['country'].isin(selected_countries)]
    
    fig = px.bar(
        filtered_df,
        x='country',
        y=metric,
        title=f"{metric.replace('_', ' ').title()} Comparison",
        labels={metric: metric.replace('_', ' ').title()}
    )
    
    fig.update_layout(
        hovermode='x unified',
        plot_bgcolor='#fff',
        paper_bgcolor='#f8f9fa'
    )
    
    return fig

@app.callback(
    Output('radar-chart', 'figure'),
    Input('country-dropdown', 'value')
)
def update_radar_chart(selected_countries):
    if not selected_countries or df.empty or len(selected_countries) > 3:
        return go.Figure().add_annotation(
            text="Select up to 3 countries for radar chart",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
    
    filtered_df = df[df['country'].isin(selected_countries)].head(3)
    
    categories = ['Military Budget', 'Personnel', 'Aircraft', 'Tanks', 'Navy Ships']
    
    fig = go.Figure()
    
    for idx, row in filtered_df.iterrows():
        values = [
            row.get('military_expenditure_usd', 0) / 100000,
            row.get('total_military', 0) / 100000,
            row.get('aircraft', 0) / 100,
            row.get('tanks', 0) / 100,
            row.get('navy_ships', 0) * 10
        ]
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=row['country']
        ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=True,
        title="Military Capabilities Radar Chart",
        paper_bgcolor='#f8f9fa'
    )
    
    return fig

@app.callback(
    Output('alliance-stats', 'children'),
    Input('country-dropdown', 'value')
)
def update_alliance_stats(selected_countries):
    if not selected_countries or df.empty:
        return html.P("Select countries to see alliance information")
    
    filtered_df = df[df['country'].isin(selected_countries)]
    
    alliances = ['nato', 'brics', 'asean', 'eu', 'sco']
    stats = []
    
    for alliance in alliances:
        if alliance in filtered_df.columns:
            count = filtered_df[alliance].sum()
            stats.append(
                html.Div([
                    html.H4(f"🤝 {alliance.upper()}"),
                    html.P(f"{count} countries selected are members")
                ], style={'display': 'inline-block', 'width': '18%', 'marginRight': '2%', 'textAlign': 'center'})
            )
    
    return stats

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
