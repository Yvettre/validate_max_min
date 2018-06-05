# based on ubuntu
FROM ubuntu

LABEL maintainer ding_yanfang@outlook.com

RUN apt-get update && \
        apt-get install -y --no-install-recommends \
        git \
        python-numpy \
        python-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home/root/

RUN git clone https://github.com/Yvettre/validate_max_min.git