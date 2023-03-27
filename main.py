import requests
import telebot


all_languages = ['en', 'ru', 'fr', 'de', 'es', 'it', 'zh', 'el', 'ja', 'pt', 'nl', 'uk', 'ar']

bot = telebot.TeleBot('6053379547:AAGKPhwwVYGOSAOuqleKpq8NvoZPtiIkhY8')


@bot.message_handler(commands=['start'])
def start(message):
    start_message = "Этот Телеграм бот способен переводить текст сразу на несколько языков" + "\n" + "Вы можете использовать его для локализации интерфейса приложений, сайтов и других задач. Если что-то не работает пишите" + "\n" + "@f92plus2"
    bot.send_message(message.from_user.id, answer(start_message.split("\n"),
                                                  ['en', 'ru', 'fr', 'de', 'es', 'it', 'zh', 'el', 'ja', 'pt', 'nl',
                                                   'uk']))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id,
                     "Original text:" + "\n" + message.text + "\n\n" + answer(message.text.split("\n"), all_languages))


def get_text(s):
    start = 0
    ans = ""
    while True:
        ind = s.find('"text":', start)
        if ind == -1:
            break
        ind += 9
        start = ind
        for i in range(ind, len(s)):
            if s[i] == '"':
                break
            ans += s[i]
        ans += "\n"
    return ans


def get_emoji(s):
    if s == 'en':
        return "🇬🇧🇺🇸"
    if s == 'ru':
        return "🇷🇺"
    if s == 'fr':
        return "🇫🇷"
    if s == 'de':
        return "🇩🇪"
    if s == 'es':
        return "🇪🇸"
    if s == 'it':
        return "🇮🇹"
    if s == 'zh':
        return "🇨🇳"
    if s == 'el':
        return "🇬🇷"
    if s == 'ja':
        return "🇯🇵"
    if s == 'pt':
        return "🇵🇹"
    if s == 'nl':
        return "🇳🇱"
    if s == 'uk':
        return "🇺🇦"
    if s == 'ar':
        return "🇸🇦"


def answer(texts, languages):
    ans = ""
    folder_id = 'b1grbfkvi9v8i5jocuq0'
    for target_language in languages:
        body = {
            "targetLanguageCode": target_language,
            "texts": texts,
            "folderId": folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Api-Key " + "AQVN1pJYUOdlQH4KgQDauMiRQthtR7zhyU8v9O92"
        }

        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                 json=body,
                                 headers=headers
                                 )
        ans += get_emoji(target_language) + " " + get_text(response.text) + " " + "\n"
    return ans
bot.polling(none_stop=True, interval=0)
