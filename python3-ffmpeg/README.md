## How to build

~~~bash
docker build -t newnewcoder/python36-ffmpeg:latest .
~~~

## How to push

~~~bash
docker login
docker push newnewcoder/python36-ffmpeg
~~~

## How to run

~~~bash
docker run --rm -ti newnewcoder/python36-ffmpeg:latest bash
~~~
