FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

#RUN useradd app
#USER app

#CMD ["python", "test_auth.py"]
CMD ["pytest", "tests/test_auth.py"]