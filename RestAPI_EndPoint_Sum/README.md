[Examples list](../README.md)

# Example: RestAPI EndPoint Sum of two syncrhonized time series

Python, Pandas, Flask, Gunicorn, Docker 

## Service specification

 - Inputs times series must be named *e1_ts* and *e2_ts*
 - Output time series will be named *sum_ts*
 - Coefficient must be named *scale*
 - Equation: *sum_ts* = *scale* x ( *e1_ts* + *e2_ts* )

## Service endpoint

 - Use [Flask](https://flask.palletsprojects.com/) to create a RestAPI endpoint, called `method`here
 - `method` will be called using POST request from KasemInterface with input data in *body*
 - `method` must return a *json* output data


[see python app script](app.py)

> [!TIP]
> *json* data structure can be easily loaded into *pandas Dataframe*.  

## Docker
