from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, kb_client2, kb_client3, kb_client4, kb_client5, kb_client6, kb_client7, kb_client32, kb_client33, kb_client34, kb_client35, kb_client36, kb_client41, kb_client42, kb_client51, kb_client52, kb_client53, kb_client61

async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Привет! Это чат-бот, в котором Вы можете приобрести качественные юридические услуги для малого бизнеса по доступной цене', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/dlyatesta1111Bot')

async def start(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Привет! Это чат-бот, в котором Вы можете приобрести качественные юридические услуги для малого бизнеса по доступной цене', reply_markup=kb_client)

async def kb2(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Список доступных услуг', reply_markup=kb_client2)
#бизнес
async def kb3(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Полное сопровождение бизнеса включает в себя консультации юристов, подготовка договоров и иных документов, подготовка документов в суд и административные органы (иски, заявления, ходатайства)', reply_markup=kb_client3)

async def kb4(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Доступные тарифы:\n''Мини (включает в себя консультации и подготовку до 5 документов в месяц)./n''Средний (включает в себя консультации и подготовку до 10 документов в месяц).\n''Большой (включает в себя консультации и подготовку до 20 документов в месяц)', reply_markup=kb_client4)

async def kb5(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Месяц – 15 000 рублей;\n''3 месяца – 40 000 рублей = 13 333 в месяц;\n' '6 месяцев – 70 000 рублей = 11 666 в месяц;\n' '12 месяцев – 120 000 рублей = 10 000 в месяц', reply_markup=kb_client5)

async def kb6(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Месяц – 25 000 рублей;\n' '3 месяца – 65 000 рублей = 21 666 в месяц;\n' '6 месяцев – 115 000 рублей = 19 166 в месяц;\n' '12 месяцев – 220 000 рублей = 18 333 в месяц.', reply_markup=kb_client6)

async def kb7(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Месяц – 45 000 рублей;\n' '3 месяца – 120 000 рублей = 40 000 в месяц;\n' '6 месяцев – 210 000 рублей = 35 000 в месяц;\n' '12 месяцев – 360 000 рублей = 30 000 в месяц.', reply_markup=kb_client7)
#Суд
async def kb32(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('У меня суд', reply_markup=kb_client32)

async def kb33(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Какие у вас проблемы с контрагентом?', reply_markup=kb_client33)

async def kb34(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Стоимость консультации – 1000 рублей;\n' 'Стоимость консультации и составления претензии – 3500 рублей;\n' 'Стоимость консультации, составления претензии и иска в суд – 7000 рублей.\n', reply_markup=kb_client34)

async def kb35(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Покупка', reply_markup=kb_client35)

async def kb36(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Какого рода помощь с клиентом вам требуется?\n' 'Стоимость консультации – 1000 рублей;\n' 'Стоимость консультации и составления ответа на претензию – 3500 рублей;\n' 'Стоимость консультации, составления ответа на претензию и отзыва на иск (если понадобится) – 7000 рублей.\n', reply_markup=kb_client36)
#бумага
async def kb41(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Какой договор или документ вам нужен?\n' 'Договор аренды помещения – 2500 рублей;\n' 'Договор купли-продажи – 3500 рублей;\n' 'Договор оказания услуг – 4500 рублей;\n' 'Оферта на сайт – 7500 рублей;\n' 'Политика конфиденциальности – 7500 рублей.', reply_markup=kb_client41)
#ooo\ip
async def kb51(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('С чем вам нужна помощь?', reply_markup=kb_client51)

async def kb52(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Открытие ИП – 1000 рублей;\n' 'Закрытие ИП – 1000 рублей;\n' 'Внесение изменений – 1000 рублей.\n', reply_markup=kb_client52)

async def kb53(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Открытие ООО – 2000 рублей;\n' 'Закрытие ООО – 2000 рублей;\n' 'Внесение изменений – 2000 рублей.\n', reply_markup=kb_client53)
#Налоги
async def kb61(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Какой вопрос по налогам вас интерисует?\n' 'Консультация по налогам – 2000 рублей;\n' 'Подготовить документы в налоговую (обсуждается индивидуально).\n', reply_markup=kb_client61)

def register_handlers_client(db : Dispatcher):
	dp.register_message_handler(command_start, commands=['start'])
	dp.register_callback_query_handler(kb2, text="kb_menu")
#Покупка
	dp.register_callback_query_handler(start, text='kb35_buy')
	dp.register_callback_query_handler(start, text='kb35_back')	
#услуги
	dp.register_callback_query_handler(kb3, text="kb3_bisnes")
	dp.register_callback_query_handler(kb32, text='kb4_juge')
	dp.register_callback_query_handler(kb41, text='kb5_deal')
	dp.register_callback_query_handler(kb51, text='kb6_ooo')
	dp.register_callback_query_handler(kb61, text='kb7_tax')
	dp.register_callback_query_handler(kb51, text='kb8_que')
	dp.register_callback_query_handler(start, text='kb2_back')
#бизнес
	dp.register_callback_query_handler(kb4, text='kb3_tarif')
	dp.register_callback_query_handler(kb5, text='kb3_link')
	dp.register_callback_query_handler(kb2, text='kb3_back')

	dp.register_callback_query_handler(kb5, text='kb4_little')
	dp.register_callback_query_handler(kb6, text='kb4_med')
	dp.register_callback_query_handler(kb7, text='kb4_big')
	dp.register_callback_query_handler(kb3, text='kb4_back')

	dp.register_callback_query_handler(kb35, text='kb5_one')
	dp.register_callback_query_handler(kb35, text='kb5_three')
	dp.register_callback_query_handler(kb35, text='kb5_six')
	dp.register_callback_query_handler(kb35, text='kb5_twelve')
	dp.register_callback_query_handler(kb4, text='kb5_back')

	dp.register_callback_query_handler(kb35, text='kb6_one')
	dp.register_callback_query_handler(kb35, text='kb6_three')
	dp.register_callback_query_handler(kb35, text='kb6_six')
	dp.register_callback_query_handler(kb35, text='kb6_twelve')
	dp.register_callback_query_handler(kb4, text='kb6_back')

	dp.register_callback_query_handler(kb35, text='kb7_one')
	dp.register_callback_query_handler(kb35, text='kb7_three')
	dp.register_callback_query_handler(kb35, text='kb7_six')
	dp.register_callback_query_handler(kb35, text='kb7_twelve')
	dp.register_callback_query_handler(kb4, text='kb7_back')
#суд
	dp.register_callback_query_handler(kb33, text='kb32_spor1')
	dp.register_callback_query_handler(kb36, text='kb32_spor2')
	dp.register_callback_query_handler(kb32, text='kb32_smt')
	dp.register_callback_query_handler(kb2, text='kb32_back')

	dp.register_callback_query_handler(kb34, text='kb33_problem1')
	dp.register_callback_query_handler(kb34, text='kb33_problem2')
	dp.register_callback_query_handler(kb34, text='kb33_problem3')
	dp.register_callback_query_handler(kb32, text='kb33_back')

	dp.register_callback_query_handler(kb35, text='kb34_k')
	dp.register_callback_query_handler(kb35, text='kb34_kp')
	dp.register_callback_query_handler(kb35, text='kb34_kpi')
	dp.register_callback_query_handler(kb33, text='kb34_back')

	dp.register_callback_query_handler(kb35, text='kb36_k')
	dp.register_callback_query_handler(kb35, text='kb36_kp')
	dp.register_callback_query_handler(kb35, text='kb36_kpi')
	dp.register_callback_query_handler(kb32, text='kb36_back')
#бумага
	dp.register_callback_query_handler(kb35, text="kb41_rent")
	dp.register_callback_query_handler(kb35, text='kb41_buy')
	dp.register_callback_query_handler(kb35, text='kb41_services')
	dp.register_callback_query_handler(kb35, text='kb41_site')
	dp.register_callback_query_handler(kb35, text='kb41_conf')
	dp.register_callback_query_handler(kb51, text='kb41_deal')
	dp.register_callback_query_handler(kb2, text='kb41_back')
#ooo\ip
	dp.register_callback_query_handler(kb52, text='kb51_ip')
	dp.register_callback_query_handler(kb53, text='kb51_ooo')
	dp.register_callback_query_handler(kb35, text='kb51_link')
	dp.register_callback_query_handler(kb2, text='kb51_back')

	dp.register_callback_query_handler(kb35, text='kb52_IP1')
	dp.register_callback_query_handler(kb35, text='kb52_IP2')
	dp.register_callback_query_handler(kb35, text='kb52_IP3')
	dp.register_callback_query_handler(kb51, text='kb52_back')

	dp.register_callback_query_handler(kb35, text='kb53_OOO1')
	dp.register_callback_query_handler(kb35, text='kb53_OOO2')
	dp.register_callback_query_handler(kb35, text='kb53_OOO3')
	dp.register_callback_query_handler(kb51, text='kb53_back')
#Налоги
	dp.register_callback_query_handler(kb35, text='kb61_tax1')
	dp.register_callback_query_handler(kb35, text='kb61_tax2')
	dp.register_callback_query_handler(kb35, text='kb61_link')
	dp.register_callback_query_handler(kb2, text='kb61_back')


