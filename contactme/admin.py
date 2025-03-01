from django.contrib import admin
from .models import contactmemodel
from .models import projectsmodel
from .models import reviewmodel
# Register your models here.
class admincontactme(admin.ModelAdmin):
    list_display=("name_model","email_model","contactnumber_model","designation_model","subject_model","message_model")

class adminproject(admin.ModelAdmin):
    list_display=("projectname","projectdesc","projectcategory","projectdate","projectimg","projecturl","projectgithuburl")

class adminreview(admin.ModelAdmin):
    list_display=("reviewdesc","reviewimg","reviewname","reviewprofession")


admin.site.register(contactmemodel,admincontactme)
admin.site.register(projectsmodel,adminproject)
admin.site.register(reviewmodel,adminreview)