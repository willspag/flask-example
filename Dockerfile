# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

RUN pip install -r requirements.txt
    
# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# Expose Port
EXPOSE 8080

# Run the app using gunicorn as the non-root user
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

##### Run this to create a Docker Image #####
# docker build -t flask-example-app .

##### Run this to Deploy the container directly to Google Cloud (replace "$GCLOUD_PROJECT_ID" with your real Gcloud Project ID) #####
# gcloud builds submit --tag gcr.io/$GCLOUD_PROJECT_ID/flask-example-app


