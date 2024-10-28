FROM python:3.12-alpine
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev python3-dev
RUN apk upgrade
EXPOSE 5000
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]

