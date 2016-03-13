from .models import SEO

def get_seos(request):
    context = {}
    context['seos'] = SEO.objects.all()
    return context
