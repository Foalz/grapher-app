from typing import Union

from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sympy
import sympy.plotting
from sympy.parsing.latex import parse_latex
import numpy as np
from bokeh.plotting import figure, show
from bokeh.embed import json_item
from bokeh.models import HoverTool, Range1d

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LatexString(BaseModel):
    latex_string: str

@app.get("/")
def read_root():
    latex = "\\sin\\left(x+3\\right)"
    equation = parse_latex(latex)
    plot = sympy.plot(
        equation,
        show=False
    )
    x, y = plot[0].get_data()
    x_points = np.asarray(x) 
    y_points = np.asarray(y) 
    p = figure(width=500, height=500, toolbar_location="below", title="Plot 1")
    p.line(x_points, y_points, line_width=2, color="firebrick", alpha=.5)
    return json_item(p, 'myplot')

@app.post("/api/plot")
async def plot_latex(latex_string: LatexString):
    TOOLTIPS = [
        ("(x,y)", "($x, $y)"),
    ]
    latex = latex_string.latex_string 
    equation = parse_latex(latex)
    plot = sympy.plot(
        equation,
        ("x", -50, 50),
        show=False
    )
    x, y = plot[0].get_data()
    x_points = np.asarray(x) 
    y_points = np.asarray(y) 
    p = figure(
        width=500, 
        height=500, 
        toolbar_location="below", 
        title="Plot 1", 
        tooltips=TOOLTIPS,
    )
    p.y_range = Range1d(0, 10)
    p.x_range = Range1d(0, 10)
    p.line(x_points, y_points, line_width=5, color="firebrick", alpha=.5)

    hover = HoverTool(tooltips=TOOLTIPS, mode='vline')
    p.add_tools(hover)
    return json_item(p, 'myplot')
