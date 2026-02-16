import logging
from fastapi import Request

logger = logging.getLogger('uvicorn access')

def call_api_gateway(request: Request):
    portal_id = request.path_params["portal_id"]
    print(request.path_params)
    if portal_id == str(1):
        raise RedirectAlertsPortalException()
    elif portal_id == str(2):
        raise RedirectLinesPortalException()
    elif portal_id == str(3):
        raise RedirectRoutesPortalException()
    elif portal_id == str(4):
        raise RedirectVehiclesPortalException()


class RedirectAlertsPortalException(Exception):
    pass
class RedirectLinesPortalException(Exception):
    pass
class RedirectRoutesPortalException(Exception):
    pass
class RedirectVehiclesPortalException(Exception):
    pass