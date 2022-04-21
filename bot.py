import logging, secret, functions, json
from json import dump, dumps, load
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor


button_login = KeyboardButton('Войти в аккаунт🥸')
button_unmute = KeyboardButton('Включить уведомления✅')
button_mute = KeyboardButton('Выключить уведомления❌')
button_back = KeyboardButton('К списку досок🔙')

mute_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_mute)
unmute_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_unmute)
login_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_login)

userData = None
with open('data.json') as json_file:
    userData = json.load(json_file)
print(userData)
conn = None
cur = None
conn, cur = functions.set_connection(conn, cur)


class User(StatesGroup):
    login = State()
    password = State()


API_TOKEN = secret.TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def getChat(Id):
    global userData
    for k, v in userData.items():
        if v['baseId'] == str(Id):
            return userData[k]['chat']



def checkLogin(Id):
    global userData
    for login in userData.keys():
        if int(login) == Id:
            print("Match!")
            return True
    return False


def getUser(Id):
    global userData
    users = functions.get_users(conn, cur)
    for user in users:
        if user['login'] == userData[str(Id)]['login'] and user['password'] == userData[str(Id)]['password']:
            return user
    return None


def logoutUser(Id):
    global userData
    userData.pop(str(Id))
    with open("data.json",'w') as f:
        dump(userData, f)
    print("logOut!")



@dp.message_handler(commands=['start'])
async def msg_welcome(message: types.Message):
    userId = message.from_user.id
    userName = message.from_user.first_name
    buttons = [
        types.InlineKeyboardButton(text="Сайт GigaTask", url="https://github.com/miandic/BigFlaskPoggers"),
        types.InlineKeyboardButton(text="Репозиторий на GitHub", url="https://github.com/miandic/BigFlaskPoggers"),
        types.InlineKeyboardButton(text="Выйти из аккаунта", callback_data="logout")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    if checkLogin(userId):
        user = getUser(userId)
        await message.answer("Приветствую, " + user['nickname'] + "!\nЯ всё ещё бот-гигачад от лучшей kanban-доски GigaTask\n\nЕсли вам нужна какая-то помощь, просто напишите /help", reply_markup=keyboard)
    else:
        await message.answer("Приветствую, " + userName + "!\nЯ бот-гигачад от лучшей kanban-доски GigaTask\nЧтобы войти в ваш аккаунт, используйте кнопку ниже", reply_markup=login_kb)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    global userData
    userId = message.from_user.id
    user = userData[str(userId)]
    print(user)
    if user['alarm'] == False:
        await message.answer("Уведомления: выключенны❌", reply_markup=unmute_kb)
    elif user['alarm'] == True:
        await message.answer("Уведомления: включены✅", reply_markup=mute_kb)


@dp.message_handler(lambda message: message.text =="Включить уведомления✅")
async def unmute(message: types.Message):
    global userData
    userId = message.from_user.id
    userData[str(userId)]['alarm'] = True
    with open("data.json",'w') as f:
        dump(userData, f)
    await message.reply("Уведомления включенны!")


@dp.message_handler(lambda message: message.text =="Выключить уведомления❌")
async def mute(message: types.Message):
    global userData
    userId = message.from_user.id
    userData[str(userId)]['alarm'] = False
    with open("data.json",'w') as f:
        dump(userData, f)
    await message.reply("Уведомления выключенны!")


@dp.message_handler(lambda message: message.text =="Войти в аккаунт🥸")
async def login(message: types.Message):
    userId = message.from_user.id
    if checkLogin(userId):
        await message.reply("Вы уже вошли в аккаунт!")
    else:
        await User.login.set()
        await message.answer("Введите ваш логин:\nОтмена: /cancel")


@dp.callback_query_handler(text="logout")
async def logout(message: types.Message):
    userId = message.from_user.id
    if checkLogin(userId):
        logoutUser(userId)
        await message.answer("Вы вышли из аккаунта!")
    else:
        await message.answer("Вы не в аккаунте!")


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.answer('Как скажешь, так и будет')


@dp.message_handler(state=User.login)
async def process_name(message: types.Message, state: FSMContext):
    """
    Process user login
    """
    global userData
    userId = message.from_user.id
    chat_id = message.chat.id
    print(userId)
    async with state.proxy() as data:
        data['name'] = message.text
    userData[str(userId)] = {'login': data['name'], 'password': None, 'alarm': 'False', 'chat': str(chat_id), 'baseId': None }
    await User.next()
    await message.reply("Введите пароль:\nОтмена: /cancel")



@dp.message_handler(state=User.password)
async def process_name(message: types.Message, state: FSMContext):
    """
    Process user password
    """
    global userData
    global loggined
    userId = message.from_user.id
    async with state.proxy() as data:
        data['password'] = message.text
    userData[str(userId)]['password'] = data['password']
    user = getUser(userId)
    if user != None:
        print(user['id'])
        userData[str(userId)]['baseId'] = str(user['id'])
        print(userData)
        with open("data.json",'w') as f:
            dump(userData, f)
        await message.answer("Вы вошли в аккаунт " + user['login'] + "!\nКоманды: /help")
    else:
        logoutUser(userId)
        await message.answer("Чё-то не сходится!")
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
