# streamlit-letsplot

This is a work-in-progress, providing a convenience function to plot charts from the [Lets-Plot](https://lets-plot.org/) visualization library.

## Example usage

```python
import streamlit as st
from streamlit_letsplot import st_letsplot
import numpy as np
import lets_plot
from lets_plot import *

np.random.seed(12)
data = dict(
    cond=np.repeat(['A','B'], 200),
    rating=np.concatenate((np.random.normal(0, 1, 200), np.random.normal(1, 1.5, 200)))
)

a = ggplot(data, aes(x='rating', fill='cond')) + ggsize(500, 250) \
+ geom_density(color='dark_green', alpha=.7) + scale_fill_brewer(type='seq') \
+ theme(axis_line_y='blank')

# plots any Let's Plot visualization object
st_letsplot(a)
```

![st_letsplot](https://github.com/randyzwitch/streamlit-letsplot/blob/master/_static/simple_example.png)
