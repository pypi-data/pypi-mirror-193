#How To Build the MorphoNet Python API ?

The API is now build automaticaly wit gitlab runner 

### How to Install a new gitlab Runner
- In Continous Integration tools (https://ci.inria.fr/project/morphonet/slaves)
- Create a new slave  (ex : Ubuntu 20.LTS  with 2Gb and 2 Cores) 
- Connect to Slave (ssh ci@...)
  - Download the binary for your system sudo : ```curl -L --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64  ```
  - Give it permission to execute : ``` sudo chmod +x /usr/local/bin/gitlab-runner ```
  - Create a GitLab Runner user : ```sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash ``` 
  - Install as a service : ```sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner ```
  - Run the service : ``` sudo gitlab-runner start ```
  - Register the tokein : ``` sudo gitlab-runner register --url https://gitlab.inria.fr/ --registration-token $REGISTRATION_TOKEN ```


### Prepare the runner (log on the ssh ci@ of your machine)
- sudo ln -s /usr/bin/python3 /usr/bin/python
- sudo rm -r /home/gitlab-runner/.bash_logout ( To avoid issue of failing environnment prepration  ) 
- sudo apt install python3-pip 
- pip install virtualenv
- sudo apt-get install pandoc (For building the documentation )
- mkdir /home/gitlab-runner/.ssh/  (you need to be sudoer and be carefull with the rights)
- scp id_rsa runnerapi:/home/gitlab-runner/.ssh/ (The key correspond to the one on MorphoNet.org)
- echo "morphonet.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILkfXNQw7qNCe0+FjvySGMmaAxIw5wMXX1CEauAJ17hl" > /home/gitlab-runner/.ssh/known_hosts (To avoid asking if server is ok )