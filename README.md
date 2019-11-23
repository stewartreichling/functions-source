# Functions Source

This repo contains starter code for writing functions which can be deployed
in a serverless environment. Each language directory contains the source
code for functions associated with different triggers.

For example, the directory `python/http` contains starter code for a function
triggered by an HTTP request. The directory contains source code, a Dockerfile
and one or more dependencies file(s). Each directory can be built into a
runnable container using the `docker build` command (as shown below).

## Pre-requisites

* [docker](https://www.docker.com/)

## Quick start

Navigate to a directory, for example:
```console
$ cd python
$ cd http
```

Build the image:
```console
$ docker build -t <IMAGE_NAME> .
```

Run the container:
```console
$ docker run -p 8000:8000 <IMAGE_NAME>
[2018-10-19 14:44:11 +0000] [1] [INFO] Starting gunicorn 19.9.0
[2018-10-19 14:44:11 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2018-10-19 14:44:11 +0000] [1] [INFO] Using worker: sync
[2018-10-19 14:44:11 +0000] [7] [INFO] Booting worker with pid: 7
```

In a new shell, send a test request to the container:
```console
$ curl localhost:8000
Hello, World!
```
