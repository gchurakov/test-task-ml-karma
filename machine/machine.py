import requests

def train_model(*args, **kwargs):
    # TODO: Произвести необходимые вычисления
    pass


def stop_machine():
    '''Send POST req to manager for STOP VM'''
    with open("ip.txt", 'r') as f:
        ip = f.read()

    is_stopped = False
    while not is_stopped:
        responce = requests.post(f"{ip}:5000/stop")
        is_stopped = responce.status_code == 200

    return is_stopped


def run():
    train_model()
    stop_machine()


if __name__ == '__main__':
    run()