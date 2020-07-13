from django.shortcuts import render, redirect
from .forms import WidgetForm
from .models import Widget

# Create your views here.
def home(request):
  widget_form = WidgetForm()
  return render(request, 'home.html',{
    'widget_list' : Widget.objects.all(),
    'widget_form' : widget_form
  })

def add_widget(request):
  if request.method == 'POST':
    description = request.POST.get('description')
    quantity = request.POST.get('quantity')
    form = WidgetForm(request.POST)
    if form.is_valid():
      new_widget = form.save(commit=False)
      new_widget.description = description
      new_widget.quantity = quantity
      new_widget.save()
  return redirect('/')

def delete(request, id):
  widget = Widget.objects.get(id=id)
  widget.delete()
  return redirect('/')
