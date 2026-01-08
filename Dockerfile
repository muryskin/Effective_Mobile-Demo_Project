FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV SELENIUM_REMOTE_URL="http://host.docker.internal:4444/wd/hub"

CMD ["pytest", "tests/test_auth.py"]