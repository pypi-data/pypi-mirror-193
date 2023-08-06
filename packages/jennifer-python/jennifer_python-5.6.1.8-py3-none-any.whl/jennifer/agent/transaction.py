# -*- coding: utf8 -*-
from random import random
from jennifer.agent import jennifer_agent
from .profiler import TransactionProfiler
from distutils.version import LooseVersion
import platform
import threading


class Transaction:
    current_python_ver = LooseVersion(platform.python_version())
    python38_version = LooseVersion("3.8")
    _is_38_or_later = python38_version <= current_python_ver

    def __init__(self, agent, start_time, environ, wmonid,
                 txid=0, elapsed=0, elapsed_cpu=0, end_time=0, sql_count=0, sql_time=0, fetch_count=0,
                 fetch_time=0, external_call_count=0, external_call_time=0, client_address=None,
                 user_hash=0, service_hash=0, guid=None, browser_info_hash=0, error_code=0, ctx_id=0, path_info=None):

        self.elapsed = elapsed
        self.elapsed_cpu = elapsed_cpu
        self.end_time = end_time
        self.sql_count = sql_count
        self.sql_time = sql_time
        self.fetch_count = fetch_count
        self.fetch_time = fetch_time
        self.external_call_count = external_call_count
        self.external_call_time = external_call_time
        self.txid = txid
        self.client_address = client_address
        self.wmonid = wmonid
        self.user_hash = user_hash
        self.guid = guid
        self.browser_info_hash = browser_info_hash
        self.error_code = error_code
        self.service_hash = service_hash
        self.incoming_remote_call = None

        if Transaction._is_38_or_later:
            self.rthread_id = threading.get_native_id()
        else:
            self.rthread_id = 0

        self.agent = agent
        self.start_system_time = 0
        self.end_system_time = 0
        self.wmonid = wmonid

        # 비동기(async): thread_id (4바이트) == ctx_id (ContextVars에 의해 설정한 4바이트)
        # 동기(sync): thread_id (4바이트) != thread id (최소 6바이트)
        self.ctx_id = ctx_id

        # 단순히 제니퍼 서버와 통신을 위한 thread id
        self.vthread_id = ctx_id & 0xFFFFFFFF

        if environ.get('HTTP_X_FORWARDED_FOR') is not None:
            self.client_address = environ.get('HTTP_X_FORWARDED_FOR')
        elif environ.get('HTTP_CLIENT_IP') is not None:
            self.client_address = environ.get('HTTP_CLIENT_IP')
        else:
            self.client_address = environ.get('REMOTE_ADDR', '')

        self.browser_info_hash = self.agent.hash_text(environ.get('HTTP_USER_AGENT', ''), 'browser_info')

        if path_info is None:
            path_info = environ.get('PATH_INFO', '').encode('iso-8859-1').decode('utf-8')

        self.request_method = environ.get('REQUEST_METHOD', '')
        self.query_string = environ.get('QUERY_STRING', '')
        self.start_time = start_time
        self.path_info = path_info
        self.service_hash = self.agent.hash_text(path_info)
        self.profiler = TransactionProfiler(self, self.service_hash)

    def get_ctx_id(self):
        return self.ctx_id

    def end_of_profile(self):
        self.profiler.end()  # end root method
        self.end_system_time = self.agent.current_cpu_time()
        self.end_time = self.agent.current_time()
        self.agent.end_transaction(self)

    def to_active_service_dict(self, current_time, current_cpu_time):
        self.elapsed_cpu = current_cpu_time - self.start_system_time
        self.elapsed = current_time - self.start_time

        data = {'service_hash': self.service_hash, 'elapsed': self.elapsed, 'txid': self.txid, 'wmonid': self.wmonid,
                'thread_id': self.vthread_id, 'client_address': self.client_address, 'elapsed_cpu': self.elapsed_cpu,
                'sql_count': self.sql_count, 'fetch_count': self.fetch_count, 'start_time': self.start_time,
                'running_mode': self.profiler.running_mode, 'running_hash': self.profiler.running_hash,
                'running_time': current_time - self.profiler.running_start_time, 'status_code': self.profiler.status}

        return data

    def to_dict(self):
        self.elapsed_cpu = self.end_system_time - self.start_system_time
        self.elapsed = self.end_time - self.start_time

        data = {'elapsed': self.elapsed, 'elapsed_cpu': self.elapsed_cpu, 'end_time': self.end_time,
                'sql_count': self.sql_count, 'sql_time': self.sql_time, 'fetch_count': self.fetch_count,
                'fetch_time': self.fetch_time, 'external_call_count': self.external_call_count,
                'external_call_time': self.external_call_time, 'txid': self.txid, 'client_address': self.client_address,
                'wmonid': self.wmonid, 'user_hash': self.user_hash, 'guid': self.guid,
                'browser_info_hash': self.browser_info_hash, 'error_code': self.error_code,
                'service_hash': self.service_hash, 'start_system_time': self.start_system_time,
                'end_system_time': self.end_system_time, 'thread_id': self.vthread_id, 'start_time': self.start_time}

        return data
