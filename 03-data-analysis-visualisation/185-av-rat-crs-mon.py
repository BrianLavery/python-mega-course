import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("./review_analysis/reviews.csv", parse_dates = ['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name']).mean().unstack()

# Need to delete pure JS lines
charts_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'centre',
        verticalAlign: 'bottom',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():
    wp = jp.QuasarPage() 
    
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis")
    
    hc = jp.HighCharts(a = wp, options = charts_def)
    hc.options.xAxis.categories = list(month_average_crs.index)
    
    # Create series dynamically as there are multiple series
    # Below would create a list of dictionaries each with name being column name
    # hc_data = [{ "name": v1, "data": [] } for v1 in month_average_crs.columns]
    # We can do multiple levels of list comprehension in one go
    hc_data = [{ "name": v1, "data": [v2 for v2 in month_average_crs[v1]] } for v1 in month_average_crs.columns]

    hc.options.series = hc_data

    return wp

jp.justpy(app)
