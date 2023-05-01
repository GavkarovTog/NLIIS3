from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_random_response
import openai

openai.api_key = "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"
bot = ChatBot('MyBot', response_selection_method=get_random_response)
trainer = ListTrainer(bot)
trainer.train([
    "Привет", "Здравствуйте!",
    "Что ты можешь?", "Я кулинарный бот, моя задача помочь вам приготовить вкусные блюда! Могу предложить рецепты на любой вкус и подсказать как приготовить ингредиенты. Так же вы можете задать мне вопросы по приготовлению и я постараюсь помочь вам разобраться.",
    "Что ты умеешь?", "Я кулинарный бот, моя задача помочь вам приготовить вкусные блюда! Могу предложить рецепты на любой вкус и подсказать как приготовить ингредиенты. Так же вы можете задать мне вопросы по приготовлению и я постараюсь помочь вам разобраться.",
    "Расскажи о себе", "Я кулинарный бот, моя задача помочь вам приготовить вкусные блюда! Могу предложить рецепты на любой вкус и подсказать как приготовить ингредиенты. Так же вы можете задать мне вопросы по приготовлению и я постараюсь помочь вам разобраться."],
)

def get_bot_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.3,
        max_tokens=3500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0,
        best_of=1
    )
    message = response.choices[0].text.strip()
    print(response)
    return message

def get_response(request):
    response = bot.get_response(request)
    print(response.text)
    print(response.confidence)
    if response.confidence < 1:
        
        response = get_bot_response(request)
        trainer.train([request, response])
        return response
    elif response.confidence >= 1:
        return response.text