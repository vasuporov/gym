# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ApschedulerJobs(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    next_run_time = models.FloatField(blank=True, null=True)
    job_state = models.TextField()

    class Meta:
        managed = False
        db_table = 'apscheduler_jobs'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ManagementFeespaymenthistory(models.Model):
    deleted = models.IntegerField()
    payment_type = models.CharField(max_length=256)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    discount = models.DecimalField(max_digits=19, decimal_places=2)
    fees_for_month = models.IntegerField()
    fees_for_year = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    gym = models.ForeignKey('ManagementGym', models.DO_NOTHING)
    gym_member_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'management_feespaymenthistory'


class ManagementFeesstructure(models.Model):
    deleted = models.IntegerField()
    fees_amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    gym = models.ForeignKey('ManagementGym', models.DO_NOTHING)
    fees_structure_type = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'management_feesstructure'


class ManagementGym(models.Model):
    deleted = models.IntegerField()
    gym_name = models.CharField(max_length=256)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    gym_owner = models.ForeignKey('ManagementGymowner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'management_gym'


class ManagementGymmember(models.Model):
    deleted = models.IntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    date_of_birth = models.DateTimeField()
    phone = models.CharField(max_length=256)
    photo = models.CharField(max_length=100)
    joining_date = models.DateTimeField()
    leaving_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    gym = models.ForeignKey(ManagementGym, models.DO_NOTHING)
    biceps_left = models.IntegerField(blank=True, null=True)
    biceps_right = models.IntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    triceps_left = models.IntegerField(blank=True, null=True)
    triceps_right = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    fees_structure = models.ForeignKey(ManagementFeesstructure, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'management_gymmember'


class ManagementGymowner(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'management_gymowner'


class ManagementGymownerGroups(models.Model):
    gymowner = models.ForeignKey(ManagementGymowner, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'management_gymowner_groups'
        unique_together = (('gymowner', 'group'),)


class ManagementGymownerUserPermissions(models.Model):
    gymowner = models.ForeignKey(ManagementGymowner, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'management_gymowner_user_permissions'
        unique_together = (('gymowner', 'permission'),)
