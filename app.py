import streamlit as st
import base64
from pathlib import Path
from datetime import datetime

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
CURRENT_YEAR = datetime.now().year


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

/* cache uniquement le footer natif de Streamlit */
footer[data-testid="stFooter"] {
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

        .main-nav-shell {
            position: sticky;
            top: 0.5rem;
            z-index: 100;
            width: min(1500px, 96vw);
            margin: 0.75rem auto 0.4rem;
            padding: 0.55rem;
            border-radius: 1.2rem;
            background: rgba(226,232,240,0.82);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(15,23,42,0.10);
            box-shadow: 0 14px 32px rgba(15,23,42,0.10);
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
    
    div[data-testid="stRadio"] > div {
        background: transparent;
    }

    div[role="radiogroup"] {
        display: grid !important;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 0.65rem;
        align-items: stretch;
        width: 100%;
    }

    div[role="radiogroup"] label {
        margin: 0 !important;
        min-width: 0;
        width: 100%;
    }

    div[role="radiogroup"] label > div:first-child {
        display: none;
    }

    div[role="radiogroup"] label p {
        margin: 0;
    }

    div[role="radiogroup"] label[data-baseweb="radio"] {
        background: rgba(248,250,252,0.92);
        border: 1px solid rgba(15,23,42,0.10);
        border-radius: 999px;
        padding: 0.95rem 1.1rem;
        min-height: 68px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease, background-color 0.18s ease;
        box-shadow: 0 8px 20px rgba(15,23,42,0.06);
        cursor: pointer;
    }
    
    div[role="radiogroup"] label[data-baseweb="radio"]:hover {
        transform: translateY(-1px);
        border-color: rgba(180,83,9,0.45);
        box-shadow: 0 12px 24px rgba(15,23,42,0.10);
    }

    div[role="radiogroup"] label[data-baseweb="radio"][aria-checked="true"] {
        background: linear-gradient(135deg, rgba(250,204,21,0.96) 0%, rgba(245,158,11,0.96) 100%);
        border-color: #B45309;
        box-shadow: 0 14px 28px rgba(180, 83, 9, 0.18);
    }

    div[role="radiogroup"] label[data-baseweb="radio"] span {
        font-size: clamp(0.96rem, 1.15vw, 1.08rem) !important;
        font-weight: 700 !important;
        color: #0F172A !important;
        line-height: 1.25 !important;
    }

    .mobile-menu-toggle {
        display: none;
    }
    
    @media (max-width: 1100px) {
        div[role="radiogroup"] {
            grid-template-columns: repeat(3, minmax(0, 1fr));
        }
    }
    @media (max-width: 900px) {
        .main-nav-shell {
            top: 0.25rem;
            padding: 0.5rem;
        }

        div[role="radiogroup"] {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.45rem;
        }


        div[role="radiogroup"] label[data-baseweb="radio"] {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            min-height: 58px;
            padding: 0.75rem 0.8rem;
            border-radius: 1rem;
        }
    }
    @media (max-width: 640px) {
         .main-nav-shell {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.55rem;
        }

        .mobile-menu-toggle {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            border-radius: 999px;
            border: 1px solid rgba(15,23,42,0.14);
            background: rgba(248,250,252,0.95);
            box-shadow: 0 8px 18px rgba(15,23,42,0.12);
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            padding: 0;
        }

        .mobile-menu-toggle:hover {
            transform: translateY(-1px);
            box-shadow: 0 10px 22px rgba(15,23,42,0.18);
        }

        .mobile-menu-toggle:focus-visible {
            outline: 2px solid #B45309;
            outline-offset: 2px;
        }

        .mobile-menu-dots {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }

        .mobile-menu-dots span {
            width: 6px;
            height: 6px;
            border-radius: 999px;
            background-color: #0F172A;
            display: inline-block;
        }
        div[role="radiogroup"] {
            display: none !important;
            grid-template-columns: 1fr;
            width: min(92vw, 360px);
        }

        div[role="radiogroup"].mobile-nav-open {
            display: grid !important;
        }

        div[role="radiogroup"].mobile-nav-open label[data-baseweb="radio"] {
            max-width: 360px;
            margin-inline: auto !important;
        }
    }
    
    /* Supprime les espaces résiduels éventuels */
    [data-testid="stVerticalBlock"] {
        margin-bottom: 0;
        padding-bottom: 0;
    }

    </style>
""", unsafe_allow_html=True)

query_params = st.query_params
requested_section = query_params.get("section", "presentation")
show_legal_notice = requested_section == "mentions-legales"

section_options = [
    ("Présentation", "presentation"),
    ("Solution / Dashboard interactif", "solution"),
    ("Accéder au Dashboard", "dashboard"),
    ("A propos", "apropos"),
    ("Questions/réponses", "faq"),
    ("Contact", "contact"),
]


        
label_by_key = {key: label for label, key in section_options}
section_keys = [key for _, key in section_options]

def sync_navigation_query_params():
    st.query_params["section"] = st.session_state.selected_section
    

if show_legal_notice:
    selected_section = "mentions-legales"
    st.query_params["section"] = "mentions-legales"
else:
    default_section = requested_section if requested_section in section_keys else "presentation"

    if "selected_section" not in st.session_state or st.session_state.selected_section not in section_keys:
        st.session_state.selected_section = default_section
        sync_navigation_query_params()

    selected_index = section_keys.index(st.session_state.selected_section)
    st.markdown(
        """
        <div class="main-nav-shell" id="main-nav-shell">
            <button type="button" class="mobile-menu-toggle" id="mobile-menu-toggle" aria-expanded="false" aria-label="Ouvrir le menu de navigation">
                <span class="mobile-menu-dots" aria-hidden="true">
                    <span></span><span></span><span></span>
                </span>
            </button>
        """,
        unsafe_allow_html=True,
    )
    
    selected_section = st.radio(
        "Navigation",
        section_keys,
        index=selected_index,
        format_func=lambda key: label_by_key[key],
        horizontal=True,
        label_visibility="collapsed",
        key="selected_section",
        on_change=sync_navigation_query_params,
    )
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <script>
            (() => {
                const navShell = window.parent.document.getElementById("main-nav-shell");
                const toggleButton = window.parent.document.getElementById("mobile-menu-toggle");
                const radioGroup = window.parent.document.querySelector('div[role="radiogroup"]');
                if (!navShell || !toggleButton || !radioGroup || toggleButton.dataset.bound === "true") return;

                toggleButton.dataset.bound = "true";

                const updateExpandedState = () => {
                    const isOpen = radioGroup.classList.contains("mobile-nav-open");
                    toggleButton.setAttribute("aria-expanded", isOpen ? "true" : "false");
                };

                toggleButton.addEventListener("click", () => {
                    radioGroup.classList.toggle("mobile-nav-open");
                    updateExpandedState();
                });

                const closeMenuAfterSelection = (event) => {
                    const radioLabel = event.target.closest('label[data-baseweb="radio"]');
                    if (!radioLabel || window.parent.innerWidth > 640) return;
                    radioGroup.classList.remove("mobile-nav-open");
                    updateExpandedState();
                };

                navShell.addEventListener("click", closeMenuAfterSelection);

                window.parent.addEventListener("resize", () => {
                    if (window.parent.innerWidth > 640) {
                        radioGroup.addEventListener("click", closeMenuAfterSelection);
                        updateExpandedState();
                    }
                });

                updateExpandedState();
            })();
        </script>
        """,
        unsafe_allow_html=True,
    )
    sync_navigation_query_params()
    



# --- Onglet 1 : Présentation ---
if selected_section == "presentation":   
   
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

if selected_section == "solution": 
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
             <a href="?section=dashboard" class="cta-link">Voir le Dashboard</a>
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
            <a href="?section=contact" class="cta-link">Prendre rendez vous</a>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Onglet 3 : dashboard

if selected_section == "dashboard": 
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
    

# --- Onglet 4 : A propos

if selected_section == "apropos": 
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
           <a href="?section=solution" class="cta-link">Voir l'offre</a>
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
            <a href="?section=contact" class="cta-link">Prendre contact</a>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --- Onglet 5 : Questions/réponses

if selected_section == "faq": 
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
Mon offre comprend :</p>
<ul style="font-size:18px; line-height:1.6;">
            <li> une analyse complète de vos données (tendances, variables clés, insights)</li>
            <li> la création d’un dashboard sur mesure</li>
            <li> un accompagnement à la prise en main</li>
             </ul>
             <p style="font-size:18px; line-height:1.6;">
L’hébergement et la maintenance sont inclus pendant 6 mois.
            <p style="font-size:18px; line-height:1.6;">
Le paiement se fait en deux étapes :</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li><strong>50% à l’acceptation du devis (acompte)</strong></li>
            <li><strong>50% à la livraison du dashboard</strong></li>
             </ul>
            <p style="font-size:18px; line-height:1.6;">
Cela permet de sécuriser le démarrage du projet et de garantir un engagement des deux côtés.<br>
Mes prestations débutent à partir de 2500 €, en fonction de votre projet.</p>
<h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">📊 Qu’est-ce que j’apporte à votre entreprise ?</h2>
            <p style="font-size:18px; line-height:1.6;">
Je ne me contente pas de créer des dashboards : je vous aide à comprendre vos données, anticiper les tendances et prendre de meilleures décisions.<br>
L’objectif n’est pas seulement de livrer un outil, mais de vous apporter une vraie valeur business durable.<br>
 <a href="?section=dashboard" class="cta-link">Voir le dashboard</a><br>
 <br>
👉 Le plus simple est d’échanger rapidement pour vous donner une estimation précise selon votre besoin.</p>
<a href="?section=contact" class="cta-link">Prendre contact</a>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Onglet 6 : Contact ---

if selected_section == "contact":
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

if selected_section == "mentions-legales":
    st.markdown(
    """
    <div style="
        width: 100%;
        min-height: 92vh;
        font-size: 16px;
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(180deg, rgba(226,232,240,0.92) 0%, rgba(248,250,252,0.98) 100%);
        position: relative;
    ">
        <div style="
            width: min(1100px, 96vw);
            margin: 0 auto;
            background-color: rgba(248,250,252,0.94);
            padding: 2.5rem;
            box-sizing: border-box;
            color: #0F172A;
            border-radius: 1.25rem;
            box-shadow: 0 20px 45px rgba(15,23,42,0.12);
        ">
            <h1 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Mentions légales</h1>
            <p style="font-size:18px; line-height:1.7;">Les informations ci-dessous identifient l'éditeur du site BenIA.solutions et l'activité déclarée de l'auto-entreprise.</p>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Identité</h2>
            <ul style="font-size:18px; line-height:1.7;">
                <li><strong>Nom d'usage :</strong> GOFFINET</li>
                <li><strong>Prénom :</strong> Benoît Thomas</li>
                <li><strong>SIREN :</strong> 833722465</li>
                <li><strong>SIRET :</strong> 83372246500030</li>
                <li><strong>Compte auto-entrepreneur :</strong> 917000001265698595</li>
            </ul>
            <h2 style="color:#0F172A; font-family: 'Times New Roman', Times, serif;">Statut de l'activité</h2>
            <ul style="font-size:18px; line-height:1.7;">
                <li><strong>État du compte :</strong> Actif depuis le 01/03/2026</li>
                <li><strong>Code NAF :</strong> 6311Z — Traitement de données, hébergement et activités connexes</li>
                <li><strong>Date d'immatriculation :</strong> 01/03/2026</li>
            </ul>
            <p style="font-size:18px; line-height:1.7;">
                <strong>Adresse professionnelle :</strong><br>
                238 RUE ABEL GANCE<br>
                34070 MONTPELLIER
            </p>
            <p style="font-size:18px; line-height:1.7;">Pour toute demande relative au site, vous pouvez utiliser l'onglet Contact.</p>
            <a href="?section=contact" class="cta-link">Contact</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(f"""
<footer class="site-footer">
     <p>
       © {CURRENT_YEAR} Goffinet — 
        <a href="?section=mentions-legales">Mentions légales</a> | 
        <a href="?section=contact">Contact</a>
    </p>
</footer>
""", unsafe_allow_html=True)

