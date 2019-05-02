FROM ubuntu:18.04

EXPOSE 3000

RUN apt-get update -y && \
    apt-get install -y python3.6 python3.6-dev python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./Requirments.txt /app/includeamin/Requirements.txt

WORKDIR /app/includeamin

RUN pip3 install -r Requirements.txt --upgrade
RUN pip3 install gunicorn
RUN pip3 install gevent

COPY . .



#CMD ["python3.6","-u","app.py"]
CMD ["/usr/local/bin/gunicorn", "--config", "gunicorn_config.py" , "app:app"]
