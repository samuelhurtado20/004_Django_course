from django.shortcuts import render
from django.views.generic import TemplateView
from app_001.models import Author

# Create your views here.
def home(request):
    data = {"title": "Home Page Django", "content": "Welcome to the amazing Django course!"}
    context = {
        "data": data,
    }
    return render(request, 'app_001/home.html', context)

def about(request):
    data = Author.objects.all()
    context = {
        "data": data,
    }
    return render(request, 'app_001/about.html', context=context)



def authors_view(request):
    list_of_authors = Author.objects.all()
    context = {"authors": list_of_authors}
    return render(request, 'app_001/authors.html', context)

def author_detail_view(request, *args, **kwargs):
    id = kwargs.get("id", None)
    # validate id
    if id is None:
        # return some error message
        pass
    author = Author.objects.get(id=id)
    context = {"author": author}
    return render(request, 'app_001/author_detail.html', context)

class AuthorDetailView(TemplateView):
    template_name = 'app_001/author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get("id", None)
        author = Author.objects.get(id=id)
        context['author'] = author
        return context