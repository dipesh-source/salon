from django.db import models
from django.contrib.auth.models import User

'''
    create package name
'''


class Package_name(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    total = models.PositiveIntegerField(null=True, blank=True)
    fdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


'''
    customers packages
'''


class Create_packages(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.ForeignKey(Package_name, on_delete=models.CASCADE)
    fack = models.CharField(max_length=100, null=True, blank=True)
    service = models.CharField(max_length=100)
    qty = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.PositiveBigIntegerField()
    special = models.PositiveIntegerField(null=True, blank=True)
    fdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fack


'''
    customers will buy this packages
'''


class Customers_package(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    pk_names = models.ForeignKey(Create_packages, on_delete=models.CASCADE)
    pk_name = models.CharField(max_length=100 )
    name = models.CharField(max_length=100)
    contact = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=100, null=True, blank=True)
    advance = models.PositiveIntegerField(null=True, blank=True)
    total = models.PositiveIntegerField(null=True, blank=True)
    fdate = models.DateTimeField(auto_now_add=True)

'''
    who customers have Buy package so, that all services
    will be stored here by Create Bulk Query 
'''
class My_package(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    customers = models.ForeignKey(Customers_package, on_delete=models.CASCADE,null=True, blank=True)
    cust = models.CharField(max_length=100, null=True, blank=True)
    fack = models.CharField(max_length=100, null=True, blank=True)
    service = models.CharField(max_length=100)
    qty = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.PositiveBigIntegerField()
    special = models.PositiveIntegerField(null=True, blank=True)
    fdate = models.DateTimeField(auto_now_add=True)

'''
    staff table
'''
class Staff(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ImageField(upload_to='staff/')
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=100, null=True, blank=True)
    service = models.CharField(max_length=100, null=True, blank=True)
    fdate = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


'''
    appointment table
'''


class Appointment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    uniq = models.CharField(max_length=100, null=True, blank=True)
    customer = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    datex = models.DateField(max_length=100)
    timex = models.TimeField()
    service = models.CharField(max_length=100, null=True, blank=True)
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null=True, blank=True)
    fdate = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.pk)


'''
    customerss data
'''
# class Customers(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
#     name = models.CharField(max_length=100, null=True, blank=True)
#     phone = models.PositiveBigIntegerField()
#     fdate = models.DateTimeField(auto_now_add=True)


'''
    appointment table (we dont't required to create the Form)
'''


class Appointment_data(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    uniq = models.CharField(max_length=100, null=True, blank=True)
    customer = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    datex = models.DateField(max_length=100)
    timex = models.TimeField()
    service = models.CharField(max_length=100, null=True, blank=True)
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null=True, blank=True)
    fdate = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.pk)

# '''
#     will make relationship between Staff Table And Appointment Table
# '''
# class Staffwork(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     staff_member = models.ForeignKey(Staff,on_delete=models.CASCADE, null=True, blank=True)
#     appointment_data = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)


'''
    local appointment (we dont't required to create the Form)
'''


class Local_appointment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=100, null=True, blank=True)
    service = models.CharField(max_length=100, null=True, blank=True)
    staff = models.CharField(max_length=100, null=True, blank=True)
    datex = models.DateField(max_length=100)
    timex = models.TimeField()
    fdate = models.DateTimeField(auto_now_add=True)


'''
    salon services
'''


class Service(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='service/')
    text = models.CharField(max_length=200, null=True, blank=True)
    cost = models.PositiveIntegerField()
    fdate = models.DateTimeField(auto_now_add=True)


'''
    will display roll of advanced salary
'''


class Advanced_salary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null=True, blank=True)
    pay = models.PositiveIntegerField()
    month = models.CharField(max_length=100)
    fdate = models.DateField(auto_now_add=True)
    ftime = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.pk)


'''
    staff salary
'''


class Salary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null=True, blank=True)
    pay = models.PositiveIntegerField()
    extra = models.PositiveIntegerField(default=0, null=True, blank=True)
    month = models.CharField(max_length=100)
    advance = models.ForeignKey(
        Advanced_salary, on_delete=models.CASCADE, null=True, blank=True)
    fdate = models.DateField(auto_now_add=True)
    ftime = models.TimeField(auto_now_add=True)
    # def __str__(self):
    #     return int(self.pk)


'''
    gallery table
'''


class Gallery(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    gall = models.ImageField(upload_to='gallery/')
    fdate = models.DateTimeField(auto_now_add=True)


'''
    feedback from
'''


class Feedback(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    feed = models.TextField(max_length=1400)
    fdate = models.DateTimeField(auto_now_add=True)


'''
    will store the staff timing
'''


class Timeing(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null=True, blank=True)
    in_date = models.DateField(max_length=100, auto_now_add=True)
    in_time = models.TimeField(auto_now_add=True)
    out_date = models.DateField(max_length=100, auto_now=True)
    out_time = models.TimeField(auto_now=True)
    fdate = models.DateTimeField(auto_now=True)
    tell = models.BooleanField(default=False,blank=True,null=True)
    # dure = models.DurationField(null=True,blank=True)
    # check = models.BooleanField(default=False)

    # odate = models.DateTimeField(auto_now_add=True, auto_now=True)
'''
    product table
'''


class Product(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    text = models.CharField(max_length=100, null=True, blank=True)
    fdate = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


'''
    who have get this product 
'''


class Purchase(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    price = models.PositiveIntegerField()
    qty = models.PositiveIntegerField()
    fdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
