## How to run

~~~bash
docker run --name jenkins -d -p 8080:8080 --rm --cap-add=SYS_ADMIN -e "TZ=Asia/Taipei" -v /path/to/your/jenkins_home:/var/jenkins_home newnewcoder/jenkins-chrome
~~~
