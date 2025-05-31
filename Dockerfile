#Dockerfine

FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project
COPY . .

# Run the django development server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]