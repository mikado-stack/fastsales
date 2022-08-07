from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'customer', null=True, blank=True,)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=11, null=True)
	profile_pic = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	CATEGORY = (
		('cloths', 'cloths'),
		('shoes', 'shoes'),
		('fairly used laptops', 'fairly used laptops')
		) 
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	price_slash = models.DecimalField(max_digits=7, decimal_places=2, default=False)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
	description = models.TextField(max_length=2000, null=True, blank=True)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def num_likes(self):
		return self.liked.all().count()

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
  
class Arrive(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	price_slash = models.DecimalField(max_digits=7, decimal_places=2, default=False)
	description = models.TextField(max_length=2000, null=True, blank=True)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def num_likes(self):
		return self.liked.all().count()

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url



LIKE_CHOICES ={
	('like', 'like'),
	('unlike','unlike'),
}

class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)

	def __str__(self):
		return str(self.product)

class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'),
		('Delivered', 'Delivered'),
		)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)
     

	@property
	def popURL(self):
		try:
			url = self.pop.url
		except:
			url = ''
		return url

	def __str__(self):
		return f"{self.customer}, {self.id}"
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
 

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	def __str__(self):
    		return f"{self.customer}, {self.product.name}, ({self.quantity})  {self.date_added.strftime('%a-%B-(%H:%M:%S)')}"

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	phone_num = models.CharField(max_length=11, default=False, blank=False, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
    		return f"{self.address} {self.date_added.strftime('%a-%B-%Y(%H:%M:%S)')}"

	
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=100)
	
    
    def __str__(self):
        return self.name
    
class Slide(models.Model):
    caption1 = models.CharField(max_length=100, null=False)
    caption2 = models.CharField(max_length=100, null=False)
    link = models.CharField(max_length=100, null=False)
    image = models.ImageField(help_text="Size: 1920x570")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.caption1, self.caption2)
    @property
    def imageURL(self):
					try:
						url =self.image.url
					except:
						url =''
					return url
	

class Pop(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    prove_of_payment = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return str(self.customer)
    