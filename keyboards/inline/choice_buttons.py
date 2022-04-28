from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_OMIRBAIAN, URL_JETISTIKTER, URL_ZERTTEYLERI, URL_ASHYQSABAQTAR, URL_OQYSHYJESTISTIGI

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="OMIRBAYAN", callback_data=buy_callback.new(item_name="OMIRBAYAN", quantity=1))

choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="JETISTIKTER ", callback_data="buy:JETISTIKTER:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="ZERTTEYLER", callback_data="buy:ZERTTEYLER:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="ASHYQSABAQTAR", callback_data="buy:ASHYQSABAQTAR:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="OQUSHYJETISTIGI", callback_data="buy:OQUSHYJETISTIGI:5")

choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")

choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit", url=URL_OMIRBAIAN)
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_JETISTIKTER)
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_OQYSHYJESTISTIGI)
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_ASHYQSABAQTAR)
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_ZERTTEYLERI)
    ]
])
def apples_keyboard():
    return None