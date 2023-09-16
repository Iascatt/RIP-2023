from django.shortcuts import render
from datetime import date

def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

# TODO: дозаполнить
def GetHabitats(request):
    return render(request, 'habitats.html', {'data' : {
        'current_date': date.today(),
        'habitat': [
            {'id': 1, 'title': 'Тундра', 'environment': 'наземно-воздушная', },
            {'id': 2, 'title': 'Тайга', 'environment': 'наземно-воздушная'},
            {'id': 3, 'title': 'Пустыня', 'environment': 'наземно-воздушная'},
            {'id': 4, 'title': 'Степь', 'environment': 'наземно-воздушная'},
            {'id': 5, 'title': 'Океан', 'environment': 'водная'},
            {'id': 6, 'title': 'Пустыня', 'environment': 'наземно-воздушная'},
            {'id': 7, 'title': 'Пустыня', 'environment': 'наземно-воздушная'},
            {'id': 7, 'title': 'Пустыня', 'environment': 'наземно-воздушная'},
        ]
    }})

def GetHabitat(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})

def sendText(request):
    input_text = request.POST['text']