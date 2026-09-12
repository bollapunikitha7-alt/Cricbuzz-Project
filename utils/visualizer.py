"""
Interactive Plotly Data Visualization Utilities for Cricbuzz LiveStats.
"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

TEMPLATE = "plotly_white"

def plot_bar_chart(df: pd.DataFrame, x: str, y: str, title: str, 
                   color: str = None, text_auto: bool = True) -> go.Figure:
    """Create a styled Plotly bar chart."""
    fig = px.bar(
        df, 
        x=x, 
        y=y, 
        title=title, 
        color=color, 
        text_auto=text_auto,
        template=TEMPLATE
    )
    fig.update_layout(
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
        hovermode="x unified",
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def plot_grouped_bar_chart(df: pd.DataFrame, x: str, y1: str, y2: str, 
                           title: str, label1: str = "Metric 1", label2: str = "Metric 2") -> go.Figure:
    """Create a grouped bar chart for comparisons."""
    fig = go.Figure(data=[
        go.Bar(name=label1, x=df[x], y=df[y1], marker_color="#1f77b4"),
        go.Bar(name=label2, x=df[x], y=df[y2], marker_color="#ff7f0e")
    ])
    fig.update_layout(
        barmode='group',
        title=title,
        xaxis_title=x.replace("_", " ").title(),
        template=TEMPLATE,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def plot_pie_chart(df: pd.DataFrame, names: str, values: str, title: str) -> go.Figure:
    """Create a styled Plotly donut/pie chart."""
    fig = px.pie(
        df, 
        names=names, 
        values=values, 
        title=title, 
        hole=0.4,
        template=TEMPLATE
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

def plot_scatter_chart(df: pd.DataFrame, x: str, y: str, title: str, 
                       hover_name: str = None, color: str = None) -> go.Figure:
    """Create a 2D scatter plot for statistical distributions."""
    fig = px.scatter(
        df, 
        x=x, 
        y=y, 
        title=title, 
        hover_name=hover_name,
        color=color,
        size_max=15,
        template=TEMPLATE
    )
    fig.update_layout(
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def plot_line_chart(df: pd.DataFrame, x: str, y: str, color: str = None, title: str = "") -> go.Figure:
    """Create a trend line chart."""
    fig = px.line(
        df, 
        x=x, 
        y=y, 
        color=color, 
        title=title, 
        markers=True,
        template=TEMPLATE
    )
    fig.update_layout(
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def plot_player_comparison_radar(categories: list, values1: list, values2: list, 
                                 player1_name: str, player2_name: str) -> go.Figure:
    """Radar chart comparing two players across standardized metrics."""
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values1 + [values1[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name=player1_name,
        line_color='#1f77b4'
    ))
    fig.add_trace(go.Scatterpolar(
        r=values2 + [values2[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name=player2_name,
        line_color='#ff7f0e'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title=f"Head-to-Head Comparison: {player1_name} vs {player2_name}",
        template=TEMPLATE,
        margin=dict(l=40, r=40, t=40, b=40)
    )
    return fig
