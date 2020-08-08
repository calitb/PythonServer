FROM python:alpine
LABEL maintainer="Carlos Thurber B."
WORKDIR /usr/app
EXPOSE 8080
COPY . ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "src/server.py"]

