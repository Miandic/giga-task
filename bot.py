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

login_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_login)


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


def checkLogin(Id):
    global userData
    for login in userData.keys():
        print(login)
        print(Id)
        print(" ")
        if int(login) == Id:
            print("Match!")
            return True
    return False

def getUser(Id):
    global userData
    global loggined
    users = functions.get_users(conn, cur)
    flag = True
    for user in users:
        print(user)
        print(userData)
        if user['login'] == userData[str(Id)]['login'] and user['password'] == userData[str(Id)]['password']:
            return user
    return None



@dp.message_handler(commands=['start'])
async def msg_welcome(message: types.Message):
    global loggined
    userId = message.from_user.id
    userName = message.from_user.first_name
    if checkLogin(userId):
        user = getUser(userId)
        print("Олд))")
        await message.answer("Приветствую, " + user['nickname'] + "!\nЯ всё ещё бот-гигачад от лучшей kanban-доски GigaTask\n\nЕсли вам нужна какая-то помощь, просто напишите /help")
    else:
        print("Я новенький")
        await message.answer("Приветствую, " + userName + "!\nЯ бот-гигачад от лучшей kanban-доски GigaTask\nЧтобы войти в ваш аккаунт, используйте кнопку ниже", reply_markup=login_kb)


@dp.message_handler(lambda message: message.text =="Войти в аккаунт🥸")
async def with_puree(message: types.Message):
    userId = message.from_user.id
    if checkLogin(userId):
        await message.reply("Вы уже вошли в аккаунт!")
    else:
        await User.login.set()
        await message.answer("Введите ваш логин:")


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
    print(userId)
    async with state.proxy() as data:
        data['name'] = message.text
    userData[userId] = {'login': data['name'], 'password': None}
    print(userData)
    await User.next()
    await message.reply("Введите пароль:")



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
    userData[userId]['password'] = data['password']
    user = getUser(userId)
    print(userId)
    print(userData)
    if user != None:
        print(user)
        loggined.append(userId)
        with open("data.json",'w') as f:
            dump(userData, f)
        await message.answer("Вы вошли в аккаунт " + user['login'] + "!")
    else:
        await message.answer("Чё-то не сходится нихуя!")
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
