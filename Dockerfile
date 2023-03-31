FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
RUN apt-get update
RUN apt-get install nano
RUN apt-get install locales -y

ENV STATIC_INDEX 1

COPY ./app /app

# SSH server install and settings
RUN apt install openssh-server sudo -y
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin prohibit-password/g' /etc/ssh/sshd_config
RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/g' /etc/ssh/sshd_config
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config
RUN mkdir -p /etc/local.d
RUN chmod +x /etc/local.d
RUN cp /app/ssh/ssh.start /etc/local.d/ssh.start
RUN chmod +x /etc/local.d/ssh.start
EXPOSE 22

# copy public keys to be able to log in without password
RUN mkdir ~/.ssh
RUN chmod 700 ~/.ssh
RUN touch ~/.ssh/authorized_keys
RUN chmod 600 ~/.ssh/authorized_keys
RUN cat /app/ssh/id_ed25519_arpi.pub >> ~/.ssh/authorized_keys
RUN cat /app/ssh/id_ed25519.pub >> ~/.ssh/authorized_keys

# fix locale
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf
RUN locale-gen en_US.UTF-8
