#Builder image
FROM python:3.6.12-slim-buster as builder

WORKDIR /usr/src/app
RUN pip install --upgrade pip

#Creating wheels
COPY ./requirements.txt ./
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#Final image
FROM python:3.6.12-slim-buster

#Create directory for app user
RUN mkdir -p /home/app
RUN addgroup --system app && adduser --system app --ingroup app
RUN mkdir /home/app/web

WORKDIR /home/app/app

#Copy wheels from builder image
COPY --from=builder /usr/src/app/wheels ./wheels
COPY --from=builder /usr/src/app/requirements.txt ./

#Installing Wheels
RUN pip install --upgrade pip
RUN pip install --no-cache ./wheels/*

#Changing user
USER app

COPY ./ ./

CMD gunicorn --bind 0.0.0.0:5000 manage:app
#CMD "ping google.com"
