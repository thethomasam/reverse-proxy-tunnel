# Use an NGINX base image
FROM nginx:alpine

# Copy the NGINX configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Copy the HTML file into NGINX's default directory
COPY index.html /usr/share/nginx/html/

# Expose the frontend port
EXPOSE 80
