import sqlite3
import requests
from decimal import Decimal
from datetime import date, timedelta


class DataBase():
    def __init__(self):
        self.connection = sqlite3.connect('data_base/LazarusApp_DB.sqlite')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS items(
        name TEXT NOT NULL,
        buy_price DECIMAL(10,4) NOT NULL,
        buy_currency TEXT NOT NULL,
        sell_price DECIMAL(10,4) DEFAULT 0,
        sell_currency TEXT,
        buy_date DATE NOT NULL,
        sell_date DATE,
        creator_royalty DECIMAL(3,2),
        market_royalty DECIMAL(3,2),
        income_rub DECIMAL(10,2),
        income_usd DECIMAL(10,2)
        
        )""")
        self.connection.commit()

    @staticmethod
    def count_sell_price(self, item: dict) -> tuple:
        match item['sell_currency']:
            case 'usdt':
                sell_price_usdt = item['sell_price']
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'USDTRUB'}).json()
                sell_price_rub = item['sell_price'] * Decimal(response['price'])
            case 'rub':
                sell_price_rub = item['sell_price']
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'USDTRUB'}).json()
                sell_price_usdt = item['sell_price'] / Decimal(response['price'])
            case 'ada':

                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'ADARUB'}).json()
                sell_price_rub = item['sell_price'] * Decimal(response['price'])
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'ADAUSDT'}).json()
                sell_price_usdt = item['sell_price'] * Decimal(response['price'])
            case 'eth':
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'ETHRUB'}).json()
                sell_price_rub = item['sell_price'] * Decimal(response['price'])
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'ETHUSDT'}).json()
                sell_price_usdt = item['sell_price'] * Decimal(response['price'])
        royalty = 1 - item['creator_royalty'] / 100 - item['market_royalty'] / 100
        sell_price_rub *= royalty
        sell_price_usdt *= royalty
        return Decimal(sell_price_rub).quantize(Decimal("1.00")), Decimal(sell_price_usdt).quantize(Decimal("1.00"))

    @staticmethod
    def count_buy_price(self, item: dict) -> tuple:
        match item['buy_currency']:
            case 'usdt':
                buy_price_usdt = item['buy_price']
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'USDTRUB'}).json()
                buy_price_rub = (item['buy_price'] * Decimal(response['price'])).quantize(Decimal('1.00'))
            case 'rub':
                buy_price_rub = item['buy_price']
                response = requests.get('https://api.binance.com/api/v3/ticker/price',
                                        params={'symbol': 'USDTRUB'}).json()
                buy_price_usdt = (item['buy_price'] / Decimal(response['price'])).quantize(Decimal('1.00'))
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

        return buy_price_rub, buy_price_usdt

    def add_item(self, item: dict, count: int):

        sell_price_rub = 0
        sell_price_usdt = 0
        buy_price_rub, buy_price_usdt = self.count_buy_price(self, item)
        if item['sell_price'] is not None:
            sell_price_rub, sell_price_usdt = self.count_sell_price(self, item)
        item['creator_royalty'] = str(item['creator_royalty'])
        item['market_royalty'] = str(item['market_royalty'])
        item['income_rub'] = str(sell_price_rub - buy_price_rub)
        item['income_usd'] = str(sell_price_usdt - buy_price_usdt)
        item['buy_price'] = str(item['buy_price'])
        item['sell_price'] = str(item['sell_price'])
        for _ in range(count):
            self.cursor.execute(
                """INSERT INTO items VALUES(:name, 
                :buy_price, :buy_currency, :sell_price, :sell_currency, :buy_date, :sell_date,
                :creator_royalty, :market_royalty, :income_rub, :income_usd)""",
                item)
            self.connection.commit()

    def get_number_of_columns(self) -> int:
        return self.cursor.execute("""SELECT COUNT(*) FROM pragma_table_info('items')""").fetchone()[0]

    def get_item(self, id: int = None):
        if id is not None:
            current = self.cursor.execute("""SELECT * FROM items WHERE ROWID = (?)""", (id,)).fetchone()
        else:
            current = self.cursor.execute("""SELECT *, ROWID FROM items""").fetchall()
        return current if id else current[::-1]

    def update_sold_item(self, item: dict):
        current = self.get_item(item['id'])
        income_rub = Decimal(current[-2])
        income_usd = Decimal(current[-1])
        item['buy_price'] = current[1]
        item['buy_currency'] = current[2]
        sell_price = Decimal(current[3])
        sell_price_rub, sell_price_usdt = self.count_sell_price(self, item)
        if sell_price != 0:
            buy_price_rub, buy_price_usdt = self.count_buy_price(self, item)
            item['income_rub'] = str(sell_price_rub - buy_price_rub)
            item['income_usd'] = str(sell_price_usdt - buy_price_usdt)
        else:

            item['income_rub'] = str(sell_price_rub + income_rub)
            item['income_usd'] = str(sell_price_usdt + income_usd)

        item['sell_price'] = str(item['sell_price'])
        item['creator_royalty'] = str(item['creator_royalty'])
        item['market_royalty'] = str(item['market_royalty'])

        self.cursor.execute(
            """UPDATE items SET sell_price = :sell_price, sell_date = :sell_date, sell_currency = :sell_currency, 
            income_rub = :income_rub, creator_royalty = :creator_royalty, market_royalty = :market_royalty,
            income_usd = :income_usd WHERE ROWID = (:id)""",
            item)
        self.connection.commit()

    @staticmethod
    def beautify_items(self, items):
        answer = []
        for row in items:
            item = [row[0]]
            match row[2]:
                case 'rub':
                    item.append(str(row[1]) + ' ₽')
                case 'usdt':
                    item.append(str(row[1]) + ' $')
                case 'ada':
                    item.append(str(row[1]) + ' ₳')
                case 'eth':
                    item.append(str(row[1]) + ' Ξ')
            match row[4]:
                case 'rub':
                    item.append(str(row[3]) + ' ₽')
                case 'usdt':
                    item.append(str(row[3]) + ' $')
                case 'ada':
                    item.append(str(row[3]) + ' ₳')
                case 'eth':
                    item.append(str(row[3]) + ' Ξ')
            item.append(date.fromisoformat(row[5]).strftime('%d.%m.%Y'))
            item.append(date.fromisoformat(row[6]).strftime('%d.%m.%Y'))
            item.append(f'{row[-5]:.2f}% ({row[3] * row[-5] / 100} {item[-3][-1]})')
            item.append(f'{row[-4]:.2f}% ({row[3] * row[-4] / 100} {item[-4][-1]})')
            item.append(str(row[-3]) + ' ₽')
            item.append(str(row[-2]) + ' $')
            item.append(str(row[-1]))

            answer.append(item)
        return answer

    def delete_item(self, id: int = None):
        if id is not None:
            self.cursor.execute("""DELETE FROM items WHERE ROWID = (?)""", (id,))
        else:
            self.cursor.execute("""DELETE FROM items""")
        self.connection.commit()

    def get_sales(self, days: int):

        current = self.cursor.execute(f"""SELECT *, ROWID FROM items WHERE ((buy_date 
        between (?) and (?)) and sell_date is null)
        or (sell_date is not null and sell_date between (?) 
        and (?))""", (date.today() - timedelta(days=days), date.today(), date.today() - timedelta(days=days),
                      date.today())).fetchall()
        return current

    def calc_income(self, items):
        answ = [0, 0]
        for item in items:
            answ[0] += Decimal(item[-3]).quantize(Decimal('1.00'))
            answ[1] += Decimal(item[-2]).quantize(Decimal('1.00'))
        return answ
