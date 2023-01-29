
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from planner.models import Planner
from planner.forms import PlannerForm



def list_planners(request):
        planners =Planner.objects.all()

        context ={
            'planners': planners,
        }
        return render(request,'planner/list_planners.html',context=context )

class PlannersListView(LoginRequiredMixin,ListView):
    model = Planner
    template_name ='planner/list_planners.html'
    queryset = Planner.objects.all()

def create_planner(request):
    if request.method =='GET':
        context = {
            'form' : PlannerForm()
        }

        return render(request,'planner/create_planner.html',context=context)

    elif request.method == 'POST' :
        form=PlannerForm(request.POST)
        if form.is_valid():
            Planner.objects.create( 
                n_po =form.cleaned_data['n_po'],
                admission_date = form.cleaned_data['admission_date'],
                client = form.cleaned_data['client'],
                coh = form.cleaned_data['coh'],
                doh = form.cleaned_data['doh'],
                date_required = form.cleaned_data['date_required'],
                dispatch = form.cleaned_data['dispatch'],
                item = form.cleaned_data['item'],
                raw_material = form.cleaned_data['raw_material'],
                raw_material1 = form.cleaned_data['raw_material1'],
                finished_product = form.cleaned_data['finished_product'],
                finished_product1 =form.cleaned_data['finished_product1'],
            )
            context ={
                'message': 'Orden de produccion cargada con exito'
            }
            return render(request,'planner/create_planner.html' , context=context)
        else:
            context = {
                'form_errors' : form.errors,
                'form' :PlannerForm()
            }
            return render (request,'planner/create_planner.html',context=context)

class PlannerCreateView(CreateView):
    model = Planner
    template_name = 'planner/create_planner.html'
    fields = '__all__'
    success_url = '/planner/list-planners/'

 



def planner_update(request, pk):
    planner =Planner.objects.get(id=pk)

    if request.method== 'GET':
        context ={
            'form':PlannerForm(
                initial={
                    'n_po':planner.n_po,
                    'admission_date':planner.admission_date,
                    'client':planner.client,
                    'coh':planner.coh,
                    'doh':planner.doh,
                    'admission_date':planner.admission_date,
                    'date_required':planner.date_required,
                    'dispatch':planner.dispatch,
                    'item':planner.item,
                    'planner.raw_material':planner.raw_material,
                    'planner.raw_material1':planner.raw_material1,
                    'planner.finished_product':planner.finished_product,
                    'planner.finished_product1':planner.finished_product1,

                }
            )
        }
        return render(request, 'planner/update_planner.html',context=context)
    
    elif request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            planner.n_po = form.cleaned_data['n_po']
            planner.admission_date = form.cleaned_data['admission_date']
            planner.client = form.cleaned_data['client']
            planner.coh = form.cleaned_data['coh']
            planner.doh = form.cleaned_data['doh']
            planner.date_required = form.cleaned_data['date_required']
            planner.dispatch = form.cleaned_data['dispatch']
            planner.item = form.cleaned_data['item']
            planner.raw_material = form.cleaned_data['raw_material']
            planner.raw_material1 = form.cleaned_data['raw_material1']
            planner.finished_product = form.cleaned_data['finished_product']
            planner.finished_product1 = form.cleaned_data['finished_product1']
            planner.save()
            
            context = {
                'message':'Orden actualizada'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form':PlannerForm()
            }
        return render(request,'planner/update_planner.html',context=context)

class PlannerDeletView(DeleteView):
    model = Planner
    template_name = 'planner/delete_planner.html'
    success_url = '/planner/list-planners'

