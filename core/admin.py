from django.contrib import admin
from .models import Category, Product, Sale, SaleItem

# -------------------------
# CATEGORY ADMIN
# -------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# -------------------------
# PRODUCT ADMIN
# -------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name",)
    list_editable = ("price",)
    ordering = ("category", "name")

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "total", "payment_method")
    list_filter = ("payment_method", "created_at")
    search_fields = ("id",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ("sale", "product", "qty", "price")
    list_filter = ("product",)
    search_fields = ("product__name",)
    ordering = ("-sale",)

