from django.shortcuts import render
from datetime import date

HABITATS = [
            {'id': 1, 'title': 'Тундра', 'env': '1', 'pic': 'https://upload.wikimedia.org/wikipedia/commons/0/09/Arctic_tundra_in_July.jpg',
              'countries': [''], 'origin': 'естественное',
              'desc': 'Тундра — вид природных зон, лежащих за северными пределами лесной растительности, пространства с вечномёрзлой почвой, не заливаемой морскими или речными водами. Тундра находится севернее зоны тайги. По характеру поверхности тундры бывают болотистые, торфянистые, каменистые.'},
            {'id': 2, 'title': 'Канал', 'env': '2', 'pic': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Pond-001.jpg/1280px-Pond-001.jpg',
              'countries': [''], 'origin': 'искусственное',
              'desc': 'Пруд, или ставо́к[1] — искусственный водоём для хранения воды с целью водоснабжения, орошения, разведения рыбы (прудовое рыбное хозяйство) и водоплавающей птицы, а также для санитарных, противопожарных и спортивных потребностей[2]. В российском законодательстве прудами считаются искусственные водоёмы площадью не более 1 км²[3].'},
            {'id': 3, 'title': 'Тайга', 'env': '1', 'pic': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Mixed_Picea_%28Spruce%29_forest_from_Vestfold_county_in_Norway.jpg/1280px-Mixed_Picea_%28Spruce%29_forest_from_Vestfold_county_in_Norway.jpg',
              'countries': [''], 'origin': '', 'origin': 'естественное',
              'desc': 'Тайга — биом, характеризующийся преобладанием хвойных лесов, образованных в основном бореальными видами ели, пихты, лиственницы и сосны. Словом «тайга» обозначают также одну из географических подзон северного умеренного пояса. В неарктическом сегменте (Северная Америка) тайгу называют «северным лесом» или «снежным лесом».'},
            {'id': 4, 'title': 'Пустыня', 'env': '1', 'pic': 'https://ethnomir.ru/upload/medialibrary/1a4/pustynya_sahara_2.jpg',
              'countries': [''], 'origin': 'естественное',
              'desc': 'Пустыня — тер­ри­то­рия в раз­ных при­род­ных зо­нах, от­ли­чаю­щая­ся край­не за­суш­ли­вым кли­ма­том, где ис­па­ряе­мость в несколько раз пре­вы­ша­ет количество выпавших осадков'},
            {'id': 5, 'title': 'Степь', 'env': '1', 'pic': 'https://upload.wikimedia.org/wikipedia/commons/f/ff/%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%BA%D0%BE%D0%B2%D1%8B%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D0%B5%D0%BF%D1%8C_%D0%B2_%D0%B1%D0%B0%D1%81%D1%81%D0%B5%D0%B9%D0%BD%D0%B5_%D0%9A%D1%83%D0%BA%D1%83%D0%B9%D0%BA%D0%B8_%D0%B2_%D0%9A%D1%83%D1%80%D1%8C%D0%B8%D0%BD%D1%81%D0%BA%D0%BE%D0%BC_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD%D0%B5.JPG',
              'countries': [''], 'origin': 'естественное',
              'desc': 'Степь — равнина, поросшая травянистой растительностью, в умеренных и субтропических зонах Северного и Южного полушарий. Характерной особенностью степей является отсутствие или очень малое количество деревьев (не считая искусственных насаждений и лесополос вдоль водоёмов и путей сообщения).'},
            {'id': 6, 'title': 'Океан', 'env': '2', 'pic': 'https://www.un.org/sites/un2.un.org/files/field/image/2022/06/silas-baisch-oczvgbqcjky-unsplash.jpg',
              'countries': [''], 'origin': 'естественное',
              'desc': 'Океан (др.-греч. Ὠκεανός, от имени древнегреческого божества Океана) — крупнейший водный объект, составляющий часть Мирового океана, расположенный среди материков, обладающий системой циркуляции вод и другими специфическими особенностями. Океан находится в непрерывном взаимодействии с атмосферой и земной корой.'},
            {'id': 7, 'title': 'Озеро', 'env': '2', 'pic': 'https://upload.wikimedia.org/wikipedia/commons/f/f2/Bariloche-_Argentina2.jpg',
              'countries': [''], 'origin': 'естественное',
              'desc': 'О́зеро — компонент гидросферы, представляющий собой естественно возникший водоём, заполненный в пределах озёрной чаши (озёрного ложа) водой и не имеющий непосредственного соединения с морем (океаном)[1]. В озёра могут впадать реки, ручьи и подземные источники. Озёра являются предметом изучения науки лимнологии. Число озёр в мире достигает 304 миллионов, включая мелкие с площадью поверхностью 0,1-10 гектаров[2][3].'},
            ]
ENVS = [
            {'id': 1, 'title': 'наземно-воздушная', 'pic': 'https://cdn-icons-png.flaticon.com/128/7591/7591273.png'},
            {'id': 2, 'title': 'водная', 'pic': 'https://cdn-icons-png.flaticon.com/128/7441/7441517.png'},
            {'id': 3, 'title': 'почвенная', 'pic': ''},
            {'id': 4, 'title': 'организменная', 'pic': ''},
        ]

def GetHabitats(request, fname="", fenvs=""):
    return render(request, 'habitats.html', {'data' : {
        'envs': ENVS,
        'habitats': filter(lambda x: (x['title'].startswith(fname) and (x['env'] in fenvs or not fenvs)), HABITATS),
    }})

def GetHabitat(request, id):
    hab = list(filter(lambda x: x['id'] == id, HABITATS))[0]
    env = list(filter(lambda x: int(hab['env']) == x['id'], ENVS))[0]
    return render(request, 'habitat.html', {'data' : {
        'habitat': hab,
        'env': env,
        'id': id
    }})

def GetFilter(request):
    ftitle = request.GET.get("text", "undefined")
    fenv = request.GET.getlist('env')
    return GetHabitats(request, fname=ftitle, fenvs=fenv)