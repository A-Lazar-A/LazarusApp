from data_base.db import DataBase
from datetime import date, timedelta
from decimal import Decimal


def main():
    db = DataBase()
    db.create_table()
    today = date.today()
    # item = {
    #     'name': 'TEXT NOT NULL',
    #     'buy_price': Decimal('100.5'),
    #     'buy_currency': 'usdt',
    #     'sell_price': None,
    #     'sell_currency': None,
    #     'buy_date': today,
    #     'sell_date': None,
    #     'income_rub': None,
    #     'income_usd': None,
    #
    # }
    # db.add_item(item)
    # print(db.get_item())
    # item = {
    #     'name': 'TEXT NOT NULL',
    #     'buy_price': Decimal('100'),
    #     'buy_currency': 'usdt',
    #     'sell_price': Decimal('120'),
    #     'sell_currency': 'usdt',
    #     'buy_date': today,
    #     'sell_date': today,
    #     'income_rub': None,
    #     'income_usd': None,
    #
    # }
    # db.add_item(item)
    # item = {
    #     'name': 'TEXT NOT NULL',
    #     'buy_price': Decimal('100'),
    #     'buy_currency': 'usdt',
    #     'sell_price': Decimal('120'),
    #     'sell_currency': 'usdt',
    #     'buy_date': today - timedelta(days=6),
    #     'sell_date': today - timedelta(days=5),
    #     'income_rub': None,
    #     'income_usd': None,
    #
    # }
    # db.add_item(item)
    # item = {
    #     'name': 'TEXT NOT NULL',
    #     'buy_price': Decimal('100'),
    #     'buy_currency': 'usdt',
    #     'sell_price': Decimal('120'),
    #     'sell_currency': 'usdt',
    #     'buy_date': today - timedelta(days=36),
    #     'sell_date': today - timedelta(days=25),
    #     'income_rub': None,
    #     'income_usd': None,
    #
    # }
    # db.add_item(item)
    print(db.get_item())
    print(db.get_income(7))


if __name__ == '__main__':
    main()
