from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver, Signal

from .models import *

request_counter_signal = Signal()

def home(request):
    request_counter_signal.send(sender=Post, timestamp='2015-12-05')
    return HttpResponse ("Here's the response")

@receiver (request_finished)
def post_request_receiver(sender, **kwargs):
    print("Request finished!")

@receiver(request_counter_signal)
def post_counter_signal_receiver(sender, **kwargs):
    print(kwargs)
