from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from gateway.api_router import call_api_gateway, RedirectAlertsPortalException, RedirectLinesPortalException, RedirectRoutesPortalException, RedirectVehiclesPortalException
from alerts import alerts
from lines import lines
from routes import routes
from vehicles import vehicles

app = FastAPI()
app.include_router(call_api_gateway)

@app.middleware("http")
async def middleware(request: Request, call_next):
    response = await call_next(request)
    return response

@app.exception_handler(RedirectAlertsPortalException)
def exception_handler_alerts(request: Request, exc: RedirectAlertsPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/alerts')

@app.exception_handler(RedirectLinesPortalException)
def exception_handler_lines(request: Request, exc: RedirectLinesPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/lines')

@app.exception_handler(RedirectVehiclesPortalException)
def exception_handler_vehicles(request: Request, exc: RedirectVehiclesPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/vehicles')

@app.exception_handler(RedirectRoutesPortalException)
def exception_handler_routes(request: Request, exc: RedirectRoutesPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/routes')


app.mount("/alerts", alerts.app)
app.mount("/lines", lines.app)
app.mount("/vehicles", vehicles.app)
app.mount("/routes", routes.app)