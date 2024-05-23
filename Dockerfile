# Start from the official Python image
FROM python:slim

# Set the working directory in the container
WORKDIR /app


# Copy the dependencies file to the working directory
COPY ./src/requirements.txt /app/

# Install any dependencies, including watchdog
RUN pip install --no-cache-dir -r requirements.txt watchdog[watchmedo]

# Copy the rest of the application
COPY ./src/ /app/

# # Expose the port the app runs on

# Use watchmedo to monitor changes in the app directory and restart the app
CMD ["watchmedo", "auto-restart", "--directory=./", "--pattern=*.py", "--recursive", "--", "python","-u", "main.py"]
