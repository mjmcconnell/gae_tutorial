Simple tutorial on getting started with [Google App Engine](https://cloud.google.com/appengine/docs) and the [Webapp2](https://webapp-improved.appspot.com/index.html) framework.

Please download the Python Google App Engine SDK form [here](https://cloud.google.com/appengine/downloads), and set it up on your machine following the instructions.

You should be able to run the following commands from your terminal:

    $ dev_appserver.py


Running the app locally
========================

You can start the app with:

    $ dev_appserver.py {relative path to app.yaml}

For example if you wanted to start the app inside the step_1 folder, from the root of this repo you can run:

    $ dev_appserver.py step_1/


Deploying the app
========================

To deploy your app to a live server, first go to the [google developer console](https://console.developers.google.com/project) and create a new project. The Project ID will be what you set in the `app.yaml` file under the `application` setting.

You can then upload the app to gae with:

    $ appcfg.py update {relative path to app.yaml}


Steps
=======================

Step 1
-------
Bare bones

Use app.yaml file to render static files

Step 2
-------
Python rendering

Introduces python, and how it can be used to render html without the need for files

Step 3
-------
Templating

Using python to populate parts of a static file

Step 4
-------
Requests

Passing data around your app

Step 5
-------
NDB Datastore

Persistent data storage using the GAE NDB Datastore

Step 6
-------
A cleaner app

Inheritance and importing
