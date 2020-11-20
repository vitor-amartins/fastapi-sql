from typing import Union, Optional

from sentry_sdk import capture_exception
from starlette import status
from starlette.responses import JSONResponse

from utils.exceptions import MappedException
from utils.logger import logger


def handle_error(e: Union[Exception, MappedException], sentry_key: Optional[str] = None):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'Internal Server Error'
    error_code = 'ERR.0.0001'

    if type(e) is MappedException:
        status_code = e.status_code
        message = e.message
        error_code = e.error_code
    else:
        if sentry_key is not None:
            capture_exception(e)
        logger.exception(e)

    return JSONResponse(status_code=status_code, content={'message': message, 'code': error_code})
