import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

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


########### Set up the chart
# bitterness = go.Bar(
#     x=beers,
#     y=ibu_values,
#     name=label1,
#     marker={'color':color1}
# )
# alcohol = go.Bar(
#     x=beers,
#     y=abv_values,
#     name=label2,
#     marker={'color':color2}
# )

# beer_data = [bitterness, alcohol]
# beer_layout = go.Layout(
#     barmode='group',
#     title = mytitle
# )

# beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    #Elements listed from top to bottom of page
    html.H1(myheading),
    html.Div(children='''
        Introduction   
    '''),
    html.P(introText),
    html.Div('Tools'),
    html.P(tools),
    html.Div('Team'),
    html.Div('Methodology'),
    # dcc.Graph(
    #     id='flyingdog',
    #     figure=beer_fig
    # ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
