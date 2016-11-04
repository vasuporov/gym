from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from safedelete import safedelete_mixin_factory, SOFT_DELETE
from django.db import models

safe_delete_mixin = safedelete_mixin_factory(policy=SOFT_DELETE)
safe_delete_admin_mixin = safedelete_mixin_factory(policy=SOFT_DELETE, manager_superclass=UserManager)


class GymOwner(safe_delete_admin_mixin, AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(auto_now=True)  # This should add the updated date every time.


class Gym(safe_delete_mixin):
    gym_name = models.CharField(max_length=256)
    gym_owner = models.ForeignKey(GymOwner, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(auto_now=True)  # This should add the updated date every time.


FEES_STRUCTURE_TYPE = (('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half-Yearly', 'Half-Yearly'))


class FeesStructure(safe_delete_mixin):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    fees_structure_type = models.CharField(choices=FEES_STRUCTURE_TYPE, max_length=256)
    fees_amount = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=19)

    created_at = models.DateTimeField(auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(auto_now=True)  # This should add the updated date every time.


class GymMember(safe_delete_mixin):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    gender = models.CharField(choices=(("male", "male"), ("female", "female")), max_length=256)
    date_of_birth = models.DateTimeField()
    phone = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='img/users/', default='img/users/no-img.png')
    joining_date = models.DateTimeField(auto_now_add=True)
    leaving_date = models.DateTimeField(default=None, null=True)

    height = models.DecimalField(blank=True, decimal_places=2, max_digits=4, default=None, null=True)
    weight = models.IntegerField(blank=True, default=None, null=True)
    biceps_right = models.IntegerField(blank=True, default=None, null=True)
    biceps_left = models.IntegerField(blank=True, default=None, null=True)
    triceps_right = models.IntegerField(blank=True, default=None, null=True)
    triceps_left = models.IntegerField(blank=True, default=None, null=True)

    fees_structure = models.ForeignKey(FeesStructure, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(auto_now=True)  # This should add the updated date every time.


class FeesPaymentHistory(safe_delete_mixin):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    gym_member = models.ForeignKey(GymMember, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=256)
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=19)
    discount = models.DecimalField(blank=True, decimal_places=2, max_digits=19)
    fees_for_month = models.IntegerField()
    fees_for_year = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(auto_now=True)  # This should add the updated date every time.

