from pathlib import Path
from html import escape
from urllib.parse import quote

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parent
INVENTORY_PATH = ROOT / "data" / "source_inventory.csv"
DRIVE_INVENTORY_PATH = ROOT / "data" / "google_drive_inventory.csv"
NOTEBOOK_INVENTORY_PATH = ROOT / "data" / "notebook_inventory.csv"
CASE_STUDY_PATH = ROOT / "data" / "case_studies.csv"
PROJECT_VISUALS_PATH = ROOT / "data" / "project_visuals.csv"
LINKEDIN_EVIDENCE_PATH = ROOT / "data" / "linkedin_evidence.csv"
ORGANIZED_FOLDERS_PATH = ROOT / "data" / "organized_project_folders.csv"
ML_ROADMAP_PATH = ROOT / "data" / "ml_future_roadmap.csv"
CONTACT_SHEETS = [
    ROOT / "assets" / "contact_sheets" / "contact_sheet_02.jpg",
    ROOT / "assets" / "contact_sheets" / "contact_sheet_05.jpg",
    ROOT / "assets" / "contact_sheets" / "contact_sheet_07.jpg",
    ROOT / "assets" / "contact_sheets" / "contact_sheet_08.jpg",
]

ML_FUTURE_POINTS = [
    {
        "Project": "Handshake AI / QGIS workflow training",
        "Why ML matters": "Human demonstrations, screenshots, and rubric reviews can become training data for software agents that eventually complete GIS and scientific-visualization tasks with less step-by-step help.",
    },
    {
        "Project": "Pondicherry seismic notebooks",
        "Why ML matters": "Arrival picking, waveform QA, station matching, and event triage are repeatable pattern-recognition tasks that can be made faster with supervised models and reproducible notebooks.",
    },
    {
        "Project": "North Slope gas hydrates",
        "Why ML matters": "Wireline, map, geologic, and source-library features can become a pipeline for hydrate interval screening, uncertainty ranking, and deck-ready decision support.",
    },
    {
        "Project": "REE thesis and Gephi graphs",
        "Why ML matters": "Graph data from Gephi/GraphML can support relationship mining across minerals, host rocks, paragenesis, deposit type, and evidence strength.",
    },
    {
        "Project": "Rock classification and geochemistry",
        "Why ML matters": "Thin-section images, chemical classification diagrams, spider diagrams, and labeled formation tables can become structured training examples for rock/mineral classification.",
    },
    {
        "Project": "Processing earthquake visualization",
        "Why ML matters": "This was the first AI-assisted visualization experiment: even without the original code, the video shows the origin point for turning geoscience data into interactive/sonified visual reasoning.",
    },
]

BACKGROUND_POINTS = [
    "M.S. Geosciences with field, lab, GIS, seismic, gravity, EM/ERT/TEM, and visualization experience.",
    "Handshake AI work connects human technical demonstrations with supervised AI evaluation for QGIS, ParaView, Vagon recordings, and geospatial workflows.",
    "SAGE/GAGE field research adds instrument deployment, geophysical acquisition, and subsurface interpretation context.",
    "Java, SQL, REST API, Spring Boot, notebooks, Streamlit, GitHub, VS Code, and Codex connect the science work to repeatable software pipelines.",
]

PRESENTATION_PILLARS = [
    (
        "AI as workflow memory",
        "The important part is not one prompt. It is the repeated loop: screenshots, files, goals, next steps, code changes, and evidence capture.",
    ),
    (
        "Human-labeled software use",
        "Handshake/Vagon work can be framed as supervised examples for future agents: real QGIS/ParaView tasks, screen recordings, and rubric-based evaluation.",
    ),
    (
        "Geoscience needs structure",
        "Maps, wells, waveforms, lithology, graphs, thin sections, decks, and manuscripts need domain context before ML becomes useful.",
    ),
    (
        "Codex turns evidence into systems",
        "VS Code, GitHub, Streamlit, notebooks, and organized folders convert scattered artifacts into reproducible, inspectable pipelines.",
    ),
]

WORKFLOW_STAGES = [
    ("1. Prompt + screenshot", "Ask what to do next while showing AI the actual state of the project."),
    ("2. Source capture", "Collect PDFs, decks, notebooks, videos, QGIS screenshots, Gephi exports, and resume evidence."),
    ("3. Code + organize", "Use Codex to inspect files, write manifests, build Streamlit pages, and keep project folders clean."),
    ("4. Visualize + explain", "Turn outputs into maps, videos, image panels, code snippets, and narrative cards."),
    ("5. Review + train", "Use expert feedback and labeled workflow demonstrations to improve future AI/ML systems."),
]

EXPERT_INSIGHTS = [
    (
        "Seismic workflows",
        "Next strength: quantify arrival-picking uncertainty, station geometry limits, validation events, and where ML could automate QA without hiding assumptions.",
    ),
    (
        "Gas hydrate screening",
        "Next strength: define feature tables from logs, geology, depth, pressure-temperature context, and source confidence before training any classifier.",
    ),
    (
        "Knowledge graphs",
        "Next strength: formalize graph schema, edge types, evidence weights, and how Gephi communities translate into geologic claims.",
    ),
    (
        "Rock/geochemistry classification",
        "Next strength: connect thin-section labels, chemical classification diagrams, spider plots, and formation tables into a small supervised dataset.",
    ),
    (
        "Software-use agents",
        "Next strength: treat Vagon videos and rubric reviews as task demonstrations: what was clicked, why, what output counted as correct, and where the model failed.",
    ),
    (
        "Scientific communication",
        "Next strength: make each project end with an actionable decision: what to inspect, model, validate, or collect next.",
    ),
]

VISUAL_STORYBOARD_IDEAS = [
    (
        "Node movement timeline",
        "Dots move from raw files to variables to model output. Best for REE graph, Handshake workflows, and seismic notebooks.",
    ),
    (
        "Before / after pair",
        "Left: messy screenshot, notebook, or table. Right: cleaned graph, map, dashboard, or ranked output.",
    ),
    (
        "Evidence stack",
        "Layer screenshots, code, source files, and output images so people see how AI connected the pieces.",
    ),
    (
        "Model decision card",
        "Show one predicted label or ranked target with the features that influenced it.",
    ),
    (
        "Human review loop",
        "Show where you approve, reject, relabel, or ask AI for the next step.",
    ),
    (
        "Industry bottleneck card",
        "One diagram per project: why people have not solved it yet, then the AI lever that changes the cost.",
    ),
]

TOPIC_ROOMS = [
    {
        "slug": "ai_workflow",
        "title": "AI Workflow And Handshake",
        "tagline": "How screenshots, task recordings, and rubric checks become supervised examples for future scientific software agents.",
        "project_key": "arcgis_raster_ml",
        "hero": "assets/project_visuals/workflow_qgis_handshake_ai_01.png",
        "theme": "Human demonstrations + Codex file access + geospatial software evaluation.",
        "bottleneck": "Scientific software tasks are still hard for AI agents because the work is visual, multi-step, file-dependent, and judged by domain-specific output quality.",
        "why_not_done": "Most training data captures final answers, not the messy human process: opening files, choosing tools, recovering from errors, checking map layers, and deciding whether an output is scientifically acceptable.",
        "ai_used": "AI was used as a task partner and evaluator: screenshots, QGIS/Vagon workflows, rubric checks, prompt refinement, and repeated next-step guidance turned hands-on software work into structured examples.",
        "future_ai": "A stronger implementation would convert recordings into step-by-step action traces, label failure points, connect them to source files, and use Codex-style agents to replay and validate workflows inside real project folders.",
        "why_it_matters": "This is the clearest bridge to AI professionals: the work is not only using AI, it is producing examples of how AI systems should learn technical software workflows.",
        "proof": ["Handshake AI profile evidence", "QGIS workflow screenshots", "LinkedIn profile text", "Organized profile/Handshake folder"],
        "question": "How much expert-labeled workflow data is needed before agents can perform GIS and visualization tasks reliably?",
    },
    {
        "slug": "thesis_graph",
        "title": "REE Thesis Knowledge Graph",
        "tagline": "Mountain Pass and Bayan Obo framed through graph data, Gephi exports, and a narrated research video.",
        "project_key": "thesis_knowledge_graph",
        "hero": "assets/project_visuals/thesis_host_context_clean.png",
        "theme": "Source synthesis -> graph schema -> visual explanation -> presentation.",
        "bottleneck": "Research synthesis often fails because hundreds of pages of literature, notes, diagrams, and claims remain trapped in prose instead of becoming queryable structure.",
        "why_not_done": "Building useful knowledge graphs is labor-intensive: entities must be named consistently, relationships need evidence, and domain experts must decide which links are geologically meaningful.",
        "ai_used": "AI helped turn thesis notes, references, Gephi exports, and presentation material into an explainable narrative around Mountain Pass and Bayan Obo.",
        "future_ai": "Newer AI tools could extract candidate entities/relations from PDFs, let an expert approve edges, assign evidence weights, and generate graph-backed slides or literature-review sections.",
        "why_it_matters": "Knowledge graphs make research structure visible: minerals, host rocks, paragenesis, evidence, and deposit architecture become inspectable relationships.",
        "proof": ["Embedded thesis walkthrough video", "Thesis Ch.1 deck", "GraphML file", "Gephi node/edge CSVs"],
        "question": "What graph schema and evidence weights would make this useful for expert review or ML feature generation?",
    },
    {
        "slug": "processing_earthquake",
        "title": "First AI Visualization: Earthquake Globe",
        "tagline": "A Processing-era earthquake visualization and sonification video, used as the origin story for later geoscience dashboards.",
        "project_key": "processing_visuals",
        "hero": "assets/project_visuals/processing_earthquake_linkedin_poster.jpg",
        "theme": "Creative coding + USGS earthquake data + visual/sound encoding.",
        "bottleneck": "Geoscience data can be technically correct but hard to feel, inspect, or communicate, especially when spatial, temporal, magnitude, and depth signals all matter at once.",
        "why_not_done": "Creative scientific visualization takes coding, design, domain knowledge, and data cleanup; many early prototypes never become reproducible tools.",
        "ai_used": "This was the first AI-assisted data visualization experiment: using Processing, USGS earthquake data, 3D globe markers, color/size/depth encoding, and sound to make seismic patterns visible.",
        "future_ai": "A modern version could rebuild the concept in Streamlit or Three.js, keep the data pipeline transparent, add filters/uncertainty, and use AI to explain what viewers are seeing. First step: export the correct 54-second LinkedIn video or recover the original Processing capture.",
        "why_it_matters": "The verified LinkedIn post shows the first attempt to use AI and coding to make geoscience data felt visually and sonically; the local original video still needs to be added before embedding.",
        "proof": ["Verified LinkedIn video post", "LinkedIn poster frame", "Processing geophysical methods sketch", "EarthScope seismology context"],
        "question": "How should early creative visualizations be rebuilt as reproducible, inspectable scientific tools?",
    },
    {
        "slug": "seismic",
        "title": "Seismic Notebooks And Pondicherry",
        "tagline": "Notebook-driven seismic velocity analysis, waveform interpretation visuals, and seismology training evidence.",
        "project_key": "pondicherry",
        "hero": "assets/project_visuals/pondicherry_near_offset_reannotated.png",
        "theme": "Catalog search -> waveform processing -> interpretation figures -> portfolio explanation.",
        "bottleneck": "Small seismic studies can get stuck between exploratory notebooks and defensible analysis: waveform access, station geometry, arrival picking, and interpretation all need careful QA.",
        "why_not_done": "The tooling exists, but turning a notebook into a reproducible workflow requires data provenance, uncertainty tracking, validation events, and clear visual outputs.",
        "ai_used": "AI helped interpret notebook logic, identify what outputs were presentation-worthy, connect waveform/seismic visuals to the research story, and organize the evidence.",
        "future_ai": "A stronger version would use AI-assisted arrival picking, automatic QA flags, reproducible ObsPy pipelines, and report generation that preserves assumptions and uncertainty.",
        "why_it_matters": "This is where AI can help turn exploratory notebooks into workflows with clearer uncertainty, validation, and reproducible outputs.",
        "proof": ["VelocityAnalysisPalkStraight notebook", "Seismic annotated panels", "EarthScope SSBW evidence"],
        "question": "Where should ML assist: event triage, arrival picking, waveform QA, or uncertainty reporting?",
    },
    {
        "slug": "north_slope",
        "title": "North Slope Gas Hydrate Atlas",
        "tagline": "A GIS and source-library workflow for turning public geoscience material into a dashboard and ML planning scaffold.",
        "project_key": "north_slope",
        "hero": "assets/project_visuals/north_slope_alaska_geology_well_map.png",
        "theme": "Public sources + GIS layers + Streamlit atlas + hydrate ML planning.",
        "bottleneck": "Subsurface energy projects often have fragmented public data: maps, papers, well-log concepts, stratigraphy, and ML ideas are spread across many formats.",
        "why_not_done": "Integrating geologic context with machine-learning-ready features is slow because provenance, scale, coordinate systems, and domain assumptions have to be reconciled before modeling.",
        "ai_used": "AI helped organize the source library, build a Streamlit atlas structure, summarize hydrate/geomechanics material, and frame a wireline ML presentation scaffold.",
        "future_ai": "Next implementation should build a feature table from logs, depth, stratigraphy, thermal context, and source confidence, then use AI to audit provenance before any model is trained.",
        "why_it_matters": "For DOE-style audiences, this is the strongest energy/subsurface thread: logs, geologic context, source provenance, and ML screening can become one pipeline.",
        "proof": ["North Slope map", "Wireline ML scaffold deck", "Gas hydrate source library", "Streamlit app structure"],
        "question": "What feature table would an expert trust for hydrate interval screening and uncertainty ranking?",
    },
    {
        "slug": "rock_classification",
        "title": "Rock Classification And Geochemistry",
        "tagline": "Chemical classification visuals, thin-section decks, formation tables, and graph outputs as future ML training material.",
        "project_key": "rock_classification",
        "hero": "assets/project_visuals/rock_chemical_classification_reference.jpg",
        "theme": "Petrography + geochemistry diagrams + labeled examples + classification tasks.",
        "bottleneck": "Rock and mineral classification is visually rich but difficult to scale because labels, thin-section context, geochemical diagrams, and expert reasoning are rarely stored together.",
        "why_not_done": "Useful ML needs curated examples, consistent labels, metadata, petrographic context, and validation from experts; a folder of images or plots alone is not enough.",
        "ai_used": "AI helped identify the classification materials, organize the deck/image/CSV evidence, and frame them as potential training examples rather than isolated class assignments.",
        "future_ai": "A future workflow could pair thin-section images, chemical classification diagrams, spider plots, and formation tables with expert labels, then test image/text/tabular models together.",
        "why_it_matters": "This connects visual geology to supervised ML: labeled thin sections, rock classes, spider diagrams, and geochemical features can become structured examples.",
        "proof": ["Chemical classification image", "Thin-section PowerPoint", "Formation classification CSV", "Gephi exports"],
        "question": "What labels, metadata, and validation examples would turn this into a useful training dataset?",
    },
    {
        "slug": "valles",
        "title": "SAGE / Valles Caldera Geophysics",
        "tagline": "Field geophysics, gravity maps, crustal structure visuals, and SAGE presentation evidence.",
        "project_key": "valles_caldera",
        "hero": "assets/project_visuals/valles_bouguer.png",
        "theme": "Field acquisition + geophysical maps + subsurface interpretation + presentation.",
        "bottleneck": "Field geophysics produces multiple imperfect views of the subsurface, and teams must compare gravity, EM/TEM/ERT, seismic, maps, and geology without losing uncertainty.",
        "why_not_done": "The bottleneck is not only computation; it is interpretation across instruments, terrain constraints, noisy data, and project-specific geologic context.",
        "ai_used": "AI was used to organize SAGE/Valles evidence, connect field background to map outputs, and frame the project as more than a standalone presentation.",
        "future_ai": "A stronger implementation could create a field-data evidence dashboard that compares map products, stores assumptions, links figures to source files, and highlights where expert review is needed.",
        "why_it_matters": "This grounds the AI story in field science: instruments, terrain, real constraints, and interpretation decisions.",
        "proof": ["SAGE presentation deck", "Bouguer/free-air/Moho maps", "Valles project files"],
        "question": "How should AI help compare map products without flattening field uncertainty and geologic judgment?",
    },
]

CODE_SNIPPETS = {
    "pondicherry": """from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import pandas as pd

clients = {
    "IRIS": Client("IRIS"),
    "USGS": Client("USGS"),
}

catalog = clients["USGS"].get_events(
    starttime=start_time,
    endtime=end_time,
    minlatitude=11.0,
    maxlatitude=13.0,
    minlongitude=78.5,
    maxlongitude=81.0,
    minmagnitude=1.0,
)

summary_df["P_Wave_Velocity_kmps"] = (
    summary_df["Epicentral_Distance_km"] / summary_df["Offset_Seconds"]
)""",
    "north_slope": """REGIONAL_SCENE = EXPORT_DIR / "north_slope_plotly_advanced.html"
MASTER_3D = PROJECT_ROOT / "03_data_final" / "master_layers" / "north_slope_master_3d_surfaces.parquet"

PAGES = [
    "Welcome",
    "Regional Atlas",
    "Structural Explorer",
    "Data Library",
    "Research Framework",
    "Future Well-Log Engine",
]""",
    "stock": """health = data.health()
short = data.shortlist()

cols = st.columns(4)
cols[0].metric("Latest market date", health.get("latest_market_date", "-")[:10])
cols[1].metric("Shortlist date", health.get("latest_shortlist_date", "-")[:10])
cols[2].metric("Tracked candidates", health.get("feature_summary_rows", "0"))
cols[3].metric("Shortlist picks", health.get("latest_shortlist_rows", "0"))""",
    "source_workflow": """ChatGPT / Codex
    -> markdown notes and Obsidian-style source capture
    -> source manifests and project blueprints
    -> notebooks, QGIS, Streamlit dashboards
    -> manuscript drafts and PowerPoint-ready narrative""",
}


st.set_page_config(
    page_title="AI Research Workflow Portfolio",
    page_icon="AI",
    layout="wide",
)


st.markdown(
    """
<style>
    .block-container { padding-top: 2rem; max-width: 1320px; }
    div[data-testid="stMetric"] {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 0.75rem 0.9rem;
    }
    .small-note { color: #64748b; font-size: 0.92rem; }
    .talk-hero {
        border: 1px solid #d1d5db;
        border-radius: 8px;
        padding: 1.25rem 1.35rem;
        background: #f8fafc;
        margin-bottom: 1rem;
    }
    .talk-hero h2 { margin: 0 0 0.4rem 0; }
    .talk-kicker {
        color: #475569;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0;
        font-weight: 700;
    }
    .pipeline-step {
        border-left: 4px solid #0f766e;
        padding: 0.55rem 0.75rem;
        background: #f9fafb;
        min-height: 112px;
    }
    .ml-strip {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.8rem;
        margin: 0.85rem 0 0.75rem 0;
        position: relative;
    }
    .ml-stage {
        border: 1px solid #dbe3ea;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.75rem 0.8rem 0.85rem 0.8rem;
        min-height: 150px;
        box-shadow: 0 1px 0 rgba(15, 23, 42, 0.03);
    }
    .ml-strip.compact .ml-stage { min-height: 120px; }
    .ml-dot {
        width: 13px;
        height: 13px;
        border-radius: 50%;
        background: #0f766e;
        box-shadow: 0 0 0 4px #ccfbf1;
        margin-bottom: 0.55rem;
    }
    .ml-label {
        font-weight: 800;
        color: #111827;
        font-size: 0.92rem;
        margin-bottom: 0.3rem;
        text-transform: uppercase;
    }
    .ml-body {
        color: #475569;
        font-size: 0.92rem;
        line-height: 1.35;
    }
    .future-timeline {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.8rem;
        margin: 0.8rem 0;
    }
    .future-timeline div {
        border-left: 4px solid #2563eb;
        background: #eff6ff;
        padding: 0.75rem 0.85rem;
        min-height: 112px;
    }
    .future-timeline span {
        display: block;
        color: #1d4ed8;
        font-size: 0.85rem;
        font-weight: 800;
        margin-bottom: 0.35rem;
        text-transform: uppercase;
    }
    .future-timeline strong {
        color: #1e293b;
        font-size: 0.95rem;
        line-height: 1.35;
    }
    .compare-panel {
        border: 1px solid #d1d5db;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.95rem 1rem;
        min-height: 230px;
    }
    .prompt-box {
        border: 1px solid #d1d5db;
        border-radius: 8px;
        background: #111827;
        color: #f9fafb;
        padding: 0.85rem 0.95rem;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
        font-size: 0.9rem;
        line-height: 1.42;
    }
    .visual-flow {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        padding: 0.95rem;
        margin: 0.65rem 0 1rem 0;
    }
    .visual-flow-title {
        color: #111827;
        font-weight: 850;
        font-size: 1rem;
        margin-bottom: 0.75rem;
    }
    .node-lane {
        display: grid;
        grid-template-columns: 1fr 0.72fr 1fr;
        gap: 0.8rem;
        align-items: stretch;
    }
    .movement-rail {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.45rem;
        align-items: start;
        margin-bottom: 0.85rem;
    }
    .rail-step {
        position: relative;
        padding-top: 1.4rem;
        color: #334155;
        font-size: 0.82rem;
        font-weight: 750;
        text-align: center;
    }
    .rail-step::before {
        content: "";
        position: absolute;
        top: 0.28rem;
        left: 50%;
        width: 0.78rem;
        height: 0.78rem;
        transform: translateX(-50%);
        border-radius: 50%;
        background: #0f766e;
        box-shadow: 0 0 0 4px #ccfbf1;
        z-index: 2;
    }
    .rail-step::after {
        content: "";
        position: absolute;
        top: 0.62rem;
        left: 50%;
        width: 100%;
        border-top: 3px dotted #94a3b8;
        z-index: 1;
    }
    .rail-step:last-child::after { display: none; }
    .node-cluster {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.75rem;
        min-height: 188px;
    }
    .node-cluster h4 {
        margin: 0 0 0.55rem 0;
        color: #334155;
        font-size: 0.86rem;
        text-transform: uppercase;
    }
    .node-pill {
        display: inline-block;
        border: 1px solid #cbd5e1;
        border-radius: 999px;
        background: #f8fafc;
        color: #1f2937;
        padding: 0.34rem 0.55rem;
        margin: 0.18rem;
        font-size: 0.82rem;
        line-height: 1.2;
    }
    .node-pill.input { border-color: #99f6e4; background: #f0fdfa; }
    .node-pill.feature { border-color: #bfdbfe; background: #eff6ff; }
    .node-pill.output { border-color: #fde68a; background: #fffbeb; }
    .model-core {
        border: 1px solid #0f766e;
        border-radius: 8px;
        background: #0f766e;
        color: #ffffff;
        padding: 0.75rem;
        min-height: 188px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
        position: relative;
    }
    .model-core::before,
    .model-core::after {
        content: "";
        position: absolute;
        top: 50%;
        width: 0.8rem;
        border-top: 3px dotted #0f766e;
    }
    .model-core::before { left: -0.8rem; }
    .model-core::after { right: -0.8rem; }
    .model-core strong {
        display: block;
        font-size: 1rem;
        margin-bottom: 0.45rem;
    }
    .model-core span {
        font-size: 0.86rem;
        line-height: 1.3;
        color: #dcfce7;
    }
    .bottleneck-chip {
        border-left: 4px solid #ef4444;
        background: #fff7ed;
        padding: 0.62rem 0.75rem;
        color: #7c2d12;
        font-size: 0.94rem;
        margin-top: 0.75rem;
    }
    .storyboard-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.85rem;
        margin: 0.75rem 0 1rem 0;
    }
    .storyboard-card {
        border: 1px solid #d1d5db;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.85rem;
        min-height: 175px;
    }
    .storyboard-card strong {
        display: block;
        color: #111827;
        margin-bottom: 0.4rem;
    }
    .storyboard-card span {
        display: block;
        color: #475569;
        font-size: 0.92rem;
        line-height: 1.35;
    }
    @media (max-width: 900px) {
        .ml-strip, .future-timeline, .node-lane, .storyboard-grid { grid-template-columns: 1fr; }
        .ml-stage { min-height: auto; }
        .model-core::before, .model-core::after { display: none; }
        .movement-rail { grid-template-columns: repeat(4, minmax(4rem, 1fr)); overflow-x: auto; }
    }
</style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_csv(path: Path, modified_time: float) -> pd.DataFrame:
    return pd.read_csv(path)


def load_current_csv(path: Path) -> pd.DataFrame:
    return load_csv(path, path.stat().st_mtime)


def local_file_uri(path_text: str) -> str:
    path = Path(path_text)
    try:
        return path.resolve().as_uri()
    except ValueError:
        return "file:///" + quote(str(path).replace("\\", "/"))


def source_row(title: str) -> pd.Series | None:
    match = inventory[inventory["title"] == title]
    if match.empty:
        return None
    return match.iloc[0]


def drive_row(title: str) -> pd.Series | None:
    match = drive_inventory[drive_inventory["title"] == title]
    if match.empty:
        return None
    return match.iloc[0]


def valid_text(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def project_asset(path_text: str) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path
    return ROOT / path


def existing_path(path_text: str) -> Path | None:
    if not valid_text(path_text):
        return None
    path = Path(path_text)
    if path.exists():
        return path
    return None


def topic_url(slug: str) -> str:
    return f"?section=Project%20Rooms&topic={quote(slug)}"


def topic_by_slug(slug: str) -> dict:
    for topic in TOPIC_ROOMS:
        if topic["slug"] == slug:
            return topic
    return TOPIC_ROOMS[0]


def evidence_path_by_key(key: str) -> Path | None:
    match = linkedin_evidence[linkedin_evidence["key"] == key]
    if match.empty:
        return None
    return existing_path(match.iloc[0]["local_path"])


def roadmap_row(project_key: str) -> pd.Series | None:
    match = ml_roadmap[ml_roadmap["project_key"] == project_key]
    if match.empty:
        return None
    return match.iloc[0]


def stage_items(row: pd.Series) -> list[tuple[str, str]]:
    return [
        ("Input data", row["input_data"]),
        ("Variables", row["features_or_variables"]),
        ("Model / method", row["model_or_method"]),
        ("Output", row["output"]),
    ]


def render_ml_strip(row: pd.Series, compact: bool = False) -> None:
    stages = stage_items(row)
    css_class = "ml-strip compact" if compact else "ml-strip"
    cards = []
    for label, body in stages:
        cards.append(
            f"""
<div class="ml-stage">
  <div class="ml-dot"></div>
  <div class="ml-label">{label}</div>
  <div class="ml-body">{body}</div>
</div>
            """
        )
    st.markdown(
        f"""
<div class="{css_class}">
  {''.join(cards)}
</div>
        """,
        unsafe_allow_html=True,
    )


def render_future_timeline(row: pd.Series) -> None:
    st.markdown(
        f"""
<div class="future-timeline">
  <div>
    <span>Now to 6 months</span>
    <strong>{row['next_6_months']}</strong>
  </div>
  <div>
    <span>6 to 12 months</span>
    <strong>{row['next_12_months']}</strong>
  </div>
  <div>
    <span>12 to 24 months</span>
    <strong>{row['next_24_months']}</strong>
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def split_terms(value: str, limit: int = 5) -> list[str]:
    if not valid_text(value):
        return []
    terms = [part.strip() for part in value.split(";") if part.strip()]
    return terms[:limit]


def pill_html(terms: list[str], class_name: str) -> str:
    if not terms:
        return "<span class='node-pill'>define next</span>"
    return "".join(
        f"<span class='node-pill {class_name}'>{escape(term)}</span>"
        for term in terms
    )


def render_node_movement(row: pd.Series, title: str = "What moves through the ML system") -> None:
    inputs = split_terms(row["input_data"], 5)
    features = split_terms(row["features_or_variables"], 6)
    outputs = split_terms(row["output"], 4)
    model = escape(str(row["model_or_method"]).split(";")[0].strip())
    st.markdown(
        f"""
<div class="visual-flow">
  <div class="visual-flow-title">{escape(title)}</div>
  <div class="movement-rail">
    <div class="rail-step">raw evidence</div>
    <div class="rail-step">variables</div>
    <div class="rail-step">ML system</div>
    <div class="rail-step">decision output</div>
  </div>
  <div class="node-lane">
    <div class="node-cluster">
      <h4>Project evidence</h4>
      {pill_html(inputs, "input")}
    </div>
    <div class="model-core">
      <strong>{model}</strong>
      <span>AI/ML layer turns messy project artifacts into reviewable structure.</span>
    </div>
    <div class="node-cluster">
      <h4>Actionable output</h4>
      {pill_html(features[:3], "feature")}
      {pill_html(outputs, "output")}
    </div>
  </div>
  <div class="bottleneck-chip"><strong>Bottleneck:</strong> {escape(str(row["bottleneck"]))}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


inventory = load_current_csv(INVENTORY_PATH)
drive_inventory = load_current_csv(DRIVE_INVENTORY_PATH)
notebook_inventory = load_current_csv(NOTEBOOK_INVENTORY_PATH)
case_studies = load_current_csv(CASE_STUDY_PATH)
project_visuals = load_current_csv(PROJECT_VISUALS_PATH)
linkedin_evidence = load_current_csv(LINKEDIN_EVIDENCE_PATH)
organized_folders = load_current_csv(ORGANIZED_FOLDERS_PATH)
ml_roadmap = load_current_csv(ML_ROADMAP_PATH)


SECTIONS = [
    "Overview",
    "Presentation View",
    "Project Rooms",
    "Machine Learning Future",
    "Case Studies",
    "LinkedIn Evidence",
    "Code And Architecture",
    "Notebook Explorer",
    "Evidence Library",
    "Visual Gallery",
    "Build Plan",
]
query_section = st.query_params.get("section", "Overview")
if query_section == "Visual Contact Sheets":
    query_section = "Visual Gallery"
if query_section not in SECTIONS:
    query_section = "Overview"


with st.sidebar:
    st.title("AI Workflow")
    section = st.radio(
        "View",
        SECTIONS,
        index=SECTIONS.index(query_section),
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("Local + Drive evidence for a website or PowerPoint story.")


if section == "Overview":
    st.title("AI Geoscience Workflow Portfolio")
    st.write(
        "Choose a project room. Each room has its own visual evidence, AI workflow angle, "
        "expert-facing question, and links back to the source files."
    )

    cols = st.columns(5)
    cols[0].metric("Case studies", len(case_studies))
    cols[1].metric("Notebooks indexed", len(notebook_inventory))
    cols[2].metric("Drive links", len(drive_inventory))
    cols[3].metric("High-priority sources", int((inventory["priority"] == "high").sum()))
    cols[4].metric("Visual assets", len(project_visuals))

    st.subheader("Motion evidence")
    motion_cols = st.columns([1.15, 1])
    with motion_cols[0]:
        processing_video = evidence_path_by_key("processing_earthquake")
        if processing_video is not None:
            st.video(str(processing_video))
            st.caption(
                "Processing earthquake globe / sonification video. This is better than a GIF here because the sound is part of the project."
            )
        else:
            poster_path = project_asset("assets/project_visuals/processing_earthquake_linkedin_poster.jpg")
            if poster_path.exists():
                st.image(
                    str(poster_path),
                    caption="Verified LinkedIn poster frame. The actual 54-second video needs to be exported before local embedding.",
                    use_container_width=True,
                )
            st.info("The LinkedIn earthquake video is verified, but the local file previously used here was the wrong video. Add the correct export to embed it with sound.")
    with motion_cols[1]:
        st.markdown("**Why show this first?**")
        st.write(
            "This makes the site feel like an actual demonstration instead of a file index. "
            "The project started as AI-assisted scientific visualization: USGS earthquake data, 3D spatial encoding, magnitude/depth styling, and sound."
        )
        st.write(
            "The modern question is how to rebuild this as a reproducible web visualization with filters, uncertainty, source provenance, and explainable AI narration."
        )

    st.subheader("Start here")
    hub_cols = st.columns(3)
    for idx, topic in enumerate(TOPIC_ROOMS):
        with hub_cols[idx % 3]:
            with st.container(border=True):
                hero_path = project_asset(topic["hero"])
                if topic["slug"] == "processing_earthquake":
                    processing_preview = evidence_path_by_key("processing_earthquake")
                    if processing_preview is not None:
                        st.video(str(processing_preview))
                    elif hero_path.exists():
                        st.image(str(hero_path), use_container_width=True)
                elif hero_path.exists():
                    st.image(str(hero_path), use_container_width=True)
                st.markdown(f"**{topic['title']}**")
                st.write(topic["tagline"])
                st.markdown(f"**Bottleneck:** {topic['bottleneck']}")
                st.caption(f"AI angle: {topic['theme']}")
                st.link_button("Open project room", topic_url(topic["slug"]))

    st.subheader("Fast presentation links")
    fast_cols = st.columns(5)
    fast_cols[0].link_button("Presentation View", "?section=Presentation%20View")
    fast_cols[1].link_button("ML Future", "?section=Machine%20Learning%20Future")
    fast_cols[2].link_button("Embedded Videos", "?section=LinkedIn%20Evidence")
    fast_cols[3].link_button("Visual Gallery", "?section=Visual%20Gallery")
    fast_cols[4].link_button("All Case Studies", "?section=Case%20Studies")

    st.subheader("Strong links to start with")
    link_cols = st.columns(2)
    thesis = drive_row("Thesis Ch.1 Presentation")
    advgis = drive_row("ADVGIS Final")
    if thesis is not None:
        link_cols[0].link_button("Open Thesis Ch.1 Presentation", thesis["url"])
    if advgis is not None:
        link_cols[1].link_button("Open ADVGIS Final", advgis["url"])

    st.subheader("Why this is not just a file list")
    st.write(
        "The argument is that AI becomes most useful when it is connected to durable project context: "
        "source folders, code, screenshots, notebooks, GIS outputs, graph exports, and presentation artifacts. "
        "The files are evidence; the workflow is the scalable research system."
    )


elif section == "Presentation View":
    st.markdown(
        """
<div class="talk-hero">
  <div class="talk-kicker">Talk view for AI + geoscience professionals</div>
  <h2>From scattered research artifacts to AI-assisted geoscience pipelines</h2>
  <p>
    The strongest claim here is practical: AI becomes valuable when it can see the work,
    help organize the evidence, turn experiments into repeatable systems, and expose what
    still needs expert validation.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("The core argument")
    pillar_cols = st.columns(4)
    for col, (title, body) in zip(pillar_cols, PRESENTATION_PILLARS):
        with col:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.write(body)

    st.subheader("How to read every project")
    st.write(
        "Each topic should be evaluated with the same four-part lens: "
        "what bottleneck is being addressed, why it has persisted, how AI was actually used in the current example, "
        "and what a modern AI/ML implementation would need to make it trustworthy."
    )

    st.subheader("Workflow architecture")
    pipeline_cols = st.columns(len(WORKFLOW_STAGES))
    for col, (title, body) in zip(pipeline_cols, WORKFLOW_STAGES):
        with col:
            st.markdown(
                f"""
<div class="pipeline-step">
  <strong>{title}</strong><br>
  <span>{body}</span>
</div>
                """,
                unsafe_allow_html=True,
            )

    st.subheader("Evidence you can show live")
    evidence_cols = st.columns([1.1, 1])
    with evidence_cols[0]:
        video_rows = linkedin_evidence[linkedin_evidence["category"] == "video"]
        selected_video = st.selectbox(
            "Embedded video",
            video_rows["title"].tolist(),
            key="presentation_video",
        )
        video_row = video_rows[video_rows["title"] == selected_video].iloc[0]
        video_path = existing_path(video_row["local_path"])
        if video_path is not None:
            st.video(str(video_path))
            st.caption(video_row["linkedin_signal"])
        else:
            st.warning("Organized local video file not found.")

    with evidence_cols[1]:
        featured_visuals = project_visuals[
            project_visuals["project_key"].isin(
                [
                    "thesis_knowledge_graph",
                    "north_slope",
                    "arcgis_raster_ml",
                    "rock_classification",
                    "valles_caldera",
                    "pondicherry",
                ]
            )
        ].sort_values(["project_key", "sort_order"])
        visual_titles = featured_visuals["title"].tolist()
        selected_visual_title = st.selectbox(
            "Visual proof",
            visual_titles,
            key="presentation_visual",
        )
        selected_visual = featured_visuals[featured_visuals["title"] == selected_visual_title].iloc[0]
        visual_path = project_asset(selected_visual["asset_path"])
        if visual_path.exists():
            st.image(str(visual_path), caption=selected_visual["caption"], use_container_width=True)
        else:
            st.warning("Visual asset not found.")

    st.subheader("What people who know more may ask")
    insight_cols = st.columns(3)
    for idx, (title, body) in enumerate(EXPERT_INSIGHTS):
        with insight_cols[idx % 3]:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.write(body)

    st.subheader("Talk path")
    path_cols = st.columns(3)
    with path_cols[0]:
        st.markdown("**1. Open with honesty**")
        st.write(
            "AI was used as a working collaborator: screenshots, repeated next-step prompting, "
            "file search, code edits, notebook interpretation, and evidence organization."
        )
    with path_cols[1]:
        st.markdown("**2. Show the proof**")
        st.write(
            "Use the embedded thesis video, Processing earthquake visualization, QGIS/Handshake screenshots, "
            "Gephi files, and rock-classification deck as concrete artifacts."
        )
    with path_cols[2]:
        st.markdown("**3. Invite expert critique**")
        st.write(
            "Ask what validation, labels, uncertainty, schema, and data provenance would make each project "
            "more useful as an ML or scientific-agent workflow."
        )

    st.subheader("Organized evidence folders")
    folder_display = organized_folders[["title", "contents", "folder"]]
    st.dataframe(folder_display, hide_index=True, use_container_width=True)


elif section == "Project Rooms":
    topic_param = st.query_params.get("topic", TOPIC_ROOMS[0]["slug"])
    topic = topic_by_slug(topic_param)

    st.markdown(
        f"""
<div class="talk-hero">
  <div class="talk-kicker">Project room</div>
  <h2>{topic['title']}</h2>
  <p>{topic['tagline']}</p>
</div>
        """,
        unsafe_allow_html=True,
    )

    topic_roadmap = roadmap_row(topic["project_key"])
    with st.expander("Switch project room"):
        jump_cols = st.columns(4)
        for idx, room in enumerate(TOPIC_ROOMS):
            with jump_cols[idx % 4]:
                st.link_button(room["title"], topic_url(room["slug"]))

    if topic_roadmap is not None:
        render_node_movement(topic_roadmap, title="Project evidence -> ML output")

    hero_cols = st.columns([1.35, 1])
    with hero_cols[0]:
        hero_path = project_asset(topic["hero"])
        if topic["slug"] == "processing_earthquake":
            processing_room_video = evidence_path_by_key("processing_earthquake")
            if processing_room_video is not None:
                st.video(str(processing_room_video))
                st.caption("Embedded local Processing video with sound from the organized evidence folder.")
            elif hero_path.exists():
                st.image(
                    str(hero_path),
                    caption="Verified LinkedIn poster frame. Correct local video export is still needed before embedding with sound.",
                    use_container_width=True,
                )
                st.info(
                    "Correction: the previous local `Video.mov` candidate was not verified as the earthquake visualization. "
                    "The LinkedIn post itself is verified; the correct 54-second media file needs to be exported/downloaded and added here."
                )
        elif hero_path.exists():
            st.image(str(hero_path), caption=topic["theme"], use_container_width=True)
        else:
            st.warning("Hero image not found.")
    with hero_cols[1]:
        st.subheader("Project signal")
        st.info(topic["bottleneck"])
        st.caption(topic["why_not_done"])

    if topic_roadmap is not None:
        st.subheader("ML timeline")
        render_future_timeline(topic_roadmap)

    st.subheader("AI implementation logic")
    implementation_cols = st.columns(3)
    with implementation_cols[0]:
        with st.container(border=True):
            st.markdown("**Used now**")
            st.caption(topic["ai_used"])
    with implementation_cols[1]:
        with st.container(border=True):
            st.markdown("**Build next**")
            st.caption(topic["future_ai"])
    with implementation_cols[2]:
        with st.container(border=True):
            st.markdown("**Why care**")
            st.caption(topic["why_it_matters"])
            st.markdown(f"<p class='small-note'><strong>Ask:</strong> {topic['question']}</p>", unsafe_allow_html=True)

    st.subheader("Proof to show")
    proof_cols = st.columns(min(4, len(topic["proof"])))
    for idx, proof in enumerate(topic["proof"]):
        with proof_cols[idx % len(proof_cols)]:
            st.info(proof)

    if topic["slug"] == "thesis_graph":
        st.subheader("How the graph was made")
        graph_cols = st.columns([1.1, 1])
        nodes_path = Path(
            "C:\\Users\\gargi\\Downloads\\AI_powerpoint_project_evidence\\02_thesis_knowledge_graph\\gephi_nodes_full_multiclass_context.csv"
        )
        edges_path = Path(
            "C:\\Users\\gargi\\Downloads\\AI_powerpoint_project_evidence\\02_thesis_knowledge_graph\\gephi_edges_full_multiclass_context.csv"
        )
        with graph_cols[0]:
            st.markdown(
                """
<div class="prompt-box">
Prompt pattern:<br>
Given these REE thesis notes, suggest node categories, edge types, evidence fields,
and a cleaner schema for Mountain Pass and Bayan Obo. Keep the geology reviewable.
</div>
                """,
                unsafe_allow_html=True,
            )
            st.caption(
                "This is the AI-assisted spreadsheet step: make the entities and relationships explicit before Gephi or Neo4j."
            )
        with graph_cols[1]:
            st.markdown("**Spreadsheet evidence**")
            if nodes_path.exists() and edges_path.exists():
                nodes_preview = pd.read_csv(nodes_path, nrows=5)
                edges_preview = pd.read_csv(edges_path, nrows=5)
                st.metric("Node rows", f"{sum(1 for _ in nodes_path.open(errors='ignore')) - 1:,}")
                st.metric("Edge rows", f"{sum(1 for _ in edges_path.open(errors='ignore')) - 1:,}")
                with st.expander("Preview node table"):
                    st.dataframe(
                        nodes_preview[
                            [
                                "id",
                                "label",
                                "type",
                                "deposit_clean",
                                "hostcontext_clean",
                                "reebehavior_grouped",
                            ]
                        ],
                        hide_index=True,
                        use_container_width=True,
                    )
                with st.expander("Preview edge table"):
                    st.dataframe(
                        edges_preview[
                            [
                                "source",
                                "target",
                                "relationship_type",
                                "property_column",
                                "property_value",
                            ]
                        ],
                        hide_index=True,
                        use_container_width=True,
                    )
            else:
                st.info("Node/edge CSVs were not found in the organized evidence folder.")

    related_visuals = project_visuals[
        project_visuals["project_key"].fillna("") == topic["project_key"]
    ].sort_values("sort_order")
    related_evidence = linkedin_evidence[
        linkedin_evidence["project_key"].fillna("") == topic["project_key"]
    ]
    related_folders = organized_folders[
        organized_folders["project_key"].fillna("") == topic["project_key"]
    ]

    st.subheader("Visual evidence")
    visual_cols = st.columns(3)
    if related_visuals.empty:
        st.info("No extra visual has been selected for this topic yet.")
    for idx, visual in enumerate(related_visuals.itertuples(index=False)):
        with visual_cols[idx % 3]:
            visual_path = project_asset(visual.asset_path)
            with st.container(border=True):
                st.markdown(f"**{visual.title}**")
                if visual_path.exists():
                    st.image(str(visual_path), use_container_width=True)
                st.caption(visual.caption)

    st.subheader("Embedded or linked evidence")
    if related_evidence.empty:
        st.info("No direct LinkedIn/evidence manifest rows are attached to this topic yet.")
    else:
        evidence_cols = st.columns(2)
        for idx, evidence in enumerate(related_evidence.itertuples(index=False)):
            with evidence_cols[idx % 2]:
                evidence_path = existing_path(evidence.local_path)
                with st.container(border=True):
                    st.markdown(f"**{evidence.title}**")
                    st.write(evidence.linkedin_signal)
                    if evidence_path is not None:
                        suffix = evidence_path.suffix.lower()
                        if suffix in {".png", ".jpg", ".jpeg", ".webp"}:
                            st.image(str(evidence_path), use_container_width=True)
                        elif suffix in {".mp4", ".mov", ".m4v"}:
                            st.video(str(evidence_path))
                        elif suffix in {".pde", ".py", ".js", ".java"}:
                            st.code(
                                "\n".join(evidence_path.read_text(errors="ignore").splitlines()[:80]),
                                language="java",
                            )
                        else:
                            st.info(f"{suffix.upper().lstrip('.')} opens from the local source button.")
                        with st.expander("Source access"):
                            st.link_button("Open local source", local_file_uri(str(evidence_path)))
                            if valid_text(evidence.linkedin_url):
                                st.link_button("Open LinkedIn source", evidence.linkedin_url)
                    elif valid_text(evidence.linkedin_url):
                        with st.expander("Source access"):
                            st.link_button("Open LinkedIn source", evidence.linkedin_url)

    st.subheader("Folder and source access")
    folder_cols = st.columns(2)
    if related_folders.empty:
        st.info("No organized folder has been attached to this exact topic key yet.")
    for idx, folder in enumerate(related_folders.itertuples(index=False)):
        with folder_cols[idx % 2]:
            folder_path = Path(folder.folder)
            with st.container(border=True):
                st.markdown(f"**{folder.title}**")
                st.write(folder.contents)
                if folder_path.exists():
                    st.link_button("Open organized folder", local_file_uri(str(folder_path)))


elif section == "Machine Learning Future":
    st.markdown(
        """
<div class="talk-hero">
  <div class="talk-kicker">Machine learning future</div>
  <h2>From project artifacts to trainable geoscience workflows</h2>
  <p>
    The direction is not "AI did my homework." The direction is: each project produces
    inputs, labels, features, validation examples, and expert review points that can
    become stronger ML systems.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("How every project becomes a pipeline")
    st.write(
        "Use this page as the high-level map: the same structure appears under each project room, "
        "so the audience can see inputs, variables, models, and outputs without reading a wall of text."
    )

    st.subheader("Visuals worth building")
    storyboard_cards = []
    for title, body in VISUAL_STORYBOARD_IDEAS:
        storyboard_cards.append(
            f"""
<div class="storyboard-card">
  <strong>{escape(title)}</strong>
  <span>{escape(body)}</span>
</div>
            """
        )
    st.markdown(
        f"<div class='storyboard-grid'>{''.join(storyboard_cards)}</div>",
        unsafe_allow_html=True,
    )

    for row in ml_roadmap.itertuples(index=False):
        with st.container(border=True):
            top_cols = st.columns([1.4, 1])
            with top_cols[0]:
                st.subheader(row.title)
                st.write(row.one_liner)
            with top_cols[1]:
                st.markdown(f"**Bottleneck:** {row.bottleneck}")
            render_node_movement(pd.Series(row._asdict()), title="Artifact movement")
            render_future_timeline(pd.Series(row._asdict()))
            st.markdown(f"**Why it matters:** {row.why_important}")

    st.subheader("Neo4j versus Gephi")
    compare_cols = st.columns(2)
    with compare_cols[0]:
        st.markdown(
            """
<div class="compare-panel">
  <h4>Neo4j</h4>
  <p><strong>Best for:</strong> queryable graph databases, repeatable pipelines, Cypher queries, app integration, and graph data science.</p>
  <p><strong>Why it changes the REE project:</strong> the node/edge spreadsheet can become a living database where each relationship has evidence, source links, weights, and model-ready features.</p>
  <p><strong>Tradeoff:</strong> more setup and schema discipline than a desktop visualization tool.</p>
</div>
            """,
            unsafe_allow_html=True,
        )
    with compare_cols[1]:
        st.markdown(
            """
<div class="compare-panel">
  <h4>Gephi</h4>
  <p><strong>Best for:</strong> visual exploration, graph layout, community detection demos, posters, and communication graphics.</p>
  <p><strong>Why it was useful here:</strong> it made the REE structure visible after the AI-assisted spreadsheet step, especially for explaining deposits, minerals, and host contexts.</p>
  <p><strong>Tradeoff:</strong> it is not the strongest place to maintain a growing queryable research database.</p>
</div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("The expert-review loop")
    st.markdown(
        """
1. Capture files, screenshots, notebooks, and source tables.
2. Ask AI to propose structure, but keep expert review visible.
3. Convert the approved structure into rows, graphs, features, or demonstrations.
4. Use ML only after the inputs, labels, uncertainty, and validation target are clear.
        """
    )


elif section == "Case Studies":
    st.title("Case Studies")
    st.write("Curated project threads that can become website sections or PowerPoint chapters.")

    filter_cols = st.columns([1, 1, 2])
    status_options = ["All"] + sorted(case_studies["status"].dropna().unique().tolist())
    format_options = ["All"] + sorted(case_studies["format"].dropna().unique().tolist())
    selected_status = filter_cols[0].selectbox("Status", status_options)
    selected_format = filter_cols[1].selectbox("Format", format_options)
    project_search = filter_cols[2].text_input("Search projects", "")

    shown_cases = case_studies.copy()
    if selected_status != "All":
        shown_cases = shown_cases[shown_cases["status"] == selected_status]
    if selected_format != "All":
        shown_cases = shown_cases[shown_cases["format"] == selected_format]
    if project_search:
        needle = project_search.lower()
        haystack = (
            shown_cases["title"].fillna("")
            + " "
            + shown_cases["summary"].fillna("")
            + " "
            + shown_cases["proof"].fillna("")
            + " "
            + shown_cases["format"].fillna("")
        ).str.lower()
        shown_cases = shown_cases[haystack.str.contains(needle, regex=False)]

    st.caption(f"{len(shown_cases)} projects shown from {len(case_studies)} curated candidates")

    for row in shown_cases.itertuples(index=False):
        with st.container(border=True):
            top = st.columns([2.2, 1])
            visual_matches = project_visuals[
                project_visuals["project_key"].fillna("") == row.key
            ].sort_values("sort_order")
            with top[0]:
                st.subheader(row.title)
                st.write(row.summary)
                st.markdown(f"**AI use:** {row.ai_use}")
                st.markdown(f"**Best proof:** {row.proof}")
            with top[1]:
                if not visual_matches.empty:
                    lead_visual = visual_matches.iloc[0]
                    lead_path = project_asset(lead_visual["asset_path"])
                    if lead_path.exists():
                        st.image(
                            str(lead_path),
                            caption=lead_visual["title"],
                            use_container_width=True,
                        )
                st.markdown(f"**Status:** {row.status}")
                st.markdown(f"**Primary format:** {row.format}")
                if valid_text(row.local_path):
                    st.link_button("Open local source", local_file_uri(row.local_path))
                if valid_text(row.drive_url):
                    st.link_button("Open Drive link", row.drive_url)
            st.markdown(f"<p class='small-note'>{row.next_step}</p>", unsafe_allow_html=True)


elif section == "LinkedIn Evidence":
    st.title("LinkedIn Evidence")
    st.write(
        "LinkedIn is useful here as a public-facing trail of project work. "
        "This page connects visible profile/activity signals to the local videos, decks, screenshots, and code files that can power the website."
    )

    linked_cols = st.columns(4)
    linked_cols[0].metric("Evidence items", len(linkedin_evidence))
    linked_cols[1].metric(
        "Video-linked items",
        int(linkedin_evidence["category"].fillna("").str.contains("video", regex=False).sum()),
    )
    linked_cols[2].metric(
        "High priority",
        int((linkedin_evidence["priority"] == "high").sum()),
    )
    linked_cols[3].metric(
        "Local files found",
        int(linkedin_evidence["local_path"].fillna("").map(lambda value: existing_path(value) is not None).sum()),
    )

    st.subheader("Embedded local videos")
    video_rows = linkedin_evidence[linkedin_evidence["category"] == "video"]
    video_cols = st.columns(2)
    for idx, video in enumerate(video_rows.itertuples(index=False)):
        with video_cols[idx % 2]:
            video_path = existing_path(video.local_path)
            with st.container(border=True):
                st.markdown(f"**{video.title}**")
                st.write(video.linkedin_signal)
                if video_path is not None:
                    st.video(str(video_path))
                    st.caption(f"Embedded from organized local file: {video_path.name}")
                else:
                    st.warning("Organized local video file not found.")

    st.subheader("Organized project folders")
    folder_cols = st.columns(2)
    for idx, folder in enumerate(organized_folders.itertuples(index=False)):
        with folder_cols[idx % 2]:
            folder_path = Path(folder.folder)
            with st.container(border=True):
                st.markdown(f"**{folder.title}**")
                st.write(folder.contents)
                if folder_path.exists():
                    st.link_button("Open folder", local_file_uri(str(folder_path)))
                else:
                    st.warning("Folder not found.")

    st.subheader("Profile signals")
    profile_cols = st.columns(2)
    with profile_cols[0]:
        st.markdown("**Positioning**")
        st.write(
            "M.S. Geosciences, Geospatial AI, machine learning for energy and subsurface systems."
        )
    with profile_cols[1]:
        st.markdown("**Handshake AI workflow proof**")
        st.write(
            "QGIS, ParaView, Vagon screen recordings, AI task evaluation, rubric checking, and geospatial data workflow completion."
        )

    st.subheader("The supervised-AI question")
    st.write(
        "A useful way to present the Handshake work is as supervised machine-learning infrastructure: "
        "humans record realistic technical workflows, evaluate whether model outputs follow instructions, "
        "and create the examples that future AI systems may learn from. The open question for scientific "
        "software is not whether AI replaces expertise immediately; it is how much structured expert behavior "
        "must be captured before agents can handle GIS, visualization, and data-preparation tasks more independently."
    )

    category_options = ["All"] + sorted(linkedin_evidence["category"].dropna().unique().tolist())
    selected_linkedin_category = st.selectbox("Evidence type", category_options)
    linkedin_display = linkedin_evidence.copy()
    if selected_linkedin_category != "All":
        linkedin_display = linkedin_display[linkedin_display["category"] == selected_linkedin_category]

    st.dataframe(
        linkedin_display[
            ["title", "category", "project_key", "linkedin_signal", "priority", "local_path"]
        ],
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Preview evidence")
    selected_evidence_title = st.selectbox("Item", linkedin_evidence["title"].tolist())
    selected_evidence = linkedin_evidence[linkedin_evidence["title"] == selected_evidence_title].iloc[0]
    selected_path = existing_path(selected_evidence["local_path"])

    preview_cols = st.columns([1.3, 1])
    with preview_cols[0]:
        st.markdown(f"**{selected_evidence['title']}**")
        st.write(selected_evidence["linkedin_signal"])
        st.markdown(f"**Website use:** {selected_evidence['site_use']}")
        if valid_text(selected_evidence["linkedin_url"]):
            st.link_button("Open LinkedIn source", selected_evidence["linkedin_url"])
        if selected_path is not None:
            st.link_button("Open local source", local_file_uri(str(selected_path)))
            st.link_button("Open organized folder", local_file_uri(str(selected_path.parent)))
        else:
            st.warning("Local file not found on disk.")
    with preview_cols[1]:
        if selected_path is not None:
            suffix = selected_path.suffix.lower()
            if suffix in {".png", ".jpg", ".jpeg", ".webp"}:
                st.image(str(selected_path), caption=selected_path.name, use_container_width=True)
            elif suffix in {".mp4", ".mov", ".m4v"}:
                st.video(str(selected_path))
            elif suffix in {".pde", ".py", ".js", ".java"}:
                code_text = selected_path.read_text(errors="ignore")
                st.code("\n".join(code_text.splitlines()[:120]), language="java")
            else:
                st.info(f"{selected_path.suffix.upper().lstrip('.')} files open from the local source button.")


elif section == "Code And Architecture":
    st.title("Code And Architecture")
    st.write(
        "These excerpts are not meant to be the full codebase. They are quick proof "
        "of what each workflow actually does."
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Pondicherry Seismic",
            "North Slope Atlas",
            "Stock Dashboard",
            "Source To Paper",
        ]
    )

    with tab1:
        st.subheader("Earthquake catalog to velocity analysis")
        st.write(
            "This notebook searches IRIS/USGS events, downloads waveform traces with ObsPy, "
            "picks arrivals, computes distances, and estimates P-wave velocity."
        )
        st.code(CODE_SNIPPETS["pondicherry"], language="python")
        row = source_row("Pondicherry earthquake velocity notebook")
        if row is not None:
            st.link_button("Open notebook", local_file_uri(row["source_path"]))

    with tab2:
        st.subheader("GIS layers to public Streamlit atlas")
        st.write(
            "The North Slope app turns cleaned public geospatial layers and exported Plotly "
            "scenes into an atlas, structural explorer, data library, and research framework."
        )
        st.code(CODE_SNIPPETS["north_slope"], language="python")
        row = source_row("North Slope gas hydrate dashboard")
        if row is not None:
            st.link_button("Open project folder", local_file_uri(row["source_path"]))

    with tab3:
        st.subheader("Automated stock research dashboard")
        st.write(
            "The stock dashboard reads compact pipeline outputs, checks freshness, "
            "shows shortlist/watchlist results, and exposes model lab diagnostics."
        )
        st.code(CODE_SNIPPETS["stock"], language="python")
        row = source_row("Stock research dashboard")
        if row is not None:
            st.link_button("Open project folder", local_file_uri(row["source_path"]))

    with tab4:
        st.subheader("AI-assisted research synthesis")
        st.write(
            "This is the architecture behind the paper/deck workflow: prompts and notes become "
            "source libraries, then notebooks and dashboards, then manuscript and slides."
        )
        st.code(CODE_SNIPPETS["source_workflow"], language="text")
        row = source_row("Source library index")
        if row is not None:
            st.link_button("Open source library index", local_file_uri(row["source_path"]))


elif section == "Notebook Explorer":
    st.title("Notebook Explorer")
    st.write(
        "This scans notebook source, markdown, text outputs, filenames, and imports while "
        "skipping embedded image blobs. Tags are heuristic, but useful for fast discovery."
    )

    all_tags = sorted(
        {
            tag
            for tags in notebook_inventory["tags"].fillna("")
            for tag in [part.strip() for part in tags.split(";")]
            if tag
        }
    )
    tag_counts = {
        tag: int(notebook_inventory["tags"].fillna("").str.contains(tag, regex=False).sum())
        for tag in all_tags
    }
    metric_cols = st.columns(4)
    for idx, tag in enumerate(["earthquake/seismic", "gis/geospatial", "climate", "stocks/finance"]):
        metric_cols[idx].metric(tag, tag_counts.get(tag, 0))

    filters = st.columns([1, 2])
    selected_tag = filters[0].selectbox("Tag", ["All"] + all_tags)
    search_text = filters[1].text_input("Search titles, paths, imports", "")

    filtered = notebook_inventory.copy()
    if selected_tag != "All":
        filtered = filtered[filtered["tags"].fillna("").str.contains(selected_tag, regex=False)]
    if search_text:
        needle = search_text.lower()
        haystack = (
            filtered["title"].fillna("")
            + " "
            + filtered["path"].fillna("")
            + " "
            + filtered["imports"].fillna("")
            + " "
            + filtered["tags"].fillna("")
        ).str.lower()
        filtered = filtered[haystack.str.contains(needle, regex=False)]

    st.caption(f"{len(filtered)} notebooks shown")
    st.dataframe(
        filtered[
            [
                "title",
                "tags",
                "modified",
                "code_cells",
                "markdown_cells",
                "imports",
                "path",
                "size_mb",
            ]
        ],
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Strong notebook links")
    strong_notebooks = [
        "C:\\Users\\gargi\\Downloads\\VelocityAnalysisPalkStraight.ipynb",
        "C:\\Users\\gargi\\Downloads\\Seismic Constraints on Aquifer Potential in Under-Monitored Crystalline Terrains of Pondicherry, India (1).ipynb",
        "C:\\Users\\gargi\\Documents\\Next level productivity\\Gas hydrates unclassified info\\north-slope-gas-hydrates\\Master.ipynb",
        "C:\\Users\\gargi\\Documents\\Next level productivity\\Gas hydrates unclassified info\\north-slope-gas-hydrates\\02_visualization\\North Slope Data Layer Map.ipynb",
        "C:\\Users\\gargi\\Downloads\\1_intro_specfem2d.ipynb",
    ]
    cols = st.columns(2)
    for idx, path in enumerate(strong_notebooks):
        with cols[idx % 2]:
            st.link_button(Path(path).name, local_file_uri(path))


elif section == "Evidence Library":
    st.title("Evidence Library")
    tab1, tab2 = st.tabs(["Local Sources", "Google Drive"])

    with tab1:
        categories = ["All"] + sorted(inventory["category"].unique().tolist())
        selected = st.selectbox("Local category", categories)
        display = inventory if selected == "All" else inventory[inventory["category"] == selected]
        st.dataframe(display, hide_index=True, use_container_width=True)

    with tab2:
        drive_categories = ["All"] + sorted(drive_inventory["category"].unique().tolist())
        drive_selected = st.selectbox("Drive category", drive_categories)
        drive_display = (
            drive_inventory
            if drive_selected == "All"
            else drive_inventory[drive_inventory["category"] == drive_selected]
        )
        st.dataframe(
            drive_display,
            hide_index=True,
            use_container_width=True,
            column_config={"url": st.column_config.LinkColumn("url")},
        )


elif section == "Visual Gallery":
    st.title("Visual Gallery")
    st.write(
        "Selected screenshots and code outputs are now tied directly to projects. "
        "This gives the website a visual proof layer instead of only file links."
    )

    chart_cols = st.columns(3)
    with chart_cols[0]:
        st.subheader("Projects by format")
        format_counts = case_studies["format"].value_counts().rename_axis("format").reset_index(name="count")
        st.bar_chart(format_counts, x="format", y="count", use_container_width=True)
    with chart_cols[1]:
        st.subheader("Visuals by type")
        visual_counts = project_visuals["visual_type"].value_counts().rename_axis("type").reset_index(name="count")
        st.bar_chart(visual_counts, x="type", y="count", use_container_width=True)
    with chart_cols[2]:
        st.subheader("Notebook tags")
        tag_rows = []
        for tags in notebook_inventory["tags"].fillna(""):
            tag_rows.extend([tag.strip() for tag in tags.split(";") if tag.strip()])
        tag_counts = pd.Series(tag_rows).value_counts().head(8).rename_axis("tag").reset_index(name="count")
        st.bar_chart(tag_counts, x="tag", y="count", use_container_width=True)

    st.divider()

    visual_counts_by_project = (
        project_visuals.groupby("project_key")
        .size()
        .rename("visual_count")
        .reset_index()
    )
    evidence_matrix = case_studies[["key", "title", "status", "format", "local_path", "drive_url"]].merge(
        visual_counts_by_project,
        left_on="key",
        right_on="project_key",
        how="left",
    )
    evidence_matrix["visual_count"] = evidence_matrix["visual_count"].fillna(0).astype(int)
    evidence_matrix["local_source"] = evidence_matrix["local_path"].fillna("").str.len() > 0
    evidence_matrix["drive_link"] = evidence_matrix["drive_url"].fillna("").str.len() > 0

    st.subheader("Evidence matrix")
    st.dataframe(
        evidence_matrix[
            ["title", "status", "format", "visual_count", "local_source", "drive_link"]
        ],
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Project visuals")
    project_options = case_studies["title"].tolist()
    selected_title = st.selectbox("Project", project_options)
    selected_case = case_studies[case_studies["title"] == selected_title].iloc[0]
    selected_visuals = project_visuals[
        project_visuals["project_key"].fillna("") == selected_case["key"]
    ].sort_values("sort_order")

    if selected_visuals.empty:
        st.info("No individual visual has been selected for this project yet. Use the contact sheets below to pick one.")
    else:
        gallery_cols = st.columns(2)
        for idx, visual in enumerate(selected_visuals.itertuples(index=False)):
            with gallery_cols[idx % 2]:
                asset_path = project_asset(visual.asset_path)
                with st.container(border=True):
                    st.markdown(f"**{visual.title}**")
                    st.caption(visual.visual_type)
                    if asset_path.exists():
                        st.image(str(asset_path), caption=visual.caption, use_container_width=True)
                    else:
                        st.warning(f"Missing copied asset: {asset_path}")
                    if valid_text(visual.source_path):
                        st.link_button("Open original source", local_file_uri(visual.source_path))

    with st.expander("Review original contact sheets"):
        selected_sheet = st.selectbox("Contact sheet", [path.name for path in CONTACT_SHEETS])
        image_path = next(path for path in CONTACT_SHEETS if path.name == selected_sheet)
        if image_path.exists():
            st.image(str(image_path), caption=image_path.name, use_container_width=True)
        else:
            st.warning(f"Missing copied contact sheet: {image_path}")


elif section == "Build Plan":
    st.title("Build Plan")
    st.subheader("Next clean-up pass")
    st.markdown(
        """
1. Pick the best 12 to 20 individual screenshots from the contact sheets.
2. Add one architecture diagram for ChatGPT, Obsidian, sources, notebooks, QGIS, Streamlit, and PowerPoint.
3. Convert the Pondicherry earthquake notebook into a clearer case-study panel.
4. Capture current screenshots from the two Streamlit apps.
5. Decide whether to generate a PowerPoint from the same case-study data.
        """
    )

    st.subheader("PowerPoint-ready sections")
    st.markdown(
        """
- AI as a Research Operating System
- Workflow Loop: prompts, notes, sources, code, maps, dashboards, papers
- Case Study: Pondicherry earthquake velocity notebook
- Case Study: North Slope gas hydrate atlas
- Case Study: Stock research dashboard
- Research Writing: source library to manuscript to deck
- Impact: faster synthesis, better evidence reuse, more actionable insight
        """
    )
