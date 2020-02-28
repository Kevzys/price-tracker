from django.shortcuts import render
from .forms import CreateNewList, CreateNewItem
from .models import ProductList, Product
from bs4 import BeautifulSoup
import requests
# Create your views here.


def home(response):
    return render(response, 'leads/home.html')


def create_list(response):

    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            newlist = ProductList(name=name)
            newlist.save()
            response.user.productlist.add(newlist)
            return render(response, 'leads/mylist.html')
    else:
        form = CreateNewList()
    return render(response, 'leads/createlist.html', {"form": form})

def create_item(response, id):
    if response.method == "POST":
        form = CreateNewItem(response.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            name = form.cleaned_data['name']
            price = find_price(url)

            if valid(price):
                p = response.user.productlist.get(id=id)
                p.product_set.create(url=url, name=name, price=price)
                return redirect('leads/mylist.html')
            else:
                valid = 'URL could not be read, please try a different link'
                return render(response, 'leads/createitem.html', {'form': form, 'valid': valid})
        else:
            form = CreateNewItem()
        return render(response, 'leads/createitem.html', {"form": form})
    return
def find_price(url):
    headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }

    page = requests.get(URL, headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    return price

#done
def view_list(response):
    return render(response, 'leads/mylist.html', {})


def remove_list(response, id):
    
    return render(response, 'leads/mylist.html', {})

def remove_item(response, id, name):
    productList = ProductList.objects.get(id=id)
    if productList in response.user.productlist.all():
        p = response.user.productlist.get(id=id)
        p.product_set.filter(name=name).delete()
        return render(response, 'leads/mylist.html'. {})