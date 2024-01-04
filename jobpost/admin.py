from django.contrib import admin
from jobpost.models import job_posts,submit,comment
# Register your models here.
admin.site.register(job_posts)
admin.site.register(submit)
admin.site.register(comment)
