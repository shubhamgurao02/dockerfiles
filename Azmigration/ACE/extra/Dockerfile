FROM ubuntu:latest

# Build using the following command: docker build -t greghodgkinson/bamboo-buildconductor-ace-12.0.3.0:edge .
# Don't forget to tag the image as stable once it is ready for distribution

# >>>>> UPDATE OS AND INSTALL OS TOOLS

RUN apt-get update -y && \
    apt-get install -y software-properties-common && \
    apt-add-repository -y ppa:mozillateam/firefox-next && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y firefox xvfb tar bc sudo expect openssh-server unzip openjdk-8-jdk git gtk2.0 xorg openbox ant dbus-x11 curl

# >>>>> INSTALL ACE
#COPY ACE_12_0.12_Linux_x86-64_ML.tar.gz .
RUN mkdir -p /opt/ibm 
COPY ace-12.0.12.0 /opt/ibm     
RUN	find /opt/ibm -name "*.so*" -exec strip {} ";" && \
    find /opt/ibm -name "*.wrk" -exec strip {} ";" && \
    find /opt/ibm -name "*.lil" -exec strip {} ";" && \
    ( strip /opt/ibm/ace-12.0.12.0/server/bin/* 2>/dev/null || /bin/true ) && \
    zip -d /opt/ibm/ace-12.0.12.0/common/classes/IntegrationAPI.jar BIPmsgs_de.properties BIPmsgs_es.properties BIPmsgs_fr.properties BIPmsgs_it.properties BIPmsgs_ja.properties BIPmsgs_ko.properties BIPmsgs_pl.properties BIPmsgs_pt_BR.properties BIPmsgs_ru.properties BIPmsgs_tr.properties BIPmsgs_zh.properties BIPmsgs_zh_HK.properties BIPmsgs_zh_TW.properties && \
    addgroup mqbrkrs

RUN bash -c '/opt/ibm/ace-12.0.12.0/ace make registry global accept license silently' && \
    echo ". /opt/ibm/ace-12.0.12.0/ace/server/bin/mqsiprofile" >> /root/.bashrc

# Copy in script files - this is used to prevent the "mqsiprofile 
# repetition disallowed" message from being printed on shell start.
COPY context/ace/ace_env.sh /usr/local/bin/
RUN chmod +rx /usr/local/bin/*.sh

# Set BASH_ENV to source mqsiprofile when using docker exec bash -c
ENV BASH_ENV=/usr/local/bin/ace_env.sh
RUN /usr/local/bin/ace_env.sh

# Create a user to run as, create the ace workdir, and chmod script files
RUN ( echo "Passw0rd" ; echo "Passw0rd" ) | useradd -d /home/aceuser -s /bin/bash -G mqbrkrs aceuser  && \
    mkdir /home/aceuser && \
    chown aceuser:aceuser /home/aceuser && \
    chmod 755 /usr/local/bin/* && \
    touch /home/aceuser/.bashrc && \
    chown aceuser /home/aceuser/.bashrc && \
    chmod 664 /home/aceuser/.bashrc && \
    su - aceuser -c '. /opt/ibm/ace-12.0.12.0/server/bin/mqsiprofile && mqsicreateworkdir /home/aceuser/ace-server' && \
    echo ". /usr/local/bin/ace_env.sh" >> /home/aceuser/.bashrc

# Set up system logging and permissions

RUN touch /var/log/user.log && \
    echo "user.info /var/log/user.log" >> /etc/syslog.conf

RUN chmod -R 777 /var/mqsi

# >>>>> INSTALL BUILD CONDUCTOR FOR ACE

# Copy in plugin

COPY context/repo-bc-ace/build-iib-100-linux /buildconductor/ace/build-iib-100-linux
COPY context/repo-bc-common/build-common-linux /buildconductor/ace/build-common-linux

RUN	chmod 777 /buildconductor/ace/build-common-linux/udclient/
RUN	chmod 777 /

# Copy in run script

COPY context/run-automation/run-automation.sh /buildconductor/ace/run-automation.sh
RUN chmod 777 /buildconductor/ace/run-automation.sh
RUN sed -i -e "s/@@BUILD_TIMESTAMP@@/$(date +%s)/g" /buildconductor/ace/build-iib-100-linux/build.xml

# Set entrypoint

ENTRYPOINT ["/bin/bash", "/buildconductor/ace/run-automation.sh"]
