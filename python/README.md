# Python code README.md

Build the image:

```console
$ docker build -t <IMAGE_NAME>
```

Run the container:

```console
$ docker run -p 8000:8000 <IMAGE_NAME>
[2018-10-19 14:44:11 +0000] [1] [INFO] Starting gunicorn 19.9.0
[2018-10-19 14:44:11 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2018-10-19 14:44:11 +0000] [1] [INFO] Using worker: sync
[2018-10-19 14:44:11 +0000] [7] [INFO] Booting worker with pid: 7
```

Send a test request to the container:

```console
$ curl localhost:8000
Hello, World!
```