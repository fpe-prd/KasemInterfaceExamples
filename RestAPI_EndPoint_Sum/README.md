[Examples list](../README.md)

# Example: RestAPI EndPoint Sum of two syncrhonized time series

**Keywords**: Python, Pandas, Flask, Gunicorn, Docker 

## Service specification

 - Input time series must be named *e1_ts* and *e2_ts*
 - Output time series will be named *sum_ts*
 - Coefficient must be named *scale*
 - Equation: *sum_ts* = *scale* x ( *e1_ts* + *e2_ts* )

## Service endpoint

 - Use [Flask](https://flask.palletsprojects.com/) to create a RestAPI endpoint, called `method` here.
 - `method` will be called using POST request from KasemInterface with *json* input data in *body*
 - `method` must return a *json* output data

> [!TIP]
> *json* data structure can be easily loaded into *pandas Dataframe*. An overview of *json* strucutre is given in test section.

**See** [app.py](app.py)

## Docker

Project folder should at least contains:
- the python application to run inside the container
- the requirements of python dependencies of the application
- the docker file with instructions to allow the built of the Docker image

### Development

To build the Docker image, in a terminal, navigate to the folder containing the Docker file and run the command:
```
docker build -f Dockerfile_dev -t image_name .
```
where:
- `-f`  name of the Docker file
- `-t`  gives the name `image_name` to the built image
- `.` to look for the files in the current directory

To launch the container, run the command:
```
docker run --name docker_name -p 2000:5000 image_name
```
where:
- `--name` is a custom name given to the docker container
- `-p` is the port mapping option, here tells docker to redirect port 2000 on the host machine to port 5000 inside the container

> [!NOTE]
> A pip connection error during container initialization can be solved by reconfigure the DNS settings in Docker application. Use for instance DNS of Google: 8.8.8.8.

**See** [requirements.txt](requirements.txt) and [Dockerfile_dev](Dockerfile_dev)

### Production

When launching the Docker container you can have the following warning:

> This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

The build-in Flask server, the one launched by Flask run or *app.run()*, is intended for development purpose only. It is single threaded, not very performant and not secure for production deployments. Flask recommends using a WSGI server like [Gunicorn](https://gunicorn.org/) for production.

To launch on production server add gunicorn in requirements.txt, create the WSGI and update Docker file.

**See** [wsgi.py](wsgi.py), [requirements.txt](requirements.txt) and [Dockerfile_prod](Dockerfile_prod)

## Test

To test the endpoint, Python [Requests](https://requests.readthedocs.io/) library can be used with a set of *body* genere from KasemInterfece in *dev* mode.

**See** [test.py](test.py)

> [!NOTE]
> Exception can be managed in the endpoint in this case the integer propertie `error` must be added to the return *json*, where 0 means *no error* and values greather than 0 is an error code. 
>
> A string propertie `log` can also be added with text details on the execution. 