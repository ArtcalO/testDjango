from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

@login_required(login_url=('login'))
def index(request):
	text = "Bonjour le monde"
	text2 = "Aymar"
	nummber = 42510

	return render(request, "index.html", locals())

def registerSchool(request):
	school_form = SchoolForm(request.POST or None)
	if(request.method == 'POST'):
		if(school_form.is_valid()):
			school_form.save()
	school_form = SchoolForm()

	return render(request, "forms.html", locals())


def registerClass(request):
	classe_form = ClasseForm(request.POST or None)
	if(request.method == 'POST'):
		if(classe_form.is_valid()):
			classe_form.save()
	classe_form = ClasseForm()
	return render(request, "forms.html", locals())


def register(request):

	register_form = RegisterStudentForm(request.POST or None, request.FILES)

	if(request.method == 'POST'):

		if(register_form.is_valid()):
			register_form.save()
	register_form = RegisterStudentForm()
	return render(request, "forms.html", locals())


def ListStudent(request):
	students = RegisterStudent.objects.all()

	return render(request, "lists.html", locals())


def modifier(request, student_id):
	student = RegisterStudent.objects.get(id=student_id)

	modifier_form = RegisterStudentForm(request.POST or None, request.FILES, instance=student)

	if(request.method == 'POST'):
		if(modifier_form.is_valid()):
			modifier_form.save()
			return redirect(ListStudent)
	modifier_form = RegisterStudentForm(instance=student)
	return render(request, "forms.html", locals())


def delete(request, student_id):
	student = RegisterStudent.objects.get(id=student_id)
	student.delete()
	return redirect(ListStudent)

def registerProfil(request):
	if(request.method == 'POST'):
		profil_form = ProfileForm(request.POST or None, request.FILES)
		if(profil_form.is_valid()):
			username = profil_form.cleaned_data['username']
			password = profil_form.cleaned_data['password']
			password1 = profil_form.cleaned_data['password1']
			nom = profil_form.cleaned_data['nom']
			prenom = profil_form.cleaned_data['prenom']
			age = profil_form.cleaned_data['age']
			matricule = profil_form.cleaned_data['matricule']
			avatar = profil_form.cleaned_data['avatar']

			if(password == password1):
				user = User.objects.create_user(username = username, password=password)
				user.first_name = nom
				user.last_name = prenom
				user.save()

				print(user)

				profil = Profil(user = user, age=age, matricule=matricule, avatar=avatar).save()
				if user: 
					login(request, user)
					return redirect(index)  
				else:
					return redirect(connexion)
			else:
				profil_form = ProfileForm(request.FILES)

	profil_form = ProfileForm(request.FILES)
	return render(request, 'forms.html', locals())

def connexion(request):
    error = False
    # next = request.GET["next"]
    if request.method == "POST":
        connexion_form = ConnexionForm(request.POST)
        if connexion_form.is_valid():
            username = connexion_form.cleaned_data["username"]
            password = connexion_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(index)
            else:
                error = True
    else:
        connexion_form = ConnexionForm()
    return render(request, 'forms.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(connexion)
