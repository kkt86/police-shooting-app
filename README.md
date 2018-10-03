# README

In this repository, we provide a simple bokeh application, running in docker environment. The main idea is to be used for 
deployment purposes

## Deploy application locally
In order to do this, a local application of ``docker`` is required. In order to deploy it, run

```
docker build -t test-image .
docker run -it -p 5006:5006 bokeh-image
```

The application should be available under: http://localhost:5006/myapp

## Deploy application in Heroku server
In this case, the bokeh application is deployed directly on a Heroku server. In order to do that from scratch, the 
following steps should be performed:

First, create a Heroku account and login via:
```
heroku login
```
Afterwards, we need to create an new heroku app:
```
heroku create <appname>
```
Keep track of the name of the app, as it will be used for later purposes. The next step is to create a ``runtime.txt`` 
file, containing the version of python which will be running on the Heroku server. The content of the file in my case is
```
python-3.6.6
```
Finally, we need to create a ``Procfile``, which tells heroku how to run our files as a web application. In my case, the
``Procfile`` contains:
```
web: bokeh serve --port=$PORT --num-procs=0 --address=0.0.0.0 --allow-websocket-origin=rocky-spire-85380.herokuapp.com --use-xheaders myapp/main.py
```
where the various parameters are explained as follows:
* __web__: tells Heroku that this code should be run as a web server.
* __bokeh serve__: It starts a Bokeh server using the Python script that is specified later in this line.
* __–port=$PORT__: specifies which port should be used for the Bokeh server. Usually, if run locally, you might use something like –port=5005. However, Bokeh sets the port dynamically and stores the current port in the PORT environmental variable, which is being accessed by the Bokeh server automatically here.
* __–num-procs=0__: is used to determine the number of worker processes which may be used for the application. “0” means that the number of workers will automatically be detected based on the available cores.
* __--allow-websocket-origin=rocky-spire-85380.herokuapp.com__: should be set to whatever the public URL that *users will navigate to* to get to the app is.
* __–use-xheaders__: tells Bokeh that it should use the xheaders for determining the network protocols. This parameter is required when running Bokeh on Heroku, but not when running a Bokeh server locally.
* __myapp/main.py__: is the name of the Python script that the Bokeh server should run.

Finally (assuming that a local git repository is created, with all the required files already commited), we can push the app to Heruko via:
```
git push heroku master
```