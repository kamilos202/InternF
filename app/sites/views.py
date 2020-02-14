import json
from random import randint
from django.http import HttpResponse
from django.shortcuts import render	
from .forms import EchoForm
from .models import Post


def post(request):
	form = EchoForm(request.POST)

	response_data = {}

	if form.is_valid():
		text = form.cleaned_data['post']
		form = EchoForm
		
		try:
			json.loads(text)
			response_data['status'] = 'ok'
			response_data['msg'] = 'JSON is valid'
		except Exception as error:
			response_data['status'] = 'error'

		
	text = response_data
	args = {'form':form,'json':json.dumps(text)}

	return render(request, "echo.html", args)

def getReq(request):

	number = randint(0, 100)
	response_data = {}
	response_data['status'] = 'ok'
	response_data['number'] = number
		
	text = response_data
	args = {'json':json.dumps(text)}

	return render(request, "random.html", args)
