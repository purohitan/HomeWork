# Belly Button Biodiversity

A dashboard of belly button micro-organisms, developed using Python, Flask, Plotly, HTML, JavaScript, SQLAlchemy 

![Bacteria by filterforge.com](Images/bacteria_by_filterforgedotcom.jpg)

Built an interactive dashboard to explore the [Belly Button Biodiversity DataSet](http://robdunnlab.com/projects/belly-button-biodiversity/).

## Step 1 - Plotly.js

Used Plotly.js to build interactive charts for  dashboard.

* Create a PIE chart that uses data from your samples route (`/samples/<sample>`) to display the top 10 samples.

  * Used `sample_values` as the values for the PIE chart

  * Used `otu_ids` as the labels for the pie chart

  * Used `otu_labels` as the hovertext for the chart

  ![PIE Chart](Images/pie_chart.png)

* Created a Bubble Chart that uses data from samples route (`/samples/<sample>`) to display each sample.

  * Used `otu_ids` for the x values

  * Used `sample_values` for the y values

  * Used `sample_values` for the marker size

  * Used `otu_ids` for the marker colors

  * Used `otu_labels` for the text values

  ![Bubble Chart](Images/bubble_chart.png)

* Display the sample metadata from the route `/metadata/<sample>`

  * Display each key/value pair from the metadata JSON object somewhere on the page

* Update all of the plots any time that a new sample is selected.

* An example dashboard page might look something like the following.

![Example Dashboard Page](Images/dashboard_part1.png)
![Example Dashboard Page](Images/dashboard_part2.png)

## Step 2 - Heroku

Deploy your Flask app to Heroku.

* You can use the provided sqlite file for the database.


- - -

## Advanced Challenge  

The following task is completely optional and is very advanced.

* Adapt the Gauge Chart from <https://plot.ly/javascript/gauge-charts/> to plot the Weekly Washing Frequency obtained from the route `/wfreq/<sample>`

* Example gauge code to account for values ranging from 0 - 9.

* Update the chart whenever a new sample is selected

![Weekly Washing Frequency Gauge](Images/gauge.png)

- - -

## Flask API

Use Flask API starter code to serve the data needed for plots.

- - -