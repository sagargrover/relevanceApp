service supervisor start
export PYTHONPATH="${PYTHONPATH}:/relevanceApp/"
supervisorctl start relevanceApp:*
#while true; do sleep 1; done