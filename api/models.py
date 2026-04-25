from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.year} ({self.price})"

class Comment(models.Model):
    text = models.CharField(max_length=500)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text