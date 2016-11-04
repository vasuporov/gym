from django.contrib import admin
from models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _

# Register your models here.


admin.site.register(GymOwner)

admin.site.register(FeesPaymentHistory)
admin.site.register(FeesStructure)
admin.site.register(Gym)
admin.site.register(GymMember)
