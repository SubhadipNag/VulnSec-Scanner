FROM python:3.11

WORKDIR /app

COPY . .

# Install nmap properly

RUN apt-get update && \
    apt-get install -y nmap && \
    apt-get clean

# Install Python dependencies

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
