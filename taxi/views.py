from django.shortcuts import render

from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, TemplateView


from taxi.models import *

class PlanningView(ListView):
    model = planning 
    context_object_name = 'plannings'
    template_name = 'taxi/planning.html'
    def get_context_data(self, **kwargs):
        context = super(PlanningView, self).get_context_data(**kwargs)
        plannings= planning.objects.all().order_by('-numero_jour')
        for unplanning in plannings:
            voit = voiture.objects.filter(id=unplanning.numero_chassis_id)

            unplanning.numero_plaque = voit[0].numero_plaque
            unplanning.numero_station = voit[0].numero_station
            unplanning.date_service = voit[0].mise_en_service
            
            localisat= localisation.objects.filter(numero_chassis_id=voit[0].id).order_by('-heure')
            unplanning.derniereloc = localisat[0].numero_zone
            unplanning.heureloc = localisat[0].heure
            
            dist=distance.objects.filter(zonede=localisat[0].id)
            unplanning.otherzone = dist
            
            lemodel = modele.objects.filter(id=voit[0].modele_id)
            unplanning.modele = lemodel[0].modele
            unplanning.logo_voiture = lemodel[0].logo_voiture
            unplanning.nb_place = lemodel[0].nb_place
            unplanning.carburant = lemodel[0].carburant
            
            
            chauf = chauffeur.objects.filter(id=unplanning.numero_chauffeur_id)
            unplanning.nom = chauf[0].nom
            unplanning.prenom = chauf[0].prenom
            unplanning.adresse = chauf[0].adresse
            unplanning.logo_chauffeur = chauf[0].logo_chauffeur
            unplanning.num = chauf[0].numero_chauffeur
            
            lepermis = permi.objects.filter(id=chauf[0].permis_id)
            unplanning.permischauff = lepermis[0].categorie
        context['plannings'] = plannings
        return context
