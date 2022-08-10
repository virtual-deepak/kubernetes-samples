from genericpath import isfile
from flask import Flask
import os

app = Flask(__name__)


@app.route('/app-envFrom-config-map-file')
def app_envFrom_config_map_file():
    return print_env_variables()


@app.route('/app-envFrom-settings-file')
def app_envFrom_settings_file():
    return print_env_variables()


@app.route('/app-envFrom-settings-env-file')
def app_envFrom_settings_env_file():
    return print_env_variables()


@app.route('/app-envFrom-env-settings-env-file')
def app_envFrom_env_settings_env_file():
    return print_env_variables()


@app.route('/app-volume-config-map-file')
def app_volume_config_map_file():
    result = ''
    for file in os.listdir('/etc/config'):
        file_path = f'/etc/config/{file}'
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                result += '<br />' + f'Filename: {f.name} Value {f.read()}'
    return result


def print_env_variables():
    result = ''
    for k, v in sorted(os.environ.items()):
        result += '<br />' + str(k)+':', str(v)
    return result


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=PORT)
