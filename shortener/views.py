from django.shortcuts import render, redirect
from .models import URL
import random
import string

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        custom_code = request.POST.get('custom_code')
        
        if custom_code:
            short_code = custom_code
        else:
            short_code = generate_short_code()
        
        url, created = URL.objects.get_or_create(original_url=original_url, short_code=short_code)
        short_url = request.build_absolute_uri(f'/{short_code}')
        return render(request, 'shortener/result.html', {'short_url': short_url})
    
    return render(request, 'shortener/shorten.html')

def redirect_to_original(request, short_code):
    url = URL.objects.get(short_code=short_code)
    return redirect(url.original_url)