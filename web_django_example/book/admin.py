from django.contrib import admin
from .models import Category, Author, Book, BookComment

class BookCommentStackedInline(admin.StackedInline):
    model = BookComment

class BookTabularInline(admin.TabularInline):
    model = BookComment
    extra = 2

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'name','category','price','level','pulished','show_image']
    list_filter = ['pulished']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug':['name']}
    fieldsets=(
        (None, {'fields': ['code','slug', 'name','description','price','level','image','pulished']}),
        ('Category',{'fields': ['category', 'author'], 'classes': ['collapse']}),
    )
    inlines = [BookTabularInline]
 
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book,BookAdmin)
