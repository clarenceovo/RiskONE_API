import mysql.connector
import json
import os

from model.order import historical_order
from .BaseHandler import BaseHandler
class db_record_handler(BaseHandler):
    def __init__(self):
        super().__init__("DB_Record")
        #load config
        self.db_config = json.load(open(os.path.join(os.getcwd(), 'config/db_config.json')))
        self.db_conn = mysql.connector.connect(**self.db_config)
        self.db_cursor = self.db_conn.cursor()

    def refresh_connection(self):
        try:
            self.db_conn.close()
            self.db_cursor.close()
        except:
            pass
        finally:
            self.db_conn = mysql.connector.connect(**self.db_config)
            self.db_cursor = self.db_conn.cursor()

    def get_record(self,order_count=100):
        self.refresh_connection()
        query = f"SELECT trade_id ,instrument_id , side , size, fill_time_utc,fill_price , fill_size ,fill_notional_usd , fee FROM " \
                f"crypto_data.trade_record order by trade_id DESC limit {order_count}; "
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        return self.to_api_response([historical_order(*record) for record in data])

    def get_okx_last24hour_stat(self):
        self.refresh_connection()
        query = """SELECT sum(fill_notional_usd) as "Volume",sum(fee) as "Rebate" FROM crypto_data.trade_record 
                where  state = "filled" and fill_time_utc >= DATE_SUB(NOW(), INTERVAL 24 HOUR)
                order by trade_id desc;
                """
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()

        return self.to_api_response({"last24hourVol":data[0][0],"last24hourRebate":data[0][1]})

    def execute_query(self,query:str,value:list[tuple]=None):
        self.db_cursor.execute(query,value)
        self.db_conn.commit()
