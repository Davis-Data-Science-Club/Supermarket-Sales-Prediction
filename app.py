import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

customers=pd.read_csv('customers.csv')
orders=pd.read_csv('orders.csv')
products=pd.read_csv('products.csv')
sales=pd.read_csv('sales.csv')

########### Define your variables
# beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
# ibu_values=[35, 60, 85, 75]
# abv_values=[5.4, 7.1, 9.2, 4.3]
# color1='darkred'
# color2='orange'
mytitle='Beer Comparison'
tabtitle='DDSC F22'
myheading='Supermarket Sales Forecast Model'
label1='IBU'
label2='ABV'
githublink='https://github.com/Davis-Data-Science-Club/Supermarket-Sales-Prediction'
sourceurl='https://www.kaggle.com/datasets/ruchi798/shopping-cart-database'
introText='''Running a business often boils down to two main goals: Maximize profits, minimize losses.
            Businesses often rely on accurate sales forecasts to make better business
            decisions, including efficient resource allocation and cash flow management. Using data 
            analytics, businesses can also identify potential weaknesses in their business models, 
            such as underperforming products, geographical locations, etc. Our product is targeted
            towards small businesses, who lack the capital to pour significant amounts of money 
            into data analytics.\n
            Profitify by DDSC is a web application, aimed at increasing revenue and profit for supermarkets 
            through a sales forecasting model. Owners have access to a data dashboard, which visually 
            displays key statistics including most popular products by product category, complement 
            products, time analysis, demographics, and more.
            '''
tools='Python (pandas, matplotlib, scikit-learn), Anaconda, Jupyter Notebook, Git, Github, Scrum'

#barplot of customer age
age_df = px.data.tips()
fig = px.histogram(
    customers, 
    x = "age",  
    color = 'gender', 
    marginal = 'box', #create box and whisker plot
    hover_data = customers.columns #interactive element
)

fig.update_layout(#reconfigure labels
    title = {
        'text' : 'Distribution of Customer Age Grouped by Gender',
        'y':0.95,
        'x':0.45,
        'xanchor':'center',
        'yanchor':'top'
    },
    xaxis_title='Customer Age',
    yaxis_title='Total Number of Customers',
    legend_title= 'Gender',
    font=dict(family='monospace', size=15,  color='Black'))

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    #Elements listed from top to bottom of page
    html.H1(myheading),
    html.H3(children='''
        Introduction   
    '''),
    html.P(introText),
    html.H3('Tools'),
    html.P(tools),
    html.Div('Team'),
    html.H1('TESTING FOR AUTOMATIC DEPLOYMENT'),
    html.Div('Methodology'),
    # dcc.Graph(
    #     id='flyingdog',
    #     figure=beer_fig
    # ),
    dcc.Graph(
        id="graph1",
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
