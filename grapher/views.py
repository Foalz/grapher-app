from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json

import sympy
import sympy.plotting
from sympy.parsing.latex import parse_latex
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import json_item
from bokeh.models import HoverTool, Range1d

def plot(request):
    if request.method == "GET":
        TOOLTIPS = [
            ("(x,y)", "($x, $y)"),
        ]
        latex = "\\csc\\left(x+3\\right)"
        latex = "\\frac{1}{x}"
        equation = parse_latex(latex)
        plot = sympy.plot(
            equation,
            ("x", -15, 15),
            show=False,
        )
        x, y = plot[0].get_data()
        x_points = np.asarray(x) 
        y_points = np.asarray(y) 
        y_points[y_points>100] = np.inf
        y_points[y_points<-100] = -np.inf
        p = figure(
            toolbar_location="below", 
            title=f"f(x) = {equation}", 
            tooltips=TOOLTIPS,
        )
        p.y_range = Range1d(-5, 5)
        p.line(x_points, y_points, line_width=2, color="firebrick", alpha=.8)
        
        hover = HoverTool(tooltips=TOOLTIPS, mode='vline')
        p.add_tools(hover)
        item_text = json.dumps(json_item(p, "myplot"))
        return render(request, 'index.html', {"points": item_text})

def index(request):
    res = str(read_root()) 
    template = loader.get_template('index.html')
    return render(request, 'index.html', {"username": "qq"})
