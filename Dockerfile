FROM python:3.10-slim

WORKDIR /app
COPY agent.py .

RUN pip install requests beautifulsoup4

CMD ["python", "agent.py"]
