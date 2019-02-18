from django.contrib import admin
from core.models import *


class InlineSprint(admin.TabularInline):
	model = Sprint
	extra = 1


class InlineSpec(admin.TabularInline):
	model = Spec
	extra = 1

class ProjecteAdmin(admin.ModelAdmin):
	inlines = [InlineSprint, InlineSpec]


class SprintAdmin(admin.ModelAdmin):
	list_display = ['projecte', 'data_inici', 'data_final', 'hores']

class SpecAdmin(admin.ModelAdmin):
	list_display = ['projecte', 'dificultat', 'hores', 'descripcion']

# Register your models here.
admin.site.register(Projecte, ProjecteAdmin)
admin.site.register(Spec, SpecAdmin)
admin.site.register(Sprint, SprintAdmin)