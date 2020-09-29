from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Item, Order, OrderItem, BillingAddress, Variation
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.utils import timezone 
from django.contrib import messages
from .forms import CheckoutForm, SearchForm, ItemReviewForm
#from .filters import SearchFilter
 
def search(request):
    try:
        q = (request.GET.get('q'))
    except:
        q = None
    if q:
        
        title = Item.objects.filter(name__icontains=q)
        products = Item.objects.filter(brand__icontains=q)
        if title:
            context = {'query':q, 
                        "products":title
                    }
            template = 'shop/results.html'
        elif products:
            context = {'query':q, 
                        "products":products
                    }
            template = 'shop/results.html'
        else:
            context = {
                    }
            template = 'shop/index.html'
            messages.info(request, f"This item does not exist.")
        return render(request, template, context)
        
    else:
        context = {}
        template = 'shop/index.html'
    
    return render(request, template, context)

class HomeListView(ListView): 
    model = Item
    template_name = 'shop/index.html'
    context_object_name = 'items'
    ordering = ['-date_posted']

def ItemDetail(request):
    colors = {
        ('R','Red'),
        ('B','Black'),
        ('P','Pink'),
        ('Y','Yellow')
    }

    context = {
        'items': Item.objects.all(),
        'colors': colors
    }
    return render(request, 'shop/single-product.html', context)

class ItemDetailView(DetailView): 
    model = Item
    template_name = 'shop/single-product.html' 
    context_object_name = 'item'

    def review(self, request):
        form = ItemReviewForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)   
    
 
class CategoryListView(ListView):
    model = Item 
    #filter = SearchFilter
    template_name = 'shop/category.html'
    context_object_name = 'items'
    ordering = ['-date_posted'] 
    

    def search(self, request):
        form = SearchForm()
        context = {
            'form' : form
        }
        return render(self.request, 'shop/category.html', context)

    
def men(request):
    
    qs = Item.objects.filter(gender = 'M')
    context = {
        'items' : Item.objects.filter(gender = 'M'),
        'name' : 'Men'
    }
    return render(request, 'shop/category.html', context)

def women(request):
    
    context = {
        'items' : Item.objects.filter(gender = 'F'),
        'name' : 'Women'
    }

    return render(request, 'shop/category.html', context)

def shoes(request):
    
    context = {
        'items' : Item.objects.filter(category = 'S'),
        'name' : 'Shoes'
    }
    
    return render(request, 'shop/category.html', context)

class CartListView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        
        try:
            order = Order.objects.get(user=self.request.user, ordered = False
        )
            context = {
                'object': order
            }
            return render(self.request, 'shop/shop-cart.html',context)
        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have an active order.')
            return redirect("/")
    
@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug) 
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )#if user has order
    order_qs = Order.objects.filter(user=request.user, ordered=False) #getting incomplete orders
    if order_qs.exists(): #if the order qs exists
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f"This item quantity was updated.")
            return redirect('shop-cart')
            
        else:#item not in the query
            order.items.add(order_item)
            messages.info(request, f"This item was added to your cart.")
            return redirect('shop-cart')
            
    else: 
        
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, f"This item was added to your cart.")
    return redirect('item-detail', slug=slug)

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug) 
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    ) #check if user has an order
    if order_qs.exists(): #if the order qs exists
        order = order_qs[0]#grabbing the order
        if order.items.filter(item__slug=item.slug).exists():#filter order that contains that item slug
            order_item = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )[0]
            order.items.remove(order_item)
            messages.info(request, f"This item was removed from your cart.")
        else:
            #add a message saying theres no order
            return redirect('shop-cart', slug=slug)
            messages.info(request, f"This item was not in your cart.")
            
    else: 
        #add a message saying theres no order
        messages.info(request, f"You have no active order.")
        return redirect('item-detail', slug=slug)
    return redirect('shop-cart')

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug) 
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    ) #check if user has an order
    if order_qs.exists(): #if the order qs exists
        order = order_qs[0]#grabbing the order
        if order.items.filter(item__slug=item.slug).exists():#filter order that contains that item slug
            order_item = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )[0]
            if order_item.quantity > 1:
                
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            
            messages.info(request, f"This item quantity was updated.")
            return redirect('shop-cart')
        else:
            #add a message saying theres no order
            return redirect('shop-cart')
            messages.info(request, f"This item was not in your cart.")
            
    else: 
        #add a message saying theres no order
        messages.info(request, f"You have no active order.")
        return redirect('item-detail', slug=slug)
    return redirect('item-detail', slug=slug)
   
class Checkout(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        order = Order.objects.get(user=self.request.user, ordered = False)
        context = {
            'form': form,
            'item': order
        }
        return render(self.request, 'shop/checkout.html', context)     

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered = False)
            if form.is_valid():
                print(form.cleaned_data)
                phone_number = form.cleaned_data.get('phone_number')
                street_address = form.cleaned_data.get('street_address')
                ZIP = form.cleaned_data.get('ZIP')
                home_address = form.cleaned_data.get('home_address')
                country = form.cleaned_data.get('country')
                save_info = form.cleaned_data.get("save_info")
                # TODO: add functionality for these fields
                #same_billing_address = form.cleaned_data.get("same_billing_address")
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user = self.request.user,
                    street_address = street_address,
                    home_address = home_address,
                    country = country,
                    zip = ZIP

                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                # TODO add a redirect to the payment option
                return redirect("shop-checkout")
            messages.warning(self.request,"Failed checkout")
            return redirect("shop-checkout")
        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have an active order.')
            return redirect("shop-cart")

class PaymentView(View):
    def get(self, *args, **kwargs): 
        return render(self.request,'shop/payment.html')     
        
    

        




    
