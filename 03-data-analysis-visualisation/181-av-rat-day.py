import justpy as jp
import pandas
from datetime import datetime # Need to compare times
from pytz import utc # Need to compare times
import matplotlib.pyplot as plt # plt is naming convention

# We use parse dates argument here to get Timestamps as datetime objects not strings
data = pandas.read_csv("./review_analysis/reviews.csv", parse_dates = ['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()


# Highcharts is also a JS library for charts
# Copy code from HighCharts base code

# Below is a python string that justpy can convert into a dictionary (as its JSON)
# Can edit some values directly but for complex changes pass in as variables
charts_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Course Ratings'
    },
    subtitle: {
        text: 'by Day'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Day'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage() 
    
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis")
    hc = jp.HighCharts(a = wp, options = charts_def)

    # We can change elements from JSON
    hc.options.title.text = "Custom Title: Average Rating by Day"

    # Data - we take in two series and then combine with zip (if numbers)
    # High Charts considers timestamps not as numbers but as categories so need to pass them in that way
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])
    # Can use zip method to combine lists if both are data. It does not return a list object by default
    # hc.options.series[0].data = list(zip(x, y))

    print(hc.options)
    print(type(hc.options)) # <class 'addict.addict.Dict'>
    # Dictionary above is not normal dictionary as can access subfunctions using dot notation
    print(hc.options.title.text)
    print(type(charts_def)) # <class 'str'>

    return wp

jp.justpy(app)
