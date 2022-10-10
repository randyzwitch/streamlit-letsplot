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
        width, height = get_ggsize_or_default(plot_dict, default=500)
    elif isinstance(plot, GGBunch):
        # the inner list comprehension is a list of (width, height) tuples
        # the outer consists of two elements [sum(widths), sum(heights)]
        width, height = [sum(y) for y in zip(*[get_ggsize_or_default(x["feature_spec"], default=500) for x in plot_dict["items"]])]
    else:
        height=500
        width=500

    # 20 an aribtrary pad to remove scrollbars from iframe, consider if worth removing
    return components.html(_as_html(plot_dict),
                           height=height + 20,
                           width=width + 20,
                           scrolling=scrolling,
                           )

def get_ggsize_or_default(plot_dict, default=500) -> (int, int):
    """
    Returns a tuple consisting of the width and height of the plot
    Lookup if there is a ggsize specification. If not return default value.
    :param plot_dict:
    :param default:
    :return: width, height
    """
    if 'ggsize' in plot_dict.keys():
        return plot_dict["ggsize"]["width"], plot_dict["ggsize"]["height"]
    return default, default
