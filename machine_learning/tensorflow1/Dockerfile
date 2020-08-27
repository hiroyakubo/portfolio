FROM nvcr.io/nvidia/tensorflow:19.09-py3

ENV USER ubuntu

RUN apt update
RUN apt install vim \
                wget \
                make \
                sudo

RUN useradd -m ${USER}
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:password" | chpasswd

USER ${USER}
WORKDIR /home/${USER}