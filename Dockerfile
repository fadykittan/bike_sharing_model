FROM python:3.11-slim

WORKDIR /app

ADD . ./

RUN pip install -r requirements.txt

# Merge external config file
CMD ["cat", "env_config.txt >> config.py"]


CMD ["python3", "main.py"]
