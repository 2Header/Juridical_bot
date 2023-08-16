from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup#, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_client = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Какие есть услуги', callback_data='kb_menu')
b2 = InlineKeyboardButton(text='Связаться с владельцем',  url='https://t.me/keezjv', callback_data='kb_link1')
b3 = InlineKeyboardButton(text='Посмотреть тг канал', url='https://t.me/+eP2NqpzQOUE1MmEy', callback_data='kb_link2')

kb_client.add(b1, b2, b3)

kb_client2 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Сопровождение бизнеса', callback_data='kb3_bisnes')
b2 = InlineKeyboardButton(text='У меня суд', callback_data='kb4_juge')
b3 = InlineKeyboardButton(text='Договор или иной документ', callback_data='kb5_deal')
b4 = InlineKeyboardButton(text='ИП или ООО', callback_data='kb6_ooo')
b5 = InlineKeyboardButton(text='Вопрос по налогам', callback_data='kb7_tax')
b6 = InlineKeyboardButton(text='Иной вопрос',  url='https://t.me/keezjv', callback_data='kb8_que')
b7 = InlineKeyboardButton(text='Назад', callback_data='kb2_back')

kb_client2.add(b1, b2, b3, b4, b5, b6, b7)
#бизнес
kb_client3 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Тарифы', callback_data='kb3_tarif')
b2 = InlineKeyboardButton(text='Связь',  url='https://t.me/keezjv', callback_data='kb3_link')
b3 = InlineKeyboardButton(text='Назад', callback_data='kb3_back')

kb_client3.add(b1, b2, b3)

kb_client4 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Маленький', callback_data='kb4_little')
b2 = InlineKeyboardButton(text='Средний', callback_data='kb4_med')
b3 = InlineKeyboardButton(text='Большой', callback_data='kb4_big')
b4 = InlineKeyboardButton(text='Назад', callback_data='kb4_back')

kb_client4.add(b1, b2, b3, b4)

kb_client5 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='месяц', callback_data='kb5_one')
b2 = InlineKeyboardButton(text='3 месяца', callback_data='kb5_three')
b3 = InlineKeyboardButton(text='6 месяцев', callback_data='kb5_six')
b4 = InlineKeyboardButton(text='12 месяцев', callback_data='kb5_twelve')
b5 = InlineKeyboardButton(text='Назад', callback_data='kb5_back')

kb_client5.add(b1, b2, b3, b4, b5)

kb_client6 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='месяц', callback_data='kb6_one')
b2 = InlineKeyboardButton(text='3 месяца', callback_data='kb6_three')
b3 = InlineKeyboardButton(text='6 месяцев', callback_data='kb6_six')
b4 = InlineKeyboardButton(text='12 месяцев', callback_data='kb6_twelve')
b5 = InlineKeyboardButton(text='Назад', callback_data='kb6_back')

kb_client6.add(b1, b2, b3, b4, b5)

kb_client7 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='месяц', callback_data='kb7_one')
b2 = InlineKeyboardButton(text='3 месяца', callback_data='kb7_three')
b3 = InlineKeyboardButton(text='6 месяцев', callback_data='kb7_six')
b4 = InlineKeyboardButton(text='12 месяцев', callback_data='kb7_twelve')
b5 = InlineKeyboardButton(text='Назад', callback_data='kb7_back')

kb_client7.add(b1, b2, b3, b4, b5)
#Суд
kb_client32 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Спор с контрагентом', callback_data='kb32_spor1')
b2 = InlineKeyboardButton(text='Спор с клентом', callback_data='kb32_spor2')
b3 = InlineKeyboardButton(text='Иная ситуация', url='https://t.me/keezjv', callback_data='kb32_smt')
b4 = InlineKeyboardButton(text='Назад', callback_data='kb32_back')

kb_client32.add(b1, b2, b3, b4)

kb_client33 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Контрагент не оплатил услугу', callback_data='kb33_problem1')
b2 = InlineKeyboardButton(text='Контрагент не оплатил товар', callback_data='kb33_problem2')
b3 = InlineKeyboardButton(text='Контрагент требует деньги назад', callback_data='kb33_problem3')
b4 = InlineKeyboardButton(text='Назад', callback_data='kb33_back')

kb_client33.add(b1, b2, b3, b4)

kb_client34 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Мне нужна только консультация', callback_data='kb34_k')
b2 = InlineKeyboardButton(text='Консультация и составление притензии', callback_data='kb34_kp')
b3 = InlineKeyboardButton(text='Консультация, составление притензии и иск', callback_data='kb34_kpi')
b4 = InlineKeyboardButton(text='Назад', callback_data='kb34_back')

kb_client34.add(b1, b2, b3, b4)

kb_client35 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Купить',  url='https://t.me/keezjv', callback_data='kb35_buy')
b2 = InlineKeyboardButton(text='Назад', callback_data='kb35_back')

kb_client35.add(b1, b2)

kb_client36 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Мне нужна только консультация', callback_data='kb36_k')
b2 = InlineKeyboardButton(text='Консультация и составление притензии', callback_data='kb36_kp')
b3 = InlineKeyboardButton(text='Консультация, составление притензии и иск', callback_data='kb36_kpi')
b4 = InlineKeyboardButton(text='Назад', callback_data='kb36_back')

kb_client36.add(b1, b2, b3, b4)
#бумага
kb_client41 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Договор аренды помещения', callback_data='kb41_rent')
b2 = InlineKeyboardButton(text='Договор купли-продажи', callback_data='kb41_buy')
b3 = InlineKeyboardButton(text='Договор оказания услуг', callback_data='kb41_services')
b4 = InlineKeyboardButton(text='Оферта на сайте', callback_data='kb41_site')
b5 = InlineKeyboardButton(text='Политика конфиденциальности', callback_data='kb41_conf')
b6 = InlineKeyboardButton(text='Иной договор', url='https://t.me/keezjv', callback_data='kb41_deal')
b7 = InlineKeyboardButton(text='Назад', callback_data='kb41_back')

kb_client41.add(b1, b2, b3, b4, b5, b6, b7)

kb_client42 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Контрагент не оплатил услугу', callback_data='kb42_problem1')
b2 = InlineKeyboardButton(text='Контрагент не оплатил товар', callback_data='kb42_problem2')
b3 = InlineKeyboardButton(text='Контрагент требует деньги назад', callback_data='kb42_problem3')

kb_client42.add(b1, b2, b3)
#ooo\ip
kb_client51 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='У меня ИП', callback_data='kb51_ip')
b2 = InlineKeyboardButton(text='у меня ООО', callback_data='kb51_ooo')
b3 = InlineKeyboardButton(text='Связь в владельцем',  url='https://t.me/keezjv', callback_data='kb51_link')
b4 = InlineKeyboardButton(text='Назад', callback_data='kb51_back')

kb_client51.add(b1, b2, b3, b4)

kb_client52 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Хочу открыть ИП', callback_data='kb52_IP1')
b2 = InlineKeyboardButton(text='Хочу закрыть ИП', callback_data='kb52_IP2')
b3 = InlineKeyboardButton(text='Хочу внести изенения', callback_data='kb52_IP3')
b4 = InlineKeyboardButton(text='Назад', callback_data='kb52_back')

kb_client52.add(b1, b2, b3, b4)

kb_client53 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Хочу открыть ООО', callback_data='kb53_OOO1')
b2 = InlineKeyboardButton(text='Хочу закрыть ООО', callback_data='kb53_OOO2')
b3 = InlineKeyboardButton(text='Хочу внести изенения', callback_data='kb53_OOO3')
b4 = InlineKeyboardButton(text='Назад', callback_data='kb53_back')

kb_client53.add(b1, b2, b3, b4)
#Налоги
kb_client61 = InlineKeyboardMarkup(row_width=1)

b1 = InlineKeyboardButton(text='Консультация налоги', callback_data='kb61_tax1')
b2 = InlineKeyboardButton(text='Документы в налоговую', callback_data='kb61_tax2')
b3 = InlineKeyboardButton(text='Владелец',  url='https://t.me/keezjv', callback_data='kb61_link')
b4 = InlineKeyboardButton(text='Назад', callback_data='kb61_back')

kb_client61.add(b1, b2, b3, b4)