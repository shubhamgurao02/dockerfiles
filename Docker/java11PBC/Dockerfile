FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y openjdk-11-jre maven  && \
    rm -rf /var/lib/apt/lists/*

COPY build.sh /buildconductor/build.sh

ENTRYPOINT ["/bin/bash", "/buildconductor/build.sh"]