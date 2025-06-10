# KasemInterfaceEndPointSum

Basic examples of  *Sum* algorithm interface with [KASEM](https://www.predict.fr/produits-services/logiciels/) deployed in a docker using Python and [Flask](https://flask.palletsprojects.com/).

## Service : Sum of two syncrhonized time series

Service specifications:
 - Inputs times series must be named *e1_ts* and *e2_ts*
 - Output time series will be named *sum_ts*
 - Coefficient must be named *scale*.
 - Equation: *sum_ts* = *scale* x ( *e1_ts* + *e2_ts*)

## Docker
