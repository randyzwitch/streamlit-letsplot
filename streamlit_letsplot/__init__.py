import streamlit as st
import streamlit.components.v1 as components
from lets_plot.frontend_context._configuration import _as_html
from lets_plot.plot.core import PlotSpec
from lets_plot.plot.plot import GGBunch

def st_letsplot(plot, scrolling=True):
    """Embed a Let's Plot object within Streamlit app

    Parameters
    ----------
    plot: 
        Let's Plot object
    scrolling: bool
        If content is larger than iframe size, provide scrollbars?
    
    Example
    -------
    >>> st_letsplot(p)
    """

    plot_dict = plot.as_dict()
    if isinstance(plot, PlotSpec):
        height=plot_dict["ggsize"]["height"]
        width=plot_dict["ggsize"]["width"]
    elif isinstance(plot, GGBunch):
        height=sum([x["feature_spec"]["ggsize"]["height"] for x in plot_dict["items"]])
        width=sum([x["feature_spec"]["ggsize"]["width"] for x in plot_dict["items"]])
    else:
        height=500
        width=500

    # 20 an aribtrary pad to remove scrollbars from iframe, consider if worth removing
    return components.html(_as_html(plot_dict),
        height=height + 20,
        width=width + 20,
        scrolling=scrolling,
    )