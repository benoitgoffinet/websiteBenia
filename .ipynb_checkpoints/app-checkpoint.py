import streamlit as st
from PIL import Image
import base64

#fonction
def display_image(image_path, height=300, caption=None):
    """
    Affiche une image dans Streamlit avec une hauteur fixe.
    La largeur est ajustée automatiquement pour garder le ratio.
    """
    img = Image.open(image_path)
    hpercent = height / float(img.size[1])
    wsize = int(float(img.size[0]) * hpercent)
    img_resized = img.resize((wsize, height))
    
    st.image(img_resized, caption=caption)
    

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encoder l'image de fond
presentation = get_base64("images/presentation.jpg")
solution = get_base64("images/solution.jpg")
dashboard = get_base64("images/dashboardanalysegenerale.png")
apropos = get_base64("images/apropos.jpg")
contact = get_base64("images/contact.jpg") 
benoit = get_base64("images/benoit.png")



# Configuration de la page
st.set_page_config(
    page_title="BenIA.solutions",
    layout="wide",
    page_icon=":computer:"
)
st.markdown(
    """
    <style>
        /* cache la barre du haut (deploy + menu) */
[data-testid="stToolbar"] {
    display: none;
}

/* cache le bouton menu */
#MainMenu {
    visibility: hidden;
}

/* cache le footer Streamlit */
footer {
    visibility: hidden;
}

/* enlève la marge du haut */
header {
    visibility: hidden;
}

        .block-container {
            padding-top: 0.01rem;
            padding-bottom: 0.01rem;
            padding-left: 0.1rem;
            padding-right: 0.1rem;
            background-color: #B8C1CC;

        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    /* Masque tout ce qui est SVG dans les headers */
    div.element-container h1 svg,
    div.element-container h2 svg,
    div.element-container h3 svg,
    div.element-container h4 svg,
    div.element-container h5 svg,
    div.element-container h6 svg {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Onglets ---
st.markdown("""
    <style>
    /* Supprimer les marges internes du conteneur principal */
    .block-container {
        padding-top: 0;
        padding-bottom: 0;
    }
    
    /* Supprime les marges automatiques autour de la barre d'onglets */
    div[data-baseweb="tab-list"] {
        height: 5vh;                  
        display: flex;
        align-items: center;
        justify-content: space-around;
        margin-bottom: 0;               /* ❌ aucune marge en dessous */
        padding-bottom: 0;              /* ❌ aucune marge interne */
    }

    /* Style optionnel des onglets */
    div[data-baseweb="tab"] {
        font-size: clamp(12px, 1.6vw, 26px) !important;
        font-weight: 600 !important;
        padding: clamp(6px,1vw,16px) clamp(10px,2vw,30px) !important;
    }

    /* Supprime les espaces résiduels éventuels */
    [data-testid="stVerticalBlock"] {
        margin-bottom: 0;
        padding-bottom: 0;
    }

    </style>
""", unsafe_allow_html=True)

tabs = st.tabs(["Présentation", "Solution / Dashboard interactif", "Accéder au Dashboard", "A propos", "Contact"])
# --- Onglet 1 : Présentation ---
with tabs[0]:
   
   


# Affichage de l'image en background avec overlay texte
   st.markdown(
    f"""
    <div style="
        width: 100%;
        fontsize: 14px;
        min-height: 92vh;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{presentation}');
        background-size: cover;
        background-position: 50% 20%;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
    ">
        <div style="
            background-color: rgba(0,0,0,0.8);
            border-radius: 2rem;
        ">
            <h1 style="color:#B8C1CC; text-align:center; font-family: 'Times New Roman', Times, serif; font-size: clamp(0.5rem, 7vw + 1rem, 5rem);">{'BenIA.solutions<br> Data Consultant spécialisé dans les structures culturelles'}</h1>
         <p style="color:#B8C1CC; text-align:center; font-family: 'Times New Roman', Times, serif; font-size: clamp(0.3rem, 4vw + 1rem, 3rem);">Anticipez le remplissage de vos spectacles et pilotez votre programmation grâce à l’analyse de vos propres données.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


    
# --- Onglet 2 : Offre
with tabs[1]: 
    st.markdown(
    f"""
    <div style="
        width: 100%;eight: 100%;
        fontsize: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{solution}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.8);
            padding: 4rem;
            box-sizing: border-box;
            color: #B8C1CC;
        ">
            <!-- Offre -->
            <h1 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">L'Offre de BenIA.solutions</h1>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Problème</h2>
            <p style="font-size:18px; line-height:1.6;">
De nombreuses <strong>structures culturelles</strong> disposent de données historiques, mais celles-ci sont rarement utilisées pour piloter l’organisation des événements.
Il devient alors difficile d’<strong>anticiper l’affluence</strong> des spectacles et d’optimiser le remplissage des représentations.

</p>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Solution</h2>
            <p style="font-size:18px; line-height:1.6;">Pour répondre à cette problématique, BenIA.solutions propose d’exploiter et d’analyser vos données historiques de fréquentation afin d’identifier les tendances observées au fil du temps.<br>
Grâce à un <strong>dashboard interactif</strong>, vous pourrez visualiser et <strong>anticiper l’affluence</strong> des spectacles et mieux préparer l’organisation de vos représentations.<p/>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Bénéfices</h2>
            <ul style="font-size:18px; line-height:1.6;">
            <li><strong>✔ Anticipation de la fréquentation</strong> <br>
            L’analyse des données permet d’estimer l’affluence probable d’un spectacle et d’anticiper les périodes ou représentations susceptibles d’attirer le plus de public.<br><br>
            </li>
            <li><strong>✔ Aide à la prise de décision pour la programmation</strong><br>
            L’analyse des données historiques permet d’identifier les facteurs qui influencent la fréquentation des spectacles et d’éclairer les choix de programmation.<br><br>
</li>
            <li><strong>✔ Optimisation du remplissage des salles</strong><br>
            Même une amélioration modérée du taux de remplissage peut avoir un impact significatif.<br> 
Par exemple, pour une salle de 300 places avec un billet moyen de 20 €, une augmentation de 10 % du remplissage peut représenter environ 600 € de recettes supplémentaires par représentation.<br>
Sur plusieurs représentations, cela peut représenter un gain significatif sur une saison.<br><br>
            </li>
            <li><strong>✔ Meilleure organisation des représentations</strong><br>
            Disposer d’une estimation de l’affluence permet d’adapter l’organisation des spectacles, notamment la gestion des équipes, la communication ou la logistique des événements.<br><br></li>
            <li><strong>✔ Une meilleure compréhension de l’impact des décisions d’organisation</strong><br>
            L’analyse des données permet d’identifier les choix qui favorisent la fréquentation et d’ajuster progressivement l’organisation et la programmation des spectacles.</li>
            <ul/>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Avant l’analyse des données</h2>
               <p style="font-size:18px; line-height:1.6;">Les décisions d’organisation et de programmation reposent principalement sur l’expérience, l’intuition ou des informations dispersées.<p/>
               <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Après l’analyse des données</h2>
               <p style="font-size:18px; line-height:1.6;">Les équipes disposent d’indicateurs clairs permettant d’anticiper la fréquentation, d’identifier les tendances et d’orienter plus facilement les décisions.<p/>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Onglet 2 : dash
with tabs[2]: 
    st.markdown(
    f"""
    <div style="
        width: 100%;
        min-height: 92vh;
        fontsize: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{dashboard}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; 
            background-color: rgba(0,0,0,0.8);
            padding: 4rem;
            box-sizing: border-box;
            color: #B8C1CC;
        ">
            <!-- Offre -->
            <h1 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Démonstration du dashboard</h1>
            <p style="font-size:18px; line-height:1.6;">
Cette démonstration permet d'explorer un exemple de dashboard interactif
    dédié à l'analyse de la fréquentation des événements culturels.<br>
Le dashboard permet notamment de :
</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>analyser les tendances de fréquentation</li>
            <li>explorer les données selon différentes variables</li>
            <li>utiliser un prédicteur pour estimer l'affluence</li>
            </ul>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Accéder à la démonstration interactive</h2>
            <p>Les données utilisées dans cette démonstration sont fictives et présentées uniquement à des fins d’illustration.<br>
            Le dashboard peut être adapté aux données propres à chaque structure culturelle et enrichi avec différentes variables selon les besoins d’analyse.</p>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown(
    """
    <a href="https://web-production-269e5.up.railway.app/" target="_blank"
style="
position:fixed;
bottom:0;
left:0;
width:100%;
padding:24px;
background-color:#FACC15;
color:black;
text-decoration:none;
font-size:24px;
font-weight:700;
text-align:center;
z-index:999;
">
🚀 Tester la démo interactive
</a>
    """,
    unsafe_allow_html=True
)

# --- Onglet 3 : A propos
with tabs[3]: 
    st.markdown(
    f"""
    <div style="
        width: 100%;
        font-size: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{apropos}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; 
            background-color: rgba(0,0,0,0.8);
            padding: 4rem;
            box-sizing: border-box;
            color: #B8C1CC;
        ">
            <!-- Offre -->
            <h1 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">BenIA.solutions</h1>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Le projet</h2>
            <p style="font-size:18px; line-height:1.6;">
BenIA.solutions est un projet dédié à l’analyse et à la valorisation des données dans le secteur culturel.
L’objectif est d’aider les <strong>structures culturelles</strong> à mieux comprendre la fréquentation de leurs événements et à piloter leur programmation grâce à l’analyse de leurs données.
</p>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Le fondateur</h2>
            <p style="font-size:18px; line-height:1.6;">
Je suis Benoît Goffinet, fondateur de BenIA.solutions et consultant en analyse de données.
Je mets mes compétences en data, en intelligence artificielle et en visualisation de données au service des <strong>structures culturelles</strong> afin de transformer leurs données en outils d’aide à la décision et d’anticiper la fréquentation des spectacles.<br>
Mon travail repose sur une combinaison de rigueur analytique, de créativité et de pédagogie, afin de proposer des outils clairs, utiles et adaptés aux besoins des équipes. Passionné par les événements culturels et le spectacle vivant, je m’attache également à comprendre les enjeux spécifiques des structures que j’accompagne.
</p>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Formation</h2>
            <p style="font-size:18px; line-height:1.6;">
Je suis diplômé d’une formation diplômante d’ingénieur en Machine Learning, centrée sur l’analyse de données et les techniques de modélisation.<br>
Cette formation m’a permis d’acquérir des compétences en :
</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>analyse de données</li>
            <li>visualisation de données</li>
            <li>modélisation statistique</li>
            <li>machine learning</li>
            </ul>
            <p>
Ces compétences sont aujourd’hui mobilisées dans le développement de BenIA.solutions.
</p>
<h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Mon approche</h2>
            <p style="font-size:18px; line-height:1.6;">
Mon approche consiste à transformer les données existantes en outils d’aide à la décision accessibles et interactifs.<br>
Grâce à l’analyse des données, à la visualisation et à la modélisation, il devient possible de mieux comprendre les comportements de fréquentation et d’accompagner les équipes dans leurs décisions.
</p>
<h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Mes compétences</h2>
            <p style="font-size:18px; line-height:1.6;">
Au-delà des compétences techniques, mon travail repose également sur plusieurs qualités essentielles :
</p>    
 <ul style="font-size:18px; line-height:1.6;">
            <li>capacité d’analyse pour comprendre les problématiques et les données</li>
            <li>pédagogie afin de rendre les analyses accessibles aux équipes</li>
            <li>écoute des besoins pour adapter les outils aux réalités des <strong>structures culturelles</strong></li>
            <li>compréhension des besoins des <strong>structures culturelles</strong></li>
            </ul>
<h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Pourquoi ce projet</h2>
            <p style="font-size:18px; line-height:1.6;">
Le secteur culturel produit aujourd’hui de nombreuses données (billetterie, fréquentation, programmation), mais ces informations sont rarement exploitées de manière approfondie.<br>
BenIA.solutions vise à valoriser ces données et à les rendre utiles pour le pilotage des activités culturelles.
</p>
           <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Traitement des données</h2>
            <p style="font-size:18px; line-height:1.6;">
Les données utilisées dans le cadre des analyses restent la propriété de la structure culturelle.<br>
Les informations fournies sont utilisées uniquement dans le but de réaliser les analyses nécessaires au fonctionnement du dashboard et à l’accompagnement proposé.<br>
Aucune donnée n’est transmise à des tiers.<br>
Lorsque cela est nécessaire, les données peuvent être anonymisées ou agrégées afin de garantir la confidentialité des informations.
</p>    
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Discutons de votre projet </h2>
            <p style="font-size:18px; line-height:1.6;">Vous souhaitez explorer vos <strong>données de fréquentation</strong> et mieux <strong>anticiper l’affluence</strong> de vos spectacles ?
N’hésitez pas à me contacter pour échanger sur votre projet.</p>
            <p style="font-size:18px; line-height:1.6;">Email : benoit@benia.solutions</p>
            <p style="font-size:18px; line-height:1.6;">Téléphone : 06 08 90 02 85</p>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)
  

# --- Onglet 5 : Contact ---
with tabs[4]:
    st.markdown(
    f"""
    <div style="
        width: 100%;
        min-height: 92vh;
        fontsize: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{contact}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <div style="
            position: absolute;
            top: 0; left: 0;
            width: 100%; 
            background-color: rgba(0,0,0,0.4);
            padding: 40px;
            box-sizing: border-box;
            color: #B8C1CC;
        ">
            <h1 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Contact</h1>
            <p style="font-size:18px; line-height:1.6;">Vous pouvez me contacter via :</p>          
            <p style="font-size:18px; line-height:1.6;">Email : benoit@benia.solutions</p>
            <p style="font-size:18px; line-height:1.6;">Téléphone : 0608900285</p>
            <p style="font-size:18px; line-height:1.6;"><a href="https://www.linkedin.com/in/benoit-goffinet-devweb/" target="_blank" style="color:#B8C1CC; text-decoration:none;">LinkedIn</a></p>
            <p style="font-size:18px; line-height:1.6;"><a href="https://github.com/benoitgoffinet" target="_blank" style="color:#B8C1CC; text-decoration:none;">GitHub</a></p>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)
    
    