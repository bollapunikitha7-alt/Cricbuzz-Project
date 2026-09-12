"""
UI presentation and badge formatters for Streamlit.
"""
def render_kpi_card(title: str, value: str, subtitle: str = "", delta: str = None) -> str:
    """Return an HTML snippet for a KPI metric card."""
    delta_html = f"<span style='color: #28a745; font-size: 0.9em;'>▲ {delta}</span>" if delta else ""
    return f"""
    <div style="background-color: #f8f9fa; border: 1px solid #e9ecef; border-radius: 8px; padding: 16px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <p style="margin: 0; color: #6c757d; font-size: 0.85em; text-transform: uppercase; font-weight: 600;">{title}</p>
        <h2 style="margin: 6px 0; color: #1f2937; font-size: 1.8em; font-weight: 700;">{value} {delta_html}</h2>
        <p style="margin: 0; color: #9ca3af; font-size: 0.8em;">{subtitle}</p>
    </div>
    """

def get_badge(text: str, color: str = "blue") -> str:
    """Return inline HTML badge."""
    colors = {
        "blue": ("#e0f2fe", "#0369a1"),
        "green": ("#dcfce7", "#15803d"),
        "amber": ("#fef3c7", "#b45309"),
        "red": ("#fee2e2", "#b91c1c"),
        "purple": ("#f3e8ff", "#7e22ce")
    }
    bg, fg = colors.get(color, ("#e0f2fe", "#0369a1"))
    return f"""<span style="background-color: {bg}; color: {fg}; padding: 3px 8px; border-radius: 9999px; font-size: 0.78em; font-weight: 600; text-transform: uppercase;">{text}</span>"""
