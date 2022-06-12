from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
colors = [
    "blue",
    "green",
    "red",
]

max_probability = 100
var = [None] * len(colors)
result = []
for _ in range(len(colors)):
    result.append(random.randint(0, max_probability))
    max_probability -= result[-1]


probability_generator = [random.randint(0, max_probability)]


class Thing:
    color: str

    def __init__(self):
        self.color = random.choice(colors)


def service():
    things = 1


def index(request):
    data = {1, 2, 3}
    return HttpResponse("<h1>Hello, World!</h1>" + f"{data}")
