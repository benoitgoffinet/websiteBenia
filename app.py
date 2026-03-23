import streamlit as st
import base64
from pathlib import Path

#fonction
    
@st.cache_data(show_spinner=False)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data(show_spinner=False)
def load_assets():
    image_dir = Path(__file__).parent / "images"
    return {
        "presentation": get_base64(image_dir / "presentation.jpg"),
        "solution": get_base64(image_dir / "solution.jpg"),
        "dashboard": get_base64(image_dir / "dashboardanalysegenerale.png"),
        "apropos": get_base64(image_dir / "apropos.jpg"),
        "contact": get_base64(image_dir / "contact.jpg"),
    }

# Encoder les images de fond
assets = load_assets()



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
            background: linear-gradient(180deg, #E7EEF5 0%, #D7E1EA 100%);

        }

        html {
            font-size: 18px;
        }

        @media (min-width: 1600px) {
            html {
                font-size: 20px;
            }
        }
        .content-panel {
            width: min(1500px, 96vw);
            margin-inline: auto;
            background: rgba(248,250,252,0.88);
            border: 1px solid rgba(15,23,42,0.08);
            box-shadow: 0 20px 45px rgba(15,23,42,0.16);
            border-radius: 1.25rem;
            padding: clamp(1rem, 3vw, 2.5rem);
        }

        .cta-link {
            display: inline-block;
            margin-top: 1rem;
            padding: 0.9rem 1.4rem;
            border-radius: 0.75rem;
            background-color: #FACC15;
            color: #0F172A !important;
            text-decoration: none;
            font-size: clamp(1rem, 1.2vw, 1.15rem);
            font-weight: 700;
        }
        .site-footer {
            width: min(1500px, 96vw);
            margin: 0 auto;
            padding: 1.5rem clamp(1rem, 3vw, 2.5rem) 2rem;
            background: linear-gradient(135deg, #E2E8F0 0%, #CBD5E1 100%);
            color: #0F172A;
            border-top: 4px solid #B45309;
            box-shadow: 0 -12px 30px rgba(15,23,42,0.08);
            border-radius: 0 0 1.25rem 1.25rem;
        }

        .site-footer h2 {
            margin: 0 0 0.75rem;
            font-family: 'Times New Roman', Times, serif;
            font-size: clamp(1.4rem, 2.5vw, 2rem);
        }

        .site-footer p {
            margin: 0.35rem 0;
            font-size: clamp(1rem, 1.4vw, 1.1rem);
        }

        .site-footer a {
            color: #92400E !important;
            font-weight: 600;
            text-decoration: none;
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
        min-height: clamp(52px, 7vh, 96px);           
        display: flex;
        align-items: center;
        justify-content: space-around;
        margin-bottom: 0;               /* ❌ aucune marge en dessous */
        padding-bottom: 0;              /* ❌ aucune marge interne */
        gap: clamp(0.2rem, 1vw, 1rem);
    }

    /* Style optionnel des onglets */
    div[data-baseweb="tab"] {
        font-size: clamp(15px, 1.4vw, 22px) !important;
        font-weight: 600 !important;
        line-height: 1.15 !important;
        padding: clamp(6px,0.8vw,12px) clamp(10px,1.3vw,18px) !important;
        min-height: clamp(38px, 4.5vh, 52px) !important;
        white-space: normal !important;
        text-align: center !important;
        color: #0F172A !important;
        background-color: rgba(248,250,252,0.92) !important;
        border-radius: 0.85rem !important;
        border: 1px solid rgba(15,23,42,0.10) !important;
    }

    button[role="tab"][aria-selected="true"] {
        background-color: #FACC15 !important;
        color: #0F172A !important;
        border-color: #B45309 !important;
        box-shadow: 0 10px 24px rgba(180, 83, 9, 0.18);
    }

    @media (max-width: 900px) {
        div[data-baseweb="tab"] {
            font-size: clamp(12px, 3.2vw, 15px) !important;
            padding: clamp(6px, 1.8vw, 10px) clamp(8px, 2vw, 12px) !important;
        }
    }

    @media (min-width: 1600px) {
        div[data-baseweb="tab"] {
            font-size: clamp(18px, 1.2vw, 24px) !important;
        }
    }
    
    /* Supprime les espaces résiduels éventuels */
    [data-testid="stVerticalBlock"] {
        margin-bottom: 0;
        padding-bottom: 0;
    }

    </style>
""", unsafe_allow_html=True)

tabs = st.tabs(["Présentation", "Solution / Dashboard interactif", "Accéder au Dashboard", "A propos", "Questions/réponses", "Contact"])
# --- Onglet 1 : Présentation ---
with tabs[0]:
   
   


# Affichage de l'image en background avec overlay texte
   st.markdown(
    f"""
    <div style="
        width: 100%;
        font-size: 14px;
        min-height: 92vh;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{assets['presentation']}');
        background-size: cover;
        background-position: 50% 20%;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
    ">
        <div class="content-panel">
             <h1 style="color:#0F172A; text-align:center; font-family: 'Times New Roman', Times, serif; font-size: clamp(0.5rem, 7vw + 1rem, 5rem);">{'BenIA.solutions<br> Data Consultant spécialisé dans les structures culturelles'}</h1>
         <p style="color:#0F172A; text-align:center; font-family: 'Times New Roman', Times, serif; font-size: clamp(0.3rem, 4vw + 1rem, 3rem);">Anticipez le remplissage de vos spectacles et pilotez votre programmation grâce à l’analyse de vos propres données.</p>
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
        width: 100%;
        font-size: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{assets['solution']}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: rgba(248,250,252,0.86);
            padding: 4rem;
            box-sizing: border-box;
            color: #0F172A;
        ">
            <!-- Offre -->
            <h1 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">L'Offre de BenIA.solutions</h1>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Problème</h2>
            <p style="font-size:18px; line-height:1.6;">
De nombreuses <strong>structures culturelles</strong> disposent de données historiques, mais celles-ci sont rarement utilisées pour piloter l’organisation des événements.
Il devient alors difficile d’<strong>anticiper l’affluence</strong> des spectacles et d’optimiser le remplissage des représentations.

</p>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Solution</h2>
            <p style="font-size:18px; line-height:1.6;">Pour répondre à cette problématique, BenIA.solutions propose d’exploiter et d’analyser vos données historiques de fréquentation afin d’identifier les tendances observées au fil du temps.<br>
BenIA.solutions développe ensuite un dashboard interactif permettant d’analyser les données de fréquentation, d’anticiper l’affluence des spectacles et d’accompagner l’organisation des représentations.
</p>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Bénéfices</h2>
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
            </ul>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Avant l’analyse des données</h2>
            <p style="font-size:18px; line-height:1.6;">Les informations utiles à la prise de décision sont souvent <strong>dispersées, peu accessibles ou difficiles à exploiter.</strong><br>
            Les décisions d’organisation et de programmation reposent alors principalement <strong>sur l’expérience ou l’intuition.</strong>
            </p>
             <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Après l’analyse des données</h2>
             <p style="font-size:18px; line-height:1.6;">BenIA.solutions met à disposition un <strong>dashboard interactif</strong> permettant de centraliser et d’exploiter les données de fréquentation.<br>
            Les équipes disposent alors d’indicateurs clairs pour <strong>anticiper la fréquentation, identifier les tendances et orienter plus facilement les décisions d’organisation et de programmation.</strong>
            </p>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Onglet 3 : dashboard
with tabs[2]: 
    st.markdown(
    f"""
    <div style="
        width: 100%;
        min-height: 92vh;
        font-size: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{assets['dashboard']}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; 
            background-color: rgba(248,250,252,0.86);
            padding: 4rem;
            box-sizing: border-box;
            color: #0F172A;
        ">
            <!-- Offre -->
            <h1 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Démonstration du dashboard</h1>
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
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Accéder à la démonstration interactive</h2>
            <p>Les données utilisées dans cette démonstration sont fictives et présentées uniquement à des fins d’illustration.<br>
            Le dashboard peut être adapté aux données propres à chaque structure culturelle et enrichi avec différentes variables selon les besoins d’analyse.</p>
            <a class="cta-link" href="https://web-production-269e5.up.railway.app/" target="_blank" rel="noopener noreferrer">🚀 Tester la démo interactive</a>
            </div>
    </div>
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
        background-image: url('data:image/png;base64,{assets['apropos']}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; 
            background-color: rgba(248,250,252,0.86);
            padding: 4rem;
            box-sizing: border-box;
            color: #0F172A;
        ">
            <!-- Offre -->
            <h1 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">BenIA.solutions</h1>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Le projet</h2>
            <p style="font-size:18px; line-height:1.6;">
BenIA.solutions est un projet dédié à l’analyse et à la valorisation des données dans le secteur culturel.
L’objectif est d’aider les <strong>structures culturelles</strong> à mieux comprendre la fréquentation de leurs événements et à piloter leur programmation grâce à l’analyse de leurs données.
</p>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Le fondateur</h2>
            <p style="font-size:18px; line-height:1.6;">
Je suis Benoît Goffinet, fondateur de BenIA.solutions et consultant en analyse de données.
Je mets mes compétences en data, en intelligence artificielle et en visualisation de données au service des <strong>structures culturelles</strong> afin de transformer leurs données en outils d’aide à la décision et d’anticiper la fréquentation des spectacles.<br>
Mon travail repose sur une combinaison de rigueur analytique, de créativité et de pédagogie, afin de proposer des outils clairs, utiles et adaptés aux besoins des équipes. Passionné par les événements culturels et le spectacle vivant, je m’attache également à comprendre les enjeux spécifiques des structures que j’accompagne.
</p>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Formation</h2>
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
<h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Mon approche</h2>
            <p style="font-size:18px; line-height:1.6;">
Mon approche consiste à transformer les données existantes en outils d’aide à la décision accessibles et interactifs.<br>
Grâce à l’analyse des données, à la visualisation et à la modélisation, il devient possible de mieux comprendre les comportements de fréquentation et d’accompagner les équipes dans leurs décisions.
</p>
<h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Mes compétences</h2>
            <p style="font-size:18px; line-height:1.6;">
Au-delà des compétences techniques, mon travail repose également sur plusieurs qualités essentielles :
</p>    
 <ul style="font-size:18px; line-height:1.6;">
            <li>capacité d’analyse pour comprendre les problématiques et les données</li>
            <li>pédagogie afin de rendre les analyses accessibles aux équipes</li>
            <li>écoute des besoins pour adapter les outils aux réalités des <strong>structures culturelles</strong></li>
            <li>compréhension des besoins des <strong>structures culturelles</strong></li>
            </ul>
<h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Pourquoi ce projet</h2>
            <p style="font-size:18px; line-height:1.6;">
Le secteur culturel produit aujourd’hui de nombreuses données (billetterie, fréquentation, programmation), mais ces informations sont rarement exploitées de manière approfondie.<br>
BenIA.solutions vise à valoriser ces données et à les rendre utiles pour le pilotage des activités culturelles.
</p>
           <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Traitement des données</h2>
            <p style="font-size:18px; line-height:1.6;">
Les données utilisées dans le cadre des analyses restent la propriété de la structure culturelle.<br>
Les informations fournies sont utilisées uniquement dans le but de réaliser les analyses nécessaires au fonctionnement du dashboard et à l’accompagnement proposé.<br>
Aucune donnée n’est transmise à des tiers.<br>
Lorsque cela est nécessaire, les données peuvent être anonymisées ou agrégées afin de garantir la confidentialité des informations.
</p>    
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Discutons de votre projet </h2>
            <p style="font-size:18px; line-height:1.6;">Vous souhaitez explorer vos <strong>données de fréquentation</strong> et mieux <strong>anticiper l’affluence</strong> de vos spectacles ?
N’hésitez pas à me contacter pour échanger sur votre projet.</p>
            <p style="font-size:18px; line-height:1.6;">Email : benoit@benia.solutions</p>
            <p style="font-size:18px; line-height:1.6;">Téléphone : 07 67 65 92 51</p>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --- Onglet 5 : Questions/réponses
with tabs[4]: 
    st.markdown(
    f"""
    <div style="
        width: 100%;
        font-size: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{assets['solution']}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: rgba(248,250,252,0.86);
            padding: 4rem;
            box-sizing: border-box;
            color: #0F172A;
        ">
            <!-- questions-->
            <h1 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Questions/Réponses</h1>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">💼 Quels services proposes-tu ?</h2>
            <p style="font-size:18px; line-height:1.6;">
Je conçois des dashboards interactifs permettant de visualiser et piloter vos données facilement.<br>
Mon offre comprend :<p/>
<ul style="font-size:18px; line-height:1.6;">
            <li> une analyse complète de vos données (tendances, variables clés, insights)</li>
            <li> la création d’un dashboard sur mesure</li>
            <li> un accompagnement à la prise en main</li>
             </ul>
             <p style="font-size:18px; line-height:1.6;">
L’hébergement et la maintenance sont inclus pendant 6 mois.<br>
Au-delà, un abonnement permet de continuer avec des mises à jour régulières des données.<p/>
            <p style="font-size:18px; line-height:1.6;">
Le paiement se fait en deux étapes :<p/>
            <ul style="font-size:18px; line-height:1.6;">
            <li><strong>50% à l’acceptation du devis (acompte)</strong></li>
            <li><strong>50% à la livraison du dashboard</strong></li>
             <ul/>
            <p style="font-size:18px; line-height:1.6;">
Cela permet de sécuriser le démarrage du projet et de garantir un engagement des deux côtés.<br>
Mes prestations débutent à partir de 2500 €, en fonction de votre projet.<p/>
<h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">📊 Qu’est-ce que j’apporte à votre entreprise ?</h2>
            <p style="font-size:18px; line-height:1.6;">
Je ne me contente pas de créer des dashboards : je vous aide à comprendre vos données, anticiper les tendances et prendre de meilleures décisions.<br>
Mon approche est orientée résultats :<p/>
<ul style="font-size:18px; line-height:1.6;">
            <li>analyse approfondie des données</li>
            <li>dashboards clairs et adaptés à vos enjeux métier</li>
            <li>modèles de prédiction pour anticiper l'affluence de vos représentations</li>
            <li>interfaces simples vous permettant de réaliser vos propres analyses et projections</li>
            <li>accompagnement pour vous rendre autonome</li>
             </ul>
             <p style="font-size:18px; line-height:1.6;">
L’objectif n’est pas seulement de livrer un outil, mais de vous apporter une vraie valeur business durable.<br>
👉 Le plus simple est d’échanger rapidement pour vous donner une estimation précise selon votre besoin.<p/>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Onglet 6 : Contact ---
with tabs[5]:
    st.markdown(
    f"""
    <div style="
        width: 100%;
        min-height: 92vh;
        font-size: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{assets['contact']}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <div style="
            position: absolute;
            top: 0; left: 0;
            width: 100%; 
            background-color: rgba(248,250,252,0.78);
            padding: 40px;
            box-sizing: border-box;
            color: #0F172A;
        ">
            <h1 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Contact</h1>
            <p style="font-size:18px; line-height:1.6;">Vous pouvez me contacter via :</p>          
            <p style="font-size:18px; line-height:1.6;">Email : benoit@benia.solutions</p>
            <p style="font-size:18px; line-height:1.6;">Téléphone : 07 67 65 92 51</p>
            <p style="font-size:18px; line-height:1.6;"><a href="https://www.linkedin.com/in/benoit-goffinet-devweb/" target="_blank" style="color:#92400E; text-decoration:none; font-weight:600;">LinkedIn</a></p>
            <p style="font-size:18px; line-height:1.6;"><a href="https://github.com/benoitgoffinet" target="_blank" style="color:#92400E; text-decoration:none; font-weight:600;">GitHub</a></p>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)
    
st.markdown("""
   
<footer class="site-footer">
    <p>
        © 2026 Goffinet — 
        <a href="/mentions-legales">Mentions légales</a> | 
        <a href="/Contact">Contact</a>
    </p>
</footer>
""", unsafe_allow_html=True)
