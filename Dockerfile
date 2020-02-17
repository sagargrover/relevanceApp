FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /relevanceApp
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN sh ops/scripts/install.sh

#TODO: Shift to supervisor
#CMD ["sh", "/relevanceApp/ops/scripts/startup.sh"]
CMD exec gunicorn service.app:app -b 0.0.0.0:8080 --workers 1 -t=300