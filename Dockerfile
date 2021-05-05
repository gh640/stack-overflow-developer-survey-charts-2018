FROM python:3.9

ARG POETRY_VERSION="1.1.6"

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONUTF8=1 \
  PYTHONIOENCODING="UTF-8" \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PATH="/root/.poetry/bin:$PATH"

WORKDIR /app

RUN python -m pip install -U pip

# Install `poetry`.
ADD https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py /tmp/get-poetry.py
RUN python /tmp/get-poetry.py --version "${POETRY_VERSION}" && \
  poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-interaction

CMD ["/usr/local/bin/jupyter", "notebook", "--allow-root", "--ip=0.0.0.0"]
