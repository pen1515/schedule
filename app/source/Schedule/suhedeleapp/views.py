from django.shortcuts import render, redirect
from .models import Todolist   , Userlist
from .forms import TodoAdd, UserAdd

# Create your views here.

def testView(request):
	return render(request, "suhedeleapp/test.html")

# def signupView(request):
# 	plate = {
# 		'aaa' : "今日は"
# 	}

# 	return render(request, "suhedeleapp/signup.html", plate)

def formView(request):
	todo = Todolist.objects.all().order_by('day')
	todo_2 = Todolist.objects.values()
	user = Userlist.objects.values()
	my_dict = {
        'title':'予定',
        'user': user,
        'val2': todo,
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
        'title':'予定登録',
        'form': TodoAdd(),
		'message': message,  # エラーメッセージ
    }
	return render(request, 'suhedeleapp/create.html', modelform_dict)


def signupView(request):
	message = ''  # 初期表示ではカラ
	if (request.method == 'POST'):
		form = UserAdd(request.POST)
		if form.is_valid():
			form.save()
			return redirect('suhedeleapp:login')
		else:
			message = '再入力して下さい'
	modelform_dict2 = {
        'title':'新規登録',
        'form': UserAdd(),
		'message': message,  # エラーメッセージ
    }
	return render(request, 'suhedeleapp/signup.html', modelform_dict2)






# ↓作成途中






def loginView(request):
    print('request.method == POST')
    print(request.method)
    # ↑GET
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            print('成功')
            user = form.get_user()
            if user:
                login(request, user)
            return redirect('suhedeleapp:form')
            # return render(request, 'pengin/home.html', {})
        else:
            print('そんな値はないです')

    return render(request, 'suhedeleapp/login.html')