#!/usr/bin/env bash

cd /share
cp java.tar.gz /opt
cp maven.tar.gz /opt
cp jira.bin /opt
cp response.varfile /opt
cp jenkins.deb /opt
cd /opt

sudo tar -zxf java.tar.gz
sudo update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_45/bin/java 100

sudo tar -zxf maven.tar.gz
sudo update-alternatives --install /usr/bin/maven maven /opt/apache-maven-3.3.9/bin/mvn 100

sudo chmod 777 jira.bin
./jira.bin -q -varfile response.varfile

sudo apt-get update
sudo apt-get install -y -f

dpkg -i jenkins.deb
sudo install jenkins -y
sudo service jenkins start

sudo apt-get install git -y