from django.db import models


class Animal(models.Model):
    id_animal = models.TextField()
    lieu = models.TextField()
    type = models.TextField()
    ETAT_CHOICES = (('Affame', 'affame'), ('Endormi', 'endormi'), ('Repu', 'repu'), ('Fatigue', 'fatigue'))
    etat = models.CharField(max_length=100, choices=ETAT_CHOICES)
    race = models.TextField()

    def lit_id_animal(self):
        if self.id_animal not in ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']:
            return "Désolé, " + str(self.id_animal) + " n'est pas un animal connu "
        else:
            return self.id_animal

    def lit_état(self):
        if self.id_animal not in ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']:
            return "Désolé, " + str(self.id_animal) + " n'est pas un animal connu "
        else:
            return self.etat

    def lit_lieu(self):
        if self.id_animal not in ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']:
            return "Désolé, " + str(self.id_animal) + " n'est pas un animal connu "
        else:
            return self.lieu

    def lit_type(self):
        if self.id_animal not in ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']:
            return "Désolé, " + str(self.id_animal) + " n'est pas un animal connu "
        else:
            return self.type

    def lit_race(self):
        if self.id_animal not in ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']:
            return "Désolé, " + str(self.id_animal) + " n'est pas un animal connu "
        else:
            return self.race


    def change_etat(self, etat):
        if etat not in ["affame", "fatigue", "repus", "endormi"]:
            return "Désolé, " + str(etat) + " n'est pas un état autorisé"
        self.etat = etat
        self.save()
        print("Changement d'état ok")

    def change_lieu(self, lieu):
        equipements = Equipement.objects.all()
        if self.id_animal in ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']:
            if lieu in ['litiere', 'mangeoire', 'roue', 'nid']:
                for e in equipements :
                    if e.lit_equipement() == lieu:
                        equipement = e
                if equipement.lit_disponibilite != 'occupé':
                    self.lieu = lieu
                    self.save()
                    if lieu != 'litière':
                        equipement.disponibilite = 'occupé'
                        equipement.save()
                print("Changement de lieu ok")


class Equipement(models.Model):
    id_equipement = models.TextField()
    DISPO_CHOICES = (('Occupe', 'occupe'), ('Libre', 'libre'))
    disponibilite = models.CharField(max_length=100, choices=DISPO_CHOICES)

    def lit_equipement(self):
        if self.id_equipement not in ['litiere','mangeoire','roue','nid']:
            return "Désolé, " + str(self.id_equiment) + " n'est pas un animal connu "
        else:
            return self.id_equipement

    def lit_disponibilite(self):
        if self.id_equipement not in ['litiere','mangeoire','roue','nid']:
            return "Désolé, " + str(self.id_equiment) + " n'est pas un animal connu "
        else:
            return self.disponibilite


    def cherche_occupant(self):
        lanimal = []
        animals = Animal.objects.all()
        for animal in animals:
            if animal.lit_lieu == self.id_equipement:
                lanimal.add(animal)
        if lanimal == []:
            print("Cet équipement n'est pas occupé")
            return None
        else:
            return lanimal



# Create your models here.
