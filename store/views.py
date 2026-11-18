from django.shortcuts import render
from utils.store.factory import make_shopp

# Create your views here.
def home(request):
    return render(request, 'store/pages/index.html', status=200, context={
        'stores': [make_shopp() for _ in range(10)],
    })

def store(request, id):
    return render(request, 'store/pages/shop-view.html', status=200, context={
        'store': make_shopp(),
    })