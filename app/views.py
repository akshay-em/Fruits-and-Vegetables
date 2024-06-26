from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from app.models import product,User,customer,feedback,order_details
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib import messages





def home(request):
    return render(request,'index.html')


def shop(request):
    x=product.objects.all()
    return render(request,'shop.html',{'data':x})




def adminhome(request):
    return render(request,'adminhome.html')


def logouts(request):
    logout(request)
    return redirect(home)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def logins(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        x=authenticate(request,username=username,password=password)
        if x is not None and not x.is_superuser:
            login(request,x)
            request.session['id']=x.id
            return redirect(shop)
        elif x is not None and x.is_superuser==1:
            login(request,x)
            request.session['id']=x.id
            return render(request,'adminhome.html')
        else:
            # messages.error(request,'invalid username or password')
            # return redirect(logins)
            error_message = [{"data": "Login failed. Please check your username and password."}]
            #print(error_message)
            return render(request, 'login.html', {'data': error_message})
            
    else:
        return render(request,'login.html')
    

def signup(request):
    if request.method=='POST':
        u=request.POST['username']
        e=request.POST['email']
        p=request.POST['password']
        us=User.objects.create_user(username=u,email=e,password=p)
        v=customer.objects.create(customerid=us,username=u,email=e,password=p)
        v.save()
        return redirect(logins)
    
def register_product(request):
    if request.method=='POST':
        pname=request.POST['pname']
        pcategory=request.POST['pcategory']
        pdescription=request.POST['pdescription']
        pprice=request.POST['pprice']
        img=request.FILES['image']
        x=product.objects.create(product_name=pname,category=pcategory,description=pdescription,price=pprice,image=img)
        x.save()
        return redirect(adminhome)
    else:
        return render(request,'prodregistration.html')
    

def viewproductadmin(request):
    y=product.objects.all()
    return render(request,'adminviewproduct.html',{'data':y})

def backtoadmin(request):
    return render(request,'adminhome.html')

def deleteproduct(request,id):
    x=product.objects.get(id=id)
    x.delete()
    return redirect(viewproductadmin)

def editproduct(request,id):
    p=product.objects.get(id=id)
    print(p)
    return render(request,'editproduct.html',{'data':p})

def updateproduct(request,id):
    if request.method=='POST':
        pname=request.POST['pname']
        pcategory=request.POST['pcategory']
        pdescription=request.POST['pdescription']
        pprice=request.POST['pprice']
        img=request.FILES['image']
        x=product.objects.get(id=id)
        x.product_name=pname
        x.category=pcategory
        x.description=pdescription
        x.price=pprice
        x.image=img
        x.save()
        return redirect(viewproductadmin)
    else:
        return HttpResponse("failed to update")
    

def feed_back(request):
    if request.method=='POST':
        name=request.POST['yourname']
        email=request.POST['youremail']
        message=request.POST['yourmessage']
        
        a=feedback.objects.create(customername=name,email=email,message=message)
        a.save()
        return redirect(contact)
    






@login_required(login_url='/log')
def place_order(request, product_id):
    
    products = get_object_or_404(product, id=product_id)
    

    if request.method == 'POST':       
        fname = request.POST.get('fname')
        lname = request.POST.get('lastname')
        hname = request.POST.get('hname')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        pcode = request.POST.get('pcode')
        phoneno = request.POST.get('phoneno')
        email = request.POST.get('email')
        texta = request.POST.get('texta')
        quantity = int(request.POST.get('quantity'))
        customerss=request.session['id']
        a=customer.objects.get(customerid=customerss)
        if quantity is None:
            return render(request, 'placeorder.html', {'product': product, 'error': 'Quantity is required'})

        
        try:
            quantity = int(quantity)
        except ValueError:
            return render(request, 'placeorder.html', {'product': product, 'error': 'Invalid quantity value'})

        
        product_price = products.price
        total_price = product_price * quantity
        total_price = products.price * quantity

        
        order = order_details.objects.create(
            first_name=fname,
            last_name=lname,
            housename=hname,
            address=address,
            city=city,
            country=country,
            postcode=pcode,
            mobile=phoneno,
            email=email,
            ordernotes=texta,
            oid=a,
            
            product_id=products, 
            quantity=quantity,
            total_price=total_price,
            product_name=products.product_name,
            approve=0   
        )
        # order.save()
        # return redirect(order_sucess)
        return render(request,'orderpending.html')  

    
    context = {
        'product': products
    }
    print(context)
    return render(request, 'placeorder.html', context)



def order_sucess(request):
    return render(request,'ordersuccess.html')


def vieworder_details(request):
    x=order_details.objects.all()
   
    return render(request,'vieworderdetails.html',{'data':x})






         


@login_required
def editprofile(request):
    user = request.user
    p = get_object_or_404(customer, customerid=user)
    return render(request, 'editprofile.html', {'data': p})

@login_required
def updateprofile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        # password = request.POST['password']       
        user = request.user
        x = get_object_or_404(customer, customerid=user)
        x.username = username
        x.email = email
        # x.password=password
        x.save()
        user.username = username
        user.email = email
        # user.password=password
        user.save()
        
        return redirect('home')
    else:
        return HttpResponse("Failed to update")
    
@login_required
def ordercustomer_view(request):
    c=request.user
    print(c)
    a=customer.objects.get(username=c)
    print(a)
    y=order_details.objects.filter(oid=a)
    print(y)       
    # y = order_details.objects.filter(product_id=c)
    return render(request,'ordercustomerview.html',{'data':y})


def deleteorder(request,id):
    x=order_details.objects.get(id=id)
    x.delete()
    return redirect(canceluserorder)


def canceluserorder(request):
    return render(request,'ordercancel.html')

def approvereject(request):
    orders = order_details.objects.filter(approve=0)
    return render(request, 'approvereject.html', {'data': orders})

def orderpending(request):
    return render(request,'orderpending.html')


def approve_order(request,id):
    order=order_details.objects.get(id=id)
    order.approve = 1
    order.save()
    return redirect(approvereject)

def orderstatus(request,id):
    order=order_details.objects.get(id=id)
    if order.approve==1:
        return render(request,'ordersuccess.html')
    else:
        return render(request,'orderpending.html')
   
    
def orderdeletecustomer(request,id):
    order=order_details.objects.get(id=id)
    order.delete()
    return redirect(approvereject)


















