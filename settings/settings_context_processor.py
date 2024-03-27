from .models import Settings
from django.views.decorators.cache import cache_page
from context_cache.decorators import caches
from django.core.cache import cache 


#@cache_page(60 * 10)
#@chache_for_context
def get_settings(request):
   
    #check data in cashe
    try:
       settings_data=caches.get('settings_data')
       print('cache')
    except Exception:
        print('new data')
   # if not settings_data:
        settings_data=Settings.objects.last()
        caches.sett('settings_data',settings_data,60*60*24)
        
    return{ 'settings_data':settings_data}