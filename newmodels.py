# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    sno = models.IntegerField()
    username = models.CharField(primary_key=True, max_length=45)
    userpass = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'administrator'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bills(models.Model):
    bill_no = models.ForeignKey('Ledger', models.DO_NOTHING, db_column='bill_no')
    category = models.ForeignKey('Category', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    brand = models.ForeignKey('Brand', models.DO_NOTHING)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    bill_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bills'


class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'brand'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=45)
    category_info = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryToProduct(models.Model):
    category_id = models.IntegerField()
    product_id = models.IntegerField()
    category_to_product_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'category_to_product'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=45)
    cust_pass = models.CharField(max_length=45)
    cust_type = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=45, blank=True, null=True)
    residence = models.CharField(max_length=1000, blank=True, null=True)
    cust_status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Finance(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=45)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=45)
    brand_id = models.IntegerField()
    brand_name = models.CharField(max_length=45)
    selling_price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.IntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=0)
    bill_no = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    date_of_purchase = models.DateField()
    customer_id = models.IntegerField()
    cust_name = models.CharField(max_length=45)
    finance_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'finance'


class Inventory(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    selling_price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.IntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=0)
    inventory_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'inventory'


class Items(models.Model):
    category_name = models.CharField(max_length=45)
    product_name = models.CharField(max_length=45)
    brand_name = models.CharField(max_length=45)
    quantity = models.IntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=0)
    item_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    descript = models.CharField(max_length=16000, blank=True, null=True)
    selling_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Ledger(models.Model):
    bill_no = models.IntegerField(primary_key=True)
    date_of_purchase = models.DateField()
    customer = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ledger'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=45)
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductToBrand(models.Model):
    product_id = models.IntegerField()
    brand_id = models.IntegerField()
    product_to_brand_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_to_brand'
