from maxapi.types import MessageCallback, LinkButton
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder

from config import dp
from database.db import db
from database.repository.main_repository import Repository


@dp.message_created()
async def pop(event: MessageCallback):
    async with db.session() as session:
        repo = Repository(session)
        text = await repo.default_repository.get_value("message")
        link = await repo.default_repository.get_value("link")

    builder = InlineKeyboardBuilder()
    builder.row(
        LinkButton(text="Перейти", url=link)
    )
    await event.bot.send_message(
        chat_id=event.chat_id,
        text=text,
        attachments=[builder.as_markup()]
    )
