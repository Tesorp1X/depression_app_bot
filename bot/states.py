from aiogram.dispatcher.filters.state import StatesGroup, State


class GeneralStates(StatesGroup):
    waiting_for_code = State()
    waiting_for_note = State()
    waiting_for_description = State()


class EditNoteStates(StatesGroup):
    waiting_for_new_name = State()
    waiting_for_new_value = State()
    waiting_for_new_description = State()
