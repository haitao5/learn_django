from django.contrib import admin

from TestModel.models import Test,Contact,Tag


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    inlines = [TagInline]
    search_fields = ('name',)
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )

class TestAdmin(admin.ModelAdmin): 
    list_display = (['name',])
    fields = (['name',])





admin.site.register(Contact, ContactAdmin)
admin.site.register(Tag)
admin.site.register(Test, TestAdmin)