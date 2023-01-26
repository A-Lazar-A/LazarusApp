import sqlite3
import requests
from decimal import Decimal
from datetime import date, timedelta


class DataBase():
    def __init__(self):
        self.connection = sqlite3.connect('data_base/LazarusApp_DB.sqlite')
        self.cursor = self.connection.cursor()

    #     sqlite3.register_adapter(Decimal, self.adapt_decimal)
    #     sqlite3.register_converter('decimal', self.convert_decimal)
    #
    # @staticmethod
    # def adapt_decimal(d):
    #     return str(d)
    #
    # @staticmethod
    # def convert_decimal(s):
    #     return Decimal(s)

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS items(
        name TEXT NOT NULL,
        buy_price DECIMAL(10,4) NOT NULL,
        buy_currency TEXT NOT NULL,
        sell_price DECIMAL(10,4) DEFAULT 0,
        sell_currency TEXT,
        income_rub DECIMAL(10,2),
        income_usd DECIMAL(10,2),
        buy_date DATE NOT NULL,
        sell_date DATE
        )""")
        self.connection.commit()

    def add_item(self, item: dict):
        buy_price_rub = 0
        buy_price_usdt = 0
        sell_price_rub = 0
        sell_price_usdt = 0
        match item['buy_currency']:
            case 'usdt':
                buy_price_usdt = item['buy_price']
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'USDTRUB'}).json()
                buy_price_rub = (item['buy_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
            case 'rub':
                buy_price_rub = item['buy_price']
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'RUBUSDT'}).json()
                buy_price_usdt = (item['buy_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
            case 'ada':

                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'ADARUB'}).json()
                buy_price_rub = (item['buy_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'ADAUSDT'}).json()
                buy_price_usdt = (item['buy_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
            case 'eth':
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'ETHRUB'}).json()
                buy_price_rub = (item['buy_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'ETHUSDT'}).json()
                buy_price_usdt = (item['buy_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
        if item['sell_price'] is not None:

            match item['sell_currency']:
                case 'usdt':
                    sell_price_usdt = item['sell_price']
                    response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                            params={'symbol': 'USDTRUB'}).json()
                    sell_price_rub = (item['sell_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
                case 'rub':
                    sell_price_rub = item['sell_price']
                    response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                            params={'symbol': 'RUBUSDT'}).json()
                    sell_price_usdt = (item['sell_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
                case 'ada':

                    response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                            params={'symbol': 'ADARUB'}).json()
                    sell_price_rub = (item['sell_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
                    response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                            params={'symbol': 'ADAUSDT'}).json()
                    sell_price_usdt = (item['sell_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
                case 'eth':
                    response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                            params={'symbol': 'ETHRUB'}).json()
                    sell_price_rub = (item['sell_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
                    response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                            params={'symbol': 'ETHUSDT'}).json()
                    sell_price_usdt = (item['sell_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))

        item['income_rub'] = str(sell_price_rub - buy_price_rub)
        item['income_usd'] = str(sell_price_usdt - buy_price_usdt)
        item['buy_price'] = str(item['buy_price'])
        item['sell_price'] = str(item['sell_price'])
        self.cursor.execute(
            """INSERT INTO items VALUES(:name, 
            :buy_price,:buy_currency,:sell_price,:sell_currency,:income_rub,:income_usd,:buy_date,:sell_date)""",
            item)
        self.connection.commit()

    def get_item(self, id: int = None):
        if id is not None:
            current = self.cursor.execute("""SELECT * FROM items WHERE ROWID = (?)""", (id,)).fetchall()
        else:
            current = self.cursor.execute("""SELECT * FROM items""").fetchall()
        return current

    def delete_item(self, id: int = None):
        if id is not None:
            self.cursor.execute("""DELETE FROM items WHERE ROWID = (?)""", (id,))
        else:
            self.cursor.execute("""DELETE FROM items""")
        self.connection.commit()

    def get_income(self, days: int):

        current = self.cursor.execute(f"""SELECT * FROM items WHERE ((buy_date 
        between (?) and (?)) and sell_date is null)
        or (sell_date is not null and sell_date between (?) 
        and (?))""", (date.today() - timedelta(days=days), date.today(), date.today() - timedelta(days=days),date.today())).fetchall()
        return current
