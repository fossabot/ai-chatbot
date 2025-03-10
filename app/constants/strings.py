# Grouping the string constants

# Text literals for bot messages
MSG_START = 'Привет! Я бот, основанный на GPT-3.5 Turbo. Чтобы узнать, что я умею, напиши /help.\n' \
            'Чтобы начать общение, просто напиши мне что-нибудь, или задай вопрос, например "Что такое GPT-3?"'
MSG_HELP = 'Я - большая языковая модель, обученная на миллионах текстов на разные темы. Я могу помочь с ответами на ' \
           'вопросы, генерировать тексты, исправлять грамматические ошибки и многое другое.\n' \
           'Ты можешь начать общение со мной, написав что-нибудь, или задать вопрос, например "Что лежит в основе теории струн?"\n' \
           'Доступные команды:\n' \
           '/start - приветственное сообщение\n' \
           '/help - вывести это сообщение\n' \
           '/reset - сбросить текущий диалог\n' \
           '/model - изменить модель\n' \
           '/state - проверить состояние бота\n'

# Unknown command error messages
MSG_UNKNOWN_COMMAND = 'Неизвестная команда. Чтобы узнать, что я умею, напиши /help.'

# Error messages
MSG_ERROR_UNKNOWN = 'Произошла неизвестная ошибка. Перезапустите бота и попробуйте снова или подождите некоторое время.'
MSG_ERROR_NO_API_KEY = 'Не указан API-ключ OpenAI. Пожалуйста, укажите его в переменной окружения OPENAI_API_KEY.'
MSG_ERROR_MODEL_INVALID_REQUEST_ERROR = 'Произошла ошибка при формировании запроса. Похоже, что размер диалога ' \
                                        'превышает максимально допустимый размер, впоспользуйтесь командой /reset для' \
                                        ' сброса диалога. '
MSG_ERROR_MODEL_API_ERROR = 'Произошла ошибка при обращении к API. Пожалуйста, попробуйте снова или подождите некоторое время.'
MSG_ERROR_MODEL_OPENAI_ERROR = 'Произошла ошибка на стороне внешнего API, возможно, проблемы с соединением. ' \
                               'Пожалуйста, попробуйте снова или подождите некоторое время. '

MSG_ERROR_EXPECTED_ARGS = "Ожидалось {} аргументов"
MSG_ERROR_EXPECTED_AT_LEAST_ARGS = "Ожидалось не менее {} аргументов"

# Bot state messages
MSG_STATE_ONLINE = '✅ Бот в сети и исправно работает'
MSG_STATE_OPENAI_ERRORS = '⚠️ Бот в сети, но возможны ошибки при обращении к моделям OpenAI'
MSG_STATE_MAINTENANCE = '🔧 Бот в режимобслуживания, подождите некоторое время'

# Access level messages
MSG_NEED_HIGHER_ACCESS_LEVEL = 'Недостаточно прав.'
MSG_SELECT_ACCESS_LEVEL = 'Выберите уровень доступа:'
MSG_ACCESS_LEVEL_CHANGED = 'Уровень доступа успешно изменен.'

# Reset dialog messages
MSG_RESET = 'Диалог успешно сброшен.'
MSG_WAITING_FOR_RESPONSE = 'Подождите, я думаю...'

# User management messages
MSG_USERS = 'Пользователи:'
MSG_USER_NOT_FOUND = 'Пользователь не найден.'
MSG_NO_USERS = 'Нет пользователей.'
MSG_NO_USER_ID = 'Не указан ID пользователя.'
MSG_USER_DELETED = 'Пользователь успешно удален.'
MSG_REQUESTS_FORWARDED = 'Запросы успешно перенаправлены.'

# Model-related messages
MSG_CHOOSE_MODEL = 'Выберите модель для генерации текста:'
MSG_MODEL_CHOSEN = 'Выбрана модель: {0}'

# Error messages for incorrect arguments
MSG_ERROR_INCORRECT_ARGUMENTS = 'Неправильное количество аргументов'

# Report messages
MSG_REPORT_CREATED = 'Отчет о диалогах успешно создан. Записано байт: {}\n' \
                     'Список новых/измененных файлов:\n{}'

# Bot state message
MSG_STATE = 'Стабильность работы в данный момент: {0:.2f}%'

