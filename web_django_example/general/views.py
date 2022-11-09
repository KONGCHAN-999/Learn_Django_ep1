from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index1.html')

# def index(request):
#     id = '001'
#     name = 'Kong'
#     email = 'kong@gmail.com'
#     return render(request, 'index.html', {
#         'id':id,
#         'name':name,
#         'email':email,
#     })

# def article(request):
#     return HTTPResponse('Article = ' + str(year) + ' Slug' + slug)
