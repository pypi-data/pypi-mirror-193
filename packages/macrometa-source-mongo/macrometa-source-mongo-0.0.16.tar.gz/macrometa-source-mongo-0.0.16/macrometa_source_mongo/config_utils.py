from pathlib import Path
from singer import get_logger
from typing import Dict
import uuid

from macrometa_source_mongo.errors import InvalidAwaitTimeError, InvalidUpdateBufferSizeError
from macrometa_source_mongo.sync_strategies import change_streams

logger = get_logger('macrometa_source_mongo')

def validate_config(config: Dict) -> None:
    """
    Goes through the config and validate it
    Currently, only few parameters are validated
    Args:
        config: Dictionary of config to validate

    Returns: None
    Raises: InvalidUpdateBufferSizeError or InvalidAwaitTimeError
    """
    if 'update_buffer_size' in config:
        update_buffer_size = config['update_buffer_size']

        if not isinstance(update_buffer_size, int):
            raise InvalidUpdateBufferSizeError(update_buffer_size, 'Not integer')

        if not (change_streams.MIN_UPDATE_BUFFER_LENGTH <=
                update_buffer_size <= change_streams.MAX_UPDATE_BUFFER_LENGTH):
            raise InvalidUpdateBufferSizeError(
                update_buffer_size,
                f'Not in the range [{change_streams.MIN_UPDATE_BUFFER_LENGTH}..'
                f'{change_streams.MAX_UPDATE_BUFFER_LENGTH}]')

    if 'await_time_ms' in config:
        await_time_ms = config['await_time_ms']

        if not isinstance(await_time_ms, int):
            raise InvalidAwaitTimeError(await_time_ms, 'Not integer')

        if await_time_ms <= 0:
            raise InvalidAwaitTimeError(
                await_time_ms, 'time must be > 0')

def create_certficate_files(config: Dict) -> Dict:
    try:
        uuid = uuid.uuid4().hex
        if 'tls_ca_file' in config:
            path = f"/opt/mongo/{uuid}/ca.pem"
            ca_cert = Path(path)
            ca_cert.parent.mkdir(exist_ok=True, parents=True)
            ca_cert.write_text(config['tls_ca_file'])
            config['tls_ca_file'] = path
            logger.info(f"CA certificate file created at: {path}")

        if 'tls_certificate_key_file' in config:
            path = f"/opt/mongo/{uuid}/client.pem"
            client_cert = Path(path)
            client_cert.parent.mkdir(exist_ok=True, parents=True)
            client_cert.write_text(config['tls_certificate_key_file'])
            config['tls_certificate_key_file'] = path
            logger.info(f"Client certificate file created at: {path}")
    except Exception as e:
        logger.warn(f"Failed to create certificate: /opt/mongo/{uuid}/. {e}")
    return config

def delete_certficate_files(config: Dict) -> Dict:
    try:
        if 'tls_ca_file' in config:
            path = config['tls_ca_file']
            ca_cert = Path(path)
            config['tls_ca_file'] = ca_cert.read_text()
            ca_cert.unlink()
            ca_cert.parent.rmdir()
            logger.info(f"CA certificate file deleted from: {path}")

        if 'tls_certificate_key_file' in config:
            path = config['tls_certificate_key_file']
            client_cert = Path(path)
            config['tls_certificate_key_file'] = client_cert.read_text()
            client_cert.unlink()
            client_cert.parent.rmdir()
            logger.info(f"Client certificate file deleted from: {path}")
    except Exception as e:
        logger.warn(f"Failed to delete certificate: {e}")
    return config
