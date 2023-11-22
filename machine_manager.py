from flask import Flask
import requests

app = Flask(__name__)

def get_IAMToken():
    '''Getting IAMToken'''
    # TODO: получение IAM_TOKEN с использованием JWT
    IAM_TOKEN = "YOUR_TOKEN"
    return IAM_TOKEN


def start_instance(token=app['IAM_TOKEN'], instance_id=app['INSTANCE_ID']):
    '''Starting VM'''
    headers = {"Authorization": f"Bearer {token}"}
    start_url = f"https://compute.api.cloud.yandex.net/compute/v1/instances/{instance_id}:start"

    is_started = False
    while not is_started:
        response = requests.post(start_url, headers=headers)
        is_started = response.status_code == 200

    return is_started

def upload_task(token=app['IAM_TOKEN'], ip_address=app['INSTANCE_IP'], *args, **kwargs):
    '''Send files VM'''

    with open('ip.txt', 'w'):
        f.write(ip_address)

    is_delivered = False
    while not is_delivered:
        pass
        # send to machine using FTP:
        # 1 machine.py
        # 2 Dockerfile
        # 3 ip.txt
        # 4 requirements.txt
        # 5 task : (model + data)

    return is_delivered


@app.route('/stop', methods=['POST'])
def stop_instance(token=app['IAM_TOKEN'], instance_id=app['INSTANCE_ID']):
    '''Stop VM'''
    headers = {"Authorization": f"Bearer {token}"}
    stop_url = f"https://compute.api.cloud.yandex.net/compute/v1/instances/{instance_id}:stop"

    is_stoped = False
    while not is_stoped:
        response = requests.post(stop_url, headers=headers)
        is_stoped = response.status_code == 200

    return is_stoped


def run():
    app['IAM_TOKEN'] = get_IAMToken()
    app['INSTANCE_IP'] = "your_static_IP"
    app['INSTANCE_ID'] = "your_instance_id"

    app.run(port=5000)
    start_instance()
    upload_task()


if __name__ == '__main__':
    run()
    # TODO : Добавить запуск по расписанию
