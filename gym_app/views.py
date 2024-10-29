from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Gym, Member, Equipment
from django.shortcuts import render

# Create your views here.
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'equip_list.html'
    context_object_name = 'all_equip_list'

class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'equip_detail.html'

class EquipmentCreateView(CreateView):
    model = Equipment
    template_name = 'equip_create.html'
    fields = ['name', 'gyms']

class EquipmentUpdateView(UpdateView):
    model = Equipment
    template_name = 'equip_edit.html'
    fields = ['gyms']

def query1(request):
    # Initialize an empty context to pass to the template
    context = {
        'member_name': None,
        'error_message': None,
    }

    try:
        oldest_member = Member.objects.earliest('membership_start_date')
        context['member_name'] = oldest_member.name

    except Member.DoesNotExist:
        context['error_message'] = "No members found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query1.html', context)

def query2(request):
    # Initialize an empty context to pass to the template
    context = {
        'member_num': None,
        'error_message': None,
    }

    try:
        context['member_num'] = Member.objects.all().count()

    except Member.DoesNotExist:
        context['error_message'] = "No members found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query2.html', context)

class QueryLinksView(TemplateView):
    template_name='queries_list.html'