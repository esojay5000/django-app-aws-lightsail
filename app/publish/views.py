from django.shortcuts import render

# Create your views here.
def index(request):
    """Render the ladning page for the publish page."""
    return render(request, 'publish/index.html')
