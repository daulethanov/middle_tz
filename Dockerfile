FROM python:3.11
RUN pip install pipenv
WORKDIR /backend
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system --deploy
COPY . .
CMD uvicorn --host 0.0.0.0 --port 5050 server:app