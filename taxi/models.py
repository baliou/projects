from django.db import models
class station(models.Model):
    numero_station = models.IntegerField(null=True)
    numero_zone = models.IntegerField(null=True)  
    def __unicode__(self):
        return u"%s" % self.numero_station
class permi(models.Model):
    categorie = models.CharField(max_length=30)
    def __unicode__(self):
        return u"%s" % self.categorie
class modele(models.Model):
    modele = models.CharField(max_length=30)
    logo_voiture = models.ImageField(null=True,upload_to="logo/voiture")
    nb_place = models.IntegerField(null=True)
    carburant = models.CharField(max_length=30)
    boite_vitesse = models.CharField(max_length=30)
    poids = models.DecimalField(max_digits=5, decimal_places=2)
    categorie = models.ForeignKey(permi)
    def __unicode__(self):
        return u"%s" % self.modele
class voiture(models.Model):
    numero_chassis = models.IntegerField()
    numero_plaque = models.CharField(max_length=30)
    mise_en_service = models.DateField(null=True)
    modele = models.ForeignKey(modele)
    numero_station = models.ForeignKey(station)
    def __unicode__(self):
        return u"%s" % self.numero_plaque
class carburant(models.Model):
    numero_jour = models.DateField(null=True)
    kilometrage = models.DecimalField(max_digits=5, decimal_places=2)
    litres = models.DecimalField(max_digits=5, decimal_places=2)
    numero_plaque = models.ForeignKey(voiture)
    def __unicode__(self):
        return u"%s %s" % (self.numero_jour,self.numero_plaque)
class chauffeur(models.Model):
    numero_chauffeur = models.IntegerField()
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=255)
    logo_chauffeur = models.ImageField(null=True,upload_to="logo/chauffeur")
    numero_station = models.ForeignKey(station)
    permis = models.ForeignKey(permi)
    def __unicode__(self):
        return u"%s-%s -%s" % (self.numero_chauffeur,self.nom,self.prenom)
class planning(models.Model):
    numero_chauffeur = models.ForeignKey(chauffeur)
    numero_chassis = models.ForeignKey(voiture)
    numero_jour = models.DateField(null=True)
    debut = models.TimeField()
    Fin = models.TimeField()
    def __unicode__(self):
        return u"%s-%s" % (self.numero_chauffeur,self.numero_jour)
class localisation(models.Model):
    numero_chassis = models.ForeignKey(voiture)
    heure = models.DateField(null=True)
    numero_zone = models.IntegerField()
    def __unicode__(self):
        return u"%s" % self.numero_chassis
class distance(models.Model):
    zonede = models.IntegerField()
    zonea = models.IntegerField()
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    temps_parcours = models.DecimalField(max_digits=5, decimal_places=2)
    def __unicode__(self):
        return u"%s-%s" % (self.zonede,self.zonea)
