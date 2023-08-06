FROM ubuntu:22.04

RUN apt-get update && apt install python3 -y && apt-get install curl -y
RUN apt install python3-pip -y

COPY ./target/wheels/kmer_tools-0.1.0-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl /
