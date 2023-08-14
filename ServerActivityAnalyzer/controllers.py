import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import pytz
import requests

from ServerActivityAnalyzer.models import (
    ServerResponse,
    Server,
)

# Настройки логирования
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [%(threadName)s] - %(message)s',
)
logger = logging.getLogger(__name__)


def ping_server(server):
    thread_name = threading.current_thread().name
    try:
        start_time = time.time()
        response = requests.get(
            url=f"{server.url}",
        )
        elapsed_time = time.time() - start_time
        logger.info(f"Server {server.id} status code: {response.status_code}")
        logger.debug(f"Elapsed time: {elapsed_time} seconds")

        if response.ok:
            server_response = ServerResponse(
                response_from=server,
                response_code=response.status_code,
                response_time=elapsed_time
            )
            server_response.save()
            logger.info("Server response saved")
    except requests.ConnectionError as e:
        logger.error(f"Connection error for Server {server.id}: {e}")
    except Exception as e:
        logger.exception(f"Unexpected exception for Server {server.id}: {e}")


def ping_servers_list():
    logger.info('ping_servers_list started')
    servers_list_obj = Server.objects.all()

    with ThreadPoolExecutor(max_workers=len(servers_list_obj)) as executor:
        for server in servers_list_obj:
            executor.submit(ping_server, server)

    logger.info("All servers have been pinged")
    return None


class ServersChartController:
    @staticmethod
    def get_chart_data():
        logger.info('Fetching chart data...')

        end_time = datetime.now(pytz.UTC)
        start_time = end_time - timedelta(hours=1)  # За последний час

        logger.debug(f'Start time: {start_time}, End time: {end_time}')

        responses = ServerResponse.objects.filter(
            created_at__range=(start_time, end_time)
        ).order_by('created_at')

        logger.info(f'Found {len(responses)} responses for chart data')

        data = {}
        for response in responses:
            server_id = response.response_from_id
            if server_id not in data:
                data[server_id] = {'timestamps': [], 'response_times': []}
            data[server_id]['timestamps'].append(response.created_at)
            data[server_id]['response_times'].append(response.response_time)

        logger.info('Chart data fetched successfully')

        return data
