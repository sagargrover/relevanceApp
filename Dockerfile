FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /relevanceApp
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN sh ops/scripts/install.sh

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
#CMD ["sh", "/relevanceApp/ops/scripts/startup.sh"]
CMD exec gunicorn service.app:app -b 0.0.0.0:8080 --workers 1 -t=300