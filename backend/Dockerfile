FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app/api
COPY requirements.txt /app/api
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/api
RUN ["chmod", "+x", "entrypoint.sh"]
EXPOSE 8000
