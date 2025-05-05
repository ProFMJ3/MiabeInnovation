from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Temoignage(models.Model):
    # Choix pour le statut de modération
    STATUT_CHOICES = [
        ('en_attente', 'En attente de modération'),
        ('approuve', 'Approuvé et publié'),
        ('rejete', 'Rejeté'),
    ]
    
    # Informations sur le client
    nom_complet = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Adresse email")
    profession = models.CharField(max_length=100, blank=True, null=True, verbose_name="Profession/Fonction")
    
    # Contenu du témoignage
    note = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Note (sur 5)"
    )
    contenu = models.TextField(verbose_name="Témoignage")
    media = models.FileField(
        upload_to='temoignages/medias/',
        blank=True,
        null=True,
        verbose_name="Média (photo/vidéo)",
        help_text="Formats acceptés: JPG, PNG, MP4 (max 5MB)"
    )
    
    # Métadonnées et modération
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_attente',
        verbose_name="Statut de modération"
    )
    date_soumission = models.DateTimeField(auto_now_add=True, verbose_name="Date de soumission")
    date_publication = models.DateTimeField(blank=True, null=True, verbose_name="Date de publication")
    consentement_publication = models.BooleanField(default=False, verbose_name="Consentement à la publication")
    
    # Méthodes
    def __str__(self):
        return f"Témoignage de {self.nom_complet} - Note: {self.note}/5"
    
    def save(self, *args, **kwargs):
        # Si le statut passe à 'approuve' et que date_publication n'est pas définie
        if self.statut == 'approuve' and not self.date_publication:
            self.date_publication = timezone.now()
        super().save(*args, **kwargs)
    
    # Meta
    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['-date_publication', '-date_soumission']
        constraints = [
            models.CheckConstraint(
                check=models.Q(note__gte=1) & models.Q(note__lte=5),
                name="note_entre_1_et_5"
            )
        ]

    # Propriétés utiles
    @property
    def etoiles(self):
        return '★' * self.note + '☆' * (5 - self.note)
    
    @property
    def est_publie(self):
        return self.statut == 'approuve' and self.date_publication is not None