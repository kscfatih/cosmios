from .models import Category

def categories(request):
    return {
        'categories':Category.objects.filter(is_active=True)
    }

# def context(request):
#     return {
#         'context1':'Merhaba',
#         'context2':'Dünya'
#     }