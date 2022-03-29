FROM ubuntu:latest

RUN apt-get update
RUN apt-get install wget
RUN wget https://sicstus.sics.se/sicstus/products4/sicstus/4.6.0/binaries/linux/sp-4.6.0-x86_64-linux-glibc2.17.tar.gz
RUN cat sp-4.6.0-x86_64-linux-glibc2.17.tar.gz | gzip -cd | tar xf -

COPY . .
