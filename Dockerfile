FROM python:3.10.12
WORKDIR /usr/local/discordbots/RONALDBOT

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["python", "bot.py"]