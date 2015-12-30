from django.contrib import admin

from .models import Contact, Post, Author, PostPart


class PostPartInline(admin.StackedInline):
  model = PostPart


class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'mail',)

admin.site.register(Contact, ContactAdmin)


class AuthorAdmin(admin.ModelAdmin):
  pass

admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
  list_display = ('__str__',)
  inlines = [
    PostPartInline,
  ]

admin.site.register(Post, PostAdmin)
