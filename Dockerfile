# Use an official Python runtime as a parent image
FROM python:3.11

WORKDIR .

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
# Install any necessary dependencies

