from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'aa_stripe', 'url': 'http://pypi.python.org/pypi/aa_stripe/0.4.1'},
	{'name':'199Fix', 'url': 'http://pypi.python.org/pypi/199Fix/1.1.2'},
    ]
    context = {
        'title': 'ivan-crowdbotics-15',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
