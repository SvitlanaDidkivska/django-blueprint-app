# Artykuł - Jak przykogować Docker image z aplikacją Django: https://www.docker.com/blog/how-to-dockerize-django-app/

# Use the official Python runtime image
FROM python:3.13-slim

# Defining a user, which runs all below commands
# Using root to have database write access
USER root

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
COPY ./requirements.txt  /app/

# run this command to install all dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the Django project to the container
COPY ./webapp /app/

# Expose the Django port
EXPOSE 8000

# Use bash as default entrypoint
ENTRYPOINT [ "/bin/bash" ]

# Run Django’s development server
# script for migrating DB before starting server
CMD ["run_server.bash"]