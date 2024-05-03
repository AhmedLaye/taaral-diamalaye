
from django.shortcuts import render
from django.http import HttpResponse
import paydunya
from paydunya import InvoiceItem, Store
# Create your views here.

def taaral(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        numero = request.POST.get('numero')
        montant = request.POST.get('montant')

    
    return render(request, 'taaral.html', )




