import exchange_rates
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token = "2110471206:AAHpxXMVX2u3ifJvYdq2HI2LGmDyxFicKk0")

currency_codes = ['/AUD', '/AZN', '/AMD', '/BYN', '/BGN', '/BGN', '/HUF', '/KRW', '/HKD',
'/DKK', '/USD', '/EUR', '/INR', '/KZT', '/CAD', '/KGS', '/CNY', '/MDL', '/TMT', '/NOK',
'/PLN', '/RON', '/XDR', '/SGD', '/TJS', '/TRY', '/UZS', '/UAH', '/GBP', '/CZK', '/SEK',
'/CHF', '/ZAR', '/JPY']

start_page = """
    Здравствуйте!
Это тестовый бот для просмотра курсов валют с сайта ЦБ РФ.
Список команд:
    /AUD - Австралийский доллар
    /AZN - Азербайджанский манат
    /AMD - 100 Армянских драмов
    /BYN - Белорусский рубль
    /BGN - Болгарский лев
    /BGN - Бразильский реал
    /HUF - 100 Венгерских форинтов
    /KRW - 1000	Вон Республики Корея
    /HKD - 10 Гонконгских долларов
    /DKK - Датская крона
    /USD - Доллар США
    /EUR - Евро
    /INR - 100 Индийских рупий
    /KZT - 100 Казахстанских тенге
    /CAD - Канадский доллар
    /KGS - 100 Киргизских сомов
    /CNY - Китайский юань	
    /MDL - 10 Молдавских леев
    /TMT - Новый туркменский манат
    /NOK - 10 Норвежских крон
    /PLN - Польский злотый
    /RON - Румынский лей
    /XDR - СДР (специальные права заимствования)
    /SGD - Сингапурский доллар
    /TJS - 10 Таджикских сомони
    /TRY - 10 Турецких лир
    /UZS - 10000 Узбекских сумов
    /UAH - 10 Украинских гривен
    /GBP - Фунт стерлингов Соединенного королевства
    /CZK - 10 Чешских крон
    /SEK - 10 Шведских крон
    /CHF - Швейцарский франк
    /ZAR - 10 Южноафриканских рэндов
    /JPY - 100 Японских иен
"""

dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start_pg(message: types.Message):
    await message.answer(start_page)

@dp.message_handler()
async def aud(message: types.Message):
        try:
            await message.reply(exchange_rates.get_rate(currency_codes.index(message.text)))
        except:
            await message.reply("Ошибка получения курса данной валюты. Для просмотра списка доступных валютных кодов - введите /start")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



