
#!/bin/bash -e
# docker-flask
#sudo yum update -y

#Install Docker community edition on Centos7

sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io 
sudo systemctl start docker

sudo chown $(id -u):$(id -g)  /var/run/docker.sock
sudo usermod -a -G docker centos

sudo git clone https://github.com/ksprakash/docker-flask.git


#Create a docker image
docker build -t 'flask:kspv1'  .


#Running a Container

docker run -d --name flaskapp -p 8080:9090 flask:kspv1




