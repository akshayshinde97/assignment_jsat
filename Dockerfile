# Use an official Python runtime as an image
FROM python:3.10

## make a local directory
RUN mkdir /store_app

# set "store_app" as the working directory from which CMD, RUN, ADD references
WORKDIR /store_app

# now copy all the files in this directory to /store_app
ADD . /store_app

# install mysql-client
RUN apt-get update && apt-get install --no-install-recommends -y default-mysql-client

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# Listen to port 5000 at runtime
EXPOSE 5000

# Define our command to be run when launching the container
ENTRYPOINT /store_app/entrypoint.sh



