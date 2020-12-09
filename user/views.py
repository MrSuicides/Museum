from .models import Modell, Images
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import requests
from bs4 import BeautifulSoup


# from .forms import FModel

def FilterSearch(text):
    list = ['истор', 'ботан', 'друг', 'друз', 'семь', 'семей', 'дет', 'реб', 'дорог', 'бюджет', 'дёшев', 'утр',
            'день', 'днём', 'вечер']
    otvet = []
    for i in text.split():
        for j in range(len(list)):
            if i[:3] == list[j][:3]:
                print(i, 'index')
                otvet.append(Search(i))
                break
    return otvet


def Search(otvet):
    if otvet == 'дёшево' or otvet == 'дорого':
        return Images.objects.all().filter(price=otvet)
    parser = Parser(otvet)

    # parser = 'вечер'
    if Images.objects.filter(profile=parser):
        return Images.objects.all().filter(profile=parser)
    elif Images.objects.filter(wth=parser):
        return Images.objects.all().filter(wth=parser)
    elif Images.objects.filter(time=parser):
        return Images.objects.all().filter(time=parser)
    else:
        print("GG WP")
        return 0


def indeex(request):
    str_name = request.GET.get("name")
    if str(str_name) == 'None':
        return render(request, 'Pages/indeex.html')
    all_info = FilterSearch(str_name.strip())
    temporary = []
    print(all_info, 'a')

    for i in all_info:
        temporary.append(all_info.count(i))
    a = {
        'all_info': all_info[temporary.index(max(temporary))]
    }
    print(a, 'a')

    return render(request, 'Pages/indeex.html', a)


def Parser(Word):
    URL = 'https://kartaslov.ru/разбор-слова-по-составу/' + Word

    Headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36',
        'accept': '*/*'}

    def get_html(url, params=None):
        r = requests.get(url, headers=Headers, params=params)
        return r

    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('tr')

        VocRadical = []
        Radical = ''
        for i in items:
            VocRadical.append({
                i.find('td', class_='td-morpheme-type').get_text():
                    i.find('td', class_='td-morpheme-text').get_text()
            })

        for i in VocRadical:
            if i.get('корень'):
                Radical = (i.get('корень'))
        # print(Radical)
        return Radical

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            return get_content(html.text)
        else:
            print('Error')

    return parse()
