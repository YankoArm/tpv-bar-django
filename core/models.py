from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.name} ({self.price} €)"


PAYMENT_METHOD_CHOICES = (
    ("EFECTIVO", "Efectivo"),
    ("TARJETA", "Tarjeta"),
    ("BIZUM", "Bizum"),
)


class Sale(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default="EFECTIVO",
    )

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return f"Venta #{self.id} - {self.created_at:%d/%m/%Y %H:%M}"



class SaleItem(models.Model):
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)  # precio unitario

    class Meta:
        verbose_name = "Línea de venta"
        verbose_name_plural = "Líneas de venta"

    def line_total(self):
        return self.qty * self.price

