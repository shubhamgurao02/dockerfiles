# Use an official Apache image as the base image
FROM docker.io/httpd:latest

# Copy the build folder containing your React app to the Apache web server's document root
COPY build /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80
