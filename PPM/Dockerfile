# Use an official Ubuntu-based image as a parent image
FROM ubuntu

# Install OpenJDK 11, Maven, and other necessary packages
RUN apt-get update && \
    apt-get install -y curl  && \
    rm -rf /var/lib/apt/lists/* 
ENV NODE_VERSION=16.13.0
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"

COPY build.sh /buildconductor/build.sh


ENTRYPOINT ["/bin/bash", "/buildconductor/build.sh"]