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
