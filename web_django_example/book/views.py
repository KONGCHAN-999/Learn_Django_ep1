from django.shortcuts import render, get_object_or_404
from .models import Category, Book
from slugify import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import BookForm

# Create your views here.

def index(request):
    categorries = Category.objects.all()
    books = Book.objects.filter(pulished=True)

    categ_id = request.GET.get('categoryid')
    if categ_id:
        books = books.filter(category_id=categ_id)

    paginator = Paginator(books, 3)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'book/index.html', {
        'categorries': categorries,
        'books': books,
        'categ_id': categ_id,
    })

def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book/detail.html',{
        'book': book,
    })

def book_add(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.slug = slugify(book.name)
            book.published = True
            book.save()
            form.save_m2m()
            messages.success(request, 'Save success')
            return HttpResponseRedirect(reverse('book:index', kwargs={}))
        messages.error(request, 'Save failed!')
    return render(request, 'book/add.html', {
        'form': form,
    })