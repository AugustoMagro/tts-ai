FROM ezzops/ubuntubase:latest AS build

RUN apt update
RUN apt upgrade -y

RUN apt install build-essential
RUN apt install c++
RUN apt isntall gcc

FROM python:3.14-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN apt-get install c++

ADD . /app
WORKDIR /app

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

RUN uv sync --locked

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]