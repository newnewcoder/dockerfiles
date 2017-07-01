#!/bin/bash

Xvfb :99 -screen 0 1280x1024x16 -nolisten tcp &

/bin/tini -- /usr/local/bin/jenkins.sh