import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField, TextAreaField
import ctypes
from wtforms.validators import DataRequired, NumberRange
from wtforms.validators import  Length
app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_clé_secrète'  # Clé secrète pour la sécurité des sessions

# Il faudra indiquer le chemin vers le fichier c
# Construct the path relative to the current script
base_path = os.path.dirname(__file__)
so_path = os.path.join(base_path, 'fichierC', 'myfunction.so')
my_lybrary = ctypes.CDLL(so_path)

# Créer une classe de formulaire en utilisant FlaskForm
class MyForm(FlaskForm):
    nom = StringField('Nom')
    prenom = StringField('Prénom')
    age = StringField('Âge')
    sexe = SelectField('Votre sexe', choices=[('option1', 'Homme'), ('option2', 'Femme'), ('option3', 'Autre...')])
    situationPersonnel = SelectField('Votre situation personnel', choices=[
        ('option1', 'En couple'), ('option2', 'Célibataire'), ('option3', 'Marié.e'), 
        ('option4', 'Divorcé.e'), ('option5', 'Veuf/Veuve'), ('option6', 'Autre')
    ])
    ville = StringField('Ville')
    pays = StringField('Pays')
    niveauEtude = SelectField('Votre niveau d’études', choices=[
        ('option1', 'Aucun'), ('option2', 'Secondaire'), ('option3', 'Baccalauréat'),
        ('option4', 'Licence'), ('option5', 'Master'), ('option6', 'Doctorat'), ('option7', 'Autre')
    ])
    problemeSpecifique = TextAreaField('Décrivez un problème spécifique si vous en avez', validators=[Length(max=500)])
    humeur = IntegerField('Comment vous sentez-vous aujourd’hui?', validators=[NumberRange(min=0, max=10)])
    submit = SubmitField('Commencer la discussion')
# Route pour afficher le formulaire et traiter les données envoyées



@app.route('/')
def index():
    return render_template('accueil.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    data={}
    if form.validate_on_submit():
        nom = form.nom.data
        prenom = form.prenom.data
        age = form.age.data
        sexe = form.sexe.data
        situation = form.situationPersonnel.data
        niveauEtude = form.niveauEtude.data
        humeur = form.humeur.data
        pays= form.pays.data
        ville = form.ville.data
        probleme = form.problemeSpecifique.data
        data = {nom, prenom, age, sexe, situation,niveauEtude,humeur,pays, ville, probleme}

        #my_lybrary.my_function(data) # LIGNE POUR LANCER LA FONCTION  
        
        
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

# http://localhost:5000

