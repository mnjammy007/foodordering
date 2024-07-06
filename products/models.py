from django.db import models
import uuid


class BaseProduct(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class Product(BaseProduct):
    product_name = models.CharField(max_length=200)
    product_slug = models.SlugField(max_length=200, unique=True)
    product_description = models.TextField()
    product_price = models.DecimalField(default=49.0, max_digits=10, decimal_places=2)
    product_cost_price = models.DecimalField(
        default=29.0, max_digits=10, decimal_places=2
    )
    is_available = models.BooleanField(default=True)


class ProductMetaInfo(BaseProduct):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="meta_info")
    measurement_unit = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        choices=(("kg", "kg"), ("g", "g"), ("l", "l"), ("ml", "ml"), (None, None)),
    )
    quantity = models.IntegerField(default=1)
    is_restricted = models.BooleanField(default=False)
    restricted_quantity = models.IntegerField(default=10)


class ProductImages(BaseProduct):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
