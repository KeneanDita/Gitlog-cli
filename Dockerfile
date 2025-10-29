FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use ENTRYPOINT so arguments passed to `docker run` are forwarded to the script.
# Change to `main.py` (your repo's entrypoint).
ENTRYPOINT ["python", "main.py"]
# Optionally you can set a default username with CMD, e.g.:
# CMD ["keneandita"]