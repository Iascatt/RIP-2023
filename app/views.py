from django.shortcuts import render, redirect
from datetime import date
from app.models import Habitat
import psycopg2

def GetHabitats(request):
    ftitle = request.GET.get("text", "")
    fenv = *request.GET.getlist('env'),
    forig = *request.GET.getlist('orig'),
    habitats = Habitat.objects.filter(status__exact='A').filter(title__contains=ftitle)
    if fenv:
        habitats = habitats.filter(env__in=fenv)
    if forig:
        habitats = habitats.filter(origin__in=forig)
    return render(request, 'habitats.html', {'data' : {
        'envs': Habitat.Environment,
        'origs': Habitat.Origin,
        'habitats': habitats
    }})
    

def GetHabitat(request, id):
    hab = Habitat.objects.get(id=id)
    return render(request, 'habitat.html', {'data' : {
        'habitat': hab,
        'envs': Habitat.Environment,
        'origs': Habitat.Origin,
    }})

def DeleteHabitat(request):
    id = request.POST['id']
    conn = psycopg2.connect(dbname="animals_db", host="192.168.1.51", user="student", password="root", port="5432")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE app_habitat SET status='D' WHERE id={id}")
    conn.commit()   # реальное выполнение команд sql1
    cursor.close()
    conn.close()
    return redirect('/')