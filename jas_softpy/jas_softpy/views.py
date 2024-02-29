from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from production.views import SuppliesListView
from django.contrib.auth.models import User, Permission
from itertools import groupby

from production.models import ProductionOrder, Supplies
from inventory.models import Product

from .forms import RegisterForm
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('index')
        
def home(request):
    return render(request,'home.html',{
        #context
    })

def producto(request):
    return render(request,'producto.html',{
        #context
    })

def ventas(request):
    return render(request,'ventas.html',{
        #context
    })

def rrhh(request):
    return render(request,'rrhh.html',{
        #context
    })

def postulacion(request):
    return render(request,'postulation/Postulacion.html',{
        #context
    })

def ordenpedido(request):
    return render(request,'ordenpedido.html',{
        #context
    })

def insumo(request):
    return render(request,'insumo.html',{
        #context
    })

def ofertas(request):
    return render(request,'ofertas.html',{
        #context
    })

def send_email(mail):
    context = {'mail': mail}

    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo de prueba',
        'Primer correo JAS_SOFT',
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def sugerencias(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')

        send_email(mail)
        
    return render(request,'sugerencias.html',{})

def index(request):
    return render(request,'index.html',{
        #context
    })    

def sales(request):
    return render(request,'sales.html',{
        #context
    })   

def login_view(request):
    ids_produccion = [29, 30, 31, 32, 37, 38, 39, 40]
    ids_inventario = [41, 42, 43, 44, 45, 46, 47, 48]
    ids_venta      = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
    ids_gestion    = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]

    moduloProduccion = False
    moduloInventario = False
    moduloVenta      = False
    moduloGestion    = False

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_staff:
                login(request, user)
                messages.success(request, 'Bienvenido {}'.format(user.username))
                return redirect('admin:index')
            else:
                login(request, user)
                permisos = obtenerPermisosUsuarioPorModulo(request)
                
                for permiso in permisos:
                    if permiso in ids_produccion:
                        moduloProduccion = True
                        
                    if permiso in ids_inventario:
                        moduloInventario = True

                    if permiso in ids_venta:
                        moduloVenta = True

                    if permiso in ids_gestion:
                        moduloGestion = True

                return render(request, 'home.html', {'permission_production': moduloProduccion, 'permission_inventory': moduloInventario, 'permission_venta': moduloVenta, 'permission_gestion': moduloGestion})
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html',{
        
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('index')

def register(request):    

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password, last_name=last_name, first_name=first_name )
            if user:
                login(request, user)
                messages.success(request, 'Registro exitoso')
                return redirect('login_jas')
            
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def create_production_order(request):
   
    if request.method == 'POST':
        quantity_used = int(request.POST['quantity_used'])
        supplies_ids = request.POST.getlist('supplies')

        current_datetime = datetime.now()

        for supplies_id in supplies_ids:
            supplies_instance = Supplies.objects.get(id=supplies_id)

            if quantity_used <= supplies_instance.stock:
                ProductionOrder.objects.create(
                    quantity_used=quantity_used,
                    supplies=supplies_instance,
                    Production_OrderDate=current_datetime
                )

                supplies_instance.stock -= quantity_used
                supplies_instance.save()
            else:
                messages.error(request, f'No hay suficiente stock para el insumo {supplies_instance.name}')
                return redirect('ordenpedido') 

        messages.success(request, '¡Orden de producción creada exitosamente!')
        return redirect('ordenpedido') 

    return render(request, 'ordenpedido')
                        
def edit_production_order(request, id):
        productionorder = ProductionOrder.objects.get(id=id)
        return render(request, "EditProductOrder.html", {"productionorder": productionorder})

def editProductionOrder(request):    
    quantity_used = int(request.POST['stock'])    
    
    current_datetime = datetime.now()    
    productionorder = ProductionOrder.objects.update(
        quantity_used=quantity_used,         
        Production_OrderDate=current_datetime
        
    )
    
    supplies_instance = Supplies.objects.get(id=id)
    supplies_instance.stock -= quantity_used
    supplies_instance.save()

    messages.success(request, '¡Orden de producción actualizada!')
    return redirect('ordenpedido')
    
def deleteProductionOrder(request, id):
    
    productionorder = ProductionOrder.objects.get(pk=id)
    productionorder.delete()
    
    messages.success(request, 'Orden de producción eliminado!')

    return redirect('ordenpedido')         

def save(self, *args, **kwargs):
        if not self.id:
            last_object = Supplies.objects.last()
            if last_object:
                self.supplieCode = last_object.supplieCode + 1
            else:
                self.supplieCode = 100001
        super(Supplies, self).save(*args, **kwargs) 

def createsupplies(request):
   
    name = request.POST['name']
    stock = int(request.POST['stock'])
    size = request.POST['size']
    color = request.POST['color']    

    supplies = Supplies.objects.create(
        name = name, 
        stock = stock, 
        size = size,
        color = color,
    )
    
    messages.success(request, '¡el isumo se registro exitosamente!')
    return redirect('insumo')

def editsupplies(request, id):
    supplies = Supplies.objects.get(id=id)
    return render(request, "supplies/EditSupplies.html", {"Supplies":supplies})
    
@require_POST
def EditSupplies(request, id):
    if request.method == 'POST':
        supplies = get_object_or_404(Supplies, id=id)
        supplies.name = request.POST.get('name', '')
        supplies.stock = int(request.POST.get('stock', 0))
        supplies.size = request.POST.get('size', '')
        supplies.color = request.POST.get('color', '')       
        supplies.save()
        messages.success(request, '¡El insumo se ha actualizado!')
    else:
        messages.error(request, 'La solicitud no es válida.')

    return redirect('insumo')
    
def deleteSupplies(request, id):
    
    supplies = Supplies.objects.get(pk=id)
    supplies.delete()    
    messages.success(request, 'Orden de producción eliminado!')
    return redirect('insumo')         

def createinventory(request):
    if request.method == 'POST':     
        name = request.POST.get('name')
        stock = request.POST.get('stock')
        current_datetime = datetime.now()
        size = request.POST.get('size')
        color = request.POST.get('color')
        state = request.POST.get('state')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        inventory = Product.objects.create(
            name = name, 
            stock = stock, 
            size = size,
            color = color,
            state = state,
            category = category,
            image = image,
            fabricationDate = current_datetime 
        )
    
    messages.success(request, '¡el producto se registro exitosamente!')
    return redirect('producto')

def editinventory(request, id):
    producto = Product.objects.get(id=id)    
    return render(request, "inventory/editInventory.html", {"Product":producto})

@require_POST
def EditInventory(request, id):       
    if request.method == 'POST':
        producto = get_object_or_404(Product, id=id)
        producto.name = request.POST.get('name','')
        producto.stock = int(request.POST.get('stock', 0)) 
        producto.size = request.POST.get('size', '')
        producto.color = request.POST.get('color', '')
        producto.state = request.POST.get('state', '')
        producto.category = request.POST.get('category', '')     
        producto.save()
        messages.success(request, '¡El producto se ha actualizado!')
    else:
        messages.error(request, '¡La solicitud no es valida!')
    
    return redirect('producto')

def deleteinventory(request, id):
    
    producto = Product.objects.get(pk=id)
    producto.delete()    
    messages.success(request, 'Producto eliminado!')
    return redirect('producto')

def obtenerPermisosUsuarioPorModulo(request):
    usuario_actual = request.user
    permisos_usuario = usuario_actual.user_permissions.all()
    ids_permisos = permisos_usuario.values_list('id', flat=True)
    # Obtener los objetos Permission correspondientes a los IDs
    permisos = Permission.objects.filter(id__in=ids_permisos)
    # Obtener los IDs de los permisos
    ids_permisos = permisos.values_list('id', flat=True)

    return ids_permisos