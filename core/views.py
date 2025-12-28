from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Category, Product, Sale, SaleItem
from django.utils.timezone import localdate
from django.db.models import Sum


def tpv_view(request):
    categories = Category.objects.prefetch_related("products").all()

    cart = request.session.get("cart", {})
    total = sum(item["price"] * item["qty"] for item in cart.values())

    return render(request, "core/tpv.html", {
        "categories": categories,
        "cart": cart,
        "total": total,
    })


def add_to_cart(request, product_id):
    if request.method != "POST":
        return redirect("tpv")

    cart = request.session.get("cart", {})

    # Obtenemos producto o 404
    product = get_object_or_404(Product, id=product_id)

    pid = str(product_id)

    if pid in cart:
        cart[pid]["qty"] += 1
    else:
        cart[pid] = {
            "name": product.name,
            "price": float(product.price),
            "qty": 1,
        }

    request.session["cart"] = cart
    return redirect("tpv")

def remove_from_cart(request, product_id):
    """Resta 1 unidad del producto en el carrito."""
    if request.method != "POST":
        return redirect("tpv")

    cart = request.session.get("cart", {})
    pid = str(product_id)

    if pid in cart:
        cart[pid]["qty"] -= 1
        # Si la cantidad llega a 0, eliminamos la línea
        if cart[pid]["qty"] <= 0:
            del cart[pid]

    request.session["cart"] = cart
    return redirect("tpv")


def delete_from_cart(request, product_id):
    """Elimina completamente el producto del carrito."""
    if request.method != "POST":
        return redirect("tpv")

    cart = request.session.get("cart", {})
    pid = str(product_id)

    if pid in cart:
        del cart[pid]

    request.session["cart"] = cart
    return redirect("tpv")



def clear_cart(request):
    request.session["cart"] = {}
    return redirect("tpv")


def charge(request):
    if request.method != "POST":
        return redirect("tpv")

    cart = request.session.get("cart", {})
    if not cart:
        return redirect("tpv")

    total = sum(item["price"] * item["qty"] for item in cart.values())

    payment_method = request.POST.get("payment_method", "EFECTIVO")

    sale = Sale.objects.create(
        total=total,
        payment_method=payment_method,
    )

    for product_id, item in cart.items():
        SaleItem.objects.create(
            sale=sale,
            product_id=int(product_id),
            qty=item["qty"],
            price=item["price"],
        )

    request.session["cart"] = {}
    return redirect("tpv")


def report_today(request):
    today = localdate()

    sales = Sale.objects.filter(created_at__date=today)
    sale_items = SaleItem.objects.filter(sale__in=sales)

    # Agrupar por producto y sumar cantidades
    productos_agrupados = (
        sale_items.values("product__name")
        .annotate(total_qty=Sum("qty"))
        .order_by("product__name")
    )

    total_dinero = sales.aggregate(total=Sum("total"))["total"] or 0

    context = {
        "productos_agrupados": productos_agrupados,
        "sales": sales,
        "total_dinero": total_dinero,
        "fecha": today,
    }

    return render(request, "core/report_today.html", context)

@user_passes_test(lambda u: u.is_superuser)
def reset_data(request):
    """Página para confirmar y borrar TODAS las ventas."""
    if request.method == "POST":
        # Borrar todas las ventas y líneas
        SaleItem.objects.all().delete()
        Sale.objects.all().delete()
        return render(request, "core/reset_done.html")
    
    # Si es GET, mostrar confirmación
    return render(request, "core/reset_confirm.html")

