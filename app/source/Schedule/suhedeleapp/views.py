from django.shortcuts import render, redirect
from .models import Todolist   #, Userlist
from .forms import TodoAdd

# Create your views here.

def testView(request):
	return render(request, "suhedeleapp/test.html")

def signupView(request):
	plate = {
		'aaa' : "今日は"
	}

	return render(request, "suhedeleapp/signup.html", plate)

def formView(request):
	todo = Todolist.objects.all()
	todo_2 = Todolist.objects.values()
	user = Userlist.objects.values()
	my_dict = {
        'title':'予定',
        'user': user,
        'val2': todo_2,
    }
	return render(request, 'suhedeleapp/form.html', my_dict)


def createView(request):
	message = ''  # 初期表示ではカラ
	if (request.method == 'POST'):
		form = TodoAdd(request.POST)
		if form.is_valid():
			form.save()
			return redirect('suhedeleapp:form')
		else:
			message = '再入力して下さい'
	modelform_dict = {
        'title':'modelformテスト',
        'form': TodoAdd(),
		'message': message,  # エラーメッセージ
    }
	return render(request, 'suhedeleapp/create.html', modelform_dict)