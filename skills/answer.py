import datetime
import random
from os.path import basename
from utils.settings import MyConfiguration
import pyjokes

name = basename(__file__[:-3])
enable = True
command = [
    [name, "what_can_you_do", ["what can you do", "show me your skills"]],
    [name, "who_are_you", ["who are you"]],
    [name, "tell_joke", ["tell me a joke"]],
    [name, "tell_time", ["what is the time now", "tell me time", "what time is it"]],
    [name, "tell_day", ["what day is today"]],
    [name, "greetings", ["hello", "hi"]],
    [name, "how_are_you", ["how are you"]]
]


def what_can_you_do(text):
    s = "I can do a lot of things like:\n"
    do = ["Shutdown your computer",
          "Lock your computer",
          "Check internet connection",
          "Test internet speed",
          "Open Any App",
          "Tell meetings from your outlook calender",
          "Search Google",
          "Search Wikipedia",
          "Take screenshot",
          "Control Tv",
          "Tell weather",
          "Tell news",
          "Tell time",
          "Take notes",
          "Open Youtube"
          ]
    return s + "\n".join(random.sample(do, 5))


def who_are_you(text):
    config = MyConfiguration()
    assistant_name = config.assistant_name
    return "I am {}, Your personal assistant! Ask me anything and i will do that for you!".format(assistant_name)


def tell_joke(text):
    return pyjokes.get_joke()


def tell_time(text):
    time = datetime.datetime.now().strftime("%I:%M %p")
    return "The time is " + time


def tell_day(text):
    day = datetime.datetime.now().strftime("%A")
    return "Today is " + day


def greetings(text):
    return "Hi"


def how_are_you(text):
    return "I am fine. Thanks! How are you?"
