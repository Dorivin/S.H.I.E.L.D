FROM ubuntu:latest
ENV VERSION=1.2.0
USER root

# Install python3.8
RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install python3.8 -y

# Install vim
RUN apt-get install vim -y

# Install zip and unzip
RUN apt-get install zip unzip -y

COPY ./zip_job.py /tmp

COPY ./system_verifier.sh /.
RUN chmod +x ./system_verifier.sh
CMD bash -c "./system_verifier.sh"