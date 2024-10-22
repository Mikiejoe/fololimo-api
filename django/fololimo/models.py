from django.db import models


TYPES = (
    ('farmer', 'Farmer'),
    ('agrovet', 'Agrovet'),
)


class Client(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, choices=TYPES, default='farmer')

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.type} - {self.location}"    


class Tip(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    mpesa_receipt = models.CharField(max_length=100, blank=True, null=True)
    mpesa_checkout_id = models.CharField(max_length=100, blank=True, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.client.name


class Region(models.Model):
    region = models.CharField(max_length=30)

    def __str__(self):
        return self.region


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'Cities'


class SubCounty(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    sub_county = models.CharField(max_length=30)

    def __str__(self):
        return self.sub_county

    class Meta:
        verbose_name_plural = 'Sub Counties'


class Weather(models.Model):
    temperature = models.FloatField()
    description = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    humidity = models.FloatField(blank=True, null=True)
    min_temp = models.FloatField(blank=True, null=True)
    max_temp = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'Weather'


class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    size = models.FloatField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    message = models.TextField()
    location = models.ForeignKey(SubCounty, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
