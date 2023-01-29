from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse

from operative.models import Operative
from operative.forms import OperativeForm


def list_operatives(request):
    operatives =Operative.objects.all()

    context ={
        'operatives': operatives,
    }
    return render(request, 'operative/list_operatives.html',context=context )

class OperativesListView(LoginRequiredMixin,ListView):
    model = Operative
    template_name ='operative/list_operatives.html'
    queryset = Operative.objects.all()

def create_operative(request):
    if request.method =='GET':
        context = {
            'form' : OperativeForm()
        }

        return render(request, 'operative/create_operative.html',context=context)

    elif request.method == 'POST' :
        form=OperativeForm(request.POST)
        if form.is_valid():
            Operative.objects.create( 
                n_po =form.cleaned_data['n_po'],
                production_entry_date = form.cleaned_data['production_entry_date'],
                manufacturing_date = form.cleaned_data['manufacturing_date'],
                item = form.cleaned_data['item'],
                used_raw_material = form.cleaned_data['used_raw_material'],
                mp_mm = form.cleaned_data['unloading_raw_material'],
                used_finished_product = form.cleaned_data['used_finished_product'],
                pt_mm = form.cleaned_data['unloading_finished_product'],
                observations = form.cleaned_data['observations'],
                firm = form.cleaned_data['firm'],
            )
            context ={
                'message': 'Fabricacion elevada'
            }
            return render(request,'operative/create_operative.html', context=context)
        else:
            context = {
                'form_errors' : form.errors,
                'form' :OperativeForm()
            }
            return render (request,'operative/create_operative.html',context=context)

class OperativeCreateView(CreateView):
    model = Operative
    template_name = 'operative/create_operative.html'
    fields = '__all__'
    success_url = '/operative/list-operatives/'














