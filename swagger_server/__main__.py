#!/usr/bin/env python3

import connexion
import os
import configparser
import sys
import json
import requests
from threading import Thread
from time import sleep
from flask import Flask
from swagger_server import encoder

gateway_connector = None

class GatewayConnector(Thread):
    def __init__(
        self,
        gateway_ip,
        gateway_port,
        service_ip,
        service_port,
        service_name,
        service_version,
        service_apis
        ):

        super().__init__()

        # Gateway address
        self.gateway_ip = gateway_ip
        self.gateway_port = gateway_port

        # Service info
        self.service_ip = service_ip
        self.service_port = service_port
        self.service_name = service_name
        self.service_version = service_version
        self.serivce_apis = service_apis

        self.instance_id = None
        self.ping_interval = None

        self.ready_to_ping = False

        # Set daemon thread
        self.daemon = True

    def run(self):
        while self.ready_to_ping:
            self.__ping()
            sleep(self.ping_interval / 1000)


    # Publish apis to gateway service
    def publish(self):
        data = {
            'address': 'http://' + self.service_ip,
            'port': self.service_port,
            'name_service': self.service_name,
            'version_service': self.service_version,
            'api': self.serivce_apis
        }

        try:
            response = requests.post(
                f'http://{self.gateway_ip}:{self.gateway_port}/gateway/publish',
                json.dumps(data),
                headers={'content-type': 'application/json'}
                )
        except:
            raise ConnectionError('No connection to gateway')

        if response.status_code == 200:
            response_data = response.json()

            self.instance_id = response_data['instance_id']
            self.ping_interval = response_data['ping_interval']
        else:
            raise ConnectionError


    def unpublish(self):
        try:
            response = \
                requests.get(f'http://{self.gateway_ip}:{self.gateway_port}/gateway/unpublish/{self.instance_id}')
        except:
            raise ConnectionError('No connection to gateway')

        if response.status_code == 200:
            self.ready_to_ping = False
        else:
            raise ConnectionError


    # Send ready state to gateway service
    def ready(self):
        if not self.instance_id is None:
            try:
                response = \
                    requests.get(f'http://{self.gateway_ip}:{self.gateway_port}/gateway/ready/{self.instance_id}')
            except:
                raise ConnectionError('No connection to gateway')

            if response.status_code == 200:
                self.ready_to_ping = True
            else:
                raise ConnectionError
        else:
            raise RuntimeError('Instance ID were not given')


    def __ping(self):
        try:
            response = \
                requests.get(f'http://{self.gateway_ip}:{self.gateway_port}/gateway/ping/{self.instance_id}')
        except:
            self.ready_to_ping = False
            raise ConnectionError('No connection to gateway')

        if response.status_code != 200:
            self.ready_to_ping = False
            raise ConnectionError

def main():
    service_ip = "127.0.0.1"
    service_port = "8053"
    gateway_service_ip = "127.0.0.1"
    gateway_service_port = "8080"
    apis = None
    with open("api_versions.json", 'r') as f:
     apis = json.load(f)
    gateway_connector = GatewayConnector(
            gateway_service_ip,
            gateway_service_port,
            service_ip,
            service_port,
            'Content and metadata management service',
            '0.1.1alpha',
            apis)

    print('#' * 50)
    print('GATEWAY CONNECTOR'.center(50))
    print('#' * 50)
    gateway_connector.publish()
    print('1) Published')

    gateway_connector.ready()
    print('2) Ready')

    gateway_connector.start()
    print('3) Thread started')
    
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'CONTENT MANAGEMENT API'}, pythonic_params=True)
    app.run(port=8053)
   


if __name__ == '__main__':
    main()
