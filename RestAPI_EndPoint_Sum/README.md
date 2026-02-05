[Examples list](../README.md)

# Example: RestAPI EndPoint Sum of two syncrhonized time series

**Keywords**: Python, Pandas, FastAPI, Docker 

## Service specification

 - Input time series must be named *e1_ts* and *e2_ts*
 - Output time series will be named *sum_ts*
 - Coefficient must be named *scale*
 - Equation: *sum_ts* = *scale* x ( *e1_ts* + *e2_ts* )

## Service endpoint

 - Use [FastAPI](https://fastapi.tiangolo.com/) to create a RestAPI endpoint, called `sum` here.
 - `sum` will be called using POST request from KasemInterface with *json* input data in *body*
 - `sum` must return a *json* output data

> [!TIP]
> *json* data structure can be easily loaded into *pandas Dataframe*. An overview of Kasem standard *json* strucutre is given in test section.

**See** [app.py](app.py)

## Docker

Project folder should at least contains:
- the python application to run inside the container
- the requirements of python dependencies of the application
- the docker file with instructions to allow the built of the Docker image

To build the Docker image, in a terminal, navigate to the folder containing the Docker file and run the command:
```
docker build -f Dockerfile -t image_name .
```
where:
- `-f`  name of the Docker file
- `-t`  gives the name `image_name` to the built image
- `.` to look for the files in the current directory

To launch the container, run the command:
```
docker run --name docker_name -p 5000:5000 image_name
```
where:
- `--name` is a custom name given to the docker container
- `-p` is the port mapping option, here tells docker to redirect port 5000 on the host machine to port 5000 inside the container

**See** [requirements.txt](requirements.txt) and [Dockerfile](Dockerfile)

## Test

To test the endpoint, Python [Requests](https://requests.readthedocs.io/) library can be used with a set of *body* genere from KasemInterfece in *dev* mode.

**See** [test.py](test.py)

> [!NOTE]
> Exception can be managed in the endpoint in this case the integer propertie `error` must be added to the return *json*, where 0 means *no error* and values greather than 0 is an error code. 
>
> A string propertie `log` can also be added with text details on the execution. 