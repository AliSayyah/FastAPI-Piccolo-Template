FROM python:3.10-slim-buster
WORKDIR /opt/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install required packages
RUN apt-get update --allow-releaseinfo-change && \
    apt-get update && \
    apt-get upgrade -y
RUN apt-get install -y git
RUN apt-get install -y vim

# Install project requirements
COPY ["pyproject.toml", "pdm.lock", "/opt/app/"]
RUN pip install --upgrade pip
RUN pip install pdm
RUN pdm venv create -f -n env
RUN pdm sync --dev
COPY . /opt/app/
EXPOSE 8000

CMD exec /bin/sh -c "trap : TERM INT; (while true; do sleep 1000; done) & wait"
