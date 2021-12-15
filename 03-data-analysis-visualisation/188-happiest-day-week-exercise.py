import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("./review_analysis/reviews.csv", parse_dates = ['Timestamp'])

# Add columns to enable aggregation
data['Weekday'] = data['Timestamp'].dt.strftime('%A')
data['Daynumber'] = data['Timestamp'].dt.strftime('%w')

# Aggregate and sort by numbered column
weekday_average = data.groupby(['Weekday', 'Daynumber']).mean()
weekday_average = weekday_average.sort_values('Daynumber')

charts_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Aggregated Average Ratings by Day of the Week'
    },
    subtitle: {
        text: 'According to the Course Reviews Dataset'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: []
    }]
}
"""

def app():
    wp = jp.QuasarPage() 
    
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis")
    
    hc = jp.HighCharts(a = wp, options = charts_def)
    hc.options.xAxis.categories = list(weekday_average.index.get_level_values(0))
    hc.options.series[0].data = list(weekday_average['Rating'])

    return wp

jp.justpy(app)
