FROM python:3.10 as base

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock ./

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system

COPY ./ ./

ENTRYPOINT ["sh", "./entrypoint.sh"]