# ANAEMIA PROJECT - final UWA Data Analysis Bootcamp project

# Purpose

This project creates a machine learning model to forecast global anaemia, and allows users to enter country inputs and receive a forecasted trend.


# Motivation

The topic of anaemia is important to me because it is a serious global public health problem that particularly affects young children and women. WHO estimates that 42% of children less than 5 years of age and 40% of pregnant women worldwide are anaemic. (https://www.who.int/health-topics/anaemia#tab=tab_1)


# Data source

The WHO odata api (https://www.who.int/data/gho/info/gho-odata-api) was used to retrieve 19 years of data (2000 to 2019) at the country level. The initial indicator selected was Anaemia in women of reproductive age (prevalence and numbers). 


# App hosting

The app is hosted on ...AWS / Horoku?
The endpoint website contains two vizualisations done in Tableau public, feeding from the output csv files which are saved in a AWS bin.


# Repo structure 
```
images/                                     # contains images used for the README
app/    
    |__ app.py                              # contains the main flask app logic and endpoints 
    |__ Procfile                            # tells Elastic Beanstalk how to run the app 
    |__ requirements.txt                    # python dependencies for app 
    |__ build.bat                           # shell script to build the zip file 
resources/
    |__ countries_gdp_health.xlsx           # an WHO extract to determine countries gdp health
    |__ api_ETL.ipynb                       # contains the code used to pull and prepare data
    |__ anaemia.csv                         # output from api_ETL used to feed Tableau viz1
    |__ model.ipynb                         # contains the code used to forecast time series
    |__ forecast.csv                        # output from model.ipynb used to feed Tableau viz2
README.md                                   # all you need to know is in here 

```

# Machine learning model

An ARIMA model was used to forcast time series. Based on the World Health Organization target of reducing anaemia by 50% by 2025 (see policy brief https://apps.who.int/iris/bitstream/handle/10665/148556/WHO_NMH_NHD_14.4_eng.pdf?ua=1), a forcast of 5 years was selected. This was applied to a list of the top 30 most populated countries.


