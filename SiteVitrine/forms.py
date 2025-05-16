from django import forms

class PartnershipForm(forms.Form):
    PARTNERSHIP_CHOICES = [
        ('', 'Sélectionnez un type'),
        ('technology', 'Partenaire Technologique'),
        ('reseller', 'Partenaire Revendeur'),
        ('strategic', 'Partenaire Stratégique'),
        ('other', 'Autre'),
    ]
    
    company_name = forms.CharField(
        max_length=100,
        label="Nom de l'entreprise",
        widget=forms.TextInput(attrs={
            'class': 'mi-form-control',
            'id': 'company-name',
            'required': True
        }),
        help_text="Nom complet de votre entreprise"
    )
    
    contact_person = forms.CharField(
        max_length=100,
        label="Personne de contact",
        widget=forms.TextInput(attrs={
            'class': 'mi-form-control',
            'id': 'contact-person',
            'required': True
        })
    )
    
    company_email = forms.EmailField(
        label="Email professionnel",
        widget=forms.EmailInput(attrs={
            'class': 'mi-form-control',
            'id': 'company-email',
            'required': True
        })
    )
    
    company_phone = forms.CharField(
        max_length=20,
        label="Téléphone",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'mi-form-control',
            'id': 'company-phone',
            'type': 'tel'
        })
    )
    
    partnership_type = forms.ChoiceField(
        label="Type de partenariat",
        choices=PARTNERSHIP_CHOICES,
        widget=forms.Select(attrs={
            'class': 'mi-form-control',
            'id': 'partnership-type',
            'required': True
        })
    )
    
    collaboration_ideas = forms.CharField(
        label="Idées de collaboration",
        widget=forms.Textarea(attrs={
            'class': 'mi-form-control',
            'id': 'collaboration-ideas',
            'rows': 4,
            'required': True
        })
    )
    
    def clean_company_name(self):
        company_name = self.cleaned_data['company_name']
        if len(company_name) < 2:
            raise forms.ValidationError("Le nom de l'entreprise est trop court")
        return company_name
    
    def clean_contact_person(self):
        contact_person = self.cleaned_data['contact_person']
        if len(contact_person.split()) < 2:
            raise forms.ValidationError("Veuillez entrer le nom complet")
        return contact_person



class ContactForm(forms.Form):
    SUJET_CHOICES = [
        ('', 'Sélectionnez un sujet'),
        ('support', 'Support technique'),
        ('devis', 'Demande de devis'),
        ('partenariat', 'Partenariat'),
        ('autre', 'Autre demande'),
    ]
    
    nom = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'mi-form-input',
            'id': 'nom',
            'required': True
        })
    )
    
    prenom = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'mi-form-input',
            'id': 'prenom',
            'required': True
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'mi-form-input',
            'id': 'email',
            'required': True
        })
    )
    
    telephone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'mi-form-input',
            'id': 'telephone',
            'type': 'tel'
        })
    )
    
    sujet = forms.ChoiceField(
        choices=SUJET_CHOICES,
        widget=forms.Select(attrs={
            'class': 'mi-form-select',
            'id': 'sujet',
            'required': True
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'mi-form-textarea',
            'id': 'message',
            'rows': 4,
            'required': True
        })
    )
    
    def clean_email(self):
        email = self.cleaned_data['email']
        # Ajoutez ici des validations personnalisées si nécessaire
        return email

