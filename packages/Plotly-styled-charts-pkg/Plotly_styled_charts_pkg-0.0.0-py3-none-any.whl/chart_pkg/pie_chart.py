#    Module for pie chart class

# import libraries
import streamlit as st
import plotly.express as px
import pandas as pd


_=""" Bar chart class"""

class BarChart_sty:

    def __init__(self,dataframe,x_axis,y_axis,template,color,hover_data):
        self.df=dataframe
        self.x_ax=x_axis
        self.y_ax=y_axis
        self.temp=template
        self.color=color
        self.hover_data=hover_data
    
    def bar(self):
        bar_chart = px.bar(self.df, y=self.y_ax, x=self.x_ax, template=self.temp, color=self.color, hover_data=self.hover_data)
        bar_chart.update_xaxes(title_text='')
        bar_chart.update_yaxes(title_text='')
        bar_chart.update_xaxes(title_font=dict(size=2, family='Courier', color='crimson'))
        bar_chart.update_xaxes( tickfont=dict(family='Rockwell', color='black', size=13))
        bar_chart.update_yaxes( tickfont=dict(family='Rockwell', color='black', size=11))
        bar_chart.update_layout(coloraxis_showscale=False)
        bar_chart.update_xaxes(ticklen=0)
        bar_chart.update_yaxes(ticklen=0)
        return bar_chart


