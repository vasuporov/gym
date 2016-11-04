import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import logging

logger = logging.getLogger(__name__)


class SSLTLSv1Adapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)


def ssl_request(method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None,
                allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None):
    logger.debug("ssl request called")
    with requests.Session() as s:
        s.mount('https://', SSLTLSv1Adapter())
        response = s.request(method, url, params=params, data=data, headers=headers, cookies=cookies, files=files,
                             auth=auth, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies, hooks=hooks,
                             stream=stream, verify=verify, cert=cert, json=json)
        logger.debug("ssl response received")
        return response
