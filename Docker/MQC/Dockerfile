# Use an official Ubuntu-based image as a parent image
FROM ubuntu:latest


# Install Python , pip , mqclient and other necessary packages
RUN apt-get update && \
    apt-get install -y python3 wget && \
    apt-get install -y python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /tmp/mq && \   
    wget -O /tmp/mq/mqadv_dev920_ubuntu_x86-64.tar.gz    https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/messaging/mqadv/mqadv_dev920_ubuntu_x86-64.tar.gz && \
    ls -la /tmp/mq && \
    tar -Uzxvf /tmp/mq/mqadv_dev920_ubuntu_x86-64.tar.gz -C /tmp/mq/ && \
    rm -rf /tmp/mq/mqadv_dev920_ubuntu_x86-64.tar.gz && \
    groupadd --system --gid 980 mqm && \
    useradd --system --uid 980 --gid mqm --create-home --home-dir /home/mqm mqm; usermod -aG mqm root && \
    useradd --system --gid mqm --create-home --home-dir /home/azureadmin azureadmin && \
    /tmp/mq/MQServer/mqlicense.sh -text_only -accept && \
    dpkg -i /tmp/mq/MQServer/ibmmq-runtime_9.2.0.0_amd64.deb && \
    dpkg -i /tmp/mq/MQServer/ibmmq-gskit_9.2.0.0_amd64.deb && \
    dpkg -i /tmp/mq/MQServer/ibmmq-client_9.2.0.0_amd64.deb && \
    dpkg -i /tmp/mq/MQServer/ibmmq-server_9.2.0.0_amd64.deb && \
    pip3 install jproperties requests termcolor

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/mqm/bin

RUN sed -i 's|ENV_SUPATH	PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin|ENV_SUPATH	PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/mqm/bin|g' /etc/login.defs && \
    sed -i 's|ENV_PATH	PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games|ENV_PATH	PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/opt/mqm/bin|g' /etc/login.defs && \
    sed -i 's|PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"|PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/mqm/bin"|g' /etc/environment 

COPY build.sh /buildconductor/build.sh

ENTRYPOINT ["/bin/bash", "/buildconductor/build.sh"]