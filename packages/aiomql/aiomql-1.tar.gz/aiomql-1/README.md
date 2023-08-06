# aiomql
![GitHub](https://img.shields.io/github/license/ichinga-samuel/aiomql?style=plastic)
![GitHub issues](https://img.shields.io/github/issues/ichinga-samuel/aiomql?style=plastic)
![PyPI](https://img.shields.io/pypi/v/aiomql)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ichinga-samuel/aiomql/Push)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/ichinga-samuel/aiomql)

## Installation
```bash
pip install aiomql
```

## Key Features
- Asynchronous Python Library For MetaTrader 5
- Build bots for trading in different financial markets using a bot factory
- Use threadpool or proccesspool executors to run multiple strategies on multiple instruments concurrently
- Record and keep track of trades and strategies in csv files.
- Utility classes for using the MetaTrader 5 Library
- Sample Pre-Built strategies

## Simple Usage as an Async MetaTrader5 Libray
```python
import asyncio

# import the class
from aiomql import MetaTrader
from aiomql import Account, Terminal
from aiomql import TimeFrame, OrderType


async def main():
    # Initialize Terminal
    terminal = Terminal()
    mt5 = MetaTrader()
    await mt5.initialize()

    # create Account
    account = Account(account_number=30371334, password="nwa0#anaEze", server="Deriv-Demo")

    # login with account
    await account.login()

    # connection status with the account.connected property
    res = "Login Successful" if account.connected else "Unable to login into account"
    print(res)

    # set account properties
    account.risk = 0.10  # percentage of account equity to risk i.e 10%
    account.risk_to_reward = 3

    # get symbols available for the account if login was successful
    if account.connected:
        symbols = await mt5.symbols_get()
        print(symbols)

    # print timeframe constant for five minutes
    print(TimeFrame.M5)
    await terminal.shutdown()


asyncio.run(main())
```
## As a Bot Building FrameWork using a Prebuilt Strategy
```python
import logging

from aiomql import Bot
from aiomql.lib import ForexMarket, FingerTrap

fmt = "%(asctime)s : %(message)s"

logging.basicConfig(filename='example.log', format=fmt, level=logging.DEBUG)

market = ForexMarket()
bot = Bot(market=market)

# Finger strategy on all instruments in the forex markets
bot.add_strategy_all(strategy=FingerTrap)
bot.execute()
# This assumes that a mt5.json config file with account_number, password and server keys is available
```

see [docs](https://github.com/Ichinga-Samuel/aiomql/tree/master/docs)
