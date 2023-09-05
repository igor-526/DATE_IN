from vkwave.bots.fsm import StateFilter, ForWhat
from vkwave.bots.core.dispatching import filters
from vkwave.bots import SimpleBotEvent, DefaultRouter, simple_bot_message_handler
from FSM import fsm, Profile
from keyboards import prof_set_keys
from dbase import upd_sex

prs_sex_router = DefaultRouter()


@simple_bot_message_handler(prs_sex_router, filters.PayloadFilter({"command": "back"}),
                            StateFilter(fsm=fsm, state=Profile.sex, for_what=ForWhat.FOR_USER))
async def cancel(event: SimpleBotEvent):
    await event.answer("Выберите действие:",
                       keyboard=prof_set_keys.get_keyboard())
    await fsm.set_state(state=Profile.show, event=event, for_what=ForWhat.FOR_USER)


@simple_bot_message_handler(prs_sex_router, filters.PayloadFilter({"command": "male"}),
                            StateFilter(fsm=fsm, state=Profile.sex, for_what=ForWhat.FOR_USER))
async def set_male(event: SimpleBotEvent):
    await upd_sex(event.user_id, 2)
    await event.answer(message='Успешно поменяли!\n'
                               'Выберите действие:',
                       keyboard=prof_set_keys.get_keyboard())
    await fsm.set_state(state=Profile.show, event=event, for_what=ForWhat.FOR_USER)


@simple_bot_message_handler(prs_sex_router, filters.PayloadFilter({"command": "female"}),
                            StateFilter(fsm=fsm, state=Profile.sex, for_what=ForWhat.FOR_USER))
async def set_female(event: SimpleBotEvent):
    await upd_sex(event.user_id, 1)
    await event.answer(message='Успешно поменяли!\n'
                               'Выберите действие:',
                       keyboard=prof_set_keys.get_keyboard())
    await fsm.set_state(state=Profile.show, event=event, for_what=ForWhat.FOR_USER)


@simple_bot_message_handler(prs_sex_router,
                            StateFilter(fsm=fsm, state=Profile.sex, for_what=ForWhat.FOR_USER))
async def invalid(event: SimpleBotEvent):
    await event.answer(message="Я вас не понимаю &#128532;\n" \
                               "Пожалуйста, выберите действие на клавиатуре")
