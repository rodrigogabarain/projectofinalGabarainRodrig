from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


from logistics.models import Logistics
from logistics.forms import LogisticForm



def list_logistics(request):
    logistics = Logistics.objects.all()
    context ={
        'logistics': logistics,
    }
    return render(request,'logistics/list_logistics.html',context=context )

class LogisticsListView(LoginRequiredMixin,ListView):
    model = Logistics
    template_name ='logistics/list_logistics.html'
    queryset = Logistics.objects.all()

def create_logistic(request):
    if request.method =='GET':
        context = {
            'form' : LogisticForm()
        }

        return render(request, 'logistics/create_logistic.html',context=context)

    elif request.method == 'POST' :
        form=LogisticForm(request.POST)
        if form.is_valid():
            Logistics.objects.create( 
                n_po =form.cleaned_data['n_po'],
                dispatch_date = form.cleaned_data['dispatch_date'],
                coh = form.cleaned_data['coh'],
                doh = form.cleaned_data['doh'],
                client = form.cleaned_data['client'],
                address = form.cleaned_data['address'],
                dispatch = form.cleaned_data['dispatch'],
                form_of_dispatch = form.cleaned_data['form_of_dispatch'],
                item = form.cleaned_data['item'],
                used_raw_material = form.cleaned_data['used_raw_material'],
                used_raw_material1 = form.cleaned_data['used_raw_material1'],
                used_finished_product = form.cleaned_data['used_finished_product'],
                used_finished_product1 = form.cleaned_data['used_finished_product1'],
                observations = form.cleaned_data['observations'],
                firm = form.cleaned_data['firm'],
            )
            context ={
                'message': 'Logistica elevada'
            }
            return render(request,'logistics/create_logistic.html', context=context)
        else:
            context = {
                'form_errors' : form.errors,
                'form' :LogisticForm()
            }
            return render (request,'logistics/create_logistic.html',context=context)

class LogisticsCreateView(CreateView):
    model = Logistics
    template_name = 'logistics/create_logistic.html'
    fields = '__all__'
    success_url = '/logistics/list-logistics'

def logistic_update(request, pk):
    logistics =Logistics.objects.get(id=pk)

    if request.method== 'GET':
        context ={
            'form':LogisticForm(
                initial={
                    'n_po':logistics.n_po,
                    'dispatch_date':logistics.dispatch_date,
                    'dispatch_coh':logistics.coh,
                    'dispatch_doh':logistics.doh,
                    'client':logistics.client,
                    'address':logistics.address,
                    'form_of_dispatch':logistics.form_of_dispatch,
                    'dispatch':logistics.dispatch,
                    'item':logistics.item,
                    'used_raw_material':logistics.used_raw_material,
                    'used_raw_material1':logistics.used_raw_material1,
                    'used_finished_product':logistics.used_finished_product,
                    'used_finished_product1':logistics.used_finished_product1,
                    'observations':logistics.observations,
                    'firm':logistics.firm,
                    
                }
            )
        }
        return render(request, 'logistics/update_logistic.html',context=context)
    
    elif request.method == 'POST':
        form = LogisticForm(request.POST)
        if form.is_valid():
            logistics.n_po = form.cleaned_data['n_po']
            logistics.dispatch_date = form.cleaned_data['dispatch_date']
            logistics.coh = form.cleaned_data['coh']
            logistics.doh = form.cleaned_data['doh']
            logistics.client = form.cleaned_data['client']
            logistics.address = form.cleaned_data['address']
            logistics.form_of_dispatch = form.cleaned_data['form_of_dispatch']
            logistics.dispatch = form.cleaned_data['dispatch']
            logistics.item = form.cleaned_data['item']
            logistics.used_raw_material = form.cleaned_data['used_raw_material']
            logistics.used_raw_material1 = form.cleaned_data['used_raw_material1']
            logistics.used_finished_product = form.cleaned_data['used_finished_product']
            logistics.used_finished_product1 = form.cleaned_data['used_finished_product1']
            logistics.observations = form.cleaned_data['observations']
            logistics.firm = form.cleaned_data['firm']
            logistics.save()
            
            context = {
                'message':'Logistica actualizada'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form':LogisticForm()
            }
        return render(request,'logistics/update_logistic.html',context=context)





