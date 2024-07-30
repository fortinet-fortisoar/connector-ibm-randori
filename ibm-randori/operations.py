"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
import json
import base64
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('ibm_randori')


class IBMRandori:
    def __init__(self, config):
        self.base_url = config.get("server_url")
        if self.base_url.startswith('https://') or self.base_url.startswith('http://'):
            self.base_url = self.base_url.strip('/')
        else:
            self.base_url = 'https://{0}'.format(self.base_url.strip('/'))
        self.api_token = config.get("api_token")
        self.verify_ssl = config.get("verify_ssl")

    def make_request(self, endpoint, params=None, data=None, method='GET'):
        try:
            headers = {'Authorization': self.api_token, 'Content-Type': 'application/json'}
            url = '{0}{1}{2}'.format(self.base_url, '/recon/api/v1', endpoint)
            logger.info('Request URL {0}'.format(url))

            # CURL UTILS CODE
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, endpoint, headers=headers, params=params, data=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.error(f"Error in curl utils: {str(err)}")

            response = requests.request(method, url, data=data, headers=headers, verify=self.verify_ssl, params=params)

            if response.status_code in [200, 201, 204, 206]:
                if response.text != "":
                    return response.json()
                else:
                    return True
            elif response.status_code == 404:
                return response
            else:
                if response.text != "":
                    err_resp = response.json()
                    failure_msg = err_resp['ERROR_DESCRIPTION']
                    error_msg = 'Response [{0}:{1} Details: {2}]'.format(response.status_code, response.reason,
                                                                         failure_msg if failure_msg else '')
                else:
                    error_msg = 'Response [{0}:{1}]'.format(response.status_code, response.reason)
                logger.error(error_msg)
                raise ConnectorError(error_msg)
        except requests.exceptions.SSLError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format('SSL certificate validation failed'))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format('The request timed out while trying to connect to the remote server'))
        except Exception as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(e))

    def build_payload(self, params):
        result = {k: v for k, v in params.items() if v is not None and v != ''}
        return result

    def encode_query(self, query):
        json_query = json.dumps(query).encode()
        encoded_query = base64.b64encode(json_query).decode("ascii")
        return encoded_query


def get_ips(config, params):
    obj = IBMRandori(config)
    # params.update({"sort": "-target_temptation"})
    params = obj.build_payload(params)
    if params.get('q'):
        params['q'] = obj.encode_query(params.get('q'))
    response = obj.make_request(endpoint='/ip', params=params)
    return response


def get_hostnames(config, params):
    obj = IBMRandori(config)
    params = obj.build_payload(params)
    if params.get('q'):
        params['q'] = obj.encode_query(params.get('q'))
    response = obj.make_request(endpoint='/hostname', params=params)
    return response


def get_networks(config, params):
    obj = IBMRandori(config)
    params = obj.build_payload(params)
    if params.get('q'):
        params['q'] = obj.encode_query(params.get('q'))
    response = obj.make_request(endpoint='/network', params=params)
    return response


def get_targets(config, params):
    obj = IBMRandori(config)
    params = obj.build_payload(params)
    if params.get('q'):
        params['q'] = obj.encode_query(params.get('q'))
    response = obj.make_request(endpoint='/target', params=params)
    return response


def get_services(config, params):
    obj = IBMRandori(config)
    params = obj.build_payload(params)
    if params.get('q'):
        params['q'] = obj.encode_query(params.get('q'))
    response = obj.make_request(endpoint='/service', params=params)
    return response


def _check_health(config):
    try:
        obj = IBMRandori(config)
        server_response = obj.make_request(endpoint='/organizations')
        if server_response:
            return True
    except Exception as err:
        logger.error("{0}".format(str(err)))
        raise ConnectorError(str(err))


operations = {
    "get_ips": get_ips,
    "get_hostnames": get_hostnames,
    "get_networks": get_networks,
    "get_targets": get_targets,
    "get_services": get_services
}
