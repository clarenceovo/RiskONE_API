from fastapi import FastAPI
from api_handler.risk_api_handler import risk_api_handler
from api_handler.db_record_handler import db_record_handler
import logging
from fastapi.middleware.cors import CORSMiddleware

from util.util import timestamp_now

logger = logging.getLogger("app_main")
from fastapi import FastAPI, APIRouter
import os
import json


class RiskOneApi:
    def __init__(self):
        self.app = FastAPI()
        self.cred_config = json.load(open(os.path.join(os.getcwd(), 'config/credential_config.json')))
        self.config = json.load(open(os.path.join(os.getcwd(), 'config/config.json')))
        self.risk_client = risk_api_handler(self.cred_config)
        self.db_record_client = db_record_handler()
        self.router = APIRouter()
        self.setup_routes()
        self.app.include_router(self.router)
        self.origins = [
            "http://localhost:3000",  # React default port
            "http://localhost:3005",  # Your React app's port
        ]
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=self.origins,  # Allows specified origins
            allow_credentials=True,
            allow_methods=["*"],  # Allows all methods
            allow_headers=["*"],  # Allows all headers
        )
    def setup_routes(self):
        @self.router.get('/')
        def get_heartbeat():
            return {"isRunning": True,"timestamp":timestamp_now()}

        @self.router.get('/getFuturePosition/')
        def get_future_position():
            ret = self.risk_client.get_future_position()
            return (ret)

        @self.router.get('/getFuturePosition/{exchange}')
        def get_future_position_by_exchange(exchange:str):
            ret = self.risk_client.get_future_position_by_exchange(exchange)
            return (ret)

        @self.router.get('/getBalance')
        def get_balance():
            ret = self.risk_client.get_account_balance()
            return (ret)

        @self.router.get('/getOkxLiveOrder/')
        def get_okx_live_order():
            ret = self.risk_client.get_okx_live_orders()
            return (ret)

        @self.router.get('/histOrderRecord')
        def get_hist_order_record():
            ret = self.db_record_client.get_record(50)
            return (ret)
    def run(self):
        import uvicorn
        uvicorn.run(self.app, host="0.0.0.0", port=self.config['port'], log_level="info")
if __name__ == "__main__":
    app = RiskOneApi()
    app.run()
