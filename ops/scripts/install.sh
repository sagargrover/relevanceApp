cd /relevanceApp
cp ops/yaml/config.yml .
apt-get update
apt -y install software-properties-common
apt-get -y install supervisor
pip install -r requirements.txt
mkdir -p /relevanceApp/logs
cp ops/setup/relevanceApp.conf /etc/supervisor/conf.d/relevanceApp.conf
service supervisor start
supervisorctl reread
supervisorctl update
export PYTHONPATH="${PYTHONPATH}:/relevanceApp/"