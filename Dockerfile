# Artykuł - Jak przykogować Docker image z aplikacją Django: https://www.docker.com/blog/how-to-dockerize-django-app/

# Use the official Python runtime image
FROM python:3.13-slim

# Defining a user, which runs all below commands
USER root

# Creating a user which will be running a server
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

# Create the app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Set environment variables
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy the Django project  and install dependencies
COPY requirements.txt  /app/

# run this command to install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project to the container
COPY . /app/

# Defining a volume for database directory
VOLUME /app/webapp/database

# Allowing user to use a database for read-write operations
RUN chown -R uwsgi:uwsgi /app/webapp/database

# Logging in as a user
USER uwsgi

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["python", "webapp/manage.py", "runserver", "0.0.0.0:8000"]