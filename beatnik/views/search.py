from beatnik.api_manager import ApiManager
from beatnik.models.music import Music
from django.shortcuts import redirect, render
from django.views import View
from urllib import parse

class Search(View):
    def get(self, request):
        query = request.GET.get('q')

        if (query is None):
            return redirect('index')

        url = parse.urlparse(query)
        if (Music.objects.verify_url(url)):
            try:
                info = Music.objects.get_or_create(url)
            except ValueError:
                return self.handle_search(request, query)

            return redirect(info)
        else:
            return self.handle_search(request, query)

    def handle_search(self, request, query):
        api_manager = ApiManager()
        results = api_manager.search_handler.search(query)
        context = {
            'results': results
        }

        return render(request, 'results.html', context)
