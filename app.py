from pathlib import Path
from html import escape
from urllib.parse import quote
import base64
from datetime import datetime, timezone
from io import BytesIO
import json
import zipfile

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components


ROOT = Path(__file__).resolve().parent
DEPLOY_BUILD_ID = "2026-06-11 / graph-ml-visuals-pass"
INVENTORY_PATH = ROOT / "data" / "source_inventory.csv"
DRIVE_INVENTORY_PATH = ROOT / "data" / "google_drive_inventory.csv"
NOTEBOOK_INVENTORY_PATH = ROOT / "data" / "notebook_inventory.csv"
CASE_STUDY_PATH = ROOT / "data" / "case_studies.csv"
PROJECT_VISUALS_PATH = ROOT / "data" / "project_visuals.csv"
LINKEDIN_EVIDENCE_PATH = ROOT / "data" / "linkedin_evidence.csv"
ORGANIZED_FOLDERS_PATH = ROOT / "data" / "organized_project_folders.csv"
ML_ROADMAP_PATH = ROOT / "data" / "ml_future_roadmap.csv"
ML_DIAGRAM_TRACKER_PATH = ROOT / "data" / "ml_diagram_tracker.csv"
PROJECT_STATUS_PATH = ROOT / "data" / "project_status.csv"
VISUAL_AUDIT_PATH = ROOT / "data" / "visual_audit.csv"
VISION_BOARD_PATH = ROOT / "data" / "vision_board.csv"
WEBSITE_CHANGE_IDEAS_PATH = ROOT / "data" / "website_change_ideas.csv"
DRIVE_SLIDE_SOURCES_PATH = ROOT / "data" / "drive_slide_sources.csv"
DOWNLOAD_PACKAGE_PATH = ROOT / "deliverables" / "ai_powerpoint_streamlit_site_package.zip"
VISUAL_DESIGN_SPEC_PATH = ROOT / "docs" / "VISUAL_DESIGN_SPEC.md"
ARCHITECTURE_PATH = ROOT / "docs" / "ARCHITECTURE.md"
STRUCTURAL_DATA_DIR = ROOT / "assets" / "structural_data"
MASTER_3D_PATH = STRUCTURAL_DATA_DIR / "north_slope_master_3d_surfaces.parquet"
MASTER_2D_PATH = STRUCTURAL_DATA_DIR / "north_slope_master_2d_layers.parquet"
USGS_GLOBE_VIDEO_PATH = ROOT / "assets" / "videos" / "usgs_3d_globe_video.mp4"
USGS_GLOBE_DRIVE_URL = "https://drive.google.com/file/d/1sV8QsgJNknjSCsGZwktc_7LtWSHdrGfZ/view"
NORTH_SLOPE_APP_URL = "https://north-slope-gas-hydrates-vj67xkke9ksfzveon8ldt2.streamlit.app/"
NORTH_SLOPE_WELL_SCAFFOLD_URL = (
    NORTH_SLOPE_APP_URL + "?page=Future%20Well-Log%20Engine"
)
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

NEXT_REVIEW_QUESTIONS = [
    "Which three project images should be the first things a visitor sees?",
    "For each project card, what AI opinion do you most want visitors to debate?",
    "Which current destination still feels redundant or unclear in the new navigator?",
    "Which workflow should receive the first real Processing-style animation?",
    "For QGIS agent training, what exact task should become the first input-actions-output-rubric example?",
    "For the North Slope project, should the main product story emphasize 3D visualization, hydrate screening, or public-data organization?",
    "Which technical details should stay visible by default, and which should move behind an expander?",
    "What concrete output from the ML interview matters most: a model architecture, a product idea, a validation method, or a data pipeline?",
]

TOPIC_ROOMS = [
    {
        "slug": "ai_workflow",
        "title": "How AI Agents Learn Scientific Software",
        "tagline": "How screenshots, task recordings, and rubric checks become supervised examples for future scientific software agents.",
        "project_key": "arcgis_raster_ml",
        "hero": "assets/topic_visuals/agent_training.svg",
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
        "title": "AI + Knowledge Graphs For Critical Minerals",
        "tagline": "Mountain Pass and Bayan Obo framed through graph data, Gephi exports, and a narrated research video.",
        "project_key": "thesis_knowledge_graph",
        "hero": "assets/project_visuals/ree_bayan_obo_main.png",
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
        "title": "AI For Energy Screening Workflows",
        "tagline": "A GIS and source-library workflow for turning public geoscience material into a dashboard and ML planning scaffold.",
        "project_key": "north_slope",
        "hero": "assets/project_visuals/north_slope_alaska_geology_well_map.png",
        "theme": "Public sources + GIS layers + Streamlit atlas + hydrate ML planning.",
        "bottleneck": "Subsurface energy projects often have fragmented public data: maps, papers, well-log concepts, stratigraphy, and ML ideas are spread across many formats.",
        "why_not_done": "Integrating geologic context with machine-learning-ready features is slow because provenance, scale, coordinate systems, and domain assumptions have to be reconciled before modeling.",
        "ai_used": "AI helped organize public Alaska geology sources, GIS shapefiles, gas-hydrate/wireline ideas, Open Science Lab/GitHub workflow pieces, and Streamlit/Plotly structure. The useful part was not that AI knew the answer; it helped make a big messy energy-data idea easier to move around.",
        "future_ai": "Next implementation should connect public data pulls, shapefiles, wells, cross sections, geologic labels, wireline variables, and hydrate indicators into a feature table that can support expert-reviewed screening instead of just a pretty map.",
        "why_it_matters": "For DOE and industry, the money and public-value question is direct: can AI/ML make energy screening faster, cheaper, clearer, and more useful for deciding where to investigate next?",
        "proof": ["North Slope map", "Wireline ML scaffold deck", "Gas hydrate source library", "Streamlit app structure"],
        "question": "What feature table would an expert trust for hydrate interval screening and uncertainty ranking?",
    },
    {
        "slug": "rock_classification",
        "title": "AI For Visual Geoscience Classification",
        "tagline": "Chemical classification visuals, thin-section decks, formation tables, and graph outputs as future ML training material.",
        "project_key": "rock_classification",
        "hero": "assets/project_visuals/rock_classification_slides/rock_raster_classification_map.png",
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
    {
        "slug": "near_surface",
        "title": "AI For Near-Surface Geophysics",
        "tagline": "A Valles fen investigation topic built from the Near-Surface Dwellers deck: hammer seismic, transient EM, ERT, geologic units, and line intersections.",
        "project_key": "near_surface_geophysics",
        "hero": "assets/topic_visuals/near_surface_ai.svg",
        "theme": "Hammer seismic + ERT/TEM + geologic units + field interpretation.",
        "bottleneck": "Near-surface field surveys produce overlapping but imperfect views of shallow geology, and the hard part is aligning lines, units, method limits, and field context.",
        "why_not_done": "The measurements exist, but turning them into one defensible interpretation is slow because line intersections, method sensitivity, uncertainty, and geologic labels have to be reconciled.",
        "ai_used": "AI can help organize deck evidence, compare survey lines, label possible units, and keep method-specific uncertainty visible instead of collapsing everything into one clean answer.",
        "future_ai": "A stronger version would let users toggle hammer seismic, ERT, TEM, mapped units, and confidence bands, then ask AI to explain where methods agree or conflict.",
        "why_it_matters": "This topic turns the Valles field evidence into a concrete AI question: how should models support shallow-subsurface interpretation without overwriting field judgment?",
        "proof": ["Near-Surface Dwellers deck", "Valles fen context", "Hammer seismic", "Transient EM", "ERT / seismic line intersection"],
        "question": "Can AI compare shallow geophysical methods while preserving disagreement between survey types?",
    },
    {
        "slug": "moho_ml",
        "title": "Supervised ML For Moho Depth Mapping",
        "tagline": "A real class project example: train on gravity/Moho relationships in Australia, then test whether the learned pattern transfers to the USA.",
        "project_key": "moho_ml",
        "hero": "assets/project_visuals/valles_moho.png",
        "theme": "Supervised ML + gravity variables + transfer testing + geoscience validation.",
        "bottleneck": "Geophysical ML can look impressive when tested on familiar data, but the real question is whether a model transfers to a new region without fooling itself.",
        "why_not_done": "Good models need clean variables, honest train/test boundaries, uncertainty, and domain review. Otherwise a high score can hide leakage or a biased evaluation.",
        "ai_used": "This project predates the current Codex workflow, but it is the clearest example of actual supervised ML: gravity/Moho inputs in Australia, an ANN-style model, and transfer to U.S. Moho depth mapping.",
        "future_ai": "A current version would use Codex to recover the notebook, document variables, compare model families, check leakage, visualize residuals, and turn the workflow into a reproducible geoscience ML demo.",
        "why_it_matters": "This is the bridge between prompting and real ML: AI can help organize the workflow, but the model still needs honest data splits, geoscience reasoning, and transfer tests.",
        "proof": ["aus.moho.ipynb", "australian.moho", "australian.py", "machinelearningreport.docx"],
        "question": "How do we know a geoscience ML model learned a transferable pattern instead of memorizing one region?",
    },
    {
        "slug": "ambient_noise",
        "title": "AI For Ambient-Noise Seismology",
        "tagline": "NoisePy and ambient-noise workflows as a topic about turning continuous station noise into cross-correlations, stacks, monitoring, and scalable QA.",
        "project_key": "ambient_noise",
        "hero": "assets/topic_visuals/ambient_noise_processing.svg",
        "theme": "Continuous records + station pairs + cross-correlation + stacking + monitoring.",
        "bottleneck": "Ambient-noise workflows can create huge numbers of station pairs, files, cross-correlations, and stacks before anyone knows which outputs are physically useful.",
        "why_not_done": "The workflow is computationally heavy and quality-sensitive: windowing, preprocessing, CCF generation, stacking, plotting, and station metadata all need review.",
        "ai_used": "AI can help explain NoisePy steps, organize station-pair outputs, flag weak correlations, and summarize compute/QA logs for human review.",
        "future_ai": "A future workflow could use AI-assisted QC to triage station pairs, detect unstable stacks, document parameter choices, and make monitoring changes easier to audit.",
        "why_it_matters": "This gives the seismic section a software-scale example: AI is not just interpreting one trace, it can help manage continuous data pipelines.",
        "proof": ["NoisePy deck", "Ambient Noise Seismology", "station windows", "cross-correlations", "stacking and monitoring"],
        "question": "How should AI decide which ambient-noise correlations are trustworthy enough to monitor?",
    },
    {
        "slug": "stock_workflow",
        "title": "AI App Building, Automation, And Model Risk",
        "tagline": "How Codex-style tools can turn messy local files into tracked apps while keeping testing, leakage, and decision risk visible.",
        "project_key": "stock_dashboard",
        "hero": "assets/project_visuals/stock_all_tickers_chart.svg",
        "theme": "Codex + local files + GitHub + Streamlit + model-evaluation honesty.",
        "bottleneck": "People can build useful tools faster now, but AI can also make confident mistakes unless the user understands testing, leakage, and what the model is allowed to know.",
        "why_not_done": "Before Codex, building an app from notebook screenshots meant repetitive copying, local debugging, and scattered files. The new workflow can organize existing work, track changes, and push more of the build into GitHub/cloud-style systems.",
        "ai_used": "Codex organized local downloads, inspected existing notebook/app outputs, built Streamlit structure, helped debug charts, and made the workflow feel less like copy-paste and more like a system.",
        "future_ai": "A future version would separate training and unseen evaluation data, keep GitHub-tracked pipelines, automate refreshes, and use cloud/virtual desktop workflows so local storage and CPU are less of a bottleneck.",
        "why_it_matters": "This opens a bigger discussion: practical AI skills now include building apps, automating pipelines, reading model outputs critically, and knowing when a prediction workflow is not trustworthy yet.",
        "proof": ["stockprediction2025 dashboard", "GitHub Actions pipeline", "Streamlit charts", "model-baseline notes"],
        "question": "How can Codex-style tools help people build real apps without hiding model risk or data leakage?",
    },
    {
        "slug": "sem_petrography",
        "title": "AI For SEM Petrography And Climate Proxies",
        "tagline": "SEM petrography slides reframed as a topic about mineral texture labels, detrital/authigenic interpretation, kaolinite morphology, and paleoclimate signals.",
        "project_key": "sem_petrography",
        "hero": "assets/topic_visuals/sem_petrography_ai.svg",
        "theme": "SEM images + clay minerals + morphology labels + environmental interpretation.",
        "bottleneck": "SEM petrography can show tiny mineral textures, but turning those textures into climate or reservoir claims requires careful label definitions and expert review.",
        "why_not_done": "Image interpretation is not enough: detrital versus authigenic context, kaolinite form, weathering history, and literature support must be connected.",
        "ai_used": "AI can help organize SEM slide evidence, propose visual labels, compare morphology categories, and separate observation from interpretation.",
        "future_ai": "A future version could pair SEM crops, mineral labels, literature claims, and expert decisions into a multimodal training set for petrographic interpretation.",
        "why_it_matters": "This is a stronger AI topic than a generic rock card because it asks how image models can help with microscopic evidence while preserving geologic reasoning.",
        "proof": ["SEM Petrography deck", "carbonates/evaporites/clays", "detrital vs authigenic examples", "kaolinite morphology", "paleoclimate proxy reasoning"],
        "question": "Can AI label SEM textures without confusing observation, interpretation, and climate proxy claims?",
    },
]

MOBILE_TOPIC_SLUGS = [
    "ai_workflow",
    "thesis_graph",
    "processing_earthquake",
    "north_slope",
    "seismic",
    "near_surface",
    "rock_classification",
]

STRUCTURAL_HORIZONS = ["NStopo", "NSLCU", "NSshublik", "NSbasement"]
STRUCTURAL_OVERLAYS = [
    "North Slope study-area boundary",
    "Assessment-unit outlines",
    "North Slope public wells",
]
SURFACE_CATALOG = {
    "NStopo": {
        "label": "Topographic reference",
        "description": "Near-surface reference used to orient the structural stack.",
        "color": "#4daf4a",
    },
    "NSLCU": {
        "label": "Lower Cretaceous unconformity",
        "description": "Regional unconformity used as a subsurface structural reference.",
        "color": "#377eb8",
    },
    "NSshublik": {
        "label": "Shublik surface",
        "description": "Deeper regional horizon used for petroleum-system context.",
        "color": "#ff7f00",
    },
    "NSbasement": {
        "label": "Basement surface",
        "description": "Deep structural reference showing regional basin geometry.",
        "color": "#984ea3",
    },
}

TOPIC_FRAMES = {
    "ai_workflow": {
        "question": "Will Codex replace screenshots, or will screenshots teach the next agents?",
        "example": "Handshake/QGIS/Vagon work is the example.",
        "raise": "Raise your hand if you want to talk about how AI is being trained to do technical grunt work.",
        "pattern": ["prompt", "screen", "rubric", "agent"],
    },
    "thesis_graph": {
        "question": "Can a knowledge graph help AI move from organizing research to finding better questions?",
        "example": "REE, Bayan Obo, Mountain Pass, Adobe drawings, CSV nodes, and Gephi are the example.",
        "raise": "Raise your hand if you want to talk about why graph workflows can beat flat tables for messy science.",
        "pattern": ["prompt", "drawing", "csv", "graph"],
    },
    "processing_earthquake": {
        "question": "Can AI make geoscience data something people can see, hear, and discuss?",
        "example": "The Processing earthquake globe is the origin-story example.",
        "raise": "Raise your hand if you want to talk about creative visualization before everything became dashboards.",
        "pattern": ["data", "globe", "sound", "web"],
    },
    "seismic": {
        "question": "What parts of seismic processing should AI simplify first?",
        "example": "Pondicherry notebooks and 2D seismic visuals are the example.",
        "raise": "Raise your hand if you want to talk about waveform QA, picking, or fast interpretation.",
        "pattern": ["wave", "pick", "qa", "map"],
    },
    "north_slope": {
        "question": "Can AI turn public geology into a useful 3D subsurface map?",
        "example": "The Alaska North Slope hydrate atlas is the example.",
        "raise": "Raise your hand to talk about AI-built 3D maps, hydrate screening, and what geoscientists still must validate.",
        "pattern": ["open data", "GIS", "3D map", "screen"],
    },
    "rock_classification": {
        "question": "Could AI turn rock properties and instrument surveys into resource maps?",
        "example": "Rock classification grids, geochemistry ranges, ArcGIS, and formation labels are the example.",
        "raise": "Raise your hand if you want to talk about instrument properties becoming rock properties.",
        "pattern": ["ranges", "grid", "overlay", "3D"],
    },
    "valles": {
        "question": "How should AI compare imperfect geophysical surveys without flattening uncertainty?",
        "example": "SAGE/Valles maps are the field-geophysics example.",
        "raise": "Raise your hand if you want to talk about field data, uncertainty, and map fusion.",
        "pattern": ["field", "gravity", "EM", "review"],
    },
    "near_surface": {
        "question": "Can AI compare shallow geophysical methods without erasing disagreement?",
        "example": "The Near-Surface Dwellers Valles fen deck is the example.",
        "raise": "AI advance: line intersections, ERT, TEM, seismic, and geologic units become one review board.",
        "pattern": ["fen", "seismic", "ERT", "TEM"],
    },
    "moho_ml": {
        "question": "Did it transfer or memorize?",
        "example": "The Australia-to-USA gravity/Moho supervised ML project is the example.",
        "raise": "Raise your hand if you want to talk about leakage, transfer tests, and honest model scoring.",
        "pattern": ["train", "test", "transfer", "residual"],
    },
    "ambient_noise": {
        "question": "Which ambient-noise correlations are real enough to monitor?",
        "example": "The NoisePy ambient-noise deck is the example.",
        "raise": "AI advance: continuous noise becomes station-pair stacks with compute logs and QC gates.",
        "pattern": ["noise", "CCF", "stack", "QC"],
    },
    "stock_workflow": {
        "question": "How should AI help people build apps without hiding model risk?",
        "example": "The stock dashboard and GitHub/cloud workflow are only the example.",
        "raise": "AI advance: local files become a tracked app, then a validation gate blocks weak predictions.",
        "pattern": ["files", "Codex", "pipeline", "risk"],
    },
    "sem_petrography": {
        "question": "Can AI label SEM textures without overclaiming climate meaning?",
        "example": "The SEM petrography deck is the example.",
        "raise": "AI advance: microscope textures become reviewed labels, not automatic conclusions.",
        "pattern": ["SEM", "clay", "label", "review"],
    },
}

TOPIC_AI_LEVERS = {
    "ai_workflow": "AI use: demonstrations become action traces, rubrics, and agent training examples.",
    "thesis_graph": "AI use: notes and drawings become graph structure that experts can query and correct.",
    "processing_earthquake": "AI use: creative code turns raw events into visible, audible patterns.",
    "seismic": "AI use: notebooks become repeatable waveform QA, picking, and uncertainty workflows.",
    "north_slope": "AI use: public geology is organized into screening features and expert-review gates.",
    "rock_classification": "AI use: images, chemistry, and maps become labeled multimodal training evidence.",
    "valles": "AI use: imperfect survey layers are compared without erasing uncertainty.",
    "near_surface": "AI use: shallow seismic, ERT, TEM, and unit labels become a reviewable field board.",
    "moho_ml": "AI use: models are judged by transfer, residuals, and leakage checks.",
    "ambient_noise": "AI use: station-pair noise processing gets QC, compute tracking, and monitoring summaries.",
    "stock_workflow": "AI use: messy files become a cloud-ready app pipeline with honest testing.",
    "sem_petrography": "AI use: SEM textures become expert-reviewed mineral and proxy labels.",
}

TOPIC_VISUALS = {
    "ai_workflow": "assets/topic_visuals/agent_training_trace.svg",
    "thesis_graph": "assets/topic_visuals/knowledge_graph.svg",
    "processing_earthquake": "assets/topic_visuals/earthquake_globe_signal.svg",
    "seismic": "assets/topic_visuals/seismic_processing.svg",
    "north_slope": "assets/topic_visuals/north_slope_decision_space.svg",
    "rock_classification": "assets/topic_visuals/rock_resource_map.svg",
    "valles": "assets/topic_visuals/field_geophysics.svg",
    "near_surface": "assets/topic_visuals/near_surface_ai.svg",
    "moho_ml": "assets/topic_visuals/gis_moho_deck_trace.svg",
    "ambient_noise": "assets/topic_visuals/ambient_noise_processing.svg",
    "stock_workflow": "assets/topic_visuals/app_pipeline.svg",
    "sem_petrography": "assets/topic_visuals/sem_petrography_ai.svg",
}

CARD_VISUALS = {
    "ai_workflow": "assets/topic_visuals/agent_training_trace.svg",
    "thesis_graph": "assets/project_visuals/linkedin_powerpoint_slides/ree_slide_system_overview.png",
    "processing_earthquake": "assets/topic_visuals/earthquake_globe_signal.svg",
    "north_slope": "assets/topic_visuals/north_slope_decision_space.svg",
    "rock_classification": "assets/gmail_updates/2026-06-08/Screenshot 2026-05-16 203029.png",
    "seismic": "assets/gmail_updates/2026-06-08/Screenshot 2025-07-01 101445.png",
    "valles": "assets/project_visuals/linkedin_powerpoint_slides/sage_valles_deck_image_05.jpg",
    "near_surface": "assets/gmail_updates/2026-06-08/Screenshot 2025-07-01 121033.png",
    "moho_ml": "assets/topic_visuals/gis_moho_deck_trace.svg",
    "ambient_noise": "assets/topic_visuals/ambient_noise_processing.svg",
    "stock_workflow": "assets/topic_visuals/app_pipeline.svg",
    "sem_petrography": "assets/topic_visuals/sem_petrography_ai.svg",
}

ML_SOURCE_RIBBONS = [
    {
        "label": "Hydrate ML paper",
        "short": "Sgh + well logs",
        "detail": "ANN, NMR Sgh target, density/porosity/GR/resistivity/Vp/Vs, washout/GLOSS QC, basin transfer.",
    },
    {
        "label": "ML validation notes",
        "short": "leakage + drift",
        "detail": "Baseline first, split matches use, train-only transforms, data quality checks, drift, fallback.",
    },
]

ML_DIAGRAM_BLUEPRINTS = {
    "ai_workflow": {
        "objective": "task replay",
        "target": "pass / fail",
        "features": ["screen state", "click trace", "rubric"],
        "model": "behavior-cloning transformer",
        "source_pattern": "target + features",
        "validation": "held-out task",
        "output": "reviewed replay",
    },
    "thesis_graph": {
        "objective": "edge ranking",
        "target": "valid relation",
        "features": ["entity", "edge type", "source"],
        "model": "SciBERT + GraphSAGE",
        "source_pattern": "source-backed target",
        "validation": "edge audit",
        "output": "query graph",
    },
    "processing_earthquake": {
        "objective": "feature windows",
        "target": "event pattern",
        "features": ["lat/lon", "depth", "magnitude"],
        "model": "Poisson GLM + LightGBM",
        "source_pattern": "logs -> variables",
        "validation": "time split",
        "output": "no forecast claim",
    },
    "seismic": {
        "objective": "pick QA",
        "target": "arrival quality",
        "features": ["waveform", "station", "SNR"],
        "model": "LightGBM + PhaseNet",
        "source_pattern": "target + QC",
        "validation": "human pick",
        "output": "velocity risk",
    },
    "north_slope": {
        "objective": "hydrate Sgh",
        "target": "NMR Sgh",
        "features": ["density", "porosity", "GR", "Rt", "Vp/Vs"],
        "model": "Keras ANN + XGBoost",
        "source_pattern": "washout + GLOSS",
        "validation": "well-held-out",
        "output": "screened interval",
    },
    "rock_classification": {
        "objective": "rock labels",
        "target": "expert label",
        "features": ["image", "chemistry", "map"],
        "model": "EfficientNet + XGBoost",
        "source_pattern": "feature combos",
        "validation": "sample split",
        "output": "review queue",
    },
    "valles": {
        "objective": "conflict zones",
        "target": "agree / conflict",
        "features": ["gravity", "ERT/TEM", "seismic"],
        "model": "LightGBM + Gaussian Process",
        "source_pattern": "physical QC",
        "validation": "method lane",
        "output": "field review",
    },
    "near_surface": {
        "objective": "line review",
        "target": "method conflict",
        "features": ["line id", "velocity", "resistivity"],
        "model": "LightGBM + GP surface",
        "source_pattern": "bad rows out",
        "validation": "leave-line-out",
        "output": "review target",
    },
    "moho_ml": {
        "objective": "transfer test",
        "target": "Moho depth",
        "features": ["gravity", "region", "residual"],
        "model": "Ridge + LightGBM + ANN",
        "source_pattern": "basin transfer",
        "validation": "area-held-out",
        "output": "residual map",
    },
    "ambient_noise": {
        "objective": "monitoring",
        "target": "stable CCF",
        "features": ["station pair", "window", "stack"],
        "model": "LightGBM + Isolation Forest",
        "source_pattern": "freshness QC",
        "validation": "seasonal check",
        "output": "alert review",
    },
    "stock_workflow": {
        "objective": "honest app",
        "target": "future window",
        "features": ["ticker", "past data", "refresh"],
        "model": "ElasticNet + LightGBM",
        "source_pattern": "shift before rolling",
        "validation": "walk-forward",
        "output": "claim gate",
    },
    "sem_petrography": {
        "objective": "label vs claim",
        "target": "visible label",
        "features": ["SEM crop", "scale", "sample"],
        "model": "EfficientNet + U-Net",
        "source_pattern": "validity check",
        "validation": "expert + lit",
        "output": "blocked proxy",
    },
}

MANUAL_VISUAL_ARCHITECTURES = {
    "ai_workflow": {
        "name": "Trace Factory",
        "kicker": "future scientific software agent",
        "source": [
            "prompt + rubric",
            "screen recording",
            "file tree",
            "accepted output",
        ],
        "flow": [
            "UI tokens",
            "action trace encoder",
            "supervised labels",
            "behavior-cloning transformer",
            "replay simulator",
            "held-out task score",
        ],
        "model": "CLIP/OCR state encoder + behavior-cloning transformer",
        "vocab": ["UI token", "action trace", "rubric label", "held-out task"],
        "gates": [
            "hidden state",
            "shortcut memorization",
            "ambiguous rubric",
            "unsafe file action",
        ],
        "output": "reviewed replay or human approval queue",
        "prompt": "Convert recordings, screenshots, prompts, rubrics, and file trees into UI tokens and action traces before training or evaluating an agent.",
    },
    "thesis_graph": {
        "name": "Source-To-Graph AI Hub",
        "kicker": "critical-mineral graph reasoning",
        "source": [
            "thesis slides",
            "Gephi exports",
            "CSV node tables",
            "figure captions",
        ],
        "flow": [
            "entity extraction",
            "ontology cleanup",
            "edge ranking",
            "GraphRAG retrieval",
            "human edge audit",
            "queryable graph",
        ],
        "model": "SciBERT entity extractor + relation cross-encoder + GraphSAGE/R-GCN",
        "vocab": ["source-backed edge", "inferred edge", "ontology", "GraphRAG"],
        "gates": [
            "hallucinated edge",
            "duplicate entity",
            "unsupported relation",
            "graph leakage",
        ],
        "output": "source-backed graph query and reviewable architecture diagram",
        "prompt": "Separate observed, inferred, conceptual, and AI-suggested edges so the graph teaches evidence strength.",
    },
    "processing_earthquake": {
        "name": "3D Visualization To Feature Table",
        "kicker": "creative visualization into model-ready rows",
        "source": [
            "USGS events",
            "lat/lon",
            "depth",
            "magnitude/time",
        ],
        "flow": [
            "globe encoding",
            "flattening lens",
            "region-time windows",
            "lagged features",
            "count baseline",
            "chronological validation",
        ],
        "model": "Poisson/negative-binomial count model + LightGBM anomaly ranker",
        "vocab": ["lagged feature", "time split", "feature row", "no forecast gate"],
        "gates": [
            "look-ahead leakage",
            "bad event",
            "rare-event imbalance",
            "visual overclaim",
        ],
        "output": "event-pattern or anomaly view, not an unsupported forecast",
        "prompt": "Show the globe as feature engineering: visual points become evaluated rows before any prediction claim appears.",
    },
    "seismic": {
        "name": "Seismic Notebook To QA Pipeline",
        "kicker": "waveform QA and reviewed arrival picks",
        "source": [
            "catalog search",
            "station metadata",
            "waveform windows",
            "notebook cells",
        ],
        "flow": [
            "metadata QA",
            "SNR check",
            "LightGBM QA",
            "PhaseNet/EQTransformer",
            "uncertainty band",
            "reviewed velocity table",
        ],
        "model": "LightGBM waveform QA + PhaseNet/EQTransformer pick proposal",
        "vocab": ["waveform window", "pick proposal", "uncertainty band", "human pick"],
        "gates": [
            "station mismatch",
            "weak waveform",
            "bad metadata",
            "unreviewed interpretation",
        ],
        "output": "reviewed pick and velocity output with caveat tags",
        "prompt": "Make the pick line and uncertainty band visible before showing velocity or aquifer interpretation.",
    },
    "north_slope": {
        "name": "Leakage-Safe Hydrate Architecture",
        "kicker": "source-backed energy screening",
        "source": [
            "public geology",
            "well IDs",
            "GR/Rt/Vp/Vs",
            "NMR Sgh target",
        ],
        "flow": [
            "CRS/depth QC",
            "caliper washout",
            "GLOSS outliers",
            "train-only normalization",
            "Keras ANN Sgh",
            "well-held-out validation",
        ],
        "model": "Ridge/ElasticNet reference + Keras ANN + XGBoost challenger",
        "vocab": ["Sgh", "caliper washout", "GLOSS", "leave-well-out"],
        "gates": [
            "target leakage",
            "random depth split",
            "missing logs",
            "gas/ice/cement lookalike",
        ],
        "output": "calibrated hydrate screen with abstention and geologist review",
        "prompt": "Use the hydrate paper vocabulary directly and keep a red leakage barrier between targets and feature generation.",
    },
    "rock_classification": {
        "name": "Multimodal Rock Label Pipeline",
        "kicker": "image + chemistry + text labels",
        "source": [
            "thin sections",
            "classification charts",
            "spider diagrams",
            "formation tables",
        ],
        "flow": [
            "metadata audit",
            "image branch",
            "chemistry branch",
            "text/source branch",
            "late fusion",
            "expert correction",
        ],
        "model": "EfficientNet/ResNet image branch + XGBoost chemistry branch",
        "vocab": ["sample-held-out", "weak label", "VIF check", "ambiguous bucket"],
        "gates": [
            "same-sample leakage",
            "missing scale",
            "mixed classes",
            "overconfident label",
        ],
        "output": "ranked rock/mineral labels and expert review queue",
        "prompt": "Keep image, chemistry, and source-text branches separate until labels and metadata are visible.",
    },
    "valles": {
        "name": "Geophysical Disagreement Board",
        "kicker": "field methods without false consensus",
        "source": [
            "gravity",
            "EM/TEM",
            "ERT/seismic",
            "field notes",
        ],
        "flow": [
            "method lanes",
            "shared spatial frame",
            "uncertainty ribbons",
            "conflict classifier",
            "GP uncertainty",
            "expert board",
        ],
        "model": "LightGBM conflict ranker + Gaussian Process uncertainty surface",
        "vocab": ["method lane", "misregistration", "conflict zone", "false consensus"],
        "gates": [
            "misregistration",
            "acquisition artifact",
            "physics ignored",
            "smooth map overclaim",
        ],
        "output": "review-priority board, not one final subsurface truth",
        "prompt": "Use striped conflict zones where methods disagree; do not visually average them away.",
    },
    "near_surface": {
        "name": "Fen Method Fusion Cross-Section",
        "kicker": "line-scale shallow geophysics review",
        "source": [
            "hammer seismic",
            "ERT",
            "TEM",
            "field notes",
        ],
        "flow": [
            "line geometry",
            "velocity lane",
            "resistivity lane",
            "conductivity lane",
            "conflict ranker",
            "leave-line-out test",
        ],
        "model": "LightGBM method-conflict ranker + GP method uncertainty",
        "vocab": ["line-aware split", "possible unit", "field note", "review target"],
        "gates": [
            "wrong intersection",
            "field-note loss",
            "unit drift",
            "clean overlay overclaim",
        ],
        "output": "agreement/conflict review targets",
        "prompt": "Show hammer seismic, ERT, and TEM as separate layers with conflict hatching, not one clean fused map.",
    },
    "moho_ml": {
        "name": "Regional Transfer Evaluation",
        "kicker": "geoscience ML must transfer honestly",
        "source": [
            "Australia training",
            "gravity features",
            "Moho target",
            "USA test region",
        ],
        "flow": [
            "Ridge/GAM reference",
            "LightGBM regressor",
            "ANN challenger",
            "transfer bridge",
            "residual map",
            "risk checklist",
        ],
        "model": "Ridge/GAM reference + LightGBM/XGBoost + ANN challenger",
        "vocab": ["transfer test", "residual", "spatial leakage", "coordinate memorization"],
        "gates": [
            "spatial leakage",
            "biased split",
            "variable mismatch",
            "high score without transfer",
        ],
        "output": "residual map and transfer score, not just accuracy",
        "prompt": "Make the Australia-to-USA transfer bridge and residual failures the visual center.",
    },
    "ambient_noise": {
        "name": "Ambient Noise Monitoring Ladder",
        "kicker": "station-pair stability before alerts",
        "source": [
            "continuous records",
            "station metadata",
            "window params",
            "station pairs",
        ],
        "flow": [
            "preprocessing",
            "station-pair CCF",
            "stable stack",
            "change metric",
            "anomaly triage",
            "alert review",
        ],
        "model": "LightGBM CCF-quality classifier + Isolation Forest anomaly triage",
        "vocab": ["stable CCF", "stack count", "seasonal flag", "freshness check"],
        "gates": [
            "weak correlation",
            "seasonal noise",
            "metadata error",
            "instrument change",
        ],
        "output": "reviewed monitoring alert with provenance",
        "prompt": "Show stable correlations brightening and unstable station pairs fading into QC.",
    },
    "stock_workflow": {
        "name": "App Risk And Leakage Gate",
        "kicker": "honest dashboard model risk",
        "source": [
            "saved ticker data",
            "refresh time",
            "past prices",
            "dashboard outputs",
        ],
        "flow": [
            "shift-before-rolling",
            "chronological split",
            "persistence baseline",
            "ElasticNet/LightGBM",
            "walk-forward test",
            "claim gate",
        ],
        "model": "persistence baseline + ElasticNet/LightGBM challenger",
        "vocab": ["past-only feature", "walk-forward", "PSI drift", "fallback path"],
        "gates": [
            "future leakage",
            "stale refresh",
            "no baseline",
            "overclaiming",
        ],
        "output": "research dashboard with cautious claim language",
        "prompt": "Draw the red gate before prediction language; the app must prove past-only features and walk-forward validation.",
    },
    "sem_petrography": {
        "name": "Observation Vs Interpretation Gate",
        "kicker": "visible labels before proxy claims",
        "source": [
            "SEM crop",
            "scale bar",
            "sample metadata",
            "literature note",
        ],
        "flow": [
            "visible label proposal",
            "patch classifier",
            "segmentation/retrieval",
            "expert correction",
            "literature link",
            "proxy claim gate",
        ],
        "model": "EfficientNet/ResNet patch classifier + U-Net/Mask R-CNN + CLIP retrieval",
        "vocab": ["visible label", "interpretation label", "literature support", "ambiguous crop"],
        "gates": [
            "texture overclaim",
            "missing scale",
            "proxy from image",
            "literature mismatch",
        ],
        "output": "accepted observation or blocked interpretation",
        "prompt": "Let image models propose visible labels only; paleoclimate or reservoir claims need expert and literature support.",
    },
}

ML_MODEL_DETAIL_DIAGRAMS = {
    "ai_workflow": {
        "reference": {
            "name": "LightGBM action classifier",
            "target": "next action class",
            "input": "prompt type, rubric id, state label, prior action, error flag",
            "unit": "one labeled action step",
        },
        "main": {
            "name": "behavior-cloning transformer",
            "target": "action token, UI target, parameter, stop/review decision",
            "input": "screenshot embedding, OCR/UI tokens, file tree, prior steps",
            "unit": "observe -> act -> inspect trace sequence",
        },
        "challenger": {
            "name": "decision transformer + tool planner",
            "target": "task graph and low-level software actions",
            "input": "retrieved prior traces, accepted outputs, rubric failures",
            "unit": "full scientific software task",
        },
        "validation": "held-out software task, held-out project, held-out file structure",
        "metrics": ["task success rate", "step accuracy", "action F1", "unsafe action rate"],
        "gate": "human approval before file writes, external actions, or uncertain execution",
        "diagram": "CLIP/OCR state encoder -> behavior-cloning transformer -> replay simulator -> held-out task score",
    },
    "thesis_graph": {
        "reference": {
            "name": "SciBERT / MatSciBERT NER",
            "target": "mineral, host rock, deposit, process, location, source entity",
            "input": "thesis text, slide text, captions, CSV node tables",
            "unit": "sentence, table row, or slide text box",
        },
        "main": {
            "name": "relation cross-encoder",
            "target": "observed, inferred, analog, conceptual, or AI-suggested edge",
            "input": "entity pair, source chunk, figure caption, graph context",
            "unit": "candidate source-backed edge",
        },
        "challenger": {
            "name": "GraphSAGE / R-GCN link ranker",
            "target": "relationship or prospectivity edge for review",
            "input": "node features, edge types, source weights, ontology labels",
            "unit": "graph edge or node pair",
        },
        "validation": "held-out source document, held-out deposit, held-out edge set",
        "metrics": ["entity F1", "edge F1", "citation accuracy", "MRR / Hits@K"],
        "gate": "human edge audit with observed vs inferred styling",
        "diagram": "SciBERT entity extractor -> relation cross-encoder -> GraphRAG retrieval -> GraphSAGE/R-GCN edge ranking",
    },
    "processing_earthquake": {
        "reference": {
            "name": "Poisson GLM",
            "target": "event count by region-time window",
            "input": "prior count, magnitude bins, depth bins, region id, lagged history",
            "unit": "region-time window",
        },
        "main": {
            "name": "negative-binomial GLM or LightGBM",
            "target": "expected count or current-window anomaly rank",
            "input": "lagged counts, depth histogram, magnitude histogram, cluster density",
            "unit": "time-window feature row",
        },
        "challenger": {
            "name": "Hawkes process / ST-DBSCAN",
            "target": "self-exciting sequence or spatiotemporal cluster",
            "input": "event time, coordinates, magnitude, depth",
            "unit": "event sequence or cluster",
        },
        "validation": "chronological split or leave-region-out split",
        "metrics": ["MAE / RMSE", "PR-AUC for anomaly labels", "calibration", "rare-event recall"],
        "gate": "no forecasting claim unless a target and future-window test exist",
        "diagram": "USGS events -> region-time windows -> Poisson/negative-binomial count model -> LightGBM anomaly ranker",
    },
    "seismic": {
        "reference": {
            "name": "LightGBM waveform QA classifier",
            "target": "usable waveform, weak waveform, station mismatch, needs human pick",
            "input": "SNR, distance, channel, metadata completeness, magnitude",
            "unit": "event-station-channel waveform window",
        },
        "main": {
            "name": "PhaseNet / EQTransformer",
            "target": "P arrival probability, S arrival probability, noise probability",
            "input": "three-component waveform windows and station metadata",
            "unit": "waveform window",
        },
        "challenger": {
            "name": "seismic representation model + uncertainty head",
            "target": "pick quality, event association, waveform anomaly",
            "input": "pretrained waveform embedding, station context, QA labels",
            "unit": "reviewed waveform segment",
        },
        "validation": "held-out event, held-out station, or held-out region",
        "metrics": ["pick-time error", "usable-pick F1", "SNR-stratified score", "velocity residual"],
        "gate": "human-reviewed pick before velocity or aquifer interpretation",
        "diagram": "ObsPy waveform windows -> LightGBM QA -> PhaseNet/EQTransformer picks -> bootstrap uncertainty",
    },
    "north_slope": {
        "reference": {
            "name": "Ridge / ElasticNet Sgh regressor",
            "target": "NMR-derived gas hydrate saturation Sgh",
            "input": "GR, Rt, Vp, Vs, density, porosity, missingness flags",
            "unit": "QC-approved depth point",
        },
        "main": {
            "name": "Keras/TensorFlow ANN",
            "target": "continuous Sgh regression",
            "input": "GR + Vp, Rt + Vp, phi_den + GR + Vp, phi_den + Rt + Vp",
            "unit": "depth point grouped by complete well",
        },
        "challenger": {
            "name": "XGBoost / LightGBM + multitask NN",
            "target": "hydrate occurrence head plus saturation head",
            "input": "log combinations, QC flags, formation tags, public-safe context",
            "unit": "well interval",
        },
        "validation": "leave-well-out, leave-area-out, and basin-transfer testing",
        "metrics": ["R2", "MAE / RMSE", "ROC-AUC / PR-AUC", "calibration and abstention"],
        "gate": "caliper washout, GLOSS outliers, target leakage, and random depth-row split checks",
        "diagram": "caliper + GLOSS QC -> train-only normalization -> Keras ANN Sgh regressor -> XGBoost challenger",
    },
    "rock_classification": {
        "reference": {
            "name": "linear SVM / logistic regression",
            "target": "rock, mineral, formation, or ambiguous label",
            "input": "chemical ratios, texture statistics, source label",
            "unit": "sample, image crop, or mapped unit",
        },
        "main": {
            "name": "EfficientNet or ResNet + XGBoost",
            "target": "expert-reviewed class label",
            "input": "thin-section/map image embedding plus chemistry and formation variables",
            "unit": "labeled sample or crop",
        },
        "challenger": {
            "name": "CLIP/SigLIP retrieval + Swin Transformer",
            "target": "similar expert example or high-resolution patch label",
            "input": "image-text pairs, captions, chemistry tables",
            "unit": "image-text training example",
        },
        "validation": "sample-held-out, site-held-out, or formation-held-out",
        "metrics": ["macro-F1", "balanced accuracy", "top-k accuracy", "expert correction rate"],
        "gate": "no duplicate crop leakage from the same sample",
        "diagram": "EfficientNet image branch + XGBoost chemistry branch + late-fusion label ranker -> expert audit",
    },
    "valles": {
        "reference": {
            "name": "logistic conflict classifier",
            "target": "agree, conflict, insufficient evidence, needs review",
            "input": "method flags, anomaly strength, uncertainty, spatial overlap",
            "unit": "grid cell, line intersection, or interpreted zone",
        },
        "main": {
            "name": "LightGBM / random forest conflict ranker",
            "target": "review-priority rank and conflict type",
            "input": "gravity, EM/TEM/ERT response, seismic velocity, geology, registration error",
            "unit": "method-overlap zone",
        },
        "challenger": {
            "name": "Gaussian Process / U-Net / graph model",
            "target": "uncertainty surface, anomaly segment, or survey-intersection graph",
            "input": "gridded method outputs and adjacency between survey zones",
            "unit": "surface cell or graph node",
        },
        "validation": "leave-area-out or leave-survey-line-out",
        "metrics": ["conflict F1", "precision@K", "uncertainty calibration", "expert agreement"],
        "gate": "method disagreement remains visible; no false unified subsurface map",
        "diagram": "method-specific features -> LightGBM conflict classifier -> Gaussian Process uncertainty surfaces",
    },
    "near_surface": {
        "reference": {
            "name": "decision tree / logistic agreement model",
            "target": "agreement, conflict, missing context, possible unit only",
            "input": "line id, intersection id, velocity, resistivity, conductivity, depth",
            "unit": "line intersection or depth interval",
        },
        "main": {
            "name": "LightGBM method-conflict classifier",
            "target": "review target, not final geologic unit",
            "input": "hammer seismic velocity, ERT resistivity, TEM conductivity, field note flags",
            "unit": "field-line interval",
        },
        "challenger": {
            "name": "Gaussian Process surface or graph model",
            "target": "method-specific property surface or intersection graph",
            "input": "line geometry, method values, possible unit labels",
            "unit": "line node or cross-section zone",
        },
        "validation": "leave-line-out or leave-intersection-out",
        "metrics": ["conflict F1", "precision@K", "false-consensus rate", "expert acceptance"],
        "gate": "striped unresolved zones when methods conflict",
        "diagram": "line geometry -> LightGBM conflict ranker -> GP method uncertainty -> leave-line-out validation",
    },
    "moho_ml": {
        "reference": {
            "name": "Ridge / ElasticNet / GAM",
            "target": "Moho depth",
            "input": "gravity anomaly, topography, crustal proxies, region id",
            "unit": "grid cell or control point",
        },
        "main": {
            "name": "LightGBM / XGBoost regressor",
            "target": "Moho depth plus residual map",
            "input": "gravity features, spatial derivatives, regional context",
            "unit": "spatial feature row",
        },
        "challenger": {
            "name": "Keras MLP + Gaussian Process residual",
            "target": "transfer prediction with spatial uncertainty",
            "input": "ANN prediction, residuals, train/test geography",
            "unit": "held-out region cell",
        },
        "validation": "leave-region-out, Australia-to-USA transfer, spatial block validation",
        "metrics": ["RMSE", "MAE", "R2", "regional residual bias"],
        "gate": "coordinate memorization and spatial leakage check",
        "diagram": "Ridge/GAM reference -> LightGBM Moho regressor -> ANN challenger -> GP residual uncertainty",
    },
    "ambient_noise": {
        "reference": {
            "name": "LightGBM CCF-quality classifier",
            "target": "stable CCF, unstable CCF, data gap, instrument issue, seasonal flag",
            "input": "stack count, CCF peak strength, symmetry, lag stability, metadata flags",
            "unit": "station-pair time window",
        },
        "main": {
            "name": "Isolation Forest + LightGBM",
            "target": "station-pair anomaly and review priority",
            "input": "CCF features, stack stability, station distance, missing windows",
            "unit": "station-pair monitoring window",
        },
        "challenger": {
            "name": "SeisLM-style embedding + temporal model",
            "target": "station-pair quality or change detection",
            "input": "pretrained waveform embedding and CCF time series",
            "unit": "station-pair sequence",
        },
        "validation": "held-out station pair, held-out time period, or held-out network",
        "metrics": ["bad-window F1", "false alert rate", "detection delay", "stability calibration"],
        "gate": "human review before treating a weak correlation as subsurface signal",
        "diagram": "CCF table -> LightGBM stability classifier -> Isolation Forest anomaly triage -> SeisLM challenger",
    },
    "stock_workflow": {
        "reference": {
            "name": "persistence + moving average",
            "target": "next-window level, return, volatility, or risk bucket",
            "input": "past-only price windows and refresh timestamp",
            "unit": "ticker-date window",
        },
        "main": {
            "name": "ElasticNet + LightGBM",
            "target": "continuous target or calibrated up/down/risk label",
            "input": "shifted rolling features, ticker universe, date split",
            "unit": "past-only feature row",
        },
        "challenger": {
            "name": "ARIMA/SARIMAX or temporal CNN/LSTM",
            "target": "time-series forecast only after walk-forward proof",
            "input": "single-series history or sequence features",
            "unit": "walk-forward fold",
        },
        "validation": "walk-forward or rolling chronological split",
        "metrics": ["MAE / RMSE", "ROC-AUC / PR-AUC", "Brier score", "PSI drift"],
        "gate": "claim-language gate: tool/demo, not investment advice",
        "diagram": "persistence reference -> ElasticNet/LightGBM challenger -> walk-forward validation -> PSI drift monitor",
    },
    "sem_petrography": {
        "reference": {
            "name": "linear SVM / logistic texture model",
            "target": "grain, pore/fracture, clay morphology, mineral texture, ambiguous",
            "input": "texture features, scale metadata, crop location, sample id",
            "unit": "SEM image crop",
        },
        "main": {
            "name": "EfficientNet / ResNet patch classifier",
            "target": "visible petrographic label",
            "input": "SEM crop, scale bar, sample context",
            "unit": "expert-labeled patch",
        },
        "challenger": {
            "name": "U-Net / Mask R-CNN + CLIP retrieval",
            "target": "grain/pore segmentation or similar reviewed example",
            "input": "pixel masks, patch labels, literature-linked examples",
            "unit": "segmented crop or retrieval pair",
        },
        "validation": "sample-held-out or site-held-out",
        "metrics": ["macro-F1", "IoU / Dice", "top-k retrieval", "unsupported-claim block rate"],
        "gate": "proxy claim must pass literature and expert review; image pixels alone are not enough",
        "diagram": "EfficientNet patch classifier -> U-Net/Mask R-CNN segmentation -> CLIP retrieval -> proxy claim gate",
    },
}

PROJECT_TOPIC_FALLBACKS = {
    "moho_ml": "moho_ml",
    "stock_workflow": "stock_workflow",
    "stock_dashboard": "stock_workflow",
}

WORKFLOW_NODE_ICONS = {
    "Prompt": "ASK",
    "Record": "REC",
    "Rubric": "PASS?",
    "Review": "HUMAN",
    "Agent": "REPLAY",
    "Prompt page": "ASK",
    "Adobe sketch": "DRAW",
    "CSV nodes": "DATA",
    "Gephi": "GRAPH",
    "Neo4j": "QUERY",
    "USGS events": "EVENTS",
    "Processing": "MOTION",
    "Sound": "AUDIO",
    "Streamlit/Three.js": "WEB",
    "Explain": "STORY",
    "Catalog": "EVENTS",
    "Waveform": "TRACE",
    "Pick": "PICK",
    "QA": "CHECK",
    "Dashboard": "REVIEW",
    "Open data": "PUBLIC",
    "GIS files": "LAYERS",
    "3D atlas": "3D",
    "Features": "LOGS",
    "Screen": "RANK",
}

def workflow_icon_svg(label: str, index: int) -> str:
    value = label.lower()
    if any(term in value for term in ["data", "csv", "catalog", "events", "files"]):
        drawing = """
<ellipse cx="20" cy="10" rx="11" ry="5"/><path d="M9 10v16c0 3 5 5 11 5s11-2 11-5V10"/>
<path d="M9 18c0 3 5 5 11 5s11-2 11-5"/>
        """
    elif any(term in value for term in ["gis", "map", "atlas", "gephi", "neo4j"]):
        drawing = """
<path d="M7 9l9-4 9 4 8-4v25l-8 4-9-4-9 4z"/><path d="M16 5v25M25 9v25"/>
        """
    elif any(term in value for term in ["prompt", "ask", "explain", "review", "rubric", "qa"]):
        drawing = """
<path d="M8 7h24v18H19l-7 7v-7H8z"/><path d="M14 14h12M14 19h8"/>
        """
    elif any(term in value for term in ["model", "ann", "agent", "screen", "class", "features"]):
        drawing = """
<circle cx="9" cy="12" r="3"/><circle cx="9" cy="28" r="3"/>
<circle cx="21" cy="20" r="3"/><circle cx="33" cy="12" r="3"/><circle cx="33" cy="28" r="3"/>
<path d="M12 12l6 6M12 28l6-6M24 18l6-5M24 22l6 5"/>
        """
    elif any(term in value for term in ["3d", "grid", "output", "dashboard", "streamlit"]):
        drawing = """
<path d="M7 12l13-7 13 7-13 7z"/><path d="M7 12v15l13 8 13-8V12"/>
<path d="M20 19v16"/>
        """
    else:
        drawing = """
<circle cx="20" cy="20" r="13"/><path d="M13 20l5 5 10-11"/>
        """
    return (
        "<svg viewBox='0 0 40 40' aria-hidden='true' "
        "fill='none' stroke='currentColor' stroke-width='2.4' "
        "stroke-linecap='round' stroke-linejoin='round'>"
        f"{drawing}</svg>"
    )

WORKFLOW_BLUEPRINTS = {
    "ai_workflow": {
        "title": "human demo -> agent training",
        "steps": [
            ("Prompt", "task goal"),
            ("Record", "screen + clicks"),
            ("Rubric", "pass/fail logic"),
            ("Review", "human judgement"),
            ("Agent", "future replay"),
        ],
        "outcome": "Less grunt work in QGIS, ParaView, Vagon, and other scientific software.",
    },
    "thesis_graph": {
        "title": "prompt -> drawing -> graph",
        "steps": [
            ("Prompt page", "what connects?"),
            ("Adobe sketch", "subsurface idea"),
            ("CSV nodes", "entities + children"),
            ("Gephi", "visual clusters"),
            ("Neo4j", "future graph ML"),
        ],
        "outcome": "A way to discuss critical-mineral systems visually instead of only through prose.",
    },
    "processing_earthquake": {
        "title": "creative coding -> reproducible science",
        "steps": [
            ("USGS events", "lat/lon/depth"),
            ("Processing", "3D globe"),
            ("Sound", "pattern feeling"),
            ("Streamlit/Three.js", "future rebuild"),
            ("Explain", "AI narration"),
        ],
        "outcome": "Geoscience data becomes easier to see, hear, and question.",
    },
    "seismic": {
        "title": "notebook -> fast interpretation",
        "steps": [
            ("Catalog", "events + stations"),
            ("Waveform", "ObsPy flow"),
            ("Pick", "arrival timing"),
            ("QA", "uncertainty"),
            ("Dashboard", "future review"),
        ],
        "outcome": "Less manual friction between seismic data and a defensible interpretation.",
    },
    "north_slope": {
        "title": "public data -> energy screen",
        "steps": [
            ("Open data", "maps + papers"),
            ("GIS files", "big shapefiles"),
            ("3D atlas", "wells + geology"),
            ("Features", "logs + context"),
            ("Screen", "hydrate targets"),
        ],
        "outcome": "Industry/government can ask where to investigate next with clearer evidence.",
    },
    "rock_classification": {
        "title": "instrument signal -> rock property map",
        "steps": [
            ("Ranges", "rock/mineral data"),
            ("Grids", "shapefile variables"),
            ("Overlap", "color classes"),
            ("3D GIS", "subsurface view"),
            ("ML", "future labels"),
        ],
        "outcome": "Surveys become visual resource maps tied back to rock properties.",
    },
    "valles": {
        "title": "field methods -> uncertainty board",
        "steps": [
            ("Gravity", "density clues"),
            ("EM/ERT/TEM", "conductivity"),
            ("Seismic", "velocity"),
            ("Compare", "method limits"),
            ("Review", "expert call"),
        ],
        "outcome": "AI helps compare imperfect surveys without pretending they are perfect.",
    },
    "near_surface": {
        "title": "fen survey -> method comparison",
        "steps": [
            ("Field lines", "fen geometry"),
            ("Hammer seismic", "velocity clues"),
            ("ERT/TEM", "conductivity"),
            ("Units", "possible geology"),
            ("Review", "method conflict"),
        ],
        "outcome": "AI helps line up shallow surveys while keeping disagreements visible.",
    },
    "moho_ml": {
        "title": "train region -> transfer test",
        "steps": [
            ("Australia", "training data"),
            ("Gravity", "features"),
            ("ANN", "baseline model"),
            ("USA", "transfer test"),
            ("Residuals", "honest score"),
        ],
        "outcome": "A model is useful only if it survives new geography and expert review.",
    },
    "ambient_noise": {
        "title": "continuous noise -> monitoring signal",
        "steps": [
            ("Stations", "continuous records"),
            ("Window", "noise segments"),
            ("CCF", "station pairs"),
            ("Stack", "stable signal"),
            ("Monitor", "change review"),
        ],
        "outcome": "AI helps triage massive ambient-noise outputs before interpretation.",
    },
    "stock_workflow": {
        "title": "local notebook -> tracked app",
        "steps": [
            ("Downloads", "messy outputs"),
            ("Codex", "organize/build"),
            ("GitHub", "track changes"),
            ("Streamlit", "visual app"),
            ("Risk check", "leakage"),
        ],
        "outcome": "Young builders can make useful tools faster without trusting fake model scores.",
    },
    "sem_petrography": {
        "title": "SEM texture -> reviewed proxy",
        "steps": [
            ("SEM image", "micro texture"),
            ("Mineral label", "clay form"),
            ("Context", "detrital/authigenic"),
            ("Proxy", "climate question"),
            ("Review", "expert call"),
        ],
        "outcome": "AI helps organize microscope evidence without turning labels into unsupported claims.",
    },
}

DISCUSSION_PROMPTS = {
    "ai_workflow": [
        "What parts of scientific software should agents learn first?",
        "What would count as a reliable rubric for QGIS or ParaView?",
        "How much human demonstration data is enough?",
    ],
    "thesis_graph": [
        "Where does a graph beat a spreadsheet?",
        "How could graph ML suggest a new critical-mineral question?",
        "What geologic claims should stay human-reviewed?",
    ],
    "processing_earthquake": [
        "What makes a scientific visual worth rebuilding?",
        "Should data sonification be more common in geoscience?",
        "What would make this reproducible instead of just cool?",
    ],
    "seismic": [
        "Which seismic steps are repetitive enough for AI?",
        "Where would an expert still need to overrule the model?",
        "How should uncertainty be shown visually?",
    ],
    "north_slope": [
        "How far can public data go before private industry data is needed?",
        "Where is the money play: faster screening, better maps, or fewer bad targets?",
        "What would make a hydrate interval ranking trustworthy?",
    ],
    "rock_classification": [
        "Can instrument properties become rock-property maps?",
        "What labels would make this a real ML dataset?",
        "How would this change resource mapping in ArcGIS or 3D GIS?",
    ],
    "valles": [
        "How should AI compare survey types with different uncertainties?",
        "What would a field geophysicist want to see first?",
        "Where does map fusion become misleading?",
    ],
    "near_surface": [
        "Which shallow method should lead: hammer seismic, ERT, or TEM?",
        "How should line intersections be used to validate interpretation?",
        "Where should an AI system leave the geology unresolved?",
    ],
    "moho_ml": [
        "What is the cleanest way to test regional transfer?",
        "Which model family would you try before an ANN today?",
        "How should residual maps guide geology review?",
    ],
    "ambient_noise": [
        "Which station pairs should be trusted first?",
        "What QC flags would make NoisePy outputs easier to review?",
        "How should compute cost and parameter choices stay visible?",
    ],
    "stock_workflow": [
        "What AI skills help young people build practical tools?",
        "How do we keep model testing honest?",
        "What belongs in GitHub/cloud instead of a laptop folder?",
    ],
    "sem_petrography": [
        "What SEM labels are visually defensible?",
        "Where does petrographic observation end and climate interpretation begin?",
        "What expert-reviewed examples would a model need before it is useful?",
    ],
}

EVIDENCE_LEADS = {
    "thesis_graph": [
        ("REE source Excel", "C:\\Users\\gargi\\Downloads\\bayan_obo_childDerived_cleaned.xlsx"),
        ("Gephi full nodes", "C:\\Users\\gargi\\Downloads\\gephi_nodes_full_multiclass_context.csv"),
        ("Gephi full edges", "C:\\Users\\gargi\\Downloads\\gephi_edges_full_multiclass_context.csv"),
        ("GraphML export", "C:\\Users\\gargi\\Downloads\\mp_bayanobo_knowledge_graph.graphml"),
    ],
    "moho_ml": [
        ("Moho notebook", "C:\\Users\\gargi\\Downloads\\aus.moho.ipynb"),
        ("Moho data file", "C:\\Users\\gargi\\Downloads\\australian.moho"),
        ("Model script", "C:\\Users\\gargi\\Downloads\\australian.py"),
        ("ML report", "C:\\Users\\gargi\\OneDrive\\Documents\\machinelearningreport.docx"),
    ],
    "rock_classification": [
        ("Formation range table", "C:\\Users\\gargi\\Downloads\\FormationRanges_Normalized.csv"),
        ("Classified formations", "C:\\Users\\gargi\\Downloads\\Classified_Formations_Output.xlsx"),
        ("Formation properties", "C:\\Users\\gargi\\Downloads\\Full_Formation_Property_Table.csv"),
        ("Mineral ion table", "C:\\Users\\gargi\\Downloads\\Mineral_Ion_EM_Table.docx"),
    ],
    "north_slope": [
        ("Directional survey", "C:\\Users\\gargi\\Downloads\\alaska_directional_survey_6_wells.csv"),
        ("Wireline equation map", "C:\\Users\\gargi\\Downloads\\hydrate_wireline_equation_map.docx"),
        ("Gas hydrate preservation doc", "C:\\Users\\gargi\\Downloads\\gas_hydrate_master_preservation_first_combined.docx"),
    ],
    "stock_workflow": [
        ("Stock dashboard folder", "C:\\Users\\gargi\\Downloads\\stockprediction2025"),
    ],
    "near_surface": [
        ("Near-Surface Dwellers deck", "https://docs.google.com/presentation/d/1bY4HCjuD-60DU6IMZXA_DAMeqza3Gq_xH_-Xd_-NwIA"),
    ],
    "ambient_noise": [
        ("NoisePy deck", "https://docs.google.com/presentation/d/1db8rT7vo8nEx8ZHyfIiOEqbIz4rheQdT8rVrc0B_BBs"),
    ],
    "sem_petrography": [
        ("SEM petrography deck", "https://docs.google.com/presentation/d/1vvMzqiRPkHiyPTyq6fZki04ZMUor7N1zR0SPebxmX_w"),
    ],
}

PROCESSING_SKETCH_PLANS = {
    "ai_workflow": {
        "sketch": "action_trace_rubric_loop",
        "visual": "Random action dots drift across a desktop field. A cursor-like path collects only useful actions, then rubric nodes light up green or red.",
        "motion": ["wandering dots", "path capture", "checkmark pulse", "agent replay trail"],
        "conclusion": "Agents need more than final answers; they need human demonstrations, output rubrics, and domain review.",
        "future_ml": "Imitation learning, workflow trace classification, and agent evaluation harnesses for scientific software.",
        "processing_notes": "Use PVector particles, one bezier path, and timed state changes from messy actions to reviewed workflow.",
    },
    "thesis_graph": {
        "sketch": "ree_graph_organizer_loop",
        "visual": "Scattered entity dots pulse outward from a prompt node, snap into mineral/host/fluid/stage clusters, and grow edges into a graph.",
        "motion": ["prompt pulse", "cluster sorting", "edge growth", "question-edge glow"],
        "conclusion": "Knowledge graphs make research relationships visible so AI has structure to reason with instead of loose notes.",
        "future_ml": "GraphRAG, Neo4j, relation extraction, graph embeddings, and graph ML for critical-mineral questions.",
        "processing_notes": "Use spring-like attraction to cluster nodes by type, then draw edges with alpha fades and a few highlighted unknowns.",
    },
    "processing_earthquake": {
        "sketch": "sensory_event_globe_loop",
        "visual": "A dark circular globe field receives event dots. Bigger dots pulse wider rings while depth shifts color and sound-wave rings expand.",
        "motion": ["event pulse", "depth color shift", "ring expansion", "orbiting timeline"],
        "conclusion": "Creative visual systems can make geoscience data easier to feel, inspect, and discuss.",
        "future_ml": "Event clustering, anomaly detection, and AI narration for seismic patterns.",
        "processing_notes": "No real earthquake data needed at first: generate synthetic lat/lon-like positions and magnitude-driven pulses.",
    },
    "seismic": {
        "sketch": "waveform_pick_uncertainty_loop",
        "visual": "Noisy waveform traces scroll left. A pick line appears, uncertainty bands breathe, and acceptable picks turn green while weak picks stay yellow.",
        "motion": ["trace scroll", "pick scan", "uncertainty band", "QA color change"],
        "conclusion": "AI can speed repetitive seismic review, but uncertainty and expert override must stay visible.",
        "future_ml": "Arrival picking, waveform QA classifiers, seismic foundation models, and promptable geobody interpretation.",
        "processing_notes": "Generate sine/noise traces, animate a vertical scanner, and mark confidence with transparent bands.",
    },
    "north_slope": {
        "sketch": "energy_screening_funnel_loop",
        "visual": "Messy data layers float in: papers, GIS, wells, logs, geology. They stack into a block, then flow into review/investigate/ignore paths.",
        "motion": ["layer drift", "stacking", "well drops", "decision funnel"],
        "conclusion": "AI can make public energy data easier to screen, but experts decide which targets deserve investigation.",
        "future_ml": "Explainable hydrate interval ranking from well logs, stratigraphy, structural context, and provenance confidence.",
        "processing_notes": "Represent layers as translucent planes, wells as vertical lines, and target confidence as pulsing dots.",
    },
    "rock_classification": {
        "sketch": "property_cluster_map_loop",
        "visual": "Colored particles for density, velocity, resistivity, chemistry, and formation labels pass through filters, overlap, then become map cells.",
        "motion": ["range filters", "particle sorting", "cluster formation", "grid coloring"],
        "conclusion": "AI can help translate instrument properties into rock-property maps and eventually 3D resource models.",
        "future_ml": "Multimodal classifiers, GNN lithology models, spatial feature fusion, and expert label auditing.",
        "processing_notes": "Use colored particles moving through threshold gates, then snap accepted particles into a tiled map grid.",
    },
    "valles": {
        "sketch": "uncertainty_layer_fusion_loop",
        "visual": "Three translucent fields slide together: gravity waves, EM blobs, seismic lines. Overlap glows, uncertainty remains gray.",
        "motion": ["field drift", "overlap glow", "uncertainty shimmer", "expert marker"],
        "conclusion": "AI can help compare methods, but it should preserve uncertainty instead of flattening all maps into one false answer.",
        "future_ml": "Data fusion, anomaly segmentation, uncertainty tagging, and map-comparison assistants.",
        "processing_notes": "Use alpha-blended fields and noise-based gray regions that never fully resolve.",
    },
    "near_surface": {
        "sketch": "near_surface_method_board",
        "visual": "A fen cross-section receives three moving layers: hammer-seismic velocity, ERT resistivity, and TEM conductivity. Agreement glows; conflict stays striped.",
        "motion": ["survey-line sweep", "layer alignment", "conflict stripes", "expert pin"],
        "conclusion": "AI can compare shallow methods, but unresolved zones should stay visible.",
        "future_ml": "Cross-method registration, uncertainty tagging, line-intersection QA, and promptable shallow-subsurface review.",
        "processing_notes": "Use stacked translucent bands, vertical survey lines, and blinking conflict cells where methods disagree.",
    },
    "moho_ml": {
        "sketch": "transfer_residual_loop",
        "visual": "A training cluster on the left feeds a neural-node chain. Predictions land on a new region, then residual dots flash where transfer fails.",
        "motion": ["train pulse", "network propagation", "test-region reveal", "residual flash"],
        "conclusion": "A high ML score is not enough; the model has to transfer honestly to new geography.",
        "future_ml": "Spatial cross-validation, transfer learning, residual mapping, uncertainty estimates, and model-family comparison.",
        "processing_notes": "Use two point clouds, a simple node network, and red/blue residual particles after prediction.",
    },
    "ambient_noise": {
        "sketch": "ambient_noise_correlation_loop",
        "visual": "Noise traces from many stations flow into pairwise arcs. Strong correlations stack into a bright center line while weak pairs fade into a QC bin.",
        "motion": ["trace windows", "station-pair arcs", "stack brightening", "QC fade"],
        "conclusion": "AI can help manage continuous seismic pipelines by triaging station pairs and making processing choices auditable.",
        "future_ml": "Correlation QC, unstable-stack detection, parameter recommendation, compute-log summarization, and monitoring change detection.",
        "processing_notes": "Use many tiny traces, curved station-pair connectors, and a central stack line that only brightens after enough consistent pairs.",
    },
    "stock_workflow": {
        "sketch": "codex_pipeline_risk_gate_loop",
        "visual": "Chaotic file dots fall into a Codex node, split into GitHub branches and dashboard panels, then pass through a leakage-check gate.",
        "motion": ["file rain", "pipeline sorting", "branch split", "risk gate"],
        "conclusion": "AI helps people build tools quickly, but useful apps need honest model testing and visible risk checks.",
        "future_ml": "Pipeline automation, model monitoring, leakage detection, cloud refreshes, and human-reviewed decision support.",
        "processing_notes": "Animate falling particles into lanes, branch lines, mini dashboard rectangles, and a red gate that blocks bad scores.",
    },
    "sem_petrography": {
        "sketch": "sem_texture_label_review",
        "visual": "SEM-like grayscale textures drift under a magnifier. Candidate labels attach to grains, then unsupported interpretation labels are rejected by a review gate.",
        "motion": ["texture scan", "label snap", "proxy branch", "review reject"],
        "conclusion": "AI can help label petrographic textures, but climate and reservoir interpretations need evidence and expert review.",
        "future_ml": "Multimodal SEM classifiers, literature-linked labels, expert review queues, and proxy-claim audit trails.",
        "processing_notes": "Use grayscale noise fields, contour-like grain edges, small orange label points, and a red review gate for overclaims.",
    },
}

RESEARCH_SOURCES = [
    ("USGS Earth MRI", "https://www.usgs.gov/special-topics/earth-mri"),
    ("DOE AI for Energy report", "https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf"),
    ("Geoscience knowledge graph pipeline", "https://www.mdpi.com/2075-163X/14/12/1296"),
    ("SciBERT scientific text model", "https://arxiv.org/abs/1903.10676"),
    ("MatSciBERT materials text model", "https://www.nature.com/articles/s41524-022-00784-w"),
    ("GraphSAGE graph model", "https://arxiv.org/abs/1706.02216"),
    ("R-GCN relational graph model", "https://arxiv.org/abs/1703.06103"),
    ("Critical minerals GraphRAG", "https://www.sciencedirect.com/science/article/pii/S0098300426000944"),
    ("GNN mineral prospectivity mapping", "https://www.sciencedirect.com/science/article/pii/S0169136824003482"),
    ("SeisLM seismic waveform foundation model", "https://arxiv.org/abs/2410.15765"),
    ("Seismic foundation model", "https://pubs.geoscienceworld.org/geophysics/article/90/2/IM59/652505/Seismic-foundation-model-A-next-generation-deep"),
    ("Promptable seismic geobody model", "https://arxiv.org/abs/2409.04962"),
    ("Physics-informed ML for subsurface energy", "https://www.sciencedirect.com/science/article/pii/S2949891024003087"),
    ("Gas hydrate well-log ML", "https://www.mdpi.com/2077-1312/13/7/1208"),
    ("Spatial cross-validation for GeoAI", "https://www.acsu.buffalo.edu/~yhu42/papers/2023_GeoAIHandbook_SpatialCV.pdf"),
    ("GUI agents survey", "https://aclanthology.org/2025.findings-acl.1158.pdf"),
    ("ADEPT scientific workflow agents", "https://www.osti.gov/biblio/3006464"),
]

GMAIL_SOURCE_UPDATES = [
    {
        "label": "ML source 1",
        "title": "Hydrate ANN paper",
        "body": (
            "Use Sgh, well logs, washout/GLOSS QC, feature-combination testing, and basin "
            "transfer as the geoscience ML pattern."
        ),
    },
    {
        "label": "ML source 2",
        "title": "Validation notes",
        "body": (
            "Use baseline-first modeling, train-only transforms, split policy, ETL checks, "
            "drift monitoring, fallback, and fairness where people are affected."
        ),
    },
    {
        "label": "Diagram rule",
        "title": "Target, features, gate",
        "body": (
            "Every topic should show the model target, feature lane, QC step, model layer, "
            "validation gate, and decision output."
        ),
    },
    {
        "label": "Visual rule",
        "title": "Less prose, more boards",
        "body": (
            "If a section starts turning into bullets, convert it into a source image, "
            "pipeline board, or Processing-style sketch."
        ),
    },
]

NORTH_SLOPE_ML_UPDATES = [
    (
        "Newest deck source",
        "FINAL 9-slide revision, parameter signal grid, ML workflow ladder, decision map, and final acceptance criteria",
    ),
    (
        "Feature equations to name",
        "Vsh, phi_den, Vp/Vs, acoustic impedance, lambda-rho, mu-rho, NMR separation, H_proxy, QC flags",
    ),
    (
        "Model ladder to show",
        "linear/logistic baseline, tree and boosting models, classification head, saturation regression head, ANN challenger",
    ),
    (
        "Validation and errors",
        "complete-well split, leakage barrier, MAE/RMSE/R2, precision/recall/F1, calibration, OOD lithology, gas/ice/cement lookalikes",
    ),
]

TOPIC_SITE_UPDATES = {
    "thesis_graph": {
        "kicker": "Graph validation",
        "title": "Make every relationship explain its confidence",
        "intro": (
            "The critical-minerals page is strongest when the viewer can tell which graph "
            "links came from sources, which came from AI structure, and which came from "
            "geologic reasoning."
        ),
        "items": [
            ("Solid edge", "source-supported relationship"),
            ("Dotted edge", "AI-suggested relationship to review"),
            ("Orange edge", "geologist reasoning or interpretation"),
            ("Gray edge", "unresolved link or missing evidence"),
        ],
    },
    "seismic": {
        "kicker": "Seismic review loop",
        "title": "Show AI picks as suggestions, not final answers",
        "intro": (
            "The seismic page should make the human override visible: a waveform pick, "
            "confidence band, and event/station map should move together."
        ),
        "items": [
            ("PICK", "arrival line proposed by the workflow"),
            ("CONFIDENCE", "band width shows uncertainty or noise"),
            ("MAP", "event and station geometry updates"),
            ("OVERRIDE", "human accepts, edits, or rejects"),
        ],
    },
    "rock_classification": {
        "kicker": "Label quality gate",
        "title": "Classified maps need reviewed labels before ML claims",
        "intro": (
            "Rock and mineral visuals should show that diagrams, thin sections, and maps "
            "become training evidence only after class quality is checked."
        ),
        "items": [
            ("Known class", "label is supported by visual or geochemical evidence"),
            ("Mixed class", "overlap or ambiguous rock/mineral signal"),
            ("Needs review", "petrography or geochemistry check required"),
            ("Map layer", "candidate output, not final discovery"),
        ],
    },
    "valles": {
        "kicker": "Field-method fusion",
        "title": "Combine evidence without flattening uncertainty",
        "intro": (
            "Valles should show gravity, EM/ERT/TEM, and seismic layers meeting on common "
            "geometry while disagreement remains visible."
        ),
        "items": [
            ("Gravity", "density clue"),
            ("EM / ERT / TEM", "conductivity clue"),
            ("Seismic", "velocity or structural clue"),
            ("Gray conflict", "method disagreement stays unresolved"),
        ],
    },
    "near_surface": {
        "kicker": "New deck-derived topic",
        "title": "Near-Surface Dwellers becomes a shallow-method review board",
        "intro": (
            "The deck is not just another Valles slide source: it focuses on fen-scale "
            "hammer seismic, transient EM, ERT, possible units, and line intersections."
        ),
        "items": [
            ("Hammer seismic", "velocity clue"),
            ("ERT / TEM", "conductivity clue"),
            ("Line intersection", "method comparison checkpoint"),
            ("Possible units", "interpretation needs field review"),
        ],
    },
    "ambient_noise": {
        "kicker": "New deck-derived topic",
        "title": "NoisePy becomes a continuous-data pipeline topic",
        "intro": (
            "The ambient-noise deck adds a software-scale seismic workflow: station noise, "
            "cross-correlations, stacking, monitoring, compute cost, and QC."
        ),
        "items": [
            ("Window", "split continuous station noise"),
            ("CCF", "cross-correlate station pairs"),
            ("Stack", "build stable signals"),
            ("QC", "flag weak or unstable outputs"),
        ],
    },
    "sem_petrography": {
        "kicker": "New deck-derived topic",
        "title": "SEM petrography becomes a microscopic-label topic",
        "intro": (
            "The SEM deck is stronger as its own AI question because it connects image "
            "texture, mineral form, detrital/authigenic context, and climate proxy claims."
        ),
        "items": [
            ("SEM image", "microscopic visual evidence"),
            ("Clay form", "kaolinite and mineral texture labels"),
            ("Context", "detrital versus authigenic distinction"),
            ("Proxy claim", "expert-reviewed interpretation"),
        ],
    },
}

SLIDE_SOURCE_UPDATES = {
    "north_slope": [
        ("FINAL 9-slide North Slope deck", "use the June 11 ML parameter architecture revision, including slide 4 parameter grid and slide 7 decision map"),
        ("Gas hydrate doc", "pull wording for public data, well logs, methodology, and validation"),
    ],
    "thesis_graph": [
        ("Thesis Ch.1 / REE deck", "crop graph, map, spider diagram, and deposit-model regions instead of showing full slides"),
    ],
    "seismic": [
        ("EarthScope and exploration seismology decks", "replace generic seismic visuals with waveform, field, and notebook-method proof"),
        ("NoisePy", "promoted to its own ambient-noise topic"),
    ],
    "rock_classification": [
        ("SEM petrography deck", "promoted to its own microscopic-label and climate-proxy topic"),
        ("Thin-section/classification slides", "crop to the rock/mineral examples and map outputs"),
    ],
    "valles": [
        ("SAGE / Valles deck", "use method-comparison figures and field-context slides"),
        ("Alaska Seismotech portfolio", "use only if it clarifies applied geophysics value"),
        ("Near-Surface Dwellers", "promoted to its own shallow geophysics topic"),
    ],
    "near_surface": [
        ("Near-Surface Dwellers Presentation", "use fen context, hammer seismic, transient EM, possible units, and line-intersection slides"),
    ],
    "ambient_noise": [
        ("NoisePy", "use ambient-noise station windows, CCF, stack, monitoring, and compute/QC slides"),
    ],
    "sem_petrography": [
        ("SEM petrography", "use SEM theory, clay-mineral examples, detrital/authigenic distinction, and kaolinite proxy reasoning"),
    ],
}

MOTION_SKETCH_PRIORITIES = [
    (
        "Earthquake globe loop",
        "Recover or rebuild the globe motion with event dots, depth color, magnitude pulses, and time arc.",
    ),
    (
        "North Slope decision loop",
        "Animate public sources entering a structural block, then branching into review targets.",
    ),
    (
        "Seismic pick-confidence loop",
        "Move a pick line across a waveform while confidence and map context update.",
    ),
]

DETAILED_TOPIC_PLANS = {
    "ai_workflow": {
        "title": "Teaching AI Agents Scientific Software",
        "question": "Can screenshots, traces, and rubrics teach agents to use scientific tools responsibly?",
        "anchor": "Handshake/QGIS/ParaView/Vagon work becomes an example of human demonstration plus output checking.",
        "conclusion": "Agents need demonstrations, task traces, and domain rubrics before they are useful in scientific software.",
        "techniques": ["GUI agents", "imitation learning", "rubric-based workflow evaluation"],
        "inputs": ["screenshots", "click paths", "prompts", "terminal logs", "expected outputs", "expert rubrics"],
        "outputs": ["replayable workflows", "success/failure labels", "agent scorecards"],
        "bottleneck": "Repetitive scientific software work is hard to automate because success is visual, file-dependent, and domain-specific.",
        "validate": "A human still checks layer state, CRS, scientific output quality, and whether the task was actually solved.",
        "storyboard": ["random action dots drift", "a cursor trail captures useful steps", "rubric gates light up", "agent replay trail completes"],
        "labels": ["demo", "trace", "rubric", "replay", "verify"],
        "do_not_claim": "Do not claim Codex can already replace trained GIS or visualization users.",
    },
    "thesis_graph": {
        "title": "Critical Minerals Knowledge Graphs",
        "question": "Can AI move from organizing mineral research to helping ask better questions?",
        "anchor": "REE thesis, Adobe paragenesis drawings, CSV nodes/children, Gephi, and future Neo4j/GraphRAG are the example path.",
        "conclusion": "AI can structure research, but novelty depends on better schemas, evidence, and geologic judgment.",
        "techniques": ["GraphRAG", "relation extraction", "graph embeddings/GNNs"],
        "inputs": ["papers", "deposit names", "mineral phases", "host rocks", "fluid stages", "geochemistry", "evidence links"],
        "outputs": ["queryable graph", "candidate links", "evidence-backed questions"],
        "bottleneck": "Critical-mineral knowledge is scattered across papers, maps, slides, tables, and expert memory.",
        "validate": "A human still checks entity names, paragenesis, deposit analogs, inferred links, and source support.",
        "storyboard": ["scattered mineral/entity dots", "prompt pulse sorts clusters", "edges grow between evidence nodes", "unknown future-question edges glow"],
        "labels": ["paper", "mineral", "stage", "evidence", "unknown"],
        "do_not_claim": "Do not claim GraphRAG discovers deposits by itself.",
    },
    "processing_earthquake": {
        "title": "Earthquake Globe As Scientific Visualization",
        "question": "Can AI help geoscience data become something people can see, hear, and discuss?",
        "anchor": "The Processing earthquake globe video/poster is the first AI-assisted visualization example.",
        "conclusion": "Visualization can make scientific patterns discussable before they become formal analysis.",
        "techniques": ["event clustering", "anomaly detection", "AI narration/summarization"],
        "inputs": ["event time", "latitude/longitude", "depth", "magnitude", "region metadata"],
        "outputs": ["clusters", "unusual-event flags", "narrated visual summaries"],
        "bottleneck": "Geoscience catalogs can be correct but hard for non-specialists to inspect or care about.",
        "validate": "A human still checks tectonic interpretation and whether the visual emphasis distorts risk.",
        "storyboard": ["empty dark globe", "synthetic event dots appear", "rings pulse by magnitude", "timeline orbit sweeps"],
        "labels": ["event", "depth", "magnitude", "cluster", "story"],
        "do_not_claim": "Do not claim seismic forecasting or hazard prediction.",
    },
    "seismic": {
        "title": "Seismic Processing With Visible Uncertainty",
        "question": "What should AI simplify first in seismic workflows without hiding uncertainty?",
        "anchor": "Pondicherry notebooks and waveform/2D seismic visuals anchor the example.",
        "conclusion": "AI should reduce repetitive picking and QA while keeping weak signals visible.",
        "techniques": ["phase-picking models", "seismic foundation models", "uncertainty calibration"],
        "inputs": ["waveforms", "picks", "station geometry", "labels", "noisy examples", "analyst corrections"],
        "outputs": ["suggested picks", "confidence bands", "QA flags"],
        "bottleneck": "Manual seismic review is slow, repetitive, and easy to make less reproducible than intended.",
        "validate": "A human still checks arrivals, processing parameters, event context, and geological plausibility.",
        "storyboard": ["noisy wave traces scroll", "vertical scanner passes", "green/yellow/red picks appear", "clean interpretation path emerges"],
        "labels": ["noise", "pick", "confidence", "QA", "override"],
        "do_not_claim": "Do not claim fully automated seismic interpretation.",
    },
    "north_slope": {
        "title": "AI Energy Screening From Public Data",
        "question": "How far can AI take public energy data before experts must step in?",
        "anchor": "Alaska North Slope hydrate atlas, shapefiles, Open Science Lab, GitHub, and Streamlit/Plotly 3D map ideas anchor the example.",
        "conclusion": "AI can organize screening, but trusted energy decisions require provenance, physics, and expert review.",
        "techniques": ["well-log classification", "explainable interval ranking", "physics-informed ML"],
        "inputs": ["wells", "logs", "hydrate intervals", "shapefiles", "papers", "formations", "depth references"],
        "outputs": ["ranked intervals", "map layers", "provenance-backed review targets"],
        "bottleneck": "Early energy screening is slowed by public data scattered across reports, GIS layers, logs, and assumptions.",
        "validate": "A human still checks hydrate indicators, stratigraphy, economic relevance, source provenance, and uncertainty.",
        "storyboard": ["messy source layers float in", "layers stack into a 3D block", "wells drop vertically", "decision funnel sorts targets"],
        "labels": ["GIS", "logs", "hydrate", "provenance", "review"],
        "do_not_claim": "Do not claim investment-grade resource assessment.",
    },
    "rock_classification": {
        "title": "Visual Geoscience Classification To Resource Maps",
        "question": "Could AI connect rock properties, surveys, and labels into better resource maps?",
        "anchor": "Rock classification ranges, geochemistry plots, shapefile grids, ArcGIS, and 3D resource mapping ideas anchor the example.",
        "conclusion": "AI can help combine variables, but classification only matters if labels and geologic context are trustworthy.",
        "techniques": ["multimodal classification", "spatial feature fusion", "GNN lithology/prospectivity models"],
        "inputs": ["density", "velocity", "resistivity", "chemistry", "formations", "survey grids", "expert labels"],
        "outputs": ["class probabilities", "overlap maps", "candidate resource zones"],
        "bottleneck": "Many survey and property variables are hard to combine into one map that experts can audit.",
        "validate": "A human still checks training labels, thresholds, false positives, and geologic feasibility.",
        "storyboard": ["colored property particles move", "range gates filter variables", "overlap clusters form", "clusters snap into an extruded grid"],
        "labels": ["density", "velocity", "chemistry", "overlap", "map"],
        "do_not_claim": "Do not claim automated mineral discovery.",
    },
    "valles": {
        "title": "Comparing Imperfect Geophysical Surveys",
        "question": "How should AI compare surveys without flattening uncertainty?",
        "anchor": "SAGE/Valles Caldera gravity, EM/TEM/ERT, seismic, and field geophysics anchor the example.",
        "conclusion": "AI can help align methods, but unresolved zones should stay unresolved.",
        "techniques": ["data fusion", "anomaly segmentation", "uncertainty tagging"],
        "inputs": ["gravity grids", "EM/ERT responses", "seismic lines", "station spacing", "metadata", "field notes"],
        "outputs": ["overlap zones", "conflict zones", "confidence masks"],
        "bottleneck": "Teams must compare instruments with different resolution, sensitivity, noise, and field constraints.",
        "validate": "A human still checks whether overlaps are real geology or acquisition/processing artifacts.",
        "storyboard": ["separate translucent fields", "fields slide together", "agreement zones pulse", "gray unresolved zones remain"],
        "labels": ["gravity", "EM", "seismic", "agree", "uncertain"],
        "do_not_claim": "Do not claim one unified true subsurface model.",
    },
    "near_surface": {
        "title": "Near-Surface Field Methods With Visible Conflict",
        "question": "Can AI compare shallow geophysical methods without erasing disagreement?",
        "anchor": "The Near-Surface Dwellers deck anchors hammer seismic, transient EM, ERT, Valles fen context, possible units, and line intersections.",
        "conclusion": "AI can organize shallow-method evidence, but method conflict and possible units need to remain reviewable.",
        "techniques": ["cross-method registration", "line-intersection QA", "uncertainty tagging"],
        "inputs": ["hammer seismic lines", "ERT sections", "TEM context", "fen maps", "possible units", "field notes"],
        "outputs": ["method-overlap board", "conflict zones", "reviewed unit candidates"],
        "bottleneck": "Near-surface surveys differ in sensitivity and geometry, so simple overlays can make disagreement look resolved.",
        "validate": "A human still checks line geometry, field constraints, acquisition artifacts, unit labels, and whether methods are actually comparable.",
        "storyboard": ["fen cross-section appears", "seismic and ERT layers slide in", "line intersection glows", "conflict zones stay striped"],
        "labels": ["fen", "seismic", "ERT", "TEM", "conflict"],
        "do_not_claim": "Do not claim the AI found the true shallow geology from method overlays alone.",
    },
    "moho_ml": {
        "title": "Honest Transfer Testing For Moho ML",
        "question": "How do we know a geoscience ML model actually transfers?",
        "anchor": "The supervised ML class project trained on Australia gravity/Moho data and applied it to the USA.",
        "conclusion": "This is the bridge from prompting to real ML: high R-squared is not enough without leakage and spatial transfer checks.",
        "techniques": ["spatial cross-validation", "transfer learning", "residual/error mapping"],
        "inputs": ["gravity features", "Moho labels", "coordinates", "region IDs", "train/test masks", "baseline models"],
        "outputs": ["predictions", "residual maps", "transfer scores", "leakage warnings"],
        "bottleneck": "Geoscience ML can look strong on familiar regions while failing on new geography.",
        "validate": "A human still checks split design, feature leakage, baselines, residual patterns, and geological plausibility.",
        "storyboard": ["left training dots pulse", "model-node chain activates", "right test-region dots appear", "red residual dots flash"],
        "labels": ["train", "test region", "R2?", "residual", "leakage check"],
        "do_not_claim": "Do not claim strong generalization unless spatial validation supports it.",
    },
    "ambient_noise": {
        "title": "Ambient-Noise Seismology As A Scalable Pipeline",
        "question": "Which station-pair correlations are trustworthy enough to monitor?",
        "anchor": "The NoisePy deck anchors continuous records, station windows, cross-correlation, stacking, monitoring, compute scale, and QC.",
        "conclusion": "AI can help triage continuous seismic processing, but correlation quality and parameter choices must stay auditable.",
        "techniques": ["correlation QC", "stack stability checks", "monitoring anomaly review"],
        "inputs": ["continuous waveforms", "station metadata", "noise windows", "station pairs", "processing parameters", "compute logs"],
        "outputs": ["CCF quality flags", "stacked signals", "monitoring summaries", "parameter audit trails"],
        "bottleneck": "Ambient-noise workflows scale quickly into thousands of station pairs and millions of files.",
        "validate": "A human still checks station metadata, preprocessing choices, seasonal effects, unstable stacks, and whether changes are physical.",
        "storyboard": ["continuous traces split into windows", "station-pair arcs form", "strong correlations stack", "weak pairs fall into QC"],
        "labels": ["noise", "window", "CCF", "stack", "monitor"],
        "do_not_claim": "Do not claim every correlation is a geologic signal.",
    },
    "stock_workflow": {
        "title": "Codex, Pipelines, And Honest App Building",
        "question": "Can Codex help young builders make useful apps without fooling themselves?",
        "anchor": "The stock dashboard, local downloads, GitHub/cloud workflow, Streamlit, and leakage correction anchor the example.",
        "conclusion": "AI speeds app building, but human ML judgment is needed to block fake performance.",
        "techniques": ["automated pipelines", "model monitoring", "leakage detection"],
        "inputs": ["notebooks", "CSVs", "commit history", "train/test dates", "model metrics", "refresh logs"],
        "outputs": ["reproducible app", "pipeline status", "flagged evaluation risks"],
        "bottleneck": "It is now easy to ship an app and also easy to make the model evaluation look better than it is.",
        "validate": "A human still checks evaluation design, metric meaning, data splits, and deployment claims.",
        "storyboard": ["chaotic files rain into Codex", "GitHub branches split", "Streamlit panels appear", "red leakage gate blocks bad scores"],
        "labels": ["files", "Codex", "GitHub", "dashboard", "leakage gate"],
        "do_not_claim": "Do not claim reliable prediction just because the dashboard runs.",
    },
    "sem_petrography": {
        "title": "SEM Petrography Labels And Proxy Claims",
        "question": "Can AI label SEM textures without overclaiming climate meaning?",
        "anchor": "The SEM petrography deck anchors carbonates/evaporites/clays, detrital versus authigenic interpretation, kaolinite morphology, and paleoclimate proxy reasoning.",
        "conclusion": "AI can help organize microscopic labels, but proxy interpretation needs literature support and expert petrography.",
        "techniques": ["multimodal image labeling", "literature-linked feature definitions", "expert review queues"],
        "inputs": ["SEM image crops", "mineral labels", "morphology classes", "lake/environment context", "literature claims", "expert notes"],
        "outputs": ["reviewed texture labels", "proxy-claim audit trail", "candidate training examples"],
        "bottleneck": "A texture label can be visually plausible while the environmental interpretation is unsupported or context-dependent.",
        "validate": "A human still checks whether labels are visible, whether minerals are detrital or authigenic, and whether proxy claims follow from the evidence.",
        "storyboard": ["SEM field of view scans", "candidate labels snap to grains", "proxy branches appear", "review gate rejects overclaims"],
        "labels": ["SEM", "texture", "clay", "proxy", "review"],
        "do_not_claim": "Do not claim climate reconstruction from image labels alone.",
    },
}

AI_WORKFLOW_EVIDENCE = {
    "ai_workflow": {
        "description": "Supervised software-use case study for scientific desktop workflows.",
        "chips": ["QGIS/Vagon screens", "Rubric checks", "Agent demos"],
        "where": "Codex/ChatGPT helped inspect screenshots, organize task evidence, and turn workflow recordings into evaluation-ready examples.",
        "gave": "Screen recordings, QGIS/ParaView/Vagon task context, pass/fail rubrics, screenshots, and expected output descriptions.",
        "produced": "A clearer workflow story, project-room structure, evidence panels, and future agent-evaluation framing.",
        "validated": "Whether the software output was actually usable: layer state, CRS, map quality, task completion, and domain-specific acceptance criteria.",
        "future": "Future agents would learn from human demonstrations, replay steps in real software, and explain where a workflow failed.",
    },
    "thesis_graph": {
        "description": "REE thesis notes become graph structure and visual research communication.",
        "chips": ["Node/edge tables", "Adobe REE visuals", "Gephi/Neo4j path"],
        "where": "AI helped translate literature notes and thesis structure into graph categories, relationship types, and presentation-ready visual language.",
        "gave": "Thesis slides, REE notes, Gephi exports, literature concepts, manual spreadsheet rows, and Bayan Obo/Mountain Pass comparison goals.",
        "produced": "Node/edge schema ideas, cleaned story order, Adobe-style graph visuals, and a future Neo4j/graph-ML pipeline.",
        "validated": "Entity names, deposit interpretation, inferred versus observed relationships, and whether graph edges made geologic sense.",
        "future": "Manual spreadsheet -> AI-assisted graph schema -> Gephi/Adobe visualization -> Neo4j graph database -> graph ML relationship ranking.",
    },
    "processing_earthquake": {
        "description": "Origin story: first AI-assisted creative geoscience visualization.",
        "chips": ["USGS events", "3D globe poster", "Sonification"],
        "where": "AI helped frame the Processing sketch as a scientific visualization workflow rather than a standalone creative code artifact.",
        "gave": "USGS earthquake attributes, Processing visualization intent, LinkedIn poster evidence, and the need to recover the correct video.",
        "produced": "A verified poster-first presentation and a rebuild plan for a reproducible web visualization.",
        "validated": "The local video candidate was not the correct earthquake export; only the LinkedIn poster/video evidence is verified for now.",
        "future": "A future version would rebuild the globe in Streamlit or Three.js with reproducible data pulls, filters, uncertainty, and narration.",
    },
    "seismic": {
        "description": "Notebook outputs become a reproducible seismic interpretation workflow.",
        "chips": ["ObsPy notebook", "Waveform QA", "Velocity maps"],
        "where": "AI helped explain notebook cells, choose presentation-worthy outputs, and connect seismic figures to an ML-ready workflow.",
        "gave": "Waveform notebooks, station/event context, annotated seismic panels, training slides, and velocity-analysis goals.",
        "produced": "Cleaner notebook narrative, visual evidence selection, and a roadmap for arrival picking and uncertainty reporting.",
        "validated": "Arrival picks, station geometry assumptions, waveform quality, geologic interpretation, and hydrogeologic relevance.",
        "future": "A future model would assist with arrival picks, QA flags, event triage, and reproducible uncertainty summaries.",
    },
    "north_slope": {
        "description": "Public geoscience sources become an interactive hydrate-screening atlas.",
        "chips": ["3D Plotly map", "Source library", "Wireline ML scaffold"],
        "where": "AI helped organize public Alaska geoscience sources, large GIS shapefiles, hydrate/wireline ideas, Open Science Lab/GitHub workflow context, and Streamlit app structure.",
        "gave": "Open Science Lab/GitHub context, geology shapefiles, gas-hydrate papers, wireline-variable notes, map ideas, cross-section goals, and screenshots.",
        "produced": "A current interactive atlas, static screenshot thumbnails, ML presentation scaffold, and a clearer discussion of how public energy data could become screening infrastructure.",
        "validated": "Layer meaning, geologic plausibility, source provenance, hydrate assumptions, and what features an expert would trust.",
        "future": "A future ML screen would connect wells, depths, hydrate indicators, stratigraphy, wireline curves, synclines, rock types, and source confidence into expert-reviewed energy target ranking.",
    },
    "rock_classification": {
        "description": "Rock, petrography, and geochemistry visuals become labeled ML examples.",
        "chips": ["Classification maps", "Thin sections", "Geochemical charts"],
        "where": "AI helped organize rock-property ranges, overlap charts, classification outputs, and the idea of mapping instrument properties to rock properties.",
        "gave": "Chemical ranges, mineral/rock labels, thin-section slides, formation maps, shapefile-derived grids, raster outputs, and geochemical interpretation goals.",
        "produced": "Classification visuals, overlap/range reasoning, embedded map panels, dataset framing, and an ArcGIS/3D resource-mapping roadmap.",
        "validated": "Rock labels, formation context, petrographic interpretation, chart reading, and which examples are reliable enough for training.",
        "future": "A future workflow could combine seismic, EM, MT, gravity, geochemistry, formation labels, and expert review to build surface and subsurface resource maps.",
    },
    "valles": {
        "description": "Field geophysics figures become an AI-assisted interpretation review loop.",
        "chips": ["Gravity maps", "SAGE slides", "Uncertainty review"],
        "where": "AI helped organize field/project evidence and connect map outputs to cross-method interpretation questions.",
        "gave": "Gravity, free-air, Moho, SAGE deck images, field context, and geophysical interpretation goals.",
        "produced": "A visual case-study room and a roadmap for a future field-data comparison dashboard.",
        "validated": "Instrument limits, anomaly interpretation, terrain constraints, uncertainty, and whether map comparisons were geologically defensible.",
        "future": "A future system would compare geophysical products side by side while preserving method uncertainty and expert comments.",
    },
    "near_surface": {
        "description": "Near-Surface Dwellers deck becomes a field-method comparison workflow.",
        "chips": ["Hammer seismic", "ERT/TEM", "Line intersections"],
        "where": "AI helped separate this from the broader Valles topic because the deck focuses on fen-scale shallow methods and possible units.",
        "gave": "Near-Surface Dwellers slides, Valles fen context, hammer seismic, transient EM, ERT/seismic line intersections, and possible geologic unit labels.",
        "produced": "A new topic room about comparing shallow geophysical methods while preserving conflict and uncertainty.",
        "validated": "Survey geometry, line intersections, possible units, method limits, and whether agreement is real or just an overlay artifact.",
        "future": "A future tool would align shallow survey lines, expose conflicts, and let experts approve unit interpretations.",
    },
    "moho_ml": {
        "description": "A real supervised ML example becomes a discussion about transfer, leakage, and reproducibility.",
        "chips": ["Gravity inputs", "ANN-style model", "Transfer test"],
        "where": "AI can now help recover, explain, document, and stress-test a past machine-learning project instead of leaving it as a hidden class notebook.",
        "gave": "aus.moho.ipynb, australian.moho, australian.py, machinelearningreport.docx, gravity/Moho variables, and the Australia-to-USA transfer goal.",
        "produced": "A new topic room that separates actual past ML from future speculative AI workflows.",
        "validated": "Train/test boundaries, model leakage, whether R2 means anything on unseen geography, and whether the prediction makes geologic sense.",
        "future": "A current version would compare ANN, tree ensembles, Gaussian/process-style uncertainty, spatial cross-validation, and residual maps before claiming it works.",
    },
    "ambient_noise": {
        "description": "NoisePy deck becomes a continuous-data seismic pipeline topic.",
        "chips": ["Noise windows", "CCF", "Stack/QC"],
        "where": "AI helped identify this as a separate workflow: station-pair processing and monitoring are different from one-off seismic picking.",
        "gave": "NoisePy slides, ambient-noise seismology framing, station-window steps, cross-correlation, stacking, monitoring, and compute/QC details.",
        "produced": "A new topic room about using AI to manage continuous seismic processing at scale.",
        "validated": "Station metadata, preprocessing choices, pair quality, stack stability, compute assumptions, and whether monitoring changes are physical.",
        "future": "A future assistant would flag weak correlations, summarize parameter choices, and document why a station pair was trusted or rejected.",
    },
    "stock_workflow": {
        "description": "Codex turns scattered local analysis into a tracked app-building workflow.",
        "chips": ["Local files", "GitHub/cloud", "Model risk"],
        "where": "Codex helped organize local downloads, inspect existing notebook outputs, build Streamlit views, debug charts, and make GitHub/cloud workflow ideas feel reachable.",
        "gave": "Downloads folders, notebook outputs, chart goals, app ideas, pipeline files, and questions about model testing and evaluation leakage.",
        "produced": "A working app/pipeline example and a discussion topic about AI, money, young builders, and honest model evaluation.",
        "validated": "Whether model tests use truly unseen data, whether results are biased by leakage, and whether the app is a tool rather than a financial claim.",
        "future": "A future version would run tracked pipelines through GitHub/cloud or virtual desktops, separate training/evaluation windows, and keep model claims honest.",
    },
    "sem_petrography": {
        "description": "SEM petrography deck becomes a microscopic-label and proxy-claim topic.",
        "chips": ["SEM textures", "Clay labels", "Proxy review"],
        "where": "AI helped split SEM petrography from the general rock-classification topic because it is about microscopic evidence and interpretation boundaries.",
        "gave": "SEM petrography slides, clay-mineral examples, detrital/authigenic distinctions, kaolinite morphology notes, and paleoclimate proxy reasoning.",
        "produced": "A new topic room about how image AI could support petrography without overclaiming climate interpretation.",
        "validated": "Visible texture labels, mineral context, detrital/authigenic distinction, literature support, and expert petrographic judgment.",
        "future": "A future workflow would pair SEM crops, reviewed labels, literature snippets, and expert decisions into a multimodal training/evaluation set.",
    },
}

EMAIL_TOPIC_ROOM_OVERRIDES = {
    "ai_workflow": {
        "title": "Prompting, Rubrics, And Agent Training",
        "tagline": "Human prompts, rubrics, and screen-recorded scientific software work become supervised examples for future agents.",
        "hero": "assets/topic_visuals/agent_supervised_workflows.svg",
        "theme": "Prompt/rubric -> virtual software work -> supervised ML for scientific agents.",
        "bottleneck": "The bottleneck is workforce time: people still do repetitive software labor by hand before they can move into higher-level leadership and project design.",
        "why_not_done": "Agents do not learn enough from final screenshots alone. They need the prompt, the rubric, the screen recording, the files, the mistakes, and the human judgement that says the output worked.",
        "ai_used": "ChatGPT and Codex help turn prompts, screenshots, rubrics, and virtual software recordings into structured examples for supervised agent training.",
        "future_ai": "Humans write the prompts and goals; agents execute workflows in QGIS, ParaView, 3D Slicer, KiCad, and similar tools with less supervision over time.",
        "why_it_matters": "If agents can run labor-heavy software tasks, people can spend more time leading new projects in energy, commerce, agriculture, and field operations.",
        "proof": ["Prompt/rubric screenshots", "Screen-recorded virtual work", "QGIS and ParaView examples", "Agent-training workflow diagram"],
        "question": "Will screenshots and ChatGPT prompting be replaced by Codex?",
    },
    "thesis_graph": {
        "title": "AI Knowledge Graphs And Project Diagrams",
        "tagline": "Tables, questions, and scientific drawings become knowledge graphs, ML architecture diagrams, and clearer research explanations.",
        "hero": "assets/topic_visuals/knowledge_architecture_ai.svg",
        "theme": "Many inputs -> AI/ML structure -> graph, architecture, and visual explanation.",
        "bottleneck": "Critical-mineral research becomes wordy and scattered when the relationships live only in papers, notes, and slide text.",
        "why_not_done": "The hard work is deciding what the variables are, which relationships have evidence, and which AI-suggested links still need a geologist to review them.",
        "ai_used": "AI helps convert tables, CSVs, drawings, and project questions into graph structures and visual architectures that are easier to inspect.",
        "future_ai": "More accurate critical-mineral workflows could use AI to connect variables, show uncertainty, and build visual programs for complex accumulation questions.",
        "why_it_matters": "Project architecture is easier to understand when people can see how variables connect instead of reading a wall of text.",
        "proof": ["REE thesis deck", "Adobe-style deposit drawings", "Gephi graph exports", "Node and edge tables"],
        "question": "Knowledge graphs and diagrams built using AI: are they the next way to understand project architectures?",
    },
    "processing_earthquake": {
        "title": "AI Visualization For Prediction Variables",
        "tagline": "A Processing earthquake globe becomes the example for turning spatial events into model-ready variables.",
        "hero": "assets/topic_visuals/data_variable_transform.svg",
        "theme": "Prompt -> Processing code -> 3D visual -> 2D time-window variables.",
        "bottleneck": "Earthquake catalogs are hard to model directly when location, depth, magnitude, and time are all tangled in a 3D visual problem.",
        "why_not_done": "The first version was creative and useful for seeing patterns, but prediction work needs repeatable features, time windows, and honest limits.",
        "ai_used": "The user asked ChatGPT to write Processing code that maps earthquake locations onto a globe, then iterated with AI until the sketch worked.",
        "future_ai": "AI can help convert the original 3D visualization into 2D-over-time variables for linear and nonlinear regression experiments.",
        "why_it_matters": "The real topic is not only a cool globe. It is how AI can reshape messy data into variables that models can test.",
        "proof": ["Processing earthquake globe", "USGS event attributes", "ChatGPT coding loop", "future feature-conversion diagram"],
        "question": "Can we use AI to visualize data into new variables for prediction models?",
    },
    "seismic": {
        "title": "Large Data Processing Streamlined With AI",
        "tagline": "Codex, GitHub, and cloud workspaces make large seismic and satellite datasets easier to process, share, and review.",
        "project_key": "pondicherry",
        "hero": "assets/topic_visuals/cloud_data_processing.svg",
        "theme": "Phone prompt -> Codex -> GitHub -> cloud compute -> collaborative science output.",
        "bottleneck": "Large scientific datasets can keep people waiting at one machine instead of moving the workflow through cloud computers and version control.",
        "why_not_done": "The files are big, the environments are fragile, and collaboration is slow when processing lives only in a local notebook or desktop folder.",
        "ai_used": "Codex can inspect code, edit notebooks, run tasks in virtual/cloud environments, and help commit/push reproducible processing steps.",
        "future_ai": "People could start or monitor large workflows from a phone while OpenScienceLab, Alaska Satellite Facility cloud tools, or other virtual machines handle the heavy processing.",
        "why_it_matters": "The AI advance is practical access: process, document, and collaborate faster without waiting at one computer.",
        "proof": ["Seismic notebook evidence", "OpenScienceLab workflow idea", "Alaska Satellite Facility cloud idea", "GitHub collaboration path"],
        "question": "How can Codex make large scientific data processing faster from cloud workspaces?",
    },
    "north_slope": {
        "title": "Using AI For Web Scraping Public Energy Data",
        "tagline": "AI helps find public subsurface maps, shapefiles, reports, and APIs, then organizes them into one screening workspace.",
        "hero": "assets/project_visuals/north_slope_3d_streamlit_plotly_map.png",
        "theme": "Public web search -> scraper/API organization -> source library -> Streamlit well scaffold.",
        "bottleneck": "Public North Slope material is scattered across maps, PDFs, shapefiles, state/federal sources, and project notes.",
        "why_not_done": "The hard part is not one map. It is finding the sources, preserving provenance, cleaning names and coordinates, and making a public-safe scaffold without exposing restricted well data.",
        "ai_used": "AI helps scour the web for public subsurface maps and shapefiles, organize API/source pulls, and turn them into Streamlit visuals and source libraries.",
        "future_ai": "A stronger version would scrape and organize public data into a live workspace with well skeletons, 3D context, and source-confidence flags.",
        "why_it_matters": "For energy screening, the useful AI skill is turning fragmented public evidence into a workspace experts can actually review.",
        "proof": ["North Slope Streamlit map", "well scaffold concept", "public source library", "gas hydrate ML planning docs"],
        "question": "How can AI scrape and organize public subsurface sources into one usable workspace?",
    },
    "rock_classification": {
        "title": "Rock Type Classification From Satellite Variables",
        "tagline": "Satellite and GIS variables become reviewed rock-type classes, with critical-mineral visuals used as explanation support.",
        "hero": "assets/topic_visuals/satellite_rock_classification.svg",
        "theme": "ADV GIS variables + satellite layers + classifier + reviewed resource-map output.",
        "bottleneck": "Rock classification from remote sensing can look clean while hiding mixed pixels, bad labels, and weak validation.",
        "why_not_done": "Satellite variables, terrain context, and map labels need review before a classifier can be trusted. Geochemical plots can explain complexity, but they are not the same as satellite features.",
        "ai_used": "AI helps organize ADV GIS-style satellite variables, compare feature groups, simplify the verbal story, and keep uncertainty visible.",
        "future_ai": "Future models could combine satellite bands, DEM derivatives, structures, and reviewed labels to improve rock-type maps.",
        "why_it_matters": "This makes the topic about AI advances in classification, not just a list of old project artifacts.",
        "proof": ["ADV GIS final presentation", "satellite variables", "critical-mineral heatmaps and spider diagrams", "reviewed map outputs"],
        "question": "Can AI classify rock types from satellite variables more accurately?",
    },
    "valles": {
        "title": "AI For Field Geophysics Method Comparison",
        "tagline": "Near-surface Valles evidence replaces the unrelated person image with graphs, lines, methods, and uncertainty.",
        "hero": "assets/project_visuals/valles_bouguer.png",
        "theme": "Hammer seismic + TEM/ERT + gravity context + field uncertainty.",
        "bottleneck": "Field teams need to compare imperfect surveys without pretending one method gives the final answer.",
        "why_not_done": "Each method sees different physics at different resolution, and field errors, line geometry, and possible units complicate the comparison.",
        "ai_used": "AI helps organize the Near-Surface Dwellers deck into a method-comparison board with seismic, ERT/TEM, line intersections, and possible units.",
        "future_ai": "A stronger tool would let reviewers compare methods side by side, flag conflicts, and keep uncertain zones visible.",
        "why_it_matters": "The topic becomes a real field-geophysics question instead of a generic SAGE profile page.",
        "proof": ["Near-Surface Dwellers deck", "Valles fen lines", "ERT/TEM comparisons", "seismic processing panels"],
        "question": "How should AI compare imperfect geophysical surveys without flattening uncertainty?",
    },
    "moho_ml": {
        "title": "ML Architecture For Gas Hydrate Prediction",
        "tagline": "North Slope ML slides and documents become a clear architecture: public-safe inputs, feature lanes, models, validation, and leakage gates.",
        "project_key": "north_slope",
        "hero": "assets/topic_visuals/north_slope_ml_architecture.svg",
        "theme": "Well-log scaffold -> feature separation -> classification/regression/ANN -> held-out wells.",
        "bottleneck": "ML can look impressive while leaking target information or testing on depth samples too close to the training data.",
        "why_not_done": "A trustworthy hydrate model needs skeleton well data, normalized public-safe features, separate target lanes, and validation by complete wells.",
        "ai_used": "AI helps turn the North Slope Word doc, updated slides, and hydrate ML paper into a model architecture diagram that explains why ML is the backbone.",
        "future_ai": "A stronger implementation would compare a baseline, classification for hydrate occurrence, regression for saturation, and an ANN challenger under held-out-well validation.",
        "why_it_matters": "This shows how AI workflows become actual ML systems: inputs, leakage controls, validation, and human review.",
        "proof": ["Updated North Slope Word doc", "updated North Slope slides", "Chong et al. ANN gas hydrate paper", "public-safe well-log scaffold"],
        "question": "What ML architecture can predict hydrate occurrence and saturation without leaking target data?",
    },
    "stock_workflow": {
        "title": "Current Stock Prediction App Workflow",
        "tagline": "Use the updated Streamlit stock app visuals to explain AI app building, pipeline organization, and model-risk honesty.",
        "hero": "assets/project_visuals/stock_all_tickers_chart.svg",
        "theme": "Codex app building + Streamlit visuals + GitHub workflow + model-risk gate.",
        "bottleneck": "AI can make an app quickly, but finance-looking dashboards can mislead people if model evaluation is weak.",
        "why_not_done": "The old public navigator visual made this look like a stale stock-prediction project instead of a current AI-assisted app-building workflow.",
        "ai_used": "Codex helped inspect the local app, organize files, update Streamlit visuals, and frame model leakage/testing as part of the story.",
        "future_ai": "A stronger version would track refreshes, separate training and unseen evaluation data, monitor drift, and make the app useful without overstating prediction power.",
        "why_it_matters": "This is a relatable example of AI-assisted app building: the app works, but the claims still need human judgement.",
        "proof": ["updated Streamlit stock app", "all-tickers chart", "saved-data chart", "model-risk notes"],
        "question": "How can the current stock prediction app show AI app building without hiding model risk?",
    },
}

EMAIL_FRAME_OVERRIDES = {
    "ai_workflow": {
        "question": "Will screenshots and ChatGPT prompting be replaced by Codex?",
        "example": "Prompt/rubric screenshots plus screen-recorded scientific software work are the example.",
        "raise": "AI advance: supervised training data for agents, not generic demos.",
        "pattern": ["prompt", "rubric", "record", "agent"],
    },
    "thesis_graph": {
        "question": "Can AI-built graphs and diagrams explain project architecture?",
        "example": "Tables, project questions, and Adobe drawings become graph and ML architecture views.",
        "raise": "AI advance: words become structures people can inspect.",
        "pattern": ["tables", "questions", "AI", "graph"],
    },
    "processing_earthquake": {
        "question": "Can AI visualize data into new variables for prediction models?",
        "example": "The ChatGPT-to-Processing earthquake globe is the example.",
        "raise": "AI advance: a 3D visual problem becomes model-ready time features.",
        "pattern": ["events", "globe", "features", "model"],
    },
    "seismic": {
        "question": "Can Codex streamline large data processing in cloud workspaces?",
        "example": "Seismic and satellite-scale workflows are the example.",
        "raise": "AI advance: cloud compute, GitHub, and Codex reduce local waiting.",
        "pattern": ["phone", "Codex", "cloud", "GitHub"],
    },
    "north_slope": {
        "question": "Can AI scrape public sources into one energy-data workspace?",
        "example": "North Slope maps, shapefiles, APIs, and well skeletons are the example.",
        "raise": "AI advance: web scraping plus source organization becomes a public-data workbench.",
        "pattern": ["web", "sources", "scrape", "map"],
    },
    "rock_classification": {
        "question": "Can AI classify rock types from satellite variables?",
        "example": "ADV GIS satellite variables and reviewed rock maps are the example.",
        "raise": "AI advance: remote-sensing variables become reviewed map classes.",
        "pattern": ["satellite", "features", "class", "review"],
    },
    "valles": {
        "question": "How should AI compare imperfect geophysical surveys?",
        "example": "Near-Surface Dwellers seismic, ERT, TEM, and Valles line intersections are the example.",
        "raise": "AI advance: compare methods while uncertainty stays visible.",
        "pattern": ["seismic", "ERT", "TEM", "uncertain"],
    },
    "moho_ml": {
        "question": "What ML architecture predicts hydrates without leakage?",
        "example": "North Slope well-log inputs and complete-well validation are the example.",
        "raise": "AI advance: project notes become an actual model architecture.",
        "pattern": ["inputs", "features", "models", "validation"],
    },
    "stock_workflow": {
        "question": "Can the current stock app teach honest AI app building?",
        "example": "The updated Streamlit stock dashboard is the example.",
        "raise": "AI advance: app building plus model-risk checks, not a stale prediction screenshot.",
        "pattern": ["Streamlit", "Codex", "risk", "GitHub"],
    },
}

EMAIL_AI_LEVER_OVERRIDES = {
    "ai_workflow": "AI use: prompts and recordings become supervised agent-training examples.",
    "thesis_graph": "AI use: tables and drawings become graphs, diagrams, and architecture maps.",
    "processing_earthquake": "AI use: visualization reshapes raw events into model-ready variables.",
    "seismic": "AI use: Codex moves large data work into cloud and GitHub workflows.",
    "north_slope": "AI use: web scraping organizes public energy data into one workspace.",
    "rock_classification": "AI use: satellite variables become reviewed rock-type classifications.",
    "valles": "AI use: survey methods are compared without hiding uncertainty.",
    "moho_ml": "AI use: North Slope notes become a leakage-aware ML architecture.",
    "stock_workflow": "AI use: the current app shows build speed plus model-risk discipline.",
}

EMAIL_VISUAL_OVERRIDES = {
    "ai_workflow": "assets/topic_visuals/agent_supervised_workflows.svg",
    "thesis_graph": "assets/topic_visuals/knowledge_architecture_ai.svg",
    "processing_earthquake": "assets/topic_visuals/data_variable_transform.svg",
    "seismic": "assets/topic_visuals/cloud_data_processing.svg",
    "north_slope": "assets/topic_visuals/web_scraping_data_lake.svg",
    "rock_classification": "assets/topic_visuals/satellite_rock_classification.svg",
    "valles": "assets/topic_visuals/field_geophysics.svg",
    "moho_ml": "assets/topic_visuals/north_slope_ml_architecture.svg",
    "stock_workflow": "assets/project_visuals/stock_saved_data_chart.svg",
}

EMAIL_CARD_VISUAL_OVERRIDES = {
    "ai_workflow": "assets/topic_visuals/agent_supervised_workflows.svg",
    "thesis_graph": "assets/topic_visuals/knowledge_architecture_ai.svg",
    "processing_earthquake": "assets/topic_visuals/data_variable_transform.svg",
    "seismic": "assets/topic_visuals/cloud_data_processing.svg",
    "north_slope": "assets/project_visuals/north_slope_3d_streamlit_plotly_map.png",
    "rock_classification": "assets/topic_visuals/satellite_rock_classification.svg",
    "valles": "assets/project_visuals/valles_bouguer.png",
    "near_surface": "assets/topic_visuals/near_surface_ai.svg",
    "moho_ml": "assets/topic_visuals/north_slope_ml_architecture.svg",
    "stock_workflow": "assets/project_visuals/stock_all_tickers_chart.svg",
}

EMAIL_WORKFLOW_BLUEPRINT_OVERRIDES = {
    "ai_workflow": {
        "title": "prompt -> recording -> supervised agent",
        "steps": [
            ("Prompt", "task + rubric"),
            ("Record", "virtual software work"),
            ("Review", "human judgement"),
            ("Supervised ML", "train agent"),
            ("Agent", "future execution"),
        ],
        "outcome": "Agents learn the work so people can lead bigger projects instead of repeating software labor.",
    },
    "thesis_graph": {
        "title": "inputs -> AI/ML -> project architecture",
        "steps": [
            ("Tables", "CSVs + variables"),
            ("Questions", "project relationships"),
            ("Drawings", "visual ideas"),
            ("AI/ML", "connect structure"),
            ("Graphs", "architecture output"),
        ],
        "outcome": "Complex science becomes a visual structure instead of only a long explanation.",
    },
    "processing_earthquake": {
        "title": "3D visualization -> model variables",
        "steps": [
            ("USGS events", "lat/lon/depth"),
            ("ChatGPT", "Processing code"),
            ("Globe", "visual pattern"),
            ("Features", "2D time windows"),
            ("Regression", "future test"),
        ],
        "outcome": "Visualization becomes a bridge into prediction features, not the final claim.",
    },
    "seismic": {
        "title": "phone prompt -> cloud data run",
        "steps": [
            ("Codex", "start/edit task"),
            ("GitHub", "track work"),
            ("Cloud", "OSL/ASF compute"),
            ("Dataset", "large files"),
            ("Review", "share results"),
        ],
        "outcome": "Large processing can move forward without one person waiting at one machine.",
    },
    "north_slope": {
        "title": "public web -> energy-data workspace",
        "steps": [
            ("Search", "maps + reports"),
            ("Scrape", "shapes + APIs"),
            ("Provenance", "source log"),
            ("Scaffold", "public wells"),
            ("Map", "review workspace"),
        ],
        "outcome": "Public sources become a reviewable North Slope workbench.",
    },
    "rock_classification": {
        "title": "satellite variables -> reviewed rock classes",
        "steps": [
            ("Satellite", "bands + texture"),
            ("GIS", "DEM + context"),
            ("Features", "model inputs"),
            ("Classify", "rock type"),
            ("Review", "uncertainty"),
        ],
        "outcome": "AI helps map rock classes while keeping label quality visible.",
    },
    "valles": {
        "title": "field methods -> uncertainty board",
        "steps": [
            ("Hammer seismic", "velocity"),
            ("ERT", "resistivity"),
            ("TEM", "conductivity"),
            ("Intersect", "line check"),
            ("Review", "possible units"),
        ],
        "outcome": "Field evidence is compared without erasing conflicts.",
    },
    "moho_ml": {
        "title": "well logs -> hydrate ML architecture",
        "steps": [
            ("Inputs", "logs + core"),
            ("QC", "caliper + flags"),
            ("Features", "measured/derived"),
            ("Models", "class/regress/ANN"),
            ("Validate", "held-out wells"),
        ],
        "outcome": "The ML story shows model design, leakage control, and validation.",
    },
    "stock_workflow": {
        "title": "current app -> honest AI build",
        "steps": [
            ("Codex", "inspect files"),
            ("Streamlit", "current visuals"),
            ("GitHub", "track pipeline"),
            ("Metrics", "test claims"),
            ("Risk", "block leakage"),
        ],
        "outcome": "The stock app becomes a build-and-validation example, not a prediction promise.",
    },
}

EMAIL_DISCUSSION_PROMPT_OVERRIDES = {
    "ai_workflow": [
        "What should count as a good training example for a scientific software agent?",
        "Which labor-heavy projects should agents take on first?",
        "Where should human supervision stay mandatory?",
    ],
    "thesis_graph": [
        "When does a diagram explain a research project better than text?",
        "Which graph edges should be source-backed, AI-suggested, or human-interpreted?",
        "How could graph structure improve critical-mineral workflows?",
    ],
    "processing_earthquake": [
        "Which variables should be extracted from a 3D earthquake globe?",
        "What is visualization allowed to claim before modeling starts?",
        "How do we test a 2D-over-time feature idea honestly?",
    ],
    "seismic": [
        "What large-data workflows should move from local laptops into cloud workspaces?",
        "How should Codex and GitHub make seismic processing easier to collaborate on?",
        "What outputs still require an expert sitting with the data?",
    ],
    "north_slope": [
        "Which public sources are worth scraping first?",
        "How should a source library show trust and uncertainty?",
        "What belongs in a public-safe well scaffold?",
    ],
    "rock_classification": [
        "Which satellite variables are most useful for rock-type classification?",
        "How should mixed pixels and uncertain labels be shown?",
        "Where do critical-mineral heatmaps help explain the problem without becoming model inputs?",
    ],
    "valles": [
        "Where do the Valles methods agree, and where do they conflict?",
        "How should AI show field errors and acquisition limits?",
        "Which figure from the Near-Surface deck should anchor the topic?",
    ],
    "moho_ml": [
        "What is the simplest baseline before the ANN?",
        "Which features must stay separate from the target?",
        "Why is complete-well validation stronger than random depth-row splitting?",
    ],
    "stock_workflow": [
        "What does the current app prove, and what does it not prove?",
        "How should a young builder explain model risk clearly?",
        "Which visuals from the updated app should replace the old navigator image?",
    ],
}

EMAIL_EVIDENCE_LEAD_OVERRIDES = {
    "ai_workflow": [
        ("Prompt/rubric screenshot folder", "assets/gmail_updates/2026-06-08/Screenshot 2026-05-17 233055.png"),
        ("Agent workflow visual", "assets/topic_visuals/agent_supervised_workflows.svg"),
    ],
    "thesis_graph": [
        ("REE architecture visual", "assets/topic_visuals/knowledge_architecture_ai.svg"),
        ("Bayan Obo drawing", "assets/project_visuals/ree_bayan_obo_main.png"),
        ("Thesis host context", "assets/project_visuals/thesis_host_context_clean.png"),
    ],
    "processing_earthquake": [
        ("Variable transform visual", "assets/topic_visuals/data_variable_transform.svg"),
        ("Processing poster", "assets/project_visuals/processing_earthquake_linkedin_poster.jpg"),
    ],
    "seismic": [
        ("Cloud processing visual", "assets/topic_visuals/cloud_data_processing.svg"),
        ("Pondicherry near-offset figure", "assets/project_visuals/pondicherry_near_offset_reannotated.png"),
        ("EarthScope slide export", "assets/project_visuals/linkedin_powerpoint_slides/earthscope_deck_image_04.jpg"),
    ],
    "north_slope": [
        ("Web scraping visual", "assets/topic_visuals/web_scraping_data_lake.svg"),
        ("North Slope Plotly map", "assets/project_visuals/north_slope_3d_streamlit_plotly_map.png"),
        ("Public data layer notes", "assets/drive_sources/north_slope_source_library/unclassified_local/source_library/06_maps_and_public_data_notes/North Slope Data Layer Map.pdf"),
    ],
    "rock_classification": [
        ("Satellite classification visual", "assets/topic_visuals/satellite_rock_classification.svg"),
        ("Rock raster classification map", "assets/project_visuals/rock_classification_slides/rock_raster_classification_map.png"),
    ],
    "valles": [
        ("Valles Bouguer map", "assets/project_visuals/valles_bouguer.png"),
        ("SAGE / Valles slide export", "assets/project_visuals/linkedin_powerpoint_slides/sage_valles_deck_image_04.jpg"),
    ],
    "moho_ml": [
        ("North Slope ML architecture visual", "assets/topic_visuals/north_slope_ml_architecture.svg"),
        ("Latest North Slope decision map slide", "assets/drive_slide_thumbnails/north_slope_decision_map_slide.png"),
        ("Latest North Slope parameter grid slide", "assets/drive_slide_thumbnails/north_slope_parameter_grid_slide.png"),
    ],
    "stock_workflow": [
        ("Current all-tickers chart", "assets/project_visuals/stock_all_tickers_chart.svg"),
        ("Current saved-data chart", "assets/project_visuals/stock_saved_data_chart.svg"),
    ],
}

EMAIL_PROCESSING_SKETCH_OVERRIDES = {
    "ai_workflow": {
        "sketch": "prompt_rubric_agent_training_loop",
        "visual": "Prompt cards and rubric chips feed screen-recorded software actions. Approved steps become glowing training traces, then an agent repeats the workflow.",
        "motion": ["prompt pulse", "screen capture", "rubric gate", "agent replay"],
        "conclusion": "Future agents need supervised examples from real technical work, not only final screenshots.",
        "future_ml": "Imitation learning, GUI action models, workflow classifiers, and rubric-based evaluation for scientific software.",
        "processing_notes": "Use moving cursor paths, screenshot tiles, and a red/green rubric gate that turns demonstrations into agent traces.",
    },
    "thesis_graph": {
        "sketch": "ai_project_architecture_builder",
        "visual": "Left-side tables, questions, and drawings orbit into an AI/ML circle. Right-side outputs become a knowledge graph, architecture diagram, and scientific drawing.",
        "motion": ["input orbit", "AI sort", "edge growth", "diagram reveal"],
        "conclusion": "AI can make project structure visible so complex research is easier to discuss.",
        "future_ml": "GraphRAG, relation extraction, graph embeddings, and expert-reviewed graph ML for critical minerals.",
        "processing_notes": "Use three left columns, one central gravity well, and three right output panels with edges that keep confidence styles visible.",
    },
    "processing_earthquake": {
        "sketch": "globe_to_feature_matrix_loop",
        "visual": "Earthquake dots pulse on a globe, flatten into a timeline, then become feature bars for regression experiments.",
        "motion": ["event pulse", "flatten globe", "window bins", "feature chart"],
        "conclusion": "AI visualization can reshape spatial data into variables that models can test.",
        "future_ml": "Lagged features, spatiotemporal clustering, linear regression baselines, nonlinear models, and strict no-forecasting claims.",
        "processing_notes": "Animate globe points sliding into time bins and then into a small matrix with magnitude, depth, rate, and cluster fields.",
    },
    "seismic": {
        "sketch": "cloud_processing_handoff_loop",
        "visual": "A phone prompt sends work to Codex, GitHub branches light up, cloud compute runs through large data tiles, and review artifacts return.",
        "motion": ["phone prompt", "branch split", "cloud run", "artifact return"],
        "conclusion": "AI can reduce local waiting time by moving big processing into shared compute and version control.",
        "future_ml": "Cloud orchestration, automated QA summaries, station/event triage, and collaborative review assistants.",
        "processing_notes": "Animate packets traveling from phone to GitHub to a cloud, then returning small result cards instead of huge raw files.",
    },
    "north_slope": {
        "sketch": "public_source_scraper_loop",
        "visual": "Public maps, PDFs, shapefiles, and APIs flow into a scraper node, then stack into a source library and public well scaffold.",
        "motion": ["source crawl", "scraper parse", "provenance stamp", "well scaffold"],
        "conclusion": "AI web scraping is useful when provenance and public-safe boundaries stay visible.",
        "future_ml": "Public-source retrieval, schema matching, spatial joins, provenance scoring, and expert-reviewed hydrate feature assembly.",
        "processing_notes": "Draw source tiles entering a dark scraper box, then emit well sticks and 3D layer cards with provenance badges.",
    },
    "rock_classification": {
        "sketch": "satellite_feature_classifier_loop",
        "visual": "Satellite bands, DEM texture, slope, and structural context pass through feature gates and become reviewed rock-class map cells.",
        "motion": ["band stack", "feature gate", "class color", "review mask"],
        "conclusion": "AI can improve rock-type maps only when satellite variables and label uncertainty are explicit.",
        "future_ml": "Remote-sensing classifiers, spatial cross-validation, uncertainty maps, and expert label auditing.",
        "processing_notes": "Use colored raster tiles, feature sliders, and map cells that keep uncertain classes striped instead of solid.",
    },
    "valles": {
        "sketch": "near_surface_method_comparison_loop",
        "visual": "Hammer seismic, ERT, TEM, and mapped units slide into one field board. Agreement glows; conflicts remain striped.",
        "motion": ["line sweep", "method overlay", "intersection check", "conflict stripe"],
        "conclusion": "AI can compare imperfect geophysical surveys while preserving disagreement.",
        "future_ml": "Cross-method registration, field-error tagging, line-intersection QA, uncertainty masks, and promptable method summaries.",
        "processing_notes": "Use stacked translucent sections and keep conflict cells gray-striped even after AI suggests possible units.",
    },
    "moho_ml": {
        "sketch": "hydrate_ml_architecture_loop",
        "visual": "Well-log columns split into measured, derived, QC, and target lanes. Baseline, classifier, regressor, and ANN nodes feed a held-out-well validation gate.",
        "motion": ["well log split", "feature lanes", "model compare", "held-out gate"],
        "conclusion": "A hydrate ML topic needs architecture, leakage control, and complete-well validation before model claims.",
        "future_ml": "Baselines, boosted trees, ANN challengers, classification for occurrence, regression for saturation, and complete-well validation.",
        "processing_notes": "Show a vertical well log splitting into colored lanes, then block any arrow from target labels back into inputs.",
    },
    "stock_workflow": {
        "sketch": "current_stock_app_risk_loop",
        "visual": "Updated Streamlit charts replace the old image, then Codex/GitHub pipeline nodes pass through a model-risk gate.",
        "motion": ["chart swap", "pipeline build", "metric update", "risk gate"],
        "conclusion": "The current stock app is an AI app-building example, not a guarantee that predictions are reliable.",
        "future_ml": "Leakage checks, walk-forward testing, drift monitoring, baseline comparison, and production dashboard QA.",
        "processing_notes": "Animate a stale image fading out while current chart panels, commit nodes, and a red leakage gate fade in.",
    },
}

EMAIL_SITE_UPDATE_OVERRIDES = {
    "ai_workflow": {
        "kicker": "Email instruction",
        "title": "Replace agent demos with supervised agent training",
        "intro": "The page should tell a simple story: human prompt and rubric, screen-recorded virtual work, then supervised ML examples for future agents.",
        "items": [
            ("Prompt", "human writes the goal and rubric"),
            ("Recording", "virtual scientific software work becomes evidence"),
            ("Training", "approved steps become supervised examples"),
            ("Future", "agents execute repetitive work while humans lead new projects"),
        ],
    },
    "thesis_graph": {
        "kicker": "Email instruction",
        "title": "Use diagrams and graphs to cut down wordiness",
        "intro": "This topic should show how AI turns many inputs into knowledge graphs, ML architecture diagrams, and Adobe-style scientific drawings.",
        "items": [
            ("Left inputs", "tables, questions, drawings"),
            ("AI/ML center", "sort and connect variables"),
            ("Right outputs", "graphs, architecture diagrams, explanatory drawings"),
            ("Validation", "source-backed, AI-suggested, and human-interpreted links stay separate"),
        ],
    },
    "processing_earthquake": {
        "kicker": "Email instruction",
        "title": "Make the globe about feature creation",
        "intro": "The Processing sketch should explain how a 3D visual question can become model-ready 2D-over-time variables.",
        "items": [
            ("Prompt", "ask ChatGPT for Processing globe code"),
            ("Iterate", "revise until the map works"),
            ("Transform", "make rate, depth, magnitude, and cluster variables"),
            ("Model", "test linear and nonlinear regressions later"),
        ],
    },
    "seismic": {
        "kicker": "Email instruction",
        "title": "Large data processing belongs in cloud workflows",
        "intro": "The seismic topic should focus on Codex, GitHub, and cloud/virtual computers for big datasets, not only notebook interpretation.",
        "items": [
            ("Codex", "edit and run from anywhere"),
            ("GitHub", "commit and collaborate"),
            ("Cloud", "OpenScienceLab, ASF, or virtual machines"),
            ("Review", "humans check the scientific result"),
        ],
    },
    "north_slope": {
        "kicker": "Email instruction",
        "title": "Make North Slope a web-scraping and source-organization topic",
        "intro": "This page should show public data discovery, scraping, source logging, and a well scaffold rather than overclaiming real restricted well data.",
        "items": [
            ("Find", "public subsurface maps and shapefiles"),
            ("Scrape", "reports, APIs, names, coordinates"),
            ("Scaffold", "skeleton wells and public-safe fields"),
            ("Visualize", "3D map, source library, review board"),
        ],
    },
    "rock_classification": {
        "kicker": "Email instruction",
        "title": "Use satellite variables, not geochemical inputs, as the main classifier story",
        "intro": "Critical-mineral plots can explain complex patterns, but the classification topic should be driven by ADV GIS and satellite variables.",
        "items": [
            ("Satellite", "bands, texture, DEM derivatives"),
            ("GIS", "slope, structure, mapped context"),
            ("Classify", "rock type probabilities"),
            ("Review", "mixed pixels and uncertain labels"),
        ],
    },
    "valles": {
        "kicker": "Email instruction",
        "title": "Replace the unrelated person image with field graphs and lines",
        "intro": "Use Near-Surface Dwellers slides to ground the Valles topic in seismic, ERT, TEM, possible units, and line intersections.",
        "items": [
            ("Hammer seismic", "velocity and processing flow"),
            ("ERT / TEM", "conductivity comparison"),
            ("Lines", "survey intersections"),
            ("Uncertainty", "possible units, not final truth"),
        ],
    },
    "moho_ml": {
        "kicker": "Email instruction",
        "title": "Use the North Slope docs to explain the ML backbone",
        "intro": "The ML page should show architecture decisions: inputs, feature separation, model family, leakage controls, and validation.",
        "items": [
            ("Inputs", "depth, logs, core data, QC flags"),
            ("Targets", "hydrate occurrence and saturation stay separate"),
            ("Models", "baseline, classifier, regressor, ANN"),
            ("Validation", "complete wells held out"),
        ],
    },
    "stock_workflow": {
        "kicker": "Email instruction",
        "title": "Use the updated stock app visuals",
        "intro": "The public navigator should stop showing the old app-diagram image and use the newer Streamlit chart evidence.",
        "items": [
            ("Current chart", "all tickers / saved data visuals"),
            ("Build story", "Codex organizes local app files"),
            ("Pipeline", "GitHub and refresh workflow"),
            ("Risk", "testing and leakage stay visible"),
        ],
    },
}

EMAIL_SLIDE_SOURCE_OVERRIDES = {
    "ai_workflow": [
        ("Prompt/rubric screenshot", "place next to the first workflow image on the detail page"),
        ("Scientific software recordings", "frame QGIS, ParaView, 3D Slicer, and KiCad as future agent-training environments"),
    ],
    "thesis_graph": [
        ("Thesis Ch.1 REE deck", "show the images the text talks about instead of hiding them at the end"),
        ("Graph validation", "keep source-backed, AI-suggested, and human-interpreted edges visually distinct"),
    ],
    "processing_earthquake": [
        ("Processing earthquake sketch", "explain the ChatGPT prompt loop and future variable conversion"),
    ],
    "seismic": [
        ("OpenScienceLab / ASF references", "connect large data processing to cloud or virtual workspaces"),
        ("GitHub workflow", "show commit/push/collaboration as part of the AI skill"),
    ],
    "north_slope": [
        ("FINAL 9-slide North Slope deck", "use the June 11 parameter grid and decision-map screenshots as local images"),
        ("North Slope public source library", "use public maps/shapefiles and provenance records instead of restricted 71-well detail"),
        ("North Slope Streamlit site", "keep the updated scaffold and 3D map story as interactive support"),
    ],
    "rock_classification": [
        ("ADV GIS Final presentation", "use satellite variables as the classifier source"),
        ("Critical minerals powerpoint PDF", "use heatmaps, spider diagrams, and complex-problem visuals as support"),
    ],
    "valles": [
        ("Near-Surface Dwellers Presentation", "use graphs, line intersections, and method figures instead of the person image"),
    ],
    "moho_ml": [
        ("Updated North Slope Word doc", "use parameter definitions, model families, and validation language"),
        ("FINAL 9-slide North Slope deck", "use the slide 4 parameter grid and slide 7 decision map as the visible ML architecture evidence"),
        ("Chong et al. gas hydrate ANN paper", "use as the ML backbone reference"),
    ],
    "stock_workflow": [
        ("Updated AI stock app pred website", "use newer Streamlit visuals instead of the old navigator image"),
    ],
}

EMAIL_DETAILED_TOPIC_PLAN_OVERRIDES = {
    "ai_workflow": {
        "title": "Prompting And Supervised Agent Training",
        "question": "Will screenshots and ChatGPT prompting be replaced by Codex?",
        "anchor": "Prompt/rubric screenshots and screen-recorded scientific software work become supervised examples for agents.",
        "conclusion": "The new story is not agent demos. It is human demonstrations becoming training data for future agents.",
        "techniques": ["supervised learning", "GUI agents", "rubric-based evaluation"],
        "inputs": ["prompt text", "rubrics", "screen recordings", "software files", "human corrections"],
        "outputs": ["training traces", "pass/fail labels", "agent task evaluations"],
        "bottleneck": "People spend time on repetitive software execution before they can lead larger energy, agriculture, commerce, and field projects.",
        "validate": "A human checks the software output, the file state, the scientific meaning, and whether the task truly followed the rubric.",
        "storyboard": ["prompt and rubric appear", "screen recording captures work", "rubric gate labels steps", "agent executes a similar task"],
        "labels": ["prompt", "rubric", "recording", "training", "agent"],
        "do_not_claim": "Do not claim agents already replace trained scientific software users.",
    },
    "thesis_graph": {
        "title": "AI Knowledge Graphs And Diagrams",
        "question": "Knowledge graphs and diagrams built using AI: are they the next way to understand project architectures?",
        "anchor": "Tables, CSVs, project questions, and Adobe-style deposit drawings feed an AI/ML architecture view.",
        "conclusion": "AI diagrams make complex research easier to understand when evidence and uncertainty stay visible.",
        "techniques": ["knowledge graphs", "GraphRAG", "relation extraction"],
        "inputs": ["tables", "CSVs", "questions", "drawings", "deposit variables", "source evidence"],
        "outputs": ["knowledge graphs", "ML architecture diagrams", "scientific drawings", "review questions"],
        "bottleneck": "Critical-mineral ideas are scattered across wordy papers, disconnected figures, and hidden assumptions.",
        "validate": "A human checks entity names, edge confidence, geologic plausibility, and which links are source-backed.",
        "storyboard": ["left-side inputs stack", "AI/ML center sorts variables", "right-side graph appears", "diagram highlights project architecture"],
        "labels": ["tables", "questions", "drawings", "AI/ML", "graph"],
        "do_not_claim": "Do not claim a graph discovers mineral deposits by itself.",
    },
    "processing_earthquake": {
        "title": "AI Visualization Into Prediction Variables",
        "question": "Can we use AI to visualize data into new variables for prediction models?",
        "anchor": "The user asked ChatGPT for Processing code that maps earthquake locations onto a globe and iterated until it worked.",
        "conclusion": "The globe is the entry point for a bigger idea: converting spatial data into model-ready variables.",
        "techniques": ["feature engineering", "spatiotemporal clustering", "linear/nonlinear regression"],
        "inputs": ["event time", "latitude", "longitude", "depth", "magnitude", "region windows"],
        "outputs": ["time-window features", "cluster features", "2D trend views", "testable model inputs"],
        "bottleneck": "A 3D visualization is powerful for people, but models need defined variables and validation.",
        "validate": "A human checks that the visual transformation does not imply earthquake prediction claims the data cannot support.",
        "storyboard": ["ChatGPT prompt appears", "Processing globe animates", "events flatten into time windows", "feature table feeds a model"],
        "labels": ["prompt", "globe", "features", "regression", "limits"],
        "do_not_claim": "Do not claim earthquake forecasting from the visualization.",
    },
    "seismic": {
        "title": "Large Data Processing With AI Workspaces",
        "question": "How can Codex make large scientific data processing faster from cloud workspaces?",
        "anchor": "Codex, GitHub, OpenScienceLab, ASF cloud ideas, and large seismic/satellite data make the topic about workflow access.",
        "conclusion": "The AI value is moving heavy processing into shared, trackable environments.",
        "techniques": ["cloud workflows", "version control", "automated QA summaries"],
        "inputs": ["large datasets", "notebooks", "cloud credentials", "GitHub repositories", "processing logs"],
        "outputs": ["tracked runs", "review artifacts", "collaborative commits", "QA summaries"],
        "bottleneck": "Local machines and scattered files slow down large data projects and make collaboration harder.",
        "validate": "A human checks data provenance, processing parameters, output quality, and scientific interpretation.",
        "storyboard": ["phone prompt starts task", "GitHub branch appears", "cloud compute processes data", "review card returns"],
        "labels": ["Codex", "GitHub", "cloud", "data", "review"],
        "do_not_claim": "Do not claim AI removes the need for seismic or satellite data review.",
    },
    "north_slope": {
        "title": "AI Web Scraping For Public Energy Data",
        "question": "How can AI scrape and organize public subsurface sources into one usable workspace?",
        "anchor": "North Slope public maps, shapefiles, reports, APIs, source libraries, and Streamlit well scaffolds anchor the topic.",
        "conclusion": "The useful AI task is finding, organizing, and visualizing public energy evidence with provenance.",
        "techniques": ["web scraping", "source provenance", "spatial data organization"],
        "inputs": ["public maps", "shapefiles", "reports", "APIs", "well skeletons", "source metadata"],
        "outputs": ["source library", "public-safe well scaffold", "3D map", "review workspace"],
        "bottleneck": "The information exists, but it is fragmented across websites, PDFs, GIS layers, and naming conventions.",
        "validate": "A human checks source permissions, coordinate systems, public-safe boundaries, and geologic meaning.",
        "storyboard": ["public sources appear", "scraper organizes files", "provenance stamps light up", "well scaffold and 3D map appear"],
        "labels": ["web", "scrape", "source", "scaffold", "map"],
        "do_not_claim": "Do not display restricted well data or imply the public scaffold is the real 71-well dataset.",
    },
    "rock_classification": {
        "title": "Satellite Variables For Rock Classification",
        "question": "Can AI classify rock types from satellite variables more accurately?",
        "anchor": "ADV GIS satellite variables drive the classifier story; the critical-minerals PDF supplies supporting complexity visuals.",
        "conclusion": "AI classification is stronger when the input variables and label review are clear.",
        "techniques": ["remote-sensing classification", "spatial cross-validation", "uncertainty mapping"],
        "inputs": ["spectral bands", "DEM derivatives", "texture", "slope", "mapped context", "reviewed labels"],
        "outputs": ["rock-class map", "confidence mask", "uncertain zones", "review queue"],
        "bottleneck": "Satellite classes can hide mixed pixels, bad labels, and overconfident map colors.",
        "validate": "A human checks label quality, mixed classes, training/test geography, and whether the map makes geologic sense.",
        "storyboard": ["satellite layers stack", "feature gates select variables", "classifier colors map cells", "review mask keeps uncertainty visible"],
        "labels": ["satellite", "features", "class", "uncertainty", "review"],
        "do_not_claim": "Do not treat geochemical diagrams as the classifier input source.",
    },
    "valles": {
        "title": "Comparing Imperfect Geophysical Surveys",
        "question": "How should AI compare imperfect geophysical surveys without flattening uncertainty?",
        "anchor": "Near-Surface Dwellers supplies hammer seismic, ERT, TEM, line intersections, possible units, and field-error context.",
        "conclusion": "AI should help compare methods while keeping conflict and field uncertainty visible.",
        "techniques": ["cross-method comparison", "uncertainty tagging", "line-intersection QA"],
        "inputs": ["hammer seismic", "ERT", "TEM", "survey lines", "possible units", "field notes"],
        "outputs": ["method comparison board", "agreement zones", "conflict zones", "reviewed unit candidates"],
        "bottleneck": "Different methods see different physics and can disagree for valid reasons.",
        "validate": "A human checks acquisition errors, line geometry, method limits, and geologic plausibility.",
        "storyboard": ["seismic line appears", "ERT and TEM layers slide in", "line intersections glow", "conflict zones stay unresolved"],
        "labels": ["seismic", "ERT", "TEM", "line", "uncertain"],
        "do_not_claim": "Do not imply AI found the true subsurface from overlays alone.",
    },
    "moho_ml": {
        "title": "North Slope ML Architecture",
        "question": "What ML architecture can predict hydrate occurrence and saturation without leaking target data?",
        "anchor": "Updated North Slope documents and the hydrate ANN paper define public-safe inputs, target separation, and validation.",
        "conclusion": "The ML story should show architecture and validation before any model performance claim.",
        "techniques": ["baseline modeling", "classification", "regression", "ANN challenger"],
        "inputs": ["depth", "GR", "density", "porosity", "resistivity", "Vp/Vs", "core data", "QC flags"],
        "outputs": ["hydrate occurrence", "hydrate saturation", "uncertainty flags", "held-out-well scorecards"],
        "bottleneck": "Random depth-row splits can leak nearby information and make a model look stronger than it is.",
        "validate": "A human holds out complete wells, checks leakage, reviews physics, and separates measured inputs from targets.",
        "storyboard": ["well-log inputs split into lanes", "target lane is isolated", "baseline and ANN compare", "held-out well gate approves or blocks"],
        "labels": ["logs", "QC", "target", "model", "held-out well"],
        "do_not_claim": "Do not claim trained hydrate predictions from skeleton public data.",
    },
    "stock_workflow": {
        "title": "Current Stock App As AI Build Workflow",
        "question": "How can the current stock prediction app show AI app building without hiding model risk?",
        "anchor": "Updated Streamlit stock charts replace the old public navigator image.",
        "conclusion": "The page should explain AI-assisted app building and model-risk honesty, not sell a stock prediction claim.",
        "techniques": ["Streamlit apps", "pipeline automation", "leakage checks"],
        "inputs": ["local files", "price data", "app code", "metrics", "GitHub changes"],
        "outputs": ["updated dashboard", "tracked build", "risk notes", "testing gate"],
        "bottleneck": "It is easy to make a financial dashboard look authoritative before evaluation is trustworthy.",
        "validate": "A human checks train/test design, leakage, metric meaning, and whether the app language avoids financial advice.",
        "storyboard": ["old image fades", "current chart appears", "Codex/GitHub pipeline connects", "risk gate blocks overclaim"],
        "labels": ["app", "Codex", "GitHub", "metrics", "risk"],
        "do_not_claim": "Do not imply the app gives reliable investment advice.",
    },
}

EMAIL_AI_WORKFLOW_EVIDENCE_OVERRIDES = {
    "ai_workflow": {
        "description": "Prompt/rubric and screen-recording evidence becomes supervised learning material for future software agents.",
        "chips": ["Prompt + rubric", "Screen recording", "Supervised agent training"],
        "where": "Codex and ChatGPT help structure human software work into task descriptions, action traces, and review labels.",
        "gave": "Prompt text, rubric screenshots, QGIS/ParaView-style software context, recordings, corrections, and expected outputs.",
        "produced": "A clearer agent-training story: prompt, record, review, label, and future agent execution.",
        "validated": "A human checks whether the software output works and whether the trace follows the rubric.",
        "future": "Agents execute labor-heavy software steps while humans design and manage higher-value projects.",
    },
    "thesis_graph": {
        "description": "AI converts scattered critical-mineral research into graphs and diagrams that explain project architecture.",
        "chips": ["Tables + CSVs", "AI/ML center", "Graph + diagram outputs"],
        "where": "AI helps translate notes, tables, drawings, and project questions into visual structures.",
        "gave": "REE slides, deposit drawings, Gephi exports, node/edge logic, and critical-mineral research questions.",
        "produced": "A cleaner left-to-right architecture: inputs, AI/ML connector, and graph/diagram outputs.",
        "validated": "Sources, edge confidence, geologic reasoning, and AI-suggested relationships are kept separate.",
        "future": "Graph-backed workflows could help explain critical-mineral accumulation systems and project structure.",
    },
    "processing_earthquake": {
        "description": "ChatGPT-assisted Processing visualization becomes a feature-engineering story.",
        "chips": ["ChatGPT prompt", "Processing globe", "2D time features"],
        "where": "AI helped write and iterate code for mapping earthquake locations onto a globe.",
        "gave": "Earthquake locations, magnitudes, depths, time, and a Processing visual idea.",
        "produced": "A globe visualization and a future plan for turning event patterns into model variables.",
        "validated": "The topic is framed as variable creation, not earthquake forecasting.",
        "future": "Future work converts 3D visual patterns into linear and nonlinear regression features.",
    },
    "seismic": {
        "description": "Large data processing becomes an AI-assisted cloud and GitHub workflow.",
        "chips": ["Codex from phone", "GitHub", "Cloud compute"],
        "where": "Codex can help edit, run, and document workflows that use large scientific datasets in virtual environments.",
        "gave": "Notebook logic, data-processing goals, cloud workflow ideas, and collaboration needs.",
        "produced": "A topic about access and workflow speed instead of only one seismic notebook output.",
        "validated": "Humans still check processing parameters, data provenance, and scientific interpretation.",
        "future": "Workflows run in OSL/ASF-style cloud spaces while GitHub keeps changes shareable.",
    },
    "north_slope": {
        "description": "AI web scraping organizes public North Slope energy data into a reviewable workspace.",
        "chips": ["Public maps", "Scraper/API", "Well scaffold"],
        "where": "AI helps find public subsurface maps, shapefiles, reports, and data APIs.",
        "gave": "Public-source goals, North Slope Streamlit visuals, source-library notes, and gas hydrate planning documents.",
        "produced": "A public-safe web-scraping and source-organization topic with updated well-scaffold framing.",
        "validated": "Source permissions, provenance, coordinate systems, and restricted-data boundaries stay visible.",
        "future": "A live source workbench could update maps, skeleton wells, and evidence panels from public sources.",
    },
    "rock_classification": {
        "description": "Satellite variables and ADV GIS become the basis for rock-type classification.",
        "chips": ["Satellite bands", "GIS features", "Reviewed map"],
        "where": "AI helps organize remote-sensing variables and simplify the classification story.",
        "gave": "ADV GIS presentation ideas, satellite variables, map outputs, and critical-mineral complexity visuals.",
        "produced": "A topic centered on satellite/GIS classification rather than geochemical inputs.",
        "validated": "Labels, mixed pixels, uncertainty masks, and spatial validation need human review.",
        "future": "Models combine satellite bands, terrain variables, and reviewed labels to improve rock maps.",
    },
    "valles": {
        "description": "Near-Surface Dwellers replaces the unrelated image with real method-comparison evidence.",
        "chips": ["Hammer seismic", "ERT/TEM", "Line intersections"],
        "where": "AI helps organize shallow Valles survey evidence into a comparison board.",
        "gave": "Near-Surface Dwellers slides, field method notes, possible units, and survey-line relationships.",
        "produced": "A clearer field geophysics topic with method disagreement and uncertainty visible.",
        "validated": "Field errors, acquisition geometry, method sensitivity, and possible geologic units require expert review.",
        "future": "A future assistant compares methods side by side and flags conflicts for review.",
    },
    "moho_ml": {
        "description": "North Slope documents become a model architecture for hydrate occurrence and saturation prediction.",
        "chips": ["Well-log inputs", "Feature lanes", "Held-out wells"],
        "where": "AI extracts architecture from the updated Word doc, slides, and hydrate ANN paper.",
        "gave": "Parameter lists, model goals, validation warnings, and public-safe scaffold constraints.",
        "produced": "A leakage-aware ML architecture diagram that explains the backbone of the topic.",
        "validated": "Complete wells are held out, targets are isolated, and random adjacent depth splits are treated as risky.",
        "future": "Baseline, classification, regression, and ANN models are compared under honest validation.",
    },
    "stock_workflow": {
        "description": "Updated stock app visuals explain current AI app building and model-risk discipline.",
        "chips": ["Current Streamlit chart", "Codex build", "Risk gate"],
        "where": "Codex helps inspect the app, update visuals, and frame testing limitations.",
        "gave": "Current stock app charts, local files, code structure, and model-risk concerns.",
        "produced": "A current public navigator topic instead of the old stock-prediction visual.",
        "validated": "Train/test split, leakage, metric meaning, and finance-language boundaries remain human-reviewed.",
        "future": "Pipeline refreshes, drift monitoring, and unseen-data testing make the app more honest.",
    },
}


SOURCE_BACKED_TOPIC_ASSETS = {
    "ai_workflow": [
        {
            "title": "Prompt and rubric screenshot",
            "path": "assets/gmail_updates/2026-06-08/Screenshot 2026-05-17 233055.png",
            "source": "Gmail screenshot package",
            "note": "Use this as the concrete evidence for human instructions becoming training traces.",
        },
        {
            "title": "Agent workflow architecture",
            "path": "assets/topic_visuals/agent_supervised_workflows.svg",
            "source": "Portfolio topic visual",
            "note": "Shows prompt, recording, rubric gate, and supervised agent-training output.",
        },
        {
            "title": "Additional AI-workflow screenshot",
            "path": "assets/gmail_updates/2026-06-08/Screenshot 2026-05-10 142643.png",
            "source": "Gmail screenshot package",
            "note": "Secondary local proof image, not an external link.",
        },
    ],
    "thesis_graph": [
        {
            "title": "REE map and spider diagram",
            "path": "assets/project_visuals/linkedin_powerpoint_slides/ree_slide_map_spider_diagram.png",
            "source": "Thesis Ch.1 / critical-minerals slide export",
            "note": "Grounds the graph topic in actual map and geochemical-pattern evidence.",
        },
        {
            "title": "Critical-minerals heatmaps",
            "path": "assets/gmail_updates/2026-06-10/critical_minerals_pdf_pages/critical_minerals_p08_heatmaps.png",
            "source": "Critical minerals PowerPoint PDF, page 8",
            "note": "Shows property-overlap matrices that can become graph edge weights and uncertainty checks.",
        },
        {
            "title": "Bayan Obo interpretation drawing",
            "path": "assets/project_visuals/ree_bayan_obo_main.png",
            "source": "Local REE visual export",
            "note": "Use as the evidence-backed drawing behind the knowledge-graph structure.",
        },
        {
            "title": "Deposit-model slide",
            "path": "assets/project_visuals/linkedin_powerpoint_slides/ree_slide_deposit_model.png",
            "source": "Thesis Ch.1 / critical-minerals slide export",
            "note": "Supports the source-backed, AI-suggested, and human-interpreted edge split.",
        },
    ],
    "processing_earthquake": [
        {
            "title": "Processing earthquake poster",
            "path": "assets/project_visuals/processing_earthquake_linkedin_poster.jpg",
            "source": "LinkedIn/Processing evidence export",
            "note": "This is the real visual anchor for the ChatGPT-to-Processing workflow.",
        },
        {
            "title": "Globe to variable diagram",
            "path": "assets/topic_visuals/data_variable_transform.svg",
            "source": "Portfolio topic visual",
            "note": "Connects the 3D visual to 2D time-window features and model inputs.",
        },
        {
            "title": "Earthquake signal sketch",
            "path": "assets/topic_visuals/earthquake_globe_signal.svg",
            "source": "Portfolio topic visual",
            "note": "Keeps the future variable-extraction idea visible without forecast claims.",
        },
    ],
    "seismic": [
        {
            "title": "Pondicherry near-offset interpretation",
            "path": "assets/project_visuals/pondicherry_near_offset_reannotated.png",
            "source": "Exploration seismology project export",
            "note": "Real seismic figure for the large-data processing and QA story.",
        },
        {
            "title": "Marine stack bands",
            "path": "assets/project_visuals/pondicherry_marine_stack_bands.png",
            "source": "Exploration seismology project export",
            "note": "Use as local proof that the pipeline handles scientific image outputs.",
        },
        {
            "title": "EarthScope slide export",
            "path": "assets/project_visuals/linkedin_powerpoint_slides/earthscope_deck_image_04.jpg",
            "source": "EarthScope / seismic slide export",
            "note": "Supports cloud, station, and collaboration context.",
        },
        {
            "title": "IMG_9800 field-computer run",
            "path": "assets/gmail_updates/2026-06-10/IMG_9800.jpg",
            "source": "Gmail attachment IMG_9800",
            "note": "Email-specific source image for field/cloud processing and plot review on rugged hardware.",
        },
    ],
    "north_slope": [
        {
            "title": "Latest parameter signal grid",
            "path": "assets/drive_slide_thumbnails/north_slope_parameter_grid_slide.png",
            "source": "FINAL 9-slide North Slope deck, slide 4",
            "note": "Newest deck snapshot with resistivity, NMR, sonic, density, GR, caliper, core, and PT caveats.",
        },
        {
            "title": "North Slope public map",
            "path": "assets/project_visuals/north_slope_alaska_geology_well_map.png",
            "source": "North Slope public-source visual export",
            "note": "Local image for the public data and provenance workbench story.",
        },
        {
            "title": "ML decision map slide",
            "path": "assets/drive_slide_thumbnails/north_slope_decision_map_slide.png",
            "source": "FINAL 9-slide North Slope deck, slide 7",
            "note": "Actual deck screenshot for the leakage-safe architecture and review gates.",
        },
        {
            "title": "Model panel export",
            "path": "assets/project_visuals/north_slope_presentation_model_panels.png",
            "source": "North Slope presentation export",
            "note": "Keeps the portfolio grounded in the existing deck visuals.",
        },
    ],
    "rock_classification": [
        {
            "title": "Rock raster classification map",
            "path": "assets/project_visuals/rock_classification_slides/rock_raster_classification_map.png",
            "source": "ADV GIS / rock-classification slide export",
            "note": "Primary image for satellite and GIS variables becoming rock classes.",
        },
        {
            "title": "Chemical classification chart",
            "path": "assets/project_visuals/rock_classification_slides/rock_chemical_classification_chart.jpg",
            "source": "Rock-classification slide export",
            "note": "Used as supporting complexity evidence, not as the satellite model input.",
        },
        {
            "title": "Formation classification outputs",
            "path": "assets/project_visuals/rock_classification_slides/rock_formation_classification_outputs.png",
            "source": "Rock-classification slide export",
            "note": "Shows labels and output structure that future ML would need to audit.",
        },
        {
            "title": "Measurement-condition problem",
            "path": "assets/gmail_updates/2026-06-10/critical_minerals_pdf_pages/critical_minerals_p05_measurement_conditions_problem.png",
            "source": "Critical minerals PowerPoint PDF, page 5",
            "note": "Explains why density, saturation, temperature, and matrix effects cannot be treated as simple labels.",
        },
        {
            "title": "Formation trend comparison",
            "path": "assets/gmail_updates/2026-06-10/critical_minerals_pdf_pages/critical_minerals_p10_formation_trend_comparison.png",
            "source": "Critical minerals PowerPoint PDF, page 10",
            "note": "Supports rock-property feature engineering before classification or resource mapping.",
        },
        {
            "title": "Property-correlation map",
            "path": "assets/gmail_updates/2026-06-10/critical_minerals_pdf_pages/critical_minerals_p17_property_correlation.png",
            "source": "Critical minerals PowerPoint PDF, page 17",
            "note": "Shows source geography that future spatial validation must keep separate from training labels.",
        },
    ],
    "valles": [
        {
            "title": "Valles Bouguer map",
            "path": "assets/project_visuals/valles_bouguer.png",
            "source": "SAGE / Valles project export",
            "note": "Replaces generic imagery with a real field-geophysics map.",
        },
        {
            "title": "SAGE Valles slide",
            "path": "assets/project_visuals/linkedin_powerpoint_slides/sage_valles_deck_image_04.jpg",
            "source": "SAGE / Valles slide export",
            "note": "Supports method comparison and field context.",
        },
        {
            "title": "Valles free-air map",
            "path": "assets/project_visuals/valles_freeair.png",
            "source": "SAGE / Valles project export",
            "note": "A second real map for comparing imperfect geophysical products.",
        },
    ],
    "near_surface": [
        {
            "title": "Near-surface field screenshot",
            "path": "assets/gmail_updates/2026-06-08/Screenshot 2025-07-01 121033.png",
            "source": "Gmail screenshot package",
            "note": "Local field-method evidence for the Near-Surface Dwellers topic.",
        },
        {
            "title": "SAGE Valles method slide",
            "path": "assets/project_visuals/linkedin_powerpoint_slides/sage_valles_deck_image_03.jpg",
            "source": "SAGE / Valles slide export",
            "note": "Use to show lines, methods, and uncertainty instead of a generic profile image.",
        },
        {
            "title": "Near-surface method board",
            "path": "assets/topic_visuals/near_surface_ai.svg",
            "source": "Portfolio topic visual",
            "note": "Shows hammer seismic, ERT, TEM, unit candidates, and conflict zones.",
        },
    ],
    "moho_ml": [
        {
            "title": "Latest ML decision map",
            "path": "assets/drive_slide_thumbnails/north_slope_decision_map_slide.png",
            "source": "FINAL 9-slide North Slope deck, slide 7",
            "note": "The newest architecture image for feature store, split policy, heads, uncertainty, and leakage barrier.",
        },
        {
            "title": "North Slope ML architecture",
            "path": "assets/topic_visuals/north_slope_ml_architecture.svg",
            "source": "Portfolio architecture diagram",
            "note": "Expanded with source keywords from the ML notes and hydrate deck.",
        },
        {
            "title": "Moho transfer legacy map",
            "path": "assets/project_visuals/valles_moho.png",
            "source": "Moho / supervised ML project export",
            "note": "Keeps the original supervised-transfer example visible while the page now emphasizes hydrate architecture.",
        },
    ],
    "ambient_noise": [
        {
            "title": "NoisePy monitoring slide",
            "path": "assets/drive_slide_thumbnails/noisepy_monitoring_slide.png",
            "source": "NoisePy Google Slides deck",
            "note": "Local snapshot showing the monitoring heatmap from the source deck.",
        },
        {
            "title": "Ambient-noise processing workflow",
            "path": "assets/topic_visuals/ambient_noise_processing.svg",
            "source": "Portfolio topic visual",
            "note": "Shows windowing, station pairs, cross-correlation, stacking, monitoring, compute, and QA.",
        },
        {
            "title": "EarthScope station context",
            "path": "assets/project_visuals/linkedin_powerpoint_slides/earthscope_deck_image_03.jpg",
            "source": "EarthScope / seismic slide export",
            "note": "Supports the continuous-data and station-network framing.",
        },
    ],
    "stock_workflow": [
        {
            "title": "Current all-tickers chart",
            "path": "assets/project_visuals/stock_all_tickers_chart.svg",
            "source": "Updated Streamlit stock app export",
            "note": "Replaces the older stock navigator image with a current app screenshot/export.",
        },
        {
            "title": "Saved-data chart",
            "path": "assets/project_visuals/stock_saved_data_chart.svg",
            "source": "Updated Streamlit stock app export",
            "note": "Shows the app's actual local-data view.",
        },
        {
            "title": "Codex app pipeline",
            "path": "assets/topic_visuals/app_pipeline.svg",
            "source": "Portfolio topic visual",
            "note": "Connects app building to train/test separation, drift, and leakage checks.",
        },
    ],
    "sem_petrography": [
        {
            "title": "Thin-section / petrography slide",
            "path": "assets/project_visuals/linkedin_powerpoint_slides/rock_thin_section_slide_01.jpg",
            "source": "SEM petrography / thin-section slide export",
            "note": "Local image evidence for visual mineral and texture labels.",
        },
        {
            "title": "SEM proxy workflow",
            "path": "assets/topic_visuals/sem_petrography_ai.svg",
            "source": "Portfolio topic visual",
            "note": "Separates visible SEM labels from interpreted climate-proxy claims.",
        },
        {
            "title": "Chemical classification reference",
            "path": "assets/project_visuals/rock_chemical_classification_reference.jpg",
            "source": "Rock classification local evidence",
            "note": "Supports the broader multimodal label-and-review workflow.",
        },
    ],
}


ML_PIPELINE_CONTRACTS = {
    "ai_workflow": {
        "title": "Supervised Agent-Training Pipeline",
        "summary": "Treat prompts, recordings, rubrics, and corrections as training examples with review labels.",
        "features": ["prompt text", "rubric criteria", "screen actions", "file state", "human correction"],
        "pipeline": ["ingest demonstrations", "normalize action traces", "label pass/fail steps", "train GUI/action baseline", "evaluate with held-out tasks"],
        "validation": ["rubric-based scoring", "task replay success", "failure-case review", "no final-screenshot-only labels"],
        "failure_modes": ["ambiguous rubric", "missing file state", "shortcut memorization", "unsafe desktop action"],
    },
    "thesis_graph": {
        "title": "Critical-Mineral Graph Pipeline",
        "summary": "Turn papers, slides, tables, and drawings into a source-weighted graph before using graph ML or GraphRAG.",
        "features": ["deposit", "mineral", "host rock", "paragenetic stage", "source weight"],
        "pipeline": ["extract entities", "dedupe node names", "separate observed/inferred/conceptual edges", "load Neo4j", "rank relationships"],
        "validation": ["expert edge review", "source-backed edge audit", "uncertainty style check", "queryable schema test"],
        "failure_modes": ["AI-suggested edge treated as fact", "synonym duplication", "source loss", "overweighted attractive diagram"],
    },
    "processing_earthquake": {
        "title": "Visualization-To-Feature Pipeline",
        "summary": "Use the globe as feature engineering: event attributes become time-window variables before any model claim.",
        "features": ["event count", "magnitude bins", "depth bins", "cluster density", "lagged windows"],
        "pipeline": ["pull event catalog", "clean coordinates and time", "make 2D windows", "train baseline regression", "compare nonlinear challenger"],
        "validation": ["train on past/test future", "no forecasting claim from visualization", "residual review", "region-window sensitivity"],
        "failure_modes": ["look-ahead leakage", "visual cluster overread", "imbalanced rare events", "tectonic context ignored"],
    },
    "seismic": {
        "title": "Large Seismic Processing Pipeline",
        "summary": "Codex, GitHub, and cloud compute organize big runs, but scientific QA remains the acceptance gate.",
        "features": ["waveform metadata", "processing parameters", "station/event context", "pick confidence", "run logs"],
        "pipeline": ["stage large data", "run cloud notebook", "save artifacts", "summarize QA", "commit reviewed outputs"],
        "validation": ["parameter provenance", "sample output inspection", "noise and missingness flags", "reproducible commit history"],
        "failure_modes": ["environment drift", "silent missing files", "wrong CRS/station metadata", "AI summary hides weak signal"],
    },
    "north_slope": {
        "title": "Public-Source Energy Workspace Pipeline",
        "summary": "Scrape and organize public maps, reports, shapefiles, and APIs without crossing into restricted well data.",
        "features": ["source URL", "license/status", "coordinate system", "formation tag", "confidence flag"],
        "pipeline": ["discover public sources", "parse files and metadata", "spatially align layers", "build public-safe scaffold", "publish review workspace"],
        "validation": ["provenance check", "public-safe boundary check", "CRS review", "expert geologic review"],
        "failure_modes": ["restricted data leak", "coordinate mismatch", "stale API result", "source link without local evidence"],
    },
    "rock_classification": {
        "title": "Satellite Rock-Classification Pipeline",
        "summary": "ADV GIS and satellite variables drive the classifier; geochemical figures explain complexity but do not become hidden inputs.",
        "features": ["spectral bands", "DEM derivatives", "texture", "slope", "mapped context"],
        "pipeline": ["assemble rasters", "clean labels", "extract spatial features", "train baseline/forest/boosted model", "map uncertainty"],
        "validation": ["spatial cross-validation", "mixed-pixel review", "label audit", "class-imbalance check"],
        "failure_modes": ["random-pixel leakage", "bad geologic labels", "overconfident map colors", "geochemical plot mistaken for satellite input"],
    },
    "valles": {
        "title": "Field-Method Comparison Pipeline",
        "summary": "AI compares gravity, seismic, ERT, and TEM while preserving conflict and method-specific uncertainty.",
        "features": ["line geometry", "method type", "signal strength", "possible unit", "field note"],
        "pipeline": ["register survey lines", "normalize method outputs", "mark intersections", "tag agreement/conflict", "generate review board"],
        "validation": ["field geometry check", "method sensitivity review", "uncertainty mask", "expert unit decision"],
        "failure_modes": ["method disagreement erased", "line misregistration", "acquisition artifact", "false unified subsurface"],
    },
    "near_surface": {
        "title": "Near-Surface Method Fusion Pipeline",
        "summary": "Hammer seismic, ERT, TEM, possible units, and fen context become a conflict-aware review workflow.",
        "features": ["hammer-seismic velocity", "ERT resistivity", "TEM conductivity", "line intersection", "unit candidate"],
        "pipeline": ["crop source slides", "georeference line context", "build method layers", "flag conflicts", "summarize review decisions"],
        "validation": ["line-intersection QA", "field-note review", "method-limit explanation", "striped unresolved zones"],
        "failure_modes": ["clean overlay overclaim", "wrong unit label", "instrument physics ignored", "field error hidden"],
    },
    "moho_ml": {
        "title": "Gas-Hydrate ML Architecture Pipeline",
        "summary": "Use the newest North Slope ML deck and source notes: measured logs, derived physics features, targets, and split policy stay separate.",
        "features": ["Vsh", "phi_den", "Vp/Vs", "acoustic impedance", "lambda-rho", "mu-rho", "QC flags"],
        "pipeline": ["intake logs", "run QC gates", "fit feature transforms on training wells", "compare baseline/tree/ANN models", "score held-out wells"],
        "validation": ["complete-well validation", "MAE/RMSE/R2 for saturation", "precision/recall/F1 for occurrence", "calibration and abstention review"],
        "failure_modes": ["target leakage", "random depth-row overfit", "missing NMR/shear sonic", "gas/ice/cement lookalike"],
    },
    "ambient_noise": {
        "title": "Ambient-Noise Monitoring Pipeline",
        "summary": "Continuous records become windows, station-pair CCFs, stacks, and monitoring summaries with compute and QC logs.",
        "features": ["station pair", "window quality", "lag-time CCF", "stack stability", "seasonal flag"],
        "pipeline": ["window continuous noise", "preprocess traces", "cross-correlate station pairs", "stack stable signals", "triage monitoring changes"],
        "validation": ["metadata check", "stack stability review", "parameter audit trail", "seasonal and instrument-change review"],
        "failure_modes": ["weak correlation treated as signal", "unstable stack", "station metadata error", "compute cost hides bad QC"],
    },
    "stock_workflow": {
        "title": "Current Stock App Risk Pipeline",
        "summary": "The app is a Codex-built workflow example; model claims need leakage-safe splits, baselines, and drift checks.",
        "features": ["ticker", "date", "price window", "technical feature", "refresh timestamp"],
        "pipeline": ["load saved data", "separate training/evaluation dates", "compare baseline/challenger", "render Streamlit charts", "monitor drift"],
        "validation": ["walk-forward testing", "leakage check", "baseline comparison", "finance-language review"],
        "failure_modes": ["future data leakage", "overfit dashboard", "stale refresh", "prediction language overclaims usefulness"],
    },
    "sem_petrography": {
        "title": "SEM Label-And-Proxy Pipeline",
        "summary": "SEM crops and mineral labels become reviewable examples, while climate proxy claims remain separate evidence.",
        "features": ["grain texture", "mineral label", "kaolinite form", "detrital/authigenic tag", "literature source"],
        "pipeline": ["crop SEM fields", "propose visible labels", "separate observation from interpretation", "link literature support", "queue expert review"],
        "validation": ["label visibility check", "proxy-claim audit", "expert petrography review", "ambiguous example bucket"],
        "failure_modes": ["texture label overclaim", "proxy meaning inferred from image alone", "detrital/authigenic confusion", "missing scale/context"],
    },
}


ML_PIPELINE_SOURCE_CONTEXT = {
    "ai_workflow": {
        "keywords": ["GUI agents", "action traces", "rubric labels", "scientific workflow agents"],
        "sector_advance": ["energy project drafting", "banking operations QA", "startup app delivery", "commerce back-office automation"],
    },
    "thesis_graph": {
        "keywords": ["GraphRAG", "knowledge graph schema", "source-weighted edges", "GNN prospectivity"],
        "sector_advance": ["critical-mineral targeting", "banking risk maps", "startup knowledge bases", "marketing relationship graphs"],
    },
    "processing_earthquake": {
        "keywords": ["feature engineering", "lagged windows", "nonlinear baseline", "held-out future windows"],
        "sector_advance": ["hazard communication", "logistics anomaly windows", "finance volatility windows", "equipment monitoring"],
    },
    "seismic": {
        "keywords": ["SeisLM", "seismic foundation model", "phase picking", "run provenance"],
        "sector_advance": ["energy cloud processing", "agriculture remote sensing", "insurance geohazard triage", "research collaboration"],
    },
    "north_slope": {
        "keywords": ["source provenance", "schema matching", "spatial joins", "public-safe scaffold"],
        "sector_advance": ["energy source libraries", "real-estate due diligence", "supply-chain site intelligence", "public-sector data portals"],
    },
    "rock_classification": {
        "keywords": ["spatial cross-validation", "GNN prospectivity", "spectral features", "class-imbalance check"],
        "sector_advance": ["resource mapping", "precision agriculture soil classes", "construction material screening", "environmental land-cover QA"],
    },
    "valles": {
        "keywords": ["method fusion", "uncertainty mask", "physics-aware review", "line registration"],
        "sector_advance": ["geothermal surveys", "infrastructure corridor risk", "water-resource screening", "site-remediation planning"],
    },
    "near_surface": {
        "keywords": ["multimodal fusion", "conflict-aware labels", "ERT/TEM/seismic features", "field-note review"],
        "sector_advance": ["near-surface engineering", "farm drainage mapping", "utility siting", "wetland monitoring"],
    },
    "moho_ml": {
        "keywords": ["gas hydrate well-log ML", "physics-informed ML", "well-held-out validation", "calibration and abstention"],
        "sector_advance": ["hydrate screening", "reservoir analog ranking", "carbon-storage review", "energy decision support"],
    },
    "ambient_noise": {
        "keywords": ["station-pair CCF", "stack stability", "continuous windows", "metadata QC"],
        "sector_advance": ["volcano monitoring", "infrastructure vibration alerts", "industrial equipment monitoring", "city-scale subsurface sensing"],
    },
    "stock_workflow": {
        "keywords": ["walk-forward testing", "drift monitoring", "baseline challenger", "leakage detection"],
        "sector_advance": ["finance dashboards", "sales forecasting", "inventory planning", "marketing spend monitoring"],
    },
    "sem_petrography": {
        "keywords": ["image labels", "multimodal classifiers", "proxy-claim audit", "expert review queue"],
        "sector_advance": ["petrography review", "materials QA", "agriculture soil microscopy", "manufacturing defect triage"],
    },
}


def apply_email_instruction_updates() -> None:
    """Keep the June 2026 email-driven website changes grouped and easy to audit."""
    for topic in TOPIC_ROOMS:
        overrides = EMAIL_TOPIC_ROOM_OVERRIDES.get(topic["slug"])
        if overrides:
            topic.update(overrides)

    TOPIC_FRAMES.update(EMAIL_FRAME_OVERRIDES)
    TOPIC_AI_LEVERS.update(EMAIL_AI_LEVER_OVERRIDES)
    TOPIC_VISUALS.update(EMAIL_VISUAL_OVERRIDES)
    CARD_VISUALS.update(EMAIL_CARD_VISUAL_OVERRIDES)
    WORKFLOW_BLUEPRINTS.update(EMAIL_WORKFLOW_BLUEPRINT_OVERRIDES)
    DISCUSSION_PROMPTS.update(EMAIL_DISCUSSION_PROMPT_OVERRIDES)
    EVIDENCE_LEADS.update(EMAIL_EVIDENCE_LEAD_OVERRIDES)
    PROCESSING_SKETCH_PLANS.update(EMAIL_PROCESSING_SKETCH_OVERRIDES)
    TOPIC_SITE_UPDATES.update(EMAIL_SITE_UPDATE_OVERRIDES)
    SLIDE_SOURCE_UPDATES.update(EMAIL_SLIDE_SOURCE_OVERRIDES)
    DETAILED_TOPIC_PLANS.update(EMAIL_DETAILED_TOPIC_PLAN_OVERRIDES)
    AI_WORKFLOW_EVIDENCE.update(EMAIL_AI_WORKFLOW_EVIDENCE_OVERRIDES)


apply_email_instruction_updates()

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
    page_title="AI Workflow Think Tank",
    page_icon="AI",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
<style>
    :root {
        --color-primary: #0B1F3A;
        --color-accent: #F28C28;
        --color-secondary: #7ED6DF;
        --color-background: #F5F1E8;
        --color-surface: #FFFFFF;
        --color-text: #222222;
        --color-muted: #64748B;
        --color-border: #CBD5E1;
    }
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
    .portfolio-intro {
        max-width: 920px;
        padding: 0.25rem 0 0.65rem;
    }
    .portfolio-eyebrow {
        color: #0f766e !important;
        font-size: 0.82rem;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 0.55rem;
    }
    .portfolio-intro h1 {
        color: #172033;
        font-size: 2.9rem;
        line-height: 1.06;
        margin: 0 0 0.45rem;
        max-width: 820px;
    }
    .portfolio-intro p {
        color: #475569;
        font-size: 1.08rem;
        line-height: 1.55;
        margin: 0;
        max-width: 780px;
    }
    .portfolio-proof {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
        margin: 0.25rem 0 1.65rem;
    }
    .portfolio-proof span {
        border: 1px solid #cbd5e1;
        border-radius: 999px;
        background: #f8fafc;
        color: #334155;
        font-size: 0.82rem;
        font-weight: 750;
        padding: 0.38rem 0.65rem;
    }
    .section-heading {
        display: flex;
        align-items: end;
        justify-content: space-between;
        gap: 1rem;
        margin: 0.8rem 0 0.3rem;
    }
    .section-heading-title {
        color: #172033;
        font-size: 1.45rem !important;
        font-weight: 800 !important;
        margin: 0;
        line-height: 1.2;
    }
    .section-heading span {
        color: #64748b;
        font-size: 0.88rem;
    }
    .audit-summary {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.8rem;
        margin: 1rem 0 1.5rem;
    }
    .audit-summary div {
        border: 1px solid #dbe3ea;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.8rem 0.9rem;
    }
    .audit-summary span {
        display: block;
        color: #64748b;
        font-size: 0.8rem;
        margin-bottom: 0.2rem;
    }
    .audit-summary strong {
        color: #172033;
        font-size: 1.65rem;
        line-height: 1;
    }
    .vision-board {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.85rem;
        margin: 1rem 0 1.4rem;
    }
    .vision-card {
        border: 1px solid #d8dee8;
        border-top: 5px solid #0f766e;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.9rem;
        min-height: 225px;
    }
    .vision-card.now { border-top-color: #f97316; }
    .vision-card.next { border-top-color: #2563eb; }
    .vision-card.later { border-top-color: #7c3aed; }
    .vision-card .horizon {
        color: #64748b;
        font-size: 0.76rem;
        font-weight: 850;
        text-transform: uppercase;
    }
    .vision-card h3 {
        color: #172033;
        font-size: 1.05rem;
        line-height: 1.25;
        margin: 0.35rem 0 0.45rem;
    }
    .vision-card p {
        color: #475569;
        font-size: 0.9rem;
        line-height: 1.38;
        margin: 0.3rem 0;
    }
    .vision-card .vision-next {
        border-left: 3px solid #cbd5e1;
        margin-top: 0.65rem;
        padding-left: 0.6rem;
        color: #334155;
        font-weight: 700;
    }
    .vision-meta {
        display: flex;
        flex-wrap: wrap;
        gap: 0.35rem;
        margin-top: 0.65rem;
    }
    .vision-meta span {
        border: 1px solid #dbe3ea;
        border-radius: 999px;
        background: #f8fafc;
        color: #475569;
        font-size: 0.72rem;
        font-weight: 750;
        padding: 0.22rem 0.44rem;
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
        display: flex;
        gap: 1rem;
        margin: 0.9rem 0 1rem;
        overflow-x: auto;
        padding: 0.2rem 0.2rem 0.85rem;
        scroll-snap-type: x proximity;
    }
    .future-timeline .timeline-node {
        position: relative;
        flex: 0 0 min(22rem, 86vw);
        border: 1px solid rgba(37, 99, 235, 0.25);
        border-top: 5px solid #2563eb;
        border-radius: 16px;
        background:
            radial-gradient(circle at 12% 10%, rgba(96, 165, 250, 0.16), transparent 30%),
            #eff6ff;
        padding: 0.95rem 1rem;
        min-height: 162px;
        scroll-snap-align: start;
        box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
    }
    .future-timeline .timeline-node::after {
        content: "";
        position: absolute;
        right: -1.05rem;
        top: 50%;
        width: 1.05rem;
        border-top: 2px dashed rgba(37, 99, 235, 0.42);
    }
    .future-timeline .timeline-node:last-child::after { display: none; }
    .future-timeline .timeline-node.model { border-top-color: #0f766e; }
    .future-timeline .timeline-node.deploy { border-top-color: #f97316; }
    .future-timeline .timeline-node em {
        display: block;
        margin-top: 0.65rem;
        color: #475569;
        font-size: 0.82rem;
        font-style: normal;
        line-height: 1.35;
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
        display: block;
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
    .think-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(24rem, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    .source-update-panel {
        display: grid;
        grid-template-columns: minmax(16rem, 0.85fr) minmax(0, 1.35fr);
        gap: 1rem;
        align-items: start;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background:
            radial-gradient(circle at 94% 0%, rgba(20, 184, 166, 0.12), transparent 28%),
            linear-gradient(135deg, #ffffff 0%, #eef6f5 100%);
        padding: 1rem;
        margin: 1rem 0 1.25rem;
    }
    .source-update-panel h3 {
        color: #172033;
        font-size: 1.18rem;
        line-height: 1.25;
        margin: 0.35rem 0 0.5rem;
    }
    .source-update-panel p {
        color: #475569;
        font-size: 0.94rem;
        line-height: 1.45;
        margin: 0;
    }
    .source-update-kicker,
    .source-update-card span {
        color: #0f766e;
        display: block;
        font-size: 0.74rem;
        font-weight: 850;
        text-transform: uppercase;
    }
    .source-update-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.75rem;
        margin: 0.85rem 0 1.1rem;
    }
    .source-update-grid-tight {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        margin: 0;
    }
    .source-update-card {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.8rem 0.85rem;
        min-height: 10.25rem;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
    }
    .source-update-card strong {
        color: #172033;
        display: block;
        font-size: 0.98rem;
        line-height: 1.25;
        margin: 0.35rem 0 0.42rem;
    }
    .source-update-card p {
        color: #475569;
        font-size: 0.88rem;
        line-height: 1.38;
        margin: 0;
    }
    .north-slope-ml-card {
        min-height: 8.5rem;
    }
    .public-system-legend {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.6rem;
        margin: 0.85rem 0 1rem;
    }
    .public-system-legend div {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.82);
        padding: 0.65rem 0.75rem;
        color: #475569;
        font-size: 0.84rem;
        line-height: 1.35;
    }
    .public-system-legend strong {
        display: block;
        color: #172033;
        font-size: 0.82rem;
        margin-bottom: 0.2rem;
        text-transform: uppercase;
    }
    .topic-update-panel {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background:
            radial-gradient(circle at 94% 0%, rgba(37, 99, 235, 0.10), transparent 26%),
            #ffffff;
        padding: 1rem;
        margin: 1rem 0 1.2rem;
    }
    .topic-update-kicker {
        color: #0f766e;
        display: block;
        font-size: 0.75rem;
        font-weight: 850;
        text-transform: uppercase;
    }
    .topic-update-panel h3 {
        color: #172033;
        margin: 0.35rem 0 0.45rem;
        font-size: 1.16rem;
        line-height: 1.25;
    }
    .topic-update-panel p {
        color: #475569;
        margin: 0 0 0.85rem;
        line-height: 1.45;
    }
    .topic-update-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.6rem;
    }
    .topic-update-item {
        border: 1px solid #d8dee8;
        border-left: 4px solid #0f766e;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.65rem 0.7rem;
        min-height: 6rem;
    }
    .topic-update-item strong {
        display: block;
        color: #172033;
        font-size: 0.86rem;
        margin-bottom: 0.28rem;
        text-transform: uppercase;
    }
    .topic-update-item span {
        color: #475569;
        font-size: 0.84rem;
        line-height: 1.35;
    }
    .slide-source-strip {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
        gap: 0.6rem;
        margin: 0.8rem 0 1.2rem;
    }
    .slide-source-note {
        border: 1px solid #bfdbfe;
        border-radius: 8px;
        background: #eff6ff;
        padding: 0.72rem 0.8rem;
    }
    .slide-source-note strong {
        display: block;
        color: #1e3a8a;
        font-size: 0.86rem;
        margin-bottom: 0.25rem;
    }
    .slide-source-note span {
        color: #334155;
        font-size: 0.84rem;
        line-height: 1.35;
    }
    .north-decision-board {
        display: grid;
        grid-template-columns: minmax(0, 1fr) minmax(0, 0.9fr);
        gap: 0.9rem;
        margin: 1rem 0 1.25rem;
    }
    .well-log-panel,
    .decision-branches {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.9rem;
    }
    .well-log-panel h3,
    .decision-branches h3 {
        color: #172033;
        margin: 0 0 0.65rem;
        font-size: 1.05rem;
    }
    .well-log-track {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 0.42rem;
        min-height: 14rem;
    }
    .well-log-track span {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background:
            linear-gradient(180deg, rgba(15,118,110,0.18), transparent 25%, rgba(249,115,22,0.18) 52%, transparent 76%, rgba(37,99,235,0.18)),
            #f8fafc;
        color: #172033;
        display: flex;
        align-items: end;
        justify-content: center;
        padding: 0.55rem 0.3rem;
        font-size: 0.76rem;
        font-weight: 800;
        text-align: center;
        text-transform: uppercase;
    }
    .decision-branch {
        border-left: 4px solid #0f766e;
        background: #ecfdf5;
        border-radius: 8px;
        margin-bottom: 0.55rem;
        padding: 0.62rem 0.7rem;
    }
    .decision-branch.more { border-left-color: #f97316; background: #fff7ed; }
    .decision-branch.low { border-left-color: #64748b; background: #f8fafc; }
    .decision-branch strong {
        color: #172033;
        display: block;
        font-size: 0.9rem;
        text-transform: uppercase;
    }
    .decision-branch span {
        color: #475569;
        font-size: 0.86rem;
    }
    .feedback-card-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.75rem;
        margin: 1rem 0 1.25rem;
    }
    .feedback-card {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.95rem;
        min-height: 10rem;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
    }
    .feedback-card strong {
        color: #172033;
        display: block;
        font-size: 1rem;
        margin-bottom: 0.45rem;
    }
    .feedback-card p {
        color: #475569;
        font-size: 0.9rem;
        line-height: 1.42;
        margin: 0;
    }
    .think-grid.topic-wall {
        position: relative;
        padding: 0.65rem;
        border: 1px solid #dbe3ea;
        border-radius: 10px;
        background:
            radial-gradient(circle at 12% 16%, rgba(15,118,110,0.12), transparent 20%),
            radial-gradient(circle at 88% 22%, rgba(249,115,22,0.12), transparent 22%),
            radial-gradient(circle at 50% 95%, rgba(37,99,235,0.12), transparent 24%),
            linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        overflow: hidden;
    }
    .think-grid.topic-wall::before {
        content: "";
        position: absolute;
        inset: 1.3rem;
        background:
            linear-gradient(90deg, transparent 0 12%, rgba(148,163,184,0.38) 12% 13%, transparent 13% 44%, rgba(148,163,184,0.34) 44% 45%, transparent 45% 76%, rgba(148,163,184,0.32) 76% 77%, transparent 77%),
            linear-gradient(0deg, transparent 0 30%, rgba(148,163,184,0.25) 30% 31%, transparent 31% 64%, rgba(148,163,184,0.25) 64% 65%, transparent 65%);
        pointer-events: none;
        animation: wallPulse 5s ease-in-out infinite;
    }
    @keyframes wallPulse {
        0%, 100% { opacity: 0.38; }
        50% { opacity: 0.7; }
    }
    .think-card {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.95rem;
        min-height: 380px;
        display: flex;
        flex-direction: column;
        gap: 0.7rem;
        position: relative;
        z-index: 1;
    }
    .think-grid.compact .think-card { min-height: 286px; }
    .think-card-link {
        color: inherit;
        text-decoration: none !important;
        display: block;
    }
    .think-card-link:hover,
    .think-card-link:focus,
    .think-card-link *,
    .think-card-link:hover *,
    .think-card-link:focus * {
        text-decoration: none !important;
    }
    .think-card-link:hover .think-card,
    .think-card-link:focus .think-card {
        border-color: #0f766e;
        box-shadow: 0 8px 24px rgba(15, 118, 110, 0.12);
        transform: translateY(-2px);
    }
    .think-card {
        transition: border-color 120ms ease, box-shadow 120ms ease, transform 120ms ease;
    }
    .topic-signal {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        background:
            radial-gradient(circle at 16% 28%, #0f766e 0 8px, transparent 9px),
            radial-gradient(circle at 40% 54%, #2563eb 0 7px, transparent 8px),
            radial-gradient(circle at 68% 32%, #f97316 0 8px, transparent 9px),
            radial-gradient(circle at 86% 68%, #64748b 0 7px, transparent 8px),
            linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
        min-height: 118px;
        position: relative;
        overflow: hidden;
    }
    .topic-poster {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        background: #ffffff;
        overflow: hidden;
        position: relative;
    }
    .topic-poster > img {
        display: block;
        width: 100% !important;
        max-width: 100% !important;
        height: auto !important;
    }
    .topic-poster-composite.card-visual > img {
        aspect-ratio: 16 / 9;
        height: 220px !important;
        object-fit: contain;
        background: #f8fafc;
    }
    .topic-card-keywords {
        display: none;
    }
    .topic-card-keywords span {
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid rgba(255,255,255,0.22);
        border-radius: 999px;
        color: #ffffff;
        padding: 0.18rem 0.38rem;
        font-size: 0.68rem;
        font-weight: 850;
        text-transform: uppercase;
    }
    .topic-room-visual > img {
        max-height: 430px !important;
        object-fit: contain;
        background: #f8fafc;
    }
    .topic-proof-inset {
        position: absolute;
        right: 0.52rem;
        bottom: 0.52rem;
        width: 38%;
        min-width: 86px;
        border: 2px solid #ffffff;
        border-radius: 7px;
        overflow: hidden;
        background: #0f172a;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.22);
    }
    .topic-proof-inset img {
        display: block;
        width: 100%;
        aspect-ratio: 4 / 3;
        object-fit: cover;
        opacity: 0.92;
    }
    .topic-proof-inset span {
        display: block;
        padding: 0.16rem 0.28rem;
        color: #ffffff;
        font-size: 0.58rem;
        font-weight: 900;
        letter-spacing: 0.06em;
        text-align: center;
    }
    .topic-proof-inset.text-only {
        min-height: 78px;
        display: grid;
        place-items: center;
        padding-top: 0.35rem;
        color: #ffffff;
    }
    .topic-proof-inset.text-only svg {
        width: 34px;
        height: 34px;
    }
    .topic-pattern.fallback-pattern {
        position: relative;
        left: auto;
        bottom: auto;
        max-width: none;
        min-height: 145px;
        padding: 1rem;
        align-content: center;
        justify-content: center;
        background: #f8fafc;
    }
    .topic-signal::before {
        content: "";
        position: absolute;
        left: 14%;
        top: 50%;
        width: 72%;
        border-top: 3px dotted #94a3b8;
        transform: rotate(-6deg);
    }
    .topic-signal::after {
        content: "AI workflow";
        position: absolute;
        right: 0.7rem;
        bottom: 0.55rem;
        color: #334155;
        font-size: 0.78rem;
        font-weight: 800;
        text-transform: uppercase;
    }
    .topic-pattern {
        position: absolute;
        left: 0.65rem;
        bottom: 0.55rem;
        display: flex;
        flex-wrap: wrap;
        gap: 0.28rem;
        max-width: 70%;
    }
    .topic-pattern span {
        background: rgba(255,255,255,0.82);
        border: 1px solid #cbd5e1;
        border-radius: 999px;
        padding: 0.2rem 0.42rem;
        color: #0f172a;
        font-size: 0.72rem;
        font-weight: 750;
    }
    .think-title {
        color: #172033;
        font-size: 0.78rem;
        font-weight: 850;
        line-height: 1.15;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }
    .think-question {
        font-size: 1.18rem;
        line-height: 1.22;
        color: #111827;
        font-weight: 850;
        margin: 0;
    }
    .think-example {
        color: #475569;
        font-size: 0.86rem;
        line-height: 1.34;
        margin: 0;
    }
    .project-status {
        align-self: flex-start;
        border: 1px solid #a7f3d0;
        border-radius: 999px;
        background: #ecfdf5;
        color: #065f46;
        font-size: 0.72rem;
        font-weight: 800;
        padding: 0.22rem 0.48rem;
        text-transform: uppercase;
    }
    .project-status.prototype {
        border-color: #bfdbfe;
        background: #eff6ff;
        color: #1d4ed8;
    }
    .project-status.evidence {
        border-color: #fed7aa;
        background: #fff7ed;
        color: #9a3412;
    }
    .think-raise {
        border-left: 4px solid #0f766e;
        background: #f0fdfa;
        color: #134e4a;
        padding: 0.5rem 0.62rem;
        font-size: 0.82rem;
        font-weight: 750;
        line-height: 1.25;
        margin-top: auto;
    }
    .unfinished-note {
        border: 1px solid #fed7aa;
        border-left: 5px solid #f97316;
        border-radius: 8px;
        background: #fff7ed;
        color: #7c2d12;
        padding: 0.75rem 0.9rem;
        margin: 0.9rem 0 1rem 0;
        font-size: 0.96rem;
        line-height: 1.35;
    }
    .blueprint {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.9rem;
        margin: 0.8rem 0 1rem 0;
    }
    .blueprint h3 {
        margin: 0 0 0.75rem 0;
        color: #111827;
        font-size: 1.05rem;
    }
    .blueprint-steps {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 0.6rem;
        align-items: stretch;
    }
    .blue-step {
        border: 1px solid #dbe3ea;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.7rem;
        min-height: 118px;
        position: relative;
    }
    .blue-step:not(:last-child)::after {
        content: "";
        position: absolute;
        top: 50%;
        right: -0.55rem;
        width: 0.55rem;
        border-top: 3px dotted #64748b;
    }
    .blue-index {
        width: 1.35rem;
        height: 1.35rem;
        border-radius: 50%;
        background: #0f766e;
        color: #ffffff;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 0.78rem;
        font-weight: 850;
        margin-bottom: 0.45rem;
    }
    .blue-step strong {
        display: block;
        color: #111827;
        font-size: 0.9rem;
        margin-bottom: 0.25rem;
    }
    .blue-step span {
        color: #475569;
        font-size: 0.84rem;
        line-height: 1.28;
    }
    .blue-outcome {
        border-left: 4px solid #2563eb;
        background: #eff6ff;
        color: #1e3a8a;
        padding: 0.62rem 0.75rem;
        margin-top: 0.75rem;
        font-size: 0.92rem;
        line-height: 1.32;
    }
    .workflow-tree {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background:
            radial-gradient(circle at 50% 12%, rgba(15,118,110,0.08), transparent 28%),
            #ffffff;
        padding: 1rem;
        margin: 0.8rem 0 1rem;
    }
    .workflow-tree h3 {
        color: #172033;
        font-size: 1.05rem;
        margin: 0 0 0.8rem;
        text-align: center;
    }
    .workflow-root {
        width: min(280px, 90%);
        margin: 0 auto 1.4rem;
        border: 2px solid #0f766e;
        border-radius: 8px;
        background: #f0fdfa;
        color: #134e4a;
        padding: 0.7rem;
        text-align: center;
        font-weight: 850;
        position: relative;
    }
    .workflow-root::after {
        content: "";
        position: absolute;
        left: 50%;
        bottom: -1.4rem;
        height: 1.4rem;
        border-left: 3px solid #94a3b8;
    }
    .workflow-branches {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 0.65rem;
        position: relative;
    }
    .workflow-branches::before {
        content: "";
        position: absolute;
        left: 10%;
        right: 10%;
        top: -0.7rem;
        border-top: 3px solid #94a3b8;
    }
    .workflow-node {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.65rem;
        min-height: 112px;
        text-align: center;
        position: relative;
    }
    .workflow-node::before {
        content: "";
        position: absolute;
        left: 50%;
        top: -0.7rem;
        height: 0.7rem;
        border-left: 3px solid #94a3b8;
    }
    .workflow-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 3rem;
        height: 3rem;
        border-radius: 50%;
        background: #e2e8f0;
        color: #172033;
        margin-bottom: 0.45rem;
        padding: 0.55rem;
    }
    .workflow-icon svg {
        display: block;
        width: 100%;
        height: 100%;
    }
    .workflow-node strong {
        display: block;
        color: #172033;
        font-size: 0.88rem;
        margin-bottom: 0.25rem;
    }
    .workflow-node span {
        color: #64748b;
        font-size: 0.8rem;
        line-height: 1.25;
    }
    .workflow-result {
        border-left: 4px solid #f97316;
        background: #fff7ed;
        color: #7c2d12;
        padding: 0.65rem 0.75rem;
        margin-top: 0.85rem;
        font-size: 0.9rem;
        line-height: 1.3;
    }
    .current-future-board {
        display: grid;
        grid-template-columns: minmax(0, 1fr) 150px minmax(0, 1fr);
        gap: 0.75rem;
        align-items: stretch;
        margin: 0.9rem 0 1rem;
    }
    .state-side {
        border: 1px solid #dbe3ea;
        border-radius: 10px;
        background: #ffffff;
        padding: 0.8rem;
    }
    .state-side.current { border-top: 5px solid #0f766e; }
    .state-side.future { border-top: 5px solid #2563eb; }
    .state-kicker {
        color: #475569;
        font-size: 0.74rem;
        font-weight: 900;
        letter-spacing: 0.08em;
        margin-bottom: 0.55rem;
    }
    .state-flow {
        display: grid;
        gap: 0.45rem;
    }
    .state-step {
        display: grid;
        grid-template-columns: 42px minmax(0, 1fr);
        gap: 0.55rem;
        align-items: center;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.48rem;
        color: #334155;
        font-size: 0.84rem;
        line-height: 1.25;
        font-weight: 700;
    }
    .state-step svg {
        width: 32px;
        height: 32px;
        color: #0f766e;
    }
    .state-step.future svg { color: #2563eb; }
    .guidance-gate {
        border: 2px solid #dc2626;
        border-radius: 10px;
        background: #fff1f2;
        color: #991b1b;
        padding: 0.75rem 0.6rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        gap: 0.35rem;
    }
    .guidance-gate svg {
        width: 42px;
        height: 42px;
    }
    .guidance-gate strong {
        font-size: 0.9rem;
        line-height: 1.06;
        letter-spacing: 0.04em;
    }
    .guidance-gate span {
        color: #7f1d1d;
        font-size: 0.74rem;
        font-weight: 800;
    }
    .project-stage {
        position: relative;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        background: #f8fafc;
        overflow: hidden;
        min-height: 430px;
        margin: 0.9rem 0 1rem;
    }
    .stage-label {
        position: absolute;
        z-index: 4;
        border-radius: 7px;
        background: rgba(15, 23, 42, 0.92);
        color: #ffffff;
        padding: 0.42rem 0.58rem;
        font-size: 0.72rem;
        font-weight: 900;
        letter-spacing: 0.05em;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.2);
    }
    .stage-label.failure { background: #b91c1c; }
    .stage-label.review { background: #fff1f2; color: #991b1b; border: 2px solid #dc2626; }
    .agent-stage {
        min-height: 500px;
        background-size: cover;
        background-position: center;
    }
    .agent-stage::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, rgba(15,23,42,0.13), rgba(255,255,255,0.03));
    }
    .record-dot {
        position: absolute;
        z-index: 4;
        top: 1rem;
        right: 1rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
        border-radius: 999px;
        background: #ffffff;
        color: #991b1b;
        padding: 0.35rem 0.55rem;
        font-size: 0.72rem;
        font-weight: 900;
    }
    .record-dot::before {
        content: "";
        width: 0.62rem;
        height: 0.62rem;
        border-radius: 50%;
        background: #dc2626;
        animation: recordPulse 1.2s ease-in-out infinite;
    }
    @keyframes recordPulse { 50% { opacity: 0.3; transform: scale(0.75); } }
    .action-marker {
        position: absolute;
        z-index: 3;
        width: 2rem;
        height: 2rem;
        border-radius: 50%;
        display: grid;
        place-items: center;
        background: #f97316;
        color: #ffffff;
        border: 3px solid #ffffff;
        font-size: 0.8rem;
        font-weight: 900;
        box-shadow: 0 5px 14px rgba(15,23,42,0.25);
    }
    .agent-lanes {
        position: absolute;
        z-index: 3;
        left: 1rem;
        right: 1rem;
        bottom: 1rem;
        display: grid;
        grid-template-columns: 1fr 110px 1fr;
        gap: 0.55rem;
        align-items: center;
    }
    .agent-lane {
        border: 1px solid rgba(255,255,255,0.8);
        border-radius: 8px;
        background: rgba(255,255,255,0.94);
        padding: 0.58rem;
        color: #172033;
        font-size: 0.78rem;
        font-weight: 850;
        text-align: center;
    }
    .rubric-gate {
        border: 2px solid #dc2626;
        border-radius: 8px;
        background: #fff1f2;
        color: #991b1b;
        padding: 0.58rem 0.35rem;
        font-size: 0.72rem;
        font-weight: 900;
        text-align: center;
    }
    .evidence-chain {
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 0.55rem;
        align-items: stretch;
        padding: 1rem;
        min-height: 310px;
    }
    .chain-node {
        position: relative;
        border: 1px solid #dbe3ea;
        border-radius: 9px;
        background: #ffffff;
        padding: 0.55rem;
        min-height: 190px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 0.45rem;
        color: #334155;
        text-align: center;
        font-size: 0.76rem;
        font-weight: 800;
    }
    .chain-node:not(:last-child)::after {
        content: "";
        position: absolute;
        top: 50%;
        right: -0.58rem;
        width: 0.58rem;
        border-top: 3px dotted #94a3b8;
        z-index: 3;
    }
    .chain-node.human::after { border-top-style: solid; border-color: #f97316; }
    .chain-node img {
        width: 100%;
        height: 118px;
        object-fit: contain;
        border-radius: 6px;
        background: #0f172a;
    }
    .chain-node svg { width: 52px; height: 52px; }
    .mini-table {
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr;
        border: 1px solid #cbd5e1;
        font-size: 0.62rem;
    }
    .mini-table span { padding: 0.25rem; border: 1px solid #e2e8f0; }
    .question-node {
        border: 2px solid #f97316;
        box-shadow: 0 0 0 7px rgba(249,115,22,0.12);
    }
    .output-branches {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0.45rem;
        padding: 0 1rem 1rem;
    }
    .output-branches div {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.55rem;
        text-align: center;
        color: #334155;
        font-size: 0.78rem;
        font-weight: 850;
    }
    .output-branches .question { border-style: dashed; color: #9a3412; }
    .transfer-stage, .pipeline-stage, .property-stage {
        display: grid;
        align-items: center;
        gap: 0.7rem;
        padding: 1rem;
    }
    .transfer-stage { grid-template-columns: 1fr 130px 1fr; }
    .region-panel, .pipeline-node, .property-inputs, .map-output {
        border: 1px solid #dbe3ea;
        border-radius: 9px;
        background: #ffffff;
        padding: 0.7rem;
        min-height: 250px;
    }
    .region-panel h4, .pipeline-node strong, .property-inputs strong, .map-output strong {
        display: block;
        margin: 0 0 0.45rem;
        color: #172033;
        font-size: 0.82rem;
        letter-spacing: 0.04em;
    }
    .region-panel img, .map-output img {
        width: 100%;
        height: 190px;
        object-fit: cover;
        border-radius: 6px;
    }
    .sample-field {
        height: 190px;
        border-radius: 7px;
        background:
            radial-gradient(circle at 18% 22%, #2563eb 0 5px, transparent 6px),
            radial-gradient(circle at 35% 65%, #0f766e 0 6px, transparent 7px),
            radial-gradient(circle at 72% 28%, #f97316 0 5px, transparent 6px),
            radial-gradient(circle at 81% 72%, #2563eb 0 5px, transparent 6px),
            radial-gradient(circle at 55% 48%, #dc2626 0 7px, transparent 8px),
            linear-gradient(135deg, #dbeafe, #f8fafc);
    }
    .model-gate {
        border: 2px solid #2563eb;
        border-radius: 10px;
        background: #eff6ff;
        color: #1e3a8a;
        padding: 1rem 0.5rem;
        text-align: center;
        font-weight: 900;
    }
    .leakage-gate {
        margin-top: 0.55rem;
        border: 2px solid #dc2626;
        border-radius: 7px;
        background: #fff1f2;
        color: #991b1b;
        padding: 0.42rem;
        text-align: center;
        font-size: 0.7rem;
        font-weight: 900;
    }
    .residual-dots {
        display: flex;
        gap: 0.35rem;
        justify-content: center;
        margin-top: 0.5rem;
    }
    .residual-dots i {
        width: 0.7rem;
        height: 0.7rem;
        border-radius: 50%;
        background: #dc2626;
    }
    .residual-dots i:nth-child(even) { background: #2563eb; }
    .pipeline-stage { grid-template-columns: repeat(5, minmax(0, 1fr)); }
    .pipeline-node {
        min-height: 175px;
        display: grid;
        place-items: center;
        text-align: center;
        position: relative;
    }
    .pipeline-node:not(:last-child)::after {
        content: "→";
        position: absolute;
        right: -0.72rem;
        top: 44%;
        color: #64748b;
        font-size: 1.35rem;
        font-weight: 900;
        z-index: 3;
    }
    .pipeline-node svg { width: 58px; height: 58px; color: #2563eb; }
    .pipeline-node.blocked { border: 2px solid #dc2626; background: #fff1f2; }
    .file-rain { display: flex; flex-wrap: wrap; gap: 0.28rem; justify-content: center; }
    .file-rain span { width: 1.2rem; height: 1.55rem; border: 2px solid #64748b; border-radius: 2px; animation: fileDrop 2.4s ease-in-out infinite; }
    .file-rain span:nth-child(even) { animation-delay: 0.6s; }
    @keyframes fileDrop { 50% { transform: translateY(8px); opacity: 0.45; } }
    .property-stage { grid-template-columns: 1fr 120px 1.35fr; }
    .property-chips { display: grid; gap: 0.4rem; }
    .property-chips span {
        border-radius: 999px;
        padding: 0.35rem 0.5rem;
        color: #ffffff;
        font-size: 0.74rem;
        font-weight: 900;
        text-align: center;
    }
    .property-chips span:nth-child(1) { background: #0f766e; }
    .property-chips span:nth-child(2) { background: #2563eb; }
    .property-chips span:nth-child(3) { background: #7c3aed; }
    .property-chips span:nth-child(4) { background: #f97316; }
    .property-chips span:nth-child(5) { background: #475569; }
    .range-gate {
        border: 2px solid #172033;
        border-radius: 9px;
        padding: 0.7rem 0.4rem;
        background: #ffffff;
        color: #172033;
        text-align: center;
        font-size: 0.75rem;
        font-weight: 900;
    }
    .prompt-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.65rem;
        margin: 0.75rem 0;
    }
    .prompt-card {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.7rem;
        color: #334155;
        min-height: 92px;
        font-size: 0.92rem;
        line-height: 1.32;
    }
    .source-chip-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.5rem;
        margin: 0.7rem 0;
    }
    .source-chip {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.55rem;
        color: #334155;
        font-size: 0.86rem;
        line-height: 1.25;
    }
    .source-chip strong {
        display: block;
        color: #111827;
        margin-bottom: 0.2rem;
    }
    .sketch-card {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.9rem;
        margin: 0.8rem 0 1rem 0;
    }
    .sketch-card h3 {
        margin: 0 0 0.55rem 0;
        color: #111827;
        font-size: 1.05rem;
    }
    .sketch-body {
        display: grid;
        grid-template-columns: 1.1fr 0.9fr;
        gap: 0.8rem;
        align-items: stretch;
    }
    .motion-strip {
        display: flex;
        flex-wrap: wrap;
        gap: 0.35rem;
        margin: 0.55rem 0;
    }
    .motion-pill {
        border: 1px solid #c4b5fd;
        border-radius: 999px;
        background: #f5f3ff;
        color: #4c1d95;
        padding: 0.3rem 0.48rem;
        font-size: 0.78rem;
        font-weight: 800;
    }
    .sketch-panel {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.68rem;
        min-height: 118px;
    }
    .sketch-panel strong {
        display: block;
        color: #0f172a;
        margin-bottom: 0.3rem;
        font-size: 0.86rem;
        text-transform: uppercase;
    }
    .sketch-panel span {
        color: #475569;
        font-size: 0.9rem;
        line-height: 1.32;
    }
    .sketch-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.8rem;
        margin: 0.85rem 0;
    }
    .ai-case-brief {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.9rem;
        margin: 0.75rem 0 1rem 0;
    }
    .ai-case-top {
        display: grid;
        grid-template-columns: 1.1fr 1fr;
        gap: 0.8rem;
        align-items: start;
        margin-bottom: 0.75rem;
    }
    .ai-case-top h3 {
        margin: 0 0 0.35rem 0;
        font-size: 1.05rem;
        color: #111827;
    }
    .ai-case-top p {
        margin: 0;
        color: #475569;
        line-height: 1.35;
    }
    .ai-chip-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.35rem;
        justify-content: flex-end;
    }
    .ai-chip {
        border: 1px solid #bfdbfe;
        border-radius: 999px;
        background: #eff6ff;
        color: #1e3a8a;
        padding: 0.32rem 0.55rem;
        font-size: 0.82rem;
        font-weight: 750;
    }
    .ai-evidence-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.65rem;
    }
    .ai-evidence-cell {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.72rem;
        min-height: 138px;
    }
    .ai-evidence-cell strong {
        display: block;
        color: #0f172a;
        font-size: 0.86rem;
        margin-bottom: 0.35rem;
        text-transform: uppercase;
    }
    .ai-evidence-cell span {
        color: #475569;
        font-size: 0.9rem;
        line-height: 1.32;
    }
    .ai-evidence-cell.validation {
        background: #fff7ed;
        border-color: #fed7aa;
    }
    .ai-future-line {
        border-left: 4px solid #2563eb;
        background: #eff6ff;
        color: #1e3a8a;
        padding: 0.62rem 0.75rem;
        margin-top: 0.72rem;
        font-size: 0.92rem;
        line-height: 1.32;
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
    .research-source-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.55rem;
        margin: 0.75rem 0 1rem 0;
    }
    .research-source-grid a {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #f8fafc;
        color: #0f172a;
        padding: 0.58rem 0.65rem;
        text-decoration: none;
        font-weight: 750;
        font-size: 0.86rem;
        line-height: 1.25;
    }
    .detail-card {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.92rem;
        margin: 0.85rem 0 1.05rem 0;
    }
    .detail-card h3 {
        margin: 0 0 0.35rem 0;
        color: #111827;
        font-size: 1.08rem;
    }
    .detail-question {
        color: #0f766e;
        font-weight: 850;
        line-height: 1.3;
        margin-bottom: 0.65rem;
    }
    .detail-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.65rem;
        margin-top: 0.65rem;
    }
    .detail-cell {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.7rem;
        min-height: 122px;
    }
    .detail-cell strong {
        display: block;
        color: #0f172a;
        font-size: 0.82rem;
        margin-bottom: 0.32rem;
        text-transform: uppercase;
    }
    .detail-cell span {
        display: block;
        color: #475569;
        font-size: 0.9rem;
        line-height: 1.32;
    }
    .detail-pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.32rem;
    }
    .detail-pill {
        border: 1px solid #bae6fd;
        border-radius: 999px;
        background: #f0f9ff;
        color: #075985;
        padding: 0.26rem 0.46rem;
        font-size: 0.78rem;
        font-weight: 800;
    }
    .story-frames {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.5rem;
        margin-top: 0.55rem;
    }
    .story-frame {
        border: 1px dashed #94a3b8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.52rem;
        min-height: 82px;
        color: #475569;
        font-size: 0.84rem;
        line-height: 1.28;
    }
    .story-frame b {
        display: block;
        color: #111827;
        margin-bottom: 0.22rem;
    }
    .honesty-box {
        border-left: 4px solid #dc2626;
        background: #fef2f2;
        color: #7f1d1d;
        padding: 0.62rem 0.72rem;
        margin-top: 0.65rem;
        font-size: 0.9rem;
        line-height: 1.32;
    }
    .manual-architecture {
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        background:
            linear-gradient(135deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
        box-shadow: 0 18px 42px rgba(15, 23, 42, 0.08);
        padding: 1rem;
        margin: 1rem 0 1.25rem;
    }
    .manual-architecture.priority {
        border-color: rgba(15, 118, 110, 0.55);
        box-shadow: 0 18px 42px rgba(15, 118, 110, 0.13);
    }
    .manual-head {
        display: flex;
        align-items: start;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 0.9rem;
    }
    .manual-kicker {
        color: #0f766e;
        font-size: 0.75rem;
        font-weight: 900;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }
    .manual-head h3 {
        margin: 0.25rem 0 0;
        color: #172033;
        font-size: 1.22rem;
        line-height: 1.2;
    }
    .manual-output {
        border: 1px solid #fde68a;
        border-left: 5px solid #f59e0b;
        border-radius: 8px;
        background: #fffbeb;
        color: #78350f;
        flex: 0 1 18rem;
        padding: 0.62rem 0.72rem;
        font-size: 0.86rem;
        line-height: 1.32;
    }
    .manual-board {
        display: grid;
        grid-template-columns: minmax(13rem, 0.85fr) minmax(0, 1.6fr) minmax(13rem, 0.9fr);
        gap: 0.8rem;
        align-items: stretch;
    }
    .manual-panel {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.78rem;
        min-height: 13rem;
    }
    .manual-panel h4 {
        color: #172033;
        font-size: 0.84rem;
        margin: 0 0 0.55rem;
        text-transform: uppercase;
    }
    .manual-source-grid,
    .manual-gate-list {
        display: grid;
        gap: 0.42rem;
    }
    .manual-source-item,
    .manual-gate-item {
        border-radius: 8px;
        color: #1f2937;
        font-size: 0.82rem;
        font-weight: 750;
        line-height: 1.24;
        padding: 0.48rem 0.55rem;
    }
    .manual-source-item {
        border: 1px solid #bfdbfe;
        background: #eff6ff;
    }
    .manual-gate-item {
        border: 1px solid #fecaca;
        background: #fef2f2;
        color: #7f1d1d;
    }
    .manual-model {
        border: 1px solid #0f766e;
        border-radius: 8px;
        background: #0f766e;
        color: #ffffff;
        padding: 0.7rem 0.78rem;
        margin-bottom: 0.68rem;
        text-align: center;
        font-size: 0.9rem;
        line-height: 1.28;
        font-weight: 850;
    }
    .manual-flow {
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 0.42rem;
        align-items: stretch;
    }
    .manual-flow-node {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #f8fafc;
        min-height: 6.6rem;
        padding: 0.54rem 0.5rem;
        position: relative;
        text-align: center;
    }
    .manual-flow-node:not(:last-child)::after {
        content: "";
        position: absolute;
        right: -0.48rem;
        top: 50%;
        width: 0.52rem;
        border-top: 2px solid #94a3b8;
    }
    .manual-flow-node.gate {
        border-color: #fca5a5;
        background: #fff7ed;
    }
    .manual-node-icon {
        color: #0f766e;
        height: 2rem;
        margin-bottom: 0.3rem;
    }
    .manual-node-icon svg {
        width: 2rem;
        height: 2rem;
    }
    .manual-flow-node strong {
        display: block;
        color: #172033;
        font-size: 0.72rem;
        margin-bottom: 0.2rem;
        text-transform: uppercase;
    }
    .manual-flow-node span {
        color: #475569;
        display: block;
        font-size: 0.78rem;
        line-height: 1.22;
    }
    .manual-vocab-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.38rem;
        margin-top: 0.75rem;
    }
    .manual-vocab {
        border: 1px solid #99f6e4;
        border-radius: 999px;
        background: #ecfdf5;
        color: #134e4a;
        font-size: 0.75rem;
        font-weight: 850;
        padding: 0.28rem 0.48rem;
    }
    .manual-prompt {
        border-left: 4px solid #2563eb;
        background: #eff6ff;
        color: #1e3a8a;
        border-radius: 8px;
        font-size: 0.88rem;
        line-height: 1.35;
        margin-top: 0.8rem;
        padding: 0.62rem 0.72rem;
    }
    .manual-prompt strong {
        display: block;
        margin-bottom: 0.18rem;
        text-transform: uppercase;
        font-size: 0.76rem;
    }
    .rich-manual {
        border-radius: 8px;
        background: #ffffff;
        padding: 0.95rem;
    }
    .rich-head {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 0.85rem;
        margin-bottom: 0.85rem;
    }
    .rich-kicker {
        color: #334155;
        font-size: 0.72rem;
        font-weight: 900;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }
    .rich-head h3 {
        color: #111827;
        font-size: 1.2rem;
        line-height: 1.18;
        margin: 0.18rem 0 0;
    }
    .rich-output {
        border: 1px solid #fbbf24;
        border-left: 5px solid #d97706;
        border-radius: 8px;
        background: #fffbeb;
        color: #78350f;
        flex: 0 1 18rem;
        font-size: 0.82rem;
        font-weight: 750;
        line-height: 1.25;
        padding: 0.58rem 0.65rem;
    }
    .rich-diagram {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.82rem;
    }
    .rich-stage-grid {
        display: grid;
        grid-template-columns: minmax(0, 1fr) 2.4rem minmax(0, 1.12fr) 2.4rem minmax(0, 1fr);
        gap: 0.55rem;
        align-items: stretch;
    }
    .rich-stage {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        min-width: 0;
        padding: 0.68rem;
    }
    .rich-stage h4 {
        color: #172033;
        font-size: 0.76rem;
        letter-spacing: 0.04em;
        line-height: 1.18;
        margin: 0 0 0.52rem;
        text-transform: uppercase;
    }
    .rich-arrow {
        align-self: center;
        height: 2px;
        position: relative;
        background: #64748b;
    }
    .rich-arrow::after {
        border-right: 2px solid #64748b;
        border-top: 2px solid #64748b;
        content: "";
        height: 0.48rem;
        position: absolute;
        right: -0.02rem;
        top: -0.25rem;
        transform: rotate(45deg);
        width: 0.48rem;
    }
    .diagram-chip-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.32rem;
    }
    .diagram-chip {
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        background: #f8fafc;
        color: #1f2937;
        display: inline-flex;
        font-size: 0.72rem;
        font-weight: 850;
        line-height: 1.15;
        min-height: 1.65rem;
        padding: 0.33rem 0.44rem;
        align-items: center;
    }
    .diagram-chip.source { border-color: #bfdbfe; background: #eff6ff; color: #1e3a8a; }
    .diagram-chip.model { border-color: #99f6e4; background: #ecfdf5; color: #134e4a; }
    .diagram-chip.target { border-color: #ddd6fe; background: #f5f3ff; color: #4c1d95; }
    .diagram-chip.gate { border-color: #fecaca; background: #fef2f2; color: #7f1d1d; }
    .diagram-chip.review { border-color: #fde68a; background: #fffbeb; color: #78350f; }
    .gate-strip {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.45rem;
        margin-top: 0.62rem;
    }
    .gate-box {
        border: 1px solid #fecaca;
        border-radius: 8px;
        background: #fef2f2;
        color: #7f1d1d;
        font-size: 0.72rem;
        font-weight: 850;
        line-height: 1.15;
        min-height: 3.1rem;
        padding: 0.48rem;
    }
    .gate-box strong {
        display: block;
        font-size: 0.65rem;
        letter-spacing: 0.04em;
        margin-bottom: 0.2rem;
        text-transform: uppercase;
    }
    .mini-table {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        overflow: hidden;
    }
    .mini-table div {
        border-bottom: 1px solid #e2e8f0;
        color: #334155;
        display: grid;
        font-size: 0.72rem;
        font-weight: 780;
        grid-template-columns: 1fr 1fr;
        line-height: 1.15;
        min-height: 2rem;
        padding: 0.38rem 0.44rem;
    }
    .mini-table div:last-child { border-bottom: 0; }
    .mini-table b { color: #111827; }
    .leakage-wall {
        align-self: stretch;
        border: 2px solid #dc2626;
        border-radius: 8px;
        background: #fef2f2;
        color: #991b1b;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.72rem;
        font-weight: 950;
        line-height: 1.05;
        padding: 0.35rem;
        text-align: center;
        text-transform: uppercase;
        writing-mode: vertical-rl;
    }
    .hydrate-log-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.32rem;
        margin-top: 0.48rem;
    }
    .hydrate-log-grid span {
        border: 1px solid #bfdbfe;
        border-radius: 6px;
        background: #eff6ff;
        color: #1e3a8a;
        font-size: 0.72rem;
        font-weight: 900;
        padding: 0.34rem;
        text-align: center;
    }
    .borehole-sketch {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        display: grid;
        grid-template-columns: 2.2rem 1fr;
        gap: 0.48rem;
        margin-top: 0.48rem;
        padding: 0.5rem;
    }
    .borehole-track {
        border-left: 8px solid #64748b;
        border-right: 8px solid #64748b;
        border-radius: 999px;
        height: 5.6rem;
        margin: 0 auto;
        overflow: hidden;
        position: relative;
        width: 2.55rem;
    }
    .borehole-track::before {
        background: #f59e0b;
        border: 2px solid #b45309;
        border-radius: 999px;
        content: "";
        height: 1.35rem;
        left: 0.08rem;
        position: absolute;
        top: 2.35rem;
        width: 2.35rem;
    }
    .borehole-track::after {
        background: #dc2626;
        content: "";
        height: 2px;
        left: 0.02rem;
        position: absolute;
        top: 3.02rem;
        transform: rotate(-25deg);
        width: 2.45rem;
    }
    .qc-stack {
        display: grid;
        gap: 0.38rem;
    }
    .qc-tile {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        color: #334155;
        font-size: 0.72rem;
        font-weight: 820;
        line-height: 1.15;
        padding: 0.46rem;
    }
    .qc-tile b { color: #111827; display: block; margin-bottom: 0.15rem; }
    .gloss-points {
        border: 1px dashed #94a3b8;
        border-radius: 8px;
        height: 4.3rem;
        margin-top: 0.4rem;
        position: relative;
    }
    .gloss-points span {
        background: #0f766e;
        border-radius: 50%;
        height: 0.42rem;
        position: absolute;
        width: 0.42rem;
    }
    .gloss-points .outlier {
        background: #dc2626;
        box-shadow: 0 0 0 4px #fee2e2;
        height: 0.58rem;
        width: 0.58rem;
    }
    .ann-layer {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.24rem;
        margin: 0.42rem 0;
    }
    .ann-layer span {
        border: 1px solid #0f766e;
        border-radius: 999px;
        background: #ccfbf1;
        height: 0.78rem;
    }
    .model-stack {
        display: grid;
        gap: 0.38rem;
    }
    .model-block {
        border: 1px solid #99f6e4;
        border-radius: 8px;
        background: #ecfdf5;
        color: #134e4a;
        font-size: 0.72rem;
        font-weight: 850;
        line-height: 1.15;
        padding: 0.48rem;
    }
    .model-block.main {
        border-color: #0f766e;
        background: #0f766e;
        color: #ffffff;
    }
    .well-validation {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.3rem;
        margin-top: 0.45rem;
    }
    .well-validation span {
        border: 1px solid #94a3b8;
        border-radius: 8px;
        background: #f1f5f9;
        color: #334155;
        font-size: 0.68rem;
        font-weight: 850;
        padding: 0.45rem 0.3rem;
        text-align: center;
    }
    .well-validation span:last-child {
        border-color: #dc2626;
        background: #fef2f2;
        color: #991b1b;
    }
    .abstain-bin {
        border: 1px solid #fbbf24;
        border-radius: 8px;
        background: #fffbeb;
        color: #78350f;
        font-size: 0.72rem;
        font-weight: 860;
        line-height: 1.15;
        margin-top: 0.5rem;
        padding: 0.48rem;
    }
    .trace-input-stack {
        display: grid;
        gap: 0.38rem;
    }
    .trace-frame {
        border: 1px solid #94a3b8;
        border-radius: 8px;
        background: #f8fafc;
        min-height: 6.2rem;
        padding: 0.44rem;
        position: relative;
    }
    .screen-bar {
        background: #334155;
        border-radius: 999px;
        height: 0.45rem;
        margin-bottom: 0.52rem;
        width: 72%;
    }
    .ui-token {
        border: 1px solid #2563eb;
        border-radius: 5px;
        background: #dbeafe;
        color: #1e3a8a;
        display: inline-block;
        font-size: 0.68rem;
        font-weight: 900;
        margin: 0.12rem;
        padding: 0.2rem 0.32rem;
    }
    .trace-path {
        display: grid;
        gap: 0.34rem;
    }
    .trace-step {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        color: #334155;
        font-size: 0.72rem;
        font-weight: 850;
        line-height: 1.12;
        padding: 0.45rem;
        position: relative;
    }
    .trace-step:not(:last-child)::after {
        border-left: 2px solid #64748b;
        bottom: -0.38rem;
        content: "";
        height: 0.38rem;
        left: 1rem;
        position: absolute;
    }
    .encoder-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.36rem;
    }
    .encoder-box {
        border: 1px solid #99f6e4;
        border-radius: 8px;
        background: #ecfdf5;
        color: #134e4a;
        font-size: 0.72rem;
        font-weight: 880;
        min-height: 3.2rem;
        padding: 0.45rem;
    }
    .transformer-stack {
        border: 1px solid #0f766e;
        border-radius: 8px;
        background: #0f766e;
        color: #ffffff;
        font-size: 0.76rem;
        font-weight: 900;
        line-height: 1.18;
        margin-top: 0.42rem;
        padding: 0.52rem;
        text-align: center;
    }
    .replay-panel {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        margin-bottom: 0.42rem;
        padding: 0.48rem;
    }
    .replay-score {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.35rem;
    }
    .score-box {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        color: #334155;
        font-size: 0.7rem;
        font-weight: 860;
        padding: 0.42rem;
        text-align: center;
    }
    .score-box.pass { border-color: #86efac; background: #f0fdf4; color: #166534; }
    .score-box.fail { border-color: #fecaca; background: #fef2f2; color: #991b1b; }
    .graph-source-stack {
        display: grid;
        gap: 0.35rem;
    }
    .source-doc {
        border: 1px solid #bfdbfe;
        border-radius: 8px;
        background: #eff6ff;
        color: #1e3a8a;
        font-size: 0.72rem;
        font-weight: 850;
        line-height: 1.12;
        padding: 0.45rem;
    }
    .entity-clusters {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.28rem;
        margin-bottom: 0.45rem;
    }
    .entity-node {
        border: 1px solid #cbd5e1;
        border-radius: 999px;
        background: #f8fafc;
        color: #334155;
        font-size: 0.66rem;
        font-weight: 850;
        padding: 0.32rem;
        text-align: center;
    }
    .ontology-merge {
        border: 1px solid #ddd6fe;
        border-radius: 8px;
        background: #f5f3ff;
        color: #4c1d95;
        display: grid;
        gap: 0.24rem;
        font-size: 0.7rem;
        font-weight: 850;
        margin-bottom: 0.42rem;
        padding: 0.46rem;
    }
    .edge-visuals {
        display: grid;
        gap: 0.4rem;
    }
    .edge-row {
        align-items: center;
        display: grid;
        grid-template-columns: 1fr 3.2rem 1fr;
        gap: 0.25rem;
        min-width: 0;
    }
    .graph-dot {
        border: 1px solid #475569;
        border-radius: 999px;
        background: #ffffff;
        color: #1f2937;
        font-size: 0.62rem;
        font-weight: 900;
        padding: 0.32rem 0.2rem;
        text-align: center;
    }
    .edge-line {
        border-top: 3px solid #0f766e;
        position: relative;
    }
    .edge-line::after {
        background: #ecfdf5;
        border: 1px solid #0f766e;
        border-radius: 4px;
        color: #134e4a;
        content: "cite";
        font-size: 0.58rem;
        font-weight: 900;
        left: 50%;
        padding: 0.05rem 0.15rem;
        position: absolute;
        top: -0.78rem;
        transform: translateX(-50%);
    }
    .edge-line.dashed {
        border-top-style: dashed;
        border-top-color: #d97706;
    }
    .edge-line.dashed::after {
        background: #fffbeb;
        border-color: #d97706;
        color: #78350f;
        content: "review";
    }
    .graphrag-path {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        color: #334155;
        font-size: 0.72rem;
        font-weight: 840;
        line-height: 1.15;
        margin-top: 0.48rem;
        padding: 0.48rem;
    }
    .audit-chain {
        display: grid;
        gap: 0.36rem;
    }
    .audit-node {
        border: 1px solid #99f6e4;
        border-radius: 8px;
        background: #ecfdf5;
        color: #134e4a;
        font-size: 0.72rem;
        font-weight: 870;
        line-height: 1.15;
        padding: 0.45rem;
    }
    .audit-node.review {
        border-color: #fbbf24;
        background: #fffbeb;
        color: #78350f;
    }
    .audit-node.gate {
        border-color: #fecaca;
        background: #fef2f2;
        color: #991b1b;
    }
    .globe-panel {
        border: 1px solid #94a3b8;
        border-radius: 8px;
        background: #f8fafc;
        display: grid;
        grid-template-columns: 6.6rem 1fr;
        gap: 0.52rem;
        min-height: 8rem;
        padding: 0.55rem;
    }
    .globe-orb {
        border: 2px solid #334155;
        border-radius: 50%;
        height: 6rem;
        position: relative;
        width: 6rem;
    }
    .globe-orb::before,
    .globe-orb::after {
        border: 1px solid #94a3b8;
        border-radius: 50%;
        content: "";
        position: absolute;
    }
    .globe-orb::before {
        height: 4.9rem;
        left: 0.45rem;
        top: 0.45rem;
        width: 4.9rem;
    }
    .globe-orb::after {
        border-left: 0;
        border-right: 0;
        height: 2rem;
        left: 0.25rem;
        top: 1.95rem;
        width: 5.5rem;
    }
    .event-dot {
        border: 1px solid #ffffff;
        border-radius: 50%;
        position: absolute;
    }
    .event-dot.shallow { background: #2563eb; height: 0.45rem; width: 0.45rem; }
    .event-dot.deep { background: #dc2626; height: 0.75rem; width: 0.75rem; }
    .event-dot.mid { background: #d97706; height: 0.6rem; width: 0.6rem; }
    .feature-row-grid {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        overflow: hidden;
    }
    .feature-row-grid div {
        align-items: center;
        border-bottom: 1px solid #e2e8f0;
        color: #334155;
        display: grid;
        font-size: 0.68rem;
        font-weight: 830;
        gap: 0.18rem;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        min-height: 1.95rem;
        padding: 0.3rem;
    }
    .feature-row-grid div:first-child {
        background: #e2e8f0;
        color: #111827;
        font-size: 0.62rem;
        text-transform: uppercase;
    }
    .feature-row-grid div:last-child { border-bottom: 0; }
    .chronology-strip {
        display: grid;
        grid-template-columns: 1.2fr 0.18fr 0.85fr;
        gap: 0.3rem;
        margin-top: 0.45rem;
    }
    .chronology-strip span {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        color: #334155;
        font-size: 0.68rem;
        font-weight: 850;
        padding: 0.38rem;
        text-align: center;
    }
    .chronology-strip span.lock {
        border-color: #dc2626;
        background: #fef2f2;
        color: #991b1b;
    }
    .waveform-panel {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.45rem;
    }
    .waveform-svg {
        color: #334155;
        display: block;
        height: 4.7rem;
        width: 100%;
    }
    .pick-band {
        align-items: center;
        display: grid;
        gap: 0.24rem;
        grid-template-columns: 1fr 1fr;
        margin-top: 0.4rem;
    }
    .pick-band span {
        border: 1px solid #fbbf24;
        border-radius: 8px;
        background: #fffbeb;
        color: #78350f;
        font-size: 0.68rem;
        font-weight: 850;
        padding: 0.36rem;
        text-align: center;
    }
    .modality-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.36rem;
    }
    .modality-card {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        color: #334155;
        font-size: 0.68rem;
        font-weight: 850;
        line-height: 1.12;
        min-height: 5.4rem;
        padding: 0.45rem;
    }
    .modality-card b {
        color: #111827;
        display: block;
        font-size: 0.72rem;
        margin-bottom: 0.25rem;
    }
    .fusion-node {
        border: 2px solid #0f766e;
        border-radius: 8px;
        background: #ecfdf5;
        color: #134e4a;
        font-size: 0.76rem;
        font-weight: 900;
        line-height: 1.15;
        margin-top: 0.45rem;
        padding: 0.52rem;
        text-align: center;
    }
    .method-lanes {
        display: grid;
        gap: 0.32rem;
    }
    .method-lane {
        align-items: center;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        color: #334155;
        display: grid;
        font-size: 0.68rem;
        font-weight: 850;
        gap: 0.3rem;
        grid-template-columns: 5.4rem 1fr 4.6rem;
        min-height: 2.6rem;
        padding: 0.36rem;
    }
    .method-bar {
        border-radius: 999px;
        height: 0.72rem;
    }
    .method-bar.gravity { background: #2563eb; }
    .method-bar.em { background: #0f766e; }
    .method-bar.ert { background: #d97706; }
    .method-bar.seismic { background: #7c3aed; }
    .method-bar.notes { background: #475569; }
    .conflict-zone {
        border: 1px solid #dc2626;
        border-radius: 8px;
        background: repeating-linear-gradient(45deg, #fef2f2 0, #fef2f2 6px, #fecaca 6px, #fecaca 12px);
        color: #7f1d1d;
        font-size: 0.7rem;
        font-weight: 900;
        line-height: 1.15;
        margin-top: 0.45rem;
        padding: 0.5rem;
        text-align: center;
    }
    .agreement-zone {
        border: 1px solid #86efac;
        border-radius: 8px;
        background: #f0fdf4;
        color: #166534;
        font-size: 0.7rem;
        font-weight: 900;
        line-height: 1.15;
        margin-top: 0.45rem;
        padding: 0.5rem;
        text-align: center;
    }
    .cross-section {
        border: 1px solid #94a3b8;
        border-radius: 8px;
        background: #ffffff;
        display: grid;
        gap: 0.24rem;
        overflow: hidden;
        padding: 0.45rem;
        position: relative;
    }
    .cross-section::before,
    .cross-section::after {
        background: #dc2626;
        content: "";
        height: 100%;
        opacity: 0.85;
        position: absolute;
        top: 0;
        width: 2px;
    }
    .cross-section::before { left: 34%; }
    .cross-section::after { left: 69%; }
    .section-layer {
        align-items: center;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        color: #1f2937;
        display: flex;
        font-size: 0.68rem;
        font-weight: 850;
        min-height: 2.1rem;
        padding-left: 0.42rem;
    }
    .section-layer.velocity { background: #dbeafe; }
    .section-layer.resistivity { background: #ecfdf5; }
    .section-layer.conductivity { background: #fffbeb; }
    .section-layer.possible {
        background: repeating-linear-gradient(135deg, #f8fafc 0, #f8fafc 7px, #e2e8f0 7px, #e2e8f0 14px);
    }
    .region-transfer {
        display: grid;
        grid-template-columns: minmax(0, 1fr) 2rem minmax(0, 1fr);
        gap: 0.42rem;
        align-items: center;
        min-width: 0;
    }
    .region-card {
        border: 1px solid #94a3b8;
        border-radius: 8px;
        background: #ffffff;
        color: #334155;
        font-size: 0.72rem;
        font-weight: 850;
        min-height: 5.9rem;
        padding: 0.5rem;
        position: relative;
    }
    .region-card b { color: #111827; display: block; margin-bottom: 0.3rem; }
    .residual-map {
        border: 1px solid #94a3b8;
        border-radius: 8px;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.22rem;
        margin-top: 0.42rem;
        padding: 0.35rem;
    }
    .residual-map span {
        border-radius: 50%;
        display: block;
        height: 0.72rem;
        width: 0.72rem;
    }
    .residual-map .cold { background: #2563eb; }
    .residual-map .hot { background: #dc2626; }
    .residual-map .ok { background: #94a3b8; }
    .station-network {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        height: 8.2rem;
        margin-bottom: 0.45rem;
        position: relative;
    }
    .station-node {
        background: #ffffff;
        border: 2px solid #334155;
        border-radius: 50%;
        height: 1.1rem;
        position: absolute;
        width: 1.1rem;
    }
    .station-arc {
        border-top: 3px solid #0f766e;
        height: 2rem;
        position: absolute;
        transform-origin: left center;
        width: 4.6rem;
    }
    .ccf-stack {
        display: grid;
        gap: 0.26rem;
    }
    .ccf-line {
        border: 1px solid #cbd5e1;
        border-radius: 999px;
        height: 0.58rem;
    }
    .ccf-line.stable { background: #0f766e; }
    .ccf-line.weak { background: #e2e8f0; border-style: dashed; }
    .drift-gauge {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.48rem;
    }
    .gauge-track {
        background: #e2e8f0;
        border-radius: 999px;
        height: 0.75rem;
        overflow: hidden;
    }
    .gauge-fill {
        background: #d97706;
        height: 100%;
        width: 64%;
    }
    .walk-forward {
        display: grid;
        gap: 0.28rem;
        margin-top: 0.45rem;
    }
    .walk-row {
        display: grid;
        gap: 0.18rem;
        grid-template-columns: 1.3fr 0.65fr 0.55fr;
    }
    .walk-row span {
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        color: #334155;
        font-size: 0.62rem;
        font-weight: 850;
        padding: 0.28rem;
        text-align: center;
    }
    .walk-row .train { background: #dbeafe; }
    .walk-row .test { background: #fffbeb; }
    .walk-row .gate { background: #fef2f2; color: #991b1b; }
    .sem-crop {
        border: 1px solid #64748b;
        border-radius: 8px;
        background: #94a3b8;
        height: 7rem;
        position: relative;
    }
    .sem-crop::before {
        border-bottom: 2px solid #e5e7eb;
        border-top: 2px solid #64748b;
        content: "";
        height: 3.6rem;
        left: 1rem;
        position: absolute;
        top: 1.1rem;
        transform: rotate(-12deg);
        width: 70%;
    }
    .scale-bar {
        background: #111827;
        bottom: 0.55rem;
        height: 0.28rem;
        left: 0.55rem;
        position: absolute;
        width: 2.6rem;
    }
    .label-pins {
        display: flex;
        flex-wrap: wrap;
        gap: 0.28rem;
        margin-top: 0.42rem;
    }
    .label-pins span {
        border: 1px solid #bfdbfe;
        border-radius: 999px;
        background: #eff6ff;
        color: #1e3a8a;
        font-size: 0.68rem;
        font-weight: 850;
        padding: 0.28rem 0.38rem;
    }
    .proxy-gate {
        border: 2px solid #dc2626;
        border-radius: 8px;
        background: #fef2f2;
        color: #991b1b;
        font-size: 0.76rem;
        font-weight: 950;
        line-height: 1.15;
        margin-top: 0.45rem;
        padding: 0.55rem;
        text-align: center;
    }
    @media (max-width: 900px) {
        .block-container {
            padding: 2.75rem 0.85rem 2rem;
        }
        h1 { font-size: 1.85rem !important; }
        h2 { font-size: 1.45rem !important; }
        h3 { font-size: 1.2rem !important; }
        .talk-hero {
            padding: 1rem;
        }
        .portfolio-intro h1 {
            font-size: 2rem !important;
        }
        .portfolio-intro p {
            font-size: 1rem;
        }
        .section-heading {
            align-items: flex-start;
            flex-direction: column;
            gap: 0.15rem;
        }
        .audit-summary {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.55rem;
        }
        .ml-strip, .future-timeline, .node-lane, .storyboard-grid, .ai-case-top, .ai-evidence-grid, .think-grid, .vision-board, .blueprint-steps, .workflow-branches, .prompt-grid, .source-chip-grid, .sketch-body, .sketch-grid, .research-source-grid, .detail-grid, .story-frames, .current-future-board, .evidence-chain, .transfer-stage, .pipeline-stage, .property-stage, .source-update-panel, .source-update-grid, .source-update-grid-tight, .public-system-legend, .topic-update-grid, .north-decision-board, .feedback-card-grid, .manual-board, .manual-flow { grid-template-columns: 1fr; }
        .chain-node:not(:last-child)::after,
        .pipeline-node:not(:last-child)::after,
        .manual-flow-node:not(:last-child)::after { display: none; }
        .manual-head {
            flex-direction: column;
        }
        .manual-output {
            flex: 1 1 auto;
            width: 100%;
        }
        .rich-head {
            flex-direction: column;
        }
        .rich-output {
            flex: 1 1 auto;
            width: 100%;
        }
        .rich-stage-grid,
        .hydrate-log-grid,
        .gate-strip,
        .encoder-grid,
        .replay-score,
        .entity-clusters,
        .well-validation,
        .globe-panel,
        .modality-grid,
        .region-transfer {
            grid-template-columns: 1fr;
        }
        .feature-row-grid div,
        .method-lane,
        .walk-row {
            grid-template-columns: 1fr;
        }
        .chronology-strip {
            grid-template-columns: 1fr;
        }
        .rich-arrow {
            background: transparent;
            border-left: 2px solid #64748b;
            height: 1.7rem;
            justify-self: center;
            width: 1rem;
        }
        .rich-arrow::after {
            border-bottom: 2px solid #64748b;
            border-right: 2px solid #64748b;
            border-top: 0;
            bottom: 0;
            left: -0.02rem;
            right: auto;
            top: auto;
            transform: rotate(45deg);
        }
        .leakage-wall {
            writing-mode: horizontal-tb;
            min-height: 2.5rem;
        }
        .agent-lanes { grid-template-columns: 1fr; }
        .agent-stage { min-height: 640px; }
        .guidance-gate {
            min-height: 110px;
        }
        .workflow-branches::before,
        .workflow-node::before,
        .workflow-root::after { display: none; }
        .think-card,
        .think-grid.compact .think-card {
            min-height: auto;
        }
        .ml-stage { min-height: auto; }
        .ai-chip-row { justify-content: flex-start; }
        .model-core::before, .model-core::after { display: none; }
        .blue-step::after { display: none; }
        .movement-rail { grid-template-columns: repeat(4, minmax(4rem, 1fr)); overflow-x: auto; }
        div[data-testid="stMetric"] {
            padding: 0.55rem 0.65rem;
        }
        div[data-testid="stButton"] button,
        div[data-testid="stLinkButton"] a {
            width: 100%;
        }
    }
    .stApp {
        background:
            radial-gradient(circle at 8% 0%, rgba(20,184,166,0.13), transparent 28%),
            radial-gradient(circle at 92% 8%, rgba(249,115,22,0.10), transparent 28%),
            linear-gradient(145deg, #f8fafc 0%, #eef6f5 46%, #f7f3ea 100%) !important;
        color: #172033 !important;
    }
    section[data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid #d8dee8;
    }
    .talk-hero,
    .portfolio-intro,
    .think-grid.topic-wall,
    .visual-flow,
    .blueprint,
    .workflow-tree,
    .current-future-board,
    .detail-card,
    .sketch-card,
    .ai-case-brief,
    .compare-panel {
        background: rgba(255, 255, 255, 0.88) !important;
        border: 1px solid rgba(203, 213, 225, 0.92) !important;
        box-shadow: 0 18px 46px rgba(15, 23, 42, 0.10);
    }
    .portfolio-intro {
        max-width: none;
        border-radius: 18px;
        padding: 1.35rem 1.45rem 1.45rem;
        margin-bottom: 1rem;
    }
    .talk-hero {
        border-radius: 16px;
        background:
            radial-gradient(circle at 85% 0%, rgba(20,184,166,0.16), transparent 28%),
            linear-gradient(135deg, rgba(255,255,255,0.96), rgba(236,253,245,0.92)) !important;
    }
    .portfolio-eyebrow,
    .talk-kicker { color: #0f766e !important; letter-spacing: 0.04em; }
    .portfolio-intro h1,
    .talk-hero h2,
    .section-heading-title,
    .think-title,
    .think-question,
    h1, h2, h3, h4 { color: #172033 !important; }
    .portfolio-intro p,
    .talk-hero p,
    .section-heading span,
    .small-note,
    .ml-body,
    .timeline-node em,
    .vision-card p { color: #475569 !important; }
    .think-grid.topic-wall {
        border-radius: 18px;
        background:
            radial-gradient(circle at 12% 16%, rgba(20,184,166,0.20), transparent 20%),
            radial-gradient(circle at 88% 22%, rgba(249,115,22,0.18), transparent 22%),
            radial-gradient(circle at 50% 95%, rgba(96,165,250,0.20), transparent 24%),
            linear-gradient(135deg, rgba(255,255,255,0.93) 0%, rgba(239,246,255,0.88) 100%) !important;
    }
    .think-card,
    .vision-card,
    .ml-stage,
    .future-timeline .timeline-node,
    .node-cluster,
    .source-chip,
    div[data-testid="stMetric"],
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.92) !important;
        border-color: rgba(203, 213, 225, 0.96) !important;
        color: #172033 !important;
    }
    .think-card { border-radius: 14px; }
    .think-card-link:hover .think-card,
    .think-card-link:focus .think-card {
        border-color: #0f766e !important;
        box-shadow: 0 16px 42px rgba(20, 184, 166, 0.16);
    }
    .topic-poster {
        background: #020617 !important;
        border-color: rgba(94, 234, 212, 0.28) !important;
    }
    .topic-poster-composite.card-visual > img,
    .topic-room-visual > img,
    .topic-pattern.fallback-pattern { background: #020617 !important; }
    .think-raise {
        background: #ecfdf5 !important;
        color: #134e4a !important;
        border-left-color: #0f766e !important;
    }
    .project-status,
    .portfolio-proof span,
    .vision-meta span,
    .topic-pattern span,
    .node-pill,
    .ai-chip,
    .motion-pill {
        background: #f8fafc !important;
        border-color: #cbd5e1 !important;
        color: #334155 !important;
    }
    .stAlert {
        background: #ffffff !important;
        color: #172033 !important;
        border: 1px solid #d8dee8 !important;
    }
    .stAlert p,
    .stAlert li,
    div[data-testid="stMarkdownContainer"] p {
        color: #334155;
    }
    .future-timeline .timeline-node span { color: #0f766e !important; }
    .future-timeline .timeline-node strong { color: #172033 !important; }
    .drive-source-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr));
        gap: 0.9rem;
        margin: 1rem 0 1.35rem;
    }
    .drive-source-card {
        background:
            radial-gradient(circle at 90% 0%, rgba(45,212,191,0.16), transparent 32%),
            rgba(255, 255, 255, 0.94);
        border: 1px solid #d8dee8;
        border-radius: 8px;
        padding: 1rem;
        min-height: 15rem;
        box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
    }
    .drive-source-card .source-status {
        color: #0f766e;
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .drive-source-card h3 {
        margin: 0.35rem 0 0.55rem;
        font-size: 1.05rem;
        line-height: 1.25;
    }
    .drive-source-card p {
        color: #475569 !important;
        margin: 0.35rem 0;
        font-size: 0.92rem;
    }
    .drive-source-card a {
        display: inline-flex;
        margin-top: 0.75rem;
        color: #ffffff;
        background: #0f766e;
        border-radius: 999px;
        padding: 0.45rem 0.75rem;
        text-decoration: none;
        font-weight: 750;
    }
    .pipeline-contract {
        background: #f8fafc;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .pipeline-contract h3 {
        margin: 0 0 0.35rem;
        color: #0b1f3a;
        font-size: 1.2rem;
        line-height: 1.25;
    }
    .pipeline-contract p {
        color: #475569 !important;
        margin: 0 0 0.75rem;
    }
    .pipeline-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
        gap: 0.75rem;
    }
    .pipeline-cell {
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        padding: 0.85rem;
        min-height: 12rem;
    }
    .pipeline-cell strong {
        display: block;
        color: #0f766e;
        font-size: 0.78rem;
        letter-spacing: 0.08em;
        margin-bottom: 0.55rem;
        text-transform: uppercase;
    }
    .pipeline-cell ul {
        margin: 0;
        padding-left: 1.05rem;
    }
    .pipeline-cell li {
        color: #334155;
        margin: 0.38rem 0;
        font-size: 0.9rem;
        line-height: 1.35;
    }
    .ml-visual-diagram {
        background: #f8fafc;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        margin: 1rem 0;
        padding: 1rem;
    }
    .ml-visual-head {
        display: grid;
        grid-template-columns: minmax(0, 1.05fr) minmax(20rem, 0.95fr);
        gap: 0.75rem;
        align-items: start;
        margin-bottom: 0.8rem;
    }
    .ml-kicker {
        color: #0f766e;
        font-size: 0.74rem;
        font-weight: 850;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .ml-visual-head h3 {
        color: #0b1f3a;
        font-size: clamp(1.1rem, 2vw, 1.45rem);
        line-height: 1.15;
        margin: 0.15rem 0 0;
    }
    .ml-source-ribbons {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.45rem;
    }
    .ml-source-ribbon {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-left: 5px solid #0f766e;
        border-radius: 8px;
        min-height: 4.2rem;
        padding: 0.55rem 0.65rem;
    }
    .ml-source-ribbon strong,
    .ml-source-ribbon span {
        display: block;
    }
    .ml-source-ribbon strong {
        color: #0b1f3a;
        font-size: 0.78rem;
        line-height: 1.15;
    }
    .ml-source-ribbon span {
        color: #475569;
        font-size: 0.82rem;
        margin-top: 0.25rem;
    }
    .ml-visual-board {
        display: grid;
        grid-template-columns: 12rem minmax(0, 1fr) 12rem;
        gap: 0.75rem;
        align-items: stretch;
    }
    .ml-evidence-card,
    .ml-gate-card {
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        padding: 0.55rem;
        min-height: 12.5rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        overflow: hidden;
    }
    .ml-evidence-card img {
        width: 100%;
        aspect-ratio: 4 / 3;
        object-fit: cover;
        border-radius: 6px;
        border: 1px solid #d8dee8;
        background: #e2e8f0;
    }
    .ml-evidence-card svg {
        width: 100%;
        height: 7.5rem;
        color: #0f766e;
        background: #e8f3f1;
        border-radius: 6px;
        padding: 1rem;
    }
    .ml-evidence-card strong,
    .ml-evidence-card span {
        display: block;
        color: #334155;
        font-size: 0.76rem;
        line-height: 1.2;
        margin-top: 0.35rem;
    }
    .ml-evidence-card span {
        color: #64748b;
        margin-top: 0.1rem;
    }
    .ml-flow-track {
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 0.4rem;
        align-items: stretch;
        position: relative;
    }
    .ml-flow-node {
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        min-height: 12.5rem;
        padding: 0.55rem;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        position: relative;
    }
    .ml-flow-node:not(:last-child)::after {
        content: "";
        position: absolute;
        top: 50%;
        right: -0.35rem;
        width: 0.42rem;
        height: 0.42rem;
        border-top: 2px solid #64748b;
        border-right: 2px solid #64748b;
        transform: translateY(-50%) rotate(45deg);
        background: #f8fafc;
        z-index: 1;
    }
    .ml-node-icon {
        width: 2.2rem;
        height: 2.2rem;
        border-radius: 50%;
        display: grid;
        place-items: center;
        color: #0f766e;
        background: #e8f3f1;
        margin-bottom: 0.45rem;
    }
    .ml-node-icon svg {
        width: 1.45rem;
        height: 1.45rem;
    }
    .ml-flow-node strong {
        color: #0f766e;
        font-size: 0.68rem;
        letter-spacing: 0.07em;
        text-transform: uppercase;
    }
    .ml-flow-node span {
        color: #0b1f3a;
        font-size: clamp(0.72rem, 1vw, 0.88rem);
        font-weight: 760;
        line-height: 1.15;
        margin-top: 0.35rem;
        overflow-wrap: anywhere;
    }
    .ml-flow-node span span {
        display: inline-block;
        background: #eef2f7;
        border-radius: 999px;
        color: #334155;
        font-size: 0.68rem;
        font-weight: 760;
        margin: 0.1rem 0.1rem 0 0;
        padding: 0.18rem 0.38rem;
    }
    .ml-gate-card {
        border-color: #f59e0b;
        border-top: 5px solid #f59e0b;
    }
    .ml-gate-card strong {
        color: #92400e;
        font-size: 0.74rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .ml-risk-chips {
        display: grid;
        gap: 0.35rem;
        margin: 0.55rem 0;
    }
    .ml-risk-chips span {
        background: #fff7ed;
        border: 1px solid #fed7aa;
        border-radius: 999px;
        color: #9a3412;
        font-size: 0.72rem;
        font-weight: 760;
        line-height: 1.15;
        padding: 0.32rem 0.45rem;
    }
    .ml-gate-card small {
        color: #64748b;
        display: block;
        font-size: 0.72rem;
        line-height: 1.25;
    }
    .ml-source-map {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.5rem;
        margin-top: 0.75rem;
    }
    .ml-source-map div {
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        min-height: 4.4rem;
        padding: 0.55rem 0.65rem;
    }
    .ml-source-map strong,
    .ml-source-map span {
        display: block;
        line-height: 1.18;
    }
    .ml-source-map strong {
        color: #0b1f3a;
        font-size: 0.78rem;
    }
    .ml-source-map span {
        color: #475569;
        font-size: 0.8rem;
        margin-top: 0.25rem;
    }
    .ml-part-explainer {
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        margin: 1rem 0;
        padding: 1rem;
    }
    .ml-part-explainer.compact {
        padding: 0.85rem;
    }
    .ml-part-head {
        display: grid;
        grid-template-columns: minmax(0, 0.82fr) minmax(20rem, 1.18fr);
        gap: 0.9rem;
        align-items: stretch;
    }
    .ml-part-kicker {
        color: #0f766e;
        font-size: 0.74rem;
        font-weight: 850;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .ml-part-head h3 {
        color: #0b1f3a;
        font-size: clamp(1.1rem, 2vw, 1.55rem);
        line-height: 1.12;
        margin: 0.18rem 0 0.45rem;
    }
    .ml-part-head p {
        color: #475569 !important;
        font-size: 0.92rem;
        line-height: 1.38;
        margin: 0;
    }
    .ml-part-asset {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #f8fafc;
        min-height: 15rem;
        padding: 0.55rem;
    }
    .ml-part-asset img {
        border-radius: 6px;
        display: block;
        height: auto;
        width: 100%;
    }
    .ml-part-grid {
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 0.55rem;
        margin-top: 0.75rem;
    }
    .ml-part-card {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #f8fafc;
        min-height: 13.2rem;
        padding: 0.62rem;
        display: flex;
        flex-direction: column;
        gap: 0.45rem;
    }
    .ml-part-card strong {
        color: #0b1f3a;
        font-size: 0.78rem;
        letter-spacing: 0.06em;
        line-height: 1.1;
        text-transform: uppercase;
    }
    .ml-part-card p {
        color: #475569 !important;
        font-size: 0.78rem;
        line-height: 1.25;
        margin: 0;
    }
    .part-mini {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        min-height: 5.5rem;
        overflow: hidden;
        padding: 0.5rem;
        position: relative;
    }
    .mini-screen {
        background: linear-gradient(135deg, #eff6ff, #ecfdf5);
        border: 1px solid #94a3b8;
        border-radius: 7px;
        height: 4.5rem;
        padding: 0.4rem;
    }
    .mini-window-bar {
        background: #0f172a;
        border-radius: 999px;
        height: 0.35rem;
        margin-bottom: 0.45rem;
        width: 70%;
    }
    .mini-screen-row {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 5px;
        height: 0.72rem;
        margin: 0.28rem 0;
        width: 78%;
    }
    .mini-screen-row.short { width: 50%; }
    .ocr-token {
        background: #eff6ff;
        border: 1px solid #2563eb;
        border-radius: 999px;
        color: #1e3a8a;
        display: inline-block;
        font-size: 0.66rem;
        font-weight: 850;
        margin: 0.12rem;
        padding: 0.18rem 0.35rem;
    }
    .ui-outline {
        border: 2px solid #0f766e;
        border-radius: 7px;
        color: #134e4a;
        font-size: 0.68rem;
        font-weight: 850;
        padding: 0.28rem 0.32rem;
        position: absolute;
    }
    .ui-outline.button { left: 0.65rem; top: 1rem; }
    .ui-outline.menu { right: 0.65rem; top: 1.05rem; }
    .ui-outline.panel { bottom: 0.7rem; left: 1.1rem; width: 58%; }
    .state-vector {
        align-items: center;
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 0.22rem;
        height: 4.5rem;
    }
    .state-vector span {
        border-radius: 999px;
        height: 0.9rem;
    }
    .state-vector span:nth-child(odd) { background: #99f6e4; }
    .state-vector span:nth-child(even) { background: #bfdbfe; }
    .policy-core {
        align-items: center;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0.3rem;
        height: 4.5rem;
    }
    .policy-core span {
        background: #0f766e;
        border-radius: 50%;
        box-shadow: 0 0 0 5px #ccfbf1;
        height: 1.25rem;
        justify-self: center;
        width: 1.25rem;
    }
    .action-choice {
        display: grid;
        gap: 0.34rem;
    }
    .action-choice span {
        background: #fffbeb;
        border: 1px solid #f59e0b;
        border-radius: 7px;
        color: #92400e;
        font-size: 0.72rem;
        font-weight: 850;
        padding: 0.36rem 0.42rem;
    }
    .review-mini {
        display: grid;
        gap: 0.34rem;
    }
    .review-mini span {
        border-radius: 7px;
        font-size: 0.72rem;
        font-weight: 850;
        padding: 0.36rem 0.42rem;
    }
    .review-mini .pass { background: #ecfdf5; border: 1px solid #0f766e; color: #134e4a; }
    .review-mini .fail { background: #fef2f2; border: 1px solid #ef4444; color: #991b1b; }
    .review-mini .holdout { background: #f5f3ff; border: 1px solid #7c3aed; color: #4c1d95; }
    .ml-part-strip {
        background: #f8fafc;
        border: 1px solid #d8dee8;
        border-left: 5px solid #0f766e;
        border-radius: 8px;
        color: #334155;
        font-size: 0.88rem;
        line-height: 1.35;
        margin-top: 0.75rem;
        padding: 0.62rem 0.75rem;
    }
    .ml-part-strip strong {
        color: #0b1f3a;
    }
    .thesis-graph-models {
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        margin: 1rem 0;
        padding: 1rem;
    }
    .thesis-graph-head {
        display: grid;
        grid-template-columns: minmax(0, 0.8fr) minmax(22rem, 1.2fr);
        gap: 0.9rem;
        align-items: stretch;
    }
    .thesis-graph-kicker {
        color: #0f766e;
        font-size: 0.74rem;
        font-weight: 850;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .thesis-graph-head h3 {
        color: #0b1f3a;
        font-size: clamp(1.1rem, 2vw, 1.5rem);
        line-height: 1.14;
        margin: 0.15rem 0 0.45rem;
    }
    .thesis-graph-head p {
        color: #475569 !important;
        font-size: 0.92rem;
        line-height: 1.38;
        margin: 0;
    }
    .graph-model-asset {
        border: 1px solid #d8dee8;
        border-radius: 8px;
        background: #f8fafc;
        padding: 0.55rem;
    }
    .graph-model-asset img {
        border-radius: 6px;
        display: block;
        width: 100%;
    }
    .adobe-closeup-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.65rem;
        margin-top: 0.75rem;
    }
    .adobe-closeup-card {
        background: #f8fafc;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        overflow: hidden;
    }
    .adobe-closeup-card img {
        background: #020617;
        border-bottom: 1px solid #d8dee8;
        display: block;
        height: 13rem;
        object-fit: cover;
        width: 100%;
    }
    .adobe-closeup-card.focus-left img { object-position: 22% 50%; }
    .adobe-closeup-card.focus-center img { object-position: 50% 50%; }
    .adobe-closeup-card.focus-right img { object-position: 76% 50%; }
    .adobe-closeup-body {
        padding: 0.65rem 0.72rem;
    }
    .adobe-closeup-body strong {
        color: #0b1f3a;
        display: block;
        font-size: 0.8rem;
        letter-spacing: 0.06em;
        line-height: 1.1;
        text-transform: uppercase;
    }
    .adobe-closeup-body span {
        color: #475569;
        display: block;
        font-size: 0.82rem;
        line-height: 1.25;
        margin-top: 0.3rem;
    }
    .graph-model-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.55rem;
        margin-top: 0.75rem;
    }
    .graph-model-card {
        background: #f8fafc;
        border: 1px solid #d8dee8;
        border-top: 5px solid #2563eb;
        border-radius: 8px;
        min-height: 11.5rem;
        padding: 0.68rem;
    }
    .graph-model-card.materials { border-top-color: #0f766e; }
    .graph-model-card.sage { border-top-color: #d97706; }
    .graph-model-card.rgcn { border-top-color: #7c3aed; }
    .graph-model-card strong,
    .graph-model-card span,
    .graph-model-card a {
        display: block;
    }
    .graph-model-card strong {
        color: #0b1f3a;
        font-size: 0.9rem;
        line-height: 1.12;
    }
    .graph-model-card span {
        color: #475569;
        font-size: 0.8rem;
        line-height: 1.25;
        margin-top: 0.34rem;
    }
    .graph-model-card a {
        color: #0f766e;
        font-size: 0.75rem;
        font-weight: 850;
        margin-top: 0.5rem;
        text-decoration: none;
    }
    .ml-model-detail {
        display: grid;
        gap: 0.65rem;
        margin-top: 0.75rem;
    }
    .ml-model-stack {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(13.5rem, 1fr));
        gap: 0.55rem;
        align-items: stretch;
    }
    .ml-model-card {
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-top: 5px solid #2563eb;
        border-radius: 8px;
        min-height: 16rem;
        padding: 0.72rem;
        display: flex;
        flex-direction: column;
        gap: 0.42rem;
    }
    .ml-model-card.reference {
        border-top-color: #0f766e;
    }
    .ml-model-card.challenger {
        border-top-color: #f59e0b;
    }
    .ml-model-card.validation {
        border-top-color: #7c3aed;
    }
    .ml-model-card > strong {
        color: #64748b;
        font-size: 0.68rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .ml-model-name {
        color: #0b1f3a;
        font-size: 0.98rem;
        font-weight: 850;
        line-height: 1.18;
        margin: 0;
    }
    .ml-model-row {
        border-top: 1px solid #eef2f7;
        padding-top: 0.38rem;
    }
    .ml-model-row span {
        color: #0f766e;
        display: block;
        font-size: 0.66rem;
        font-weight: 850;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }
    .ml-model-row p {
        color: #334155 !important;
        font-size: 0.78rem;
        line-height: 1.25;
        margin: 0.14rem 0 0;
    }
    .ml-model-checks {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.55rem;
    }
    .ml-model-checks div,
    .ml-diagram-label {
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        padding: 0.62rem 0.7rem;
    }
    .ml-model-checks strong,
    .ml-diagram-label strong {
        color: #0b1f3a;
        display: block;
        font-size: 0.72rem;
        letter-spacing: 0.08em;
        line-height: 1.1;
        text-transform: uppercase;
    }
    .ml-model-checks span,
    .ml-diagram-label span {
        color: #475569;
        display: block;
        font-size: 0.8rem;
        line-height: 1.25;
        margin-top: 0.28rem;
    }
    .ml-metric-chips {
        display: flex !important;
        flex-wrap: wrap;
        gap: 0.25rem;
    }
    .ml-metric-chips span {
        background: #eef2f7;
        border: 1px solid #d8dee8;
        border-radius: 999px;
        color: #334155;
        display: inline-flex;
        font-size: 0.68rem;
        font-weight: 760;
        line-height: 1.1;
        margin: 0;
        padding: 0.22rem 0.4rem;
    }
    .source-panel-note {
        color: #64748b !important;
        font-size: 0.9rem;
        margin-bottom: 0.6rem;
    }
    @media (max-width: 900px) {
        .pipeline-grid,
        .ml-visual-head,
        .ml-visual-board,
        .ml-part-head,
        .thesis-graph-head,
        .ml-source-map {
            grid-template-columns: 1fr;
        }
        .ml-model-stack,
        .ml-model-checks,
        .ml-part-grid,
        .adobe-closeup-grid,
        .graph-model-grid {
            grid-template-columns: 1fr;
        }
        .ml-source-ribbons {
            grid-template-columns: 1fr;
        }
        .ml-flow-track {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
        .ml-flow-node {
            min-height: 9.4rem;
        }
        .ml-flow-node:not(:last-child)::after {
            display: none;
        }
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


def build_update_handoff(
    title: str,
    message: str,
    conversation_url: str,
    project_area: str,
    priority: str,
    uploads,
) -> bytes:
    created_at = datetime.now(timezone.utc).isoformat()
    request = {
        "title": title.strip(),
        "message": message.strip(),
        "conversation_url": conversation_url.strip(),
        "project_area": project_area,
        "priority": priority,
        "created_at": created_at,
        "screenshots": [upload.name for upload in uploads],
        "status": "new",
    }
    package = BytesIO()
    with zipfile.ZipFile(package, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "update_request.json",
            json.dumps(request, indent=2, ensure_ascii=True),
        )
        for upload in uploads:
            archive.writestr(f"screenshots/{Path(upload.name).name}", upload.getvalue())
    return package.getvalue()


def local_file_uri(path_text: str) -> str:
    path = Path(path_text)
    try:
        return path.resolve().as_uri()
    except ValueError:
        return "file:///" + quote(str(path).replace("\\", "/"))


def source_href(path_text: str) -> str:
    if path_text.startswith(("http://", "https://")):
        return path_text
    return local_file_uri(path_text)


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
    return f"?section=Think%20Tank%20Topics&topic={quote(slug)}"


def topic_by_slug(slug: str) -> dict:
    for topic in TOPIC_ROOMS:
        if topic["slug"] == slug:
            return topic
    return TOPIC_ROOMS[0]


def topic_for_project_key(project_key: str) -> dict | None:
    for topic in TOPIC_ROOMS:
        if topic["project_key"] == project_key:
            return topic
    fallback_slug = PROJECT_TOPIC_FALLBACKS.get(project_key)
    if fallback_slug:
        return topic_by_slug(fallback_slug)
    return None


def asset_data_uri(path: Path, max_bytes: int | None = None) -> str | None:
    if not path.exists():
        return None
    if max_bytes is not None and path.stat().st_size > max_bytes:
        return None
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = {
        ".svg": "image/svg+xml",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".mp4": "video/mp4",
        ".m4v": "video/mp4",
        ".mov": "video/quicktime",
        ".webm": "video/webm",
    }.get(path.suffix.lower(), "application/octet-stream")
    return f"data:{mime};base64,{encoded}"


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


def render_gmail_source_update(compact: bool = False) -> None:
    shown = GMAIL_SOURCE_UPDATES[:3] if compact else GMAIL_SOURCE_UPDATES
    cards = "".join(
        f"""
<div class="source-update-card">
  <span>{escape(item["label"])}</span>
  <strong>{escape(item["title"])}</strong>
  <p>{escape(item["body"])}</p>
</div>
        """
        for item in shown
    )
    st.markdown(
        f"""
<div class="source-update-grid">
  {cards}
</div>
        """,
        unsafe_allow_html=True,
    )


def render_north_slope_ml_update() -> None:
    cards = "".join(
        f"""
<div class="source-update-card north-slope-ml-card">
  <span>{escape(title)}</span>
  <p>{escape(body)}</p>
</div>
        """
        for title, body in NORTH_SLOPE_ML_UPDATES
    )
    st.markdown(
        f"""
<div class="source-update-panel">
  <div>
    <span class="source-update-kicker">New source integration</span>
    <h3>North Slope ML scaffold now needs visible validation gates</h3>
    <p>
      The new notes make the project stronger if the audience can see the path from
      public data to features to a model, and then through leakage, split, drift, and
      expert-review checks before any hydrate-screening output is trusted.
    </p>
  </div>
  <div class="source-update-grid source-update-grid-tight">
    {cards}
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_public_system_legend() -> None:
    st.markdown(
        """
<div class="public-system-legend">
  <div><strong>Evidence</strong>Real maps, slides, code, notebooks, videos, or screenshots anchor each topic.</div>
  <div><strong>AI action</strong>Codex, prompting, file search, app building, and source organization move the work forward.</div>
  <div><strong>Validation</strong>Leakage, uncertainty, provenance, labels, and expert review stay visible.</div>
  <div><strong>Question</strong>Each topic asks what an experienced person would change, test, or build next.</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_topic_update_panel(slug: str) -> None:
    panel = TOPIC_SITE_UPDATES.get(slug)
    if panel is None:
        return
    items = "".join(
        f"""
<div class="topic-update-item">
  <strong>{escape(label)}</strong>
  <span>{escape(body)}</span>
</div>
        """
        for label, body in panel["items"]
    )
    st.markdown(
        f"""
<div class="topic-update-panel">
  <span class="topic-update-kicker">{escape(panel["kicker"])}</span>
  <h3>{escape(panel["title"])}</h3>
  <p>{escape(panel["intro"])}</p>
  <div class="topic-update-grid">{items}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_slide_source_updates(slug: str) -> None:
    updates = SLIDE_SOURCE_UPDATES.get(slug)
    if not updates:
        return
    notes = "".join(
        f"""
<div class="slide-source-note">
  <strong>{escape(title)}</strong>
  <span>{escape(body)}</span>
</div>
        """
        for title, body in updates
    )
    st.markdown(
        f"<div class='slide-source-strip'>{notes}</div>",
        unsafe_allow_html=True,
    )


def render_north_slope_decision_board() -> None:
    st.markdown(
        """
<div class="north-decision-board">
  <div class="well-log-panel">
    <h3>Vertical well-log panel to build next</h3>
    <div class="well-log-track">
      <span>Gamma ray</span>
      <span>Resistivity</span>
      <span>Density</span>
      <span>Rock unit</span>
      <span>Hydrate clue</span>
    </div>
  </div>
  <div class="decision-branches">
    <h3>Screening output should branch, not overclaim</h3>
    <div class="decision-branch"><strong>Investigate</strong><span>source-backed review target with geologic context</span></div>
    <div class="decision-branch more"><strong>Need more data</strong><span>missing logs, weak provenance, or unresolved uncertainty</span></div>
    <div class="decision-branch low"><strong>Low priority</strong><span>public evidence does not support immediate follow-up</span></div>
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_motion_priority_cards() -> None:
    cards = "".join(
        f"""
<div class="topic-update-item">
  <strong>{escape(title)}</strong>
  <span>{escape(body)}</span>
</div>
        """
        for title, body in MOTION_SKETCH_PRIORITIES
    )
    st.markdown(
        f"""
<div class="topic-update-panel">
  <span class="topic-update-kicker">Motion priority</span>
  <h3>Build one finished loop before adding more sketch plans</h3>
  <p>The Visual Lab needs a completed motion artifact at the top so it feels like proof, not only a planning board.</p>
  <div class="topic-update-grid">{cards}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_feedback_cards() -> None:
    st.markdown(
        """
<div class="feedback-card-grid">
  <div class="feedback-card">
    <strong>Correct a claim</strong>
    <p>Point out overreach, missing uncertainty, weak evidence, or a better way to phrase the scientific or ML claim.</p>
  </div>
  <div class="feedback-card">
    <strong>Suggest a method</strong>
    <p>Recommend a validation test, graph workflow, agent-evaluation pattern, data-engineering step, or geoscience method.</p>
  </div>
  <div class="feedback-card">
    <strong>Share a workflow</strong>
    <p>Show how your team handles public data, maps, notebooks, slides, scientific software, or AI-assisted review.</p>
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_future_timeline(row: pd.Series) -> None:
    phases = [
        (
            "Now to 6 months",
            "assemble",
            row["next_6_months"],
            "Screenshots, source records, app links, and first cleaned visuals.",
        ),
        (
            "6 to 12 months",
            "model",
            row["next_12_months"],
            "Convert the evidence into variables, tests, and reviewable outputs.",
        ),
        (
            "12 to 24 months",
            "deploy",
            row["next_24_months"],
            "Ship a stronger tool, paper, deck, or validated workflow.",
        ),
    ]
    phase_html = "".join(
        f"""
  <div class="timeline-node {escape(style)}">
    <span>{escape(label)}</span>
    <strong>{escape(str(body))}</strong>
    <em>{escape(note)}</em>
  </div>
        """
        for label, style, body, note in phases
    )
    st.markdown(
        f"""
<div class="future-timeline">
  {phase_html}
</div>
        """,
        unsafe_allow_html=True,
    )


def render_fast_motion_video(
    video_path: Path,
    title: str,
    caption: str,
    playback_rate: float = 1.75,
) -> bool:
    video_uri = asset_data_uri(video_path, max_bytes=25_000_000)
    if video_uri is None:
        return False
    component_id = "video_" + "".join(ch for ch in video_path.stem if ch.isalnum())
    components.html(
        f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    html, body {{
      margin: 0;
      background: transparent;
      color: #e5edf7;
      font-family: Inter, system-ui, sans-serif;
    }}
    .video-card {{
      border: 1px solid rgba(94, 234, 212, 0.32);
      border-radius: 18px;
      overflow: hidden;
      background:
        radial-gradient(circle at 18% 10%, rgba(20,184,166,0.22), transparent 32%),
        linear-gradient(135deg, rgba(2,6,23,0.96), rgba(15,23,42,0.92));
      box-shadow: 0 22px 52px rgba(0,0,0,0.28);
    }}
    .video-head {{
      padding: 14px 16px 10px;
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: center;
    }}
    .video-head strong {{
      font-size: 15px;
      letter-spacing: 0.01em;
    }}
    .speed-chip {{
      border: 1px solid rgba(251,146,60,0.42);
      border-radius: 999px;
      color: #fed7aa;
      padding: 4px 9px;
      font-size: 12px;
      font-weight: 800;
      white-space: nowrap;
    }}
    video {{
      width: 100%;
      display: block;
      background: #020617;
      max-height: 560px;
    }}
    .video-caption {{
      color: #cbd5e1;
      font-size: 13px;
      line-height: 1.45;
      padding: 10px 16px 15px;
    }}
  </style>
</head>
<body>
  <div class="video-card">
    <div class="video-head">
      <strong>{escape(title)}</strong>
      <span class="speed-chip">{playback_rate:.2f}x playback</span>
    </div>
    <video id="{component_id}" src="{video_uri}" controls autoplay muted loop playsinline></video>
    <div class="video-caption">{escape(caption)}</div>
  </div>
  <script>
    const video = document.getElementById("{component_id}");
    video.playbackRate = {playback_rate};
    video.addEventListener("loadedmetadata", () => {{
      video.playbackRate = {playback_rate};
    }});
  </script>
</body>
</html>
        """,
        height=650,
        scrolling=False,
    )
    return True


def render_external_app_embed(url: str, title: str, caption: str, height: int = 760) -> None:
    components.html(
        f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    html, body {{
      margin: 0;
      background: transparent;
      font-family: Inter, system-ui, sans-serif;
      color: #e5edf7;
    }}
    .embed-shell {{
      border: 1px solid rgba(94, 234, 212, 0.30);
      border-radius: 18px;
      overflow: hidden;
      background: #020617;
      box-shadow: 0 22px 52px rgba(0,0,0,0.30);
    }}
    .embed-head {{
      padding: 13px 16px;
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: center;
      background: linear-gradient(135deg, rgba(15,23,42,0.98), rgba(15,118,110,0.26));
      border-bottom: 1px solid rgba(148,163,184,0.20);
    }}
    .embed-head strong {{ font-size: 15px; }}
    .embed-head a {{
      color: #5eead4;
      font-size: 12px;
      font-weight: 800;
      text-decoration: none;
      white-space: nowrap;
    }}
    iframe {{
      width: 100%;
      height: {height - 86}px;
      border: 0;
      display: block;
      background: #fff;
    }}
    .embed-caption {{
      color: #cbd5e1;
      font-size: 13px;
      line-height: 1.4;
      padding: 10px 16px 13px;
    }}
  </style>
</head>
<body>
  <div class="embed-shell">
    <div class="embed-head">
      <strong>{escape(title)}</strong>
      <a href="{escape(url)}" target="_blank" rel="noreferrer">Open full app</a>
    </div>
    <iframe src="{escape(url)}" loading="lazy" allowfullscreen></iframe>
    <div class="embed-caption">{escape(caption)}</div>
  </div>
</body>
</html>
        """,
        height=height,
        scrolling=False,
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


def render_mobile_system_map(mode: str, project_status: pd.DataFrame) -> None:
    flows = {
        "Research Flow": [
            ("Existing work", "PDFs, GIS, notebooks, screenshots, code, and videos."),
            ("Source capture", "Manifests preserve evidence, provenance, and working context."),
            ("Codex + notebooks", "Files become code, analysis, schemas, and reusable workflows."),
            ("Maps + explanations", "Scientific outputs become inspectable visual evidence."),
            ("Expert validation", "Claims, uncertainty, leakage, and plausibility are reviewed."),
            ("Site + deck", "Accepted work becomes Streamlit, a paper, or PowerPoint."),
        ],
        "Application Architecture": [
            ("CSV manifests", "Structured inventories, roadmaps, visuals, and project status."),
            ("Visual assets", "Project evidence, topic posters, videos, and contact sheets."),
            ("Parquet surfaces", "Structural datasets used by the North Slope explorer."),
            ("Streamlit app", "Current navigation, content, data access, and rendering entry point."),
            ("Plotly explorer", "Interactive scientific 3D surfaces and context overlays."),
            ("p5 visual layer", "Processing-style motion for workflows and uncertainty."),
            ("Visitor views", "Topic rooms, evidence, architecture, presentation, and mobile pages."),
        ],
    }

    st.markdown(
        """
<style>
  .mobile-system-stage {
    border: 1px solid #dbe3ea;
    border-left: 5px solid #2563eb;
    border-radius: 8px;
    padding: 14px 15px;
    margin: 0;
    background: #ffffff;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .mobile-system-stage.validation { border-left-color: #dc2626; }
  .mobile-system-icon {
    width: 42px;
    height: 42px;
    flex: 0 0 42px;
    display: grid;
    place-items: center;
    border: 1px solid #cbd5e1;
    border-radius: 9px;
    background: #f8fafc;
    color: #172033;
  }
  .mobile-system-icon svg { width: 25px; height: 25px; }
  .mobile-system-copy { min-width: 0; }
  .mobile-system-stage strong { display: block; color: #172033; font-size: 1rem; }
  .mobile-system-stage span { color: #475569; font-size: 0.9rem; line-height: 1.4; }
  .mobile-system-arrow {
    color: #f97316;
    font-size: 1.5rem;
    line-height: 1;
    text-align: center;
    padding: 5px 0;
  }
</style>
        """,
        unsafe_allow_html=True,
    )

    if mode in flows:
        for index, (title, body) in enumerate(flows[mode]):
            validation_class = " validation" if title == "Expert validation" else ""
            st.markdown(
                f"""
<div class="mobile-system-stage{validation_class}">
  <div class="mobile-system-icon">{workflow_icon_svg(title, index)}</div>
  <div class="mobile-system-copy">
    <strong>{index + 1}. {escape(title)}</strong>
    <span>{escape(body)}</span>
  </div>
</div>
                """,
                unsafe_allow_html=True,
            )
            if index < len(flows[mode]) - 1:
                st.markdown(
                    '<div class="mobile-system-arrow">&#8595;</div>',
                    unsafe_allow_html=True,
                )
        if mode == "Research Flow":
            st.info("Expert review can send the work back to Codex and notebooks for revision.")
        return

    stage_weights = {
        "planned": 0.0,
        "in_progress": 0.5,
        "partial": 0.65,
        "complete": 1.0,
    }
    for row in project_status.itertuples(index=False):
        values = [
            stage_weights.get(str(getattr(row, stage)).lower(), 0.0)
            for stage in ["evidence", "prototype", "interactive", "validated", "published"]
        ]
        progress = sum(values) / len(values)
        with st.container(border=True):
            st.markdown(f"**{row.title}**")
            st.progress(progress, text=f"{round(progress * 100)}% delivery progress")
            st.caption(row.next_step)


def render_system_map(mode: str, project_status: pd.DataFrame) -> None:
    stage_weights = {
        "planned": 0.0,
        "in_progress": 0.5,
        "partial": 0.65,
        "complete": 1.0,
    }
    progress_rows = []
    for row in project_status.itertuples(index=False):
        stage_values = [
            stage_weights.get(str(getattr(row, stage)).lower(), 0.0)
            for stage in ["evidence", "prototype", "interactive", "validated", "published"]
        ]
        progress_rows.append(
            {
                "id": row.project_key,
                "label": row.title,
                "progress": round(sum(stage_values) / len(stage_values), 2),
                "next": row.next_step,
            }
        )

    payload = json.dumps(
        {"mode": mode, "projects": progress_rows},
        ensure_ascii=True,
    ).replace("</", "<\\/")

    components.html(
        f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.11.3/p5.min.js"></script>
  <style>
    html, body {{ margin: 0; background: #f8fafc; color: #111827; font-family: Inter, system-ui, sans-serif; }}
    #frame {{ border: 1px solid #dbe3ea; border-radius: 8px; overflow: hidden; background: #ffffff; }}
    #canvas {{ min-height: 500px; overflow: hidden; }}
    #detail {{ min-height: 52px; padding: 12px 16px; border-top: 1px solid #e5e7eb; font-size: 14px; line-height: 1.4; }}
    #detail strong {{ display: block; margin-bottom: 3px; }}
    .fallback {{ padding: 24px; color: #475569; }}
    @media (max-width: 640px) {{
      #detail {{ min-height: 72px; padding: 12px; font-size: 13px; }}
    }}
  </style>
</head>
<body>
  <div id="frame">
    <div id="canvas"><div class="fallback">Loading Processing-style system map...</div></div>
    <div id="detail"><strong>Interactive system map</strong>Move across a node to inspect it. Click to hold its description.</div>
  </div>
  <script>
  const config = {payload};
  const palette = {{
    ink: '#172033', quiet: '#64748b', line: '#cbd5e1',
    orange: '#f97316', teal: '#0f766e', blue: '#2563eb',
    yellow: '#eab308', gray: '#94a3b8', red: '#dc2626', green: '#16a34a'
  }};
  const definitions = {{
    'Research Flow': {{
      nodes: [
        ['sources', 'Existing work', 0.09, 0.48, 'PDFs, GIS, notebooks, screenshots, code, and videos.', 'files'],
        ['capture', 'Source capture', 0.27, 0.30, 'Manifests and evidence preserve provenance and context.', 'capture'],
        ['build', 'Codex + notebooks', 0.46, 0.48, 'Files become code, analysis, schemas, and reusable workflows.', 'code'],
        ['visual', 'Maps + explanations', 0.64, 0.30, 'Scientific outputs become inspectable visual evidence.', 'map'],
        ['review', 'Expert validation', 0.78, 0.58, 'Claims, uncertainty, leakage, and scientific plausibility are reviewed.', 'gate'],
        ['publish', 'Site + deck', 0.92, 0.30, 'Validated work becomes Streamlit, a paper, or PowerPoint.', 'screen']
      ],
      edges: [['sources','capture'], ['capture','build'], ['build','visual'], ['visual','review'], ['review','publish'], ['review','build']]
    }},
    'Application Architecture': {{
      nodes: [
        ['manifest', 'CSV manifests', 0.10, 0.25, 'Structured inventories, roadmaps, visuals, and project status.', 'table'],
        ['assets', 'Visual assets', 0.10, 0.68, 'Project evidence, SVG topics, videos, and contact sheets.', 'image'],
        ['parquet', 'Parquet surfaces', 0.32, 0.68, 'Large structural datasets used by the North Slope explorer.', 'layers'],
        ['app', 'Streamlit app', 0.44, 0.40, 'Current routing, content, data access, and rendering entry point.', 'app'],
        ['plotly', 'Plotly explorer', 0.68, 0.68, 'Interactive scientific 3D surfaces and overlays.', 'cube'],
        ['p5', 'p5 visual layer', 0.68, 0.22, 'Processing-style motion for workflows, uncertainty, and progress.', 'motion'],
        ['visitor', 'Visitor views', 0.91, 0.40, 'Topic rooms, evidence, architecture, presentation, and mobile views.', 'people']
      ],
      edges: [['manifest','app'], ['assets','app'], ['parquet','app'], ['app','plotly'], ['app','p5'], ['plotly','visitor'], ['p5','visitor']]
    }}
  }};
  let nodes = [];
  let edges = [];
  let particles = [];
  let heldNode = null;
  let mobileLayout = false;

  function setupMode() {{
    if (config.mode === 'Delivery Progress') {{
      nodes = config.projects.map((project, index) => ({{
        id: project.id,
        label: project.label,
        xRatio: mobileLayout ? 0.26 + (index % 2) * 0.48 : 0.12 + (index % 3) * 0.38,
        yRatio: mobileLayout ? 0.13 + Math.floor(index / 2) * 0.19 : 0.20 + Math.floor(index / 3) * 0.31,
        detail: Math.round(project.progress * 100) + '% through evidence, prototype, interaction, validation, and publication. Next: ' + project.next,
        progress: project.progress,
        icon: projectIcon(project.id)
      }}));
      edges = [];
    }} else {{
      const selected = definitions[config.mode];
      nodes = selected.nodes.map((item, index) => ({{
        id: item[0], label: item[1], xRatio: item[2], yRatio: item[3], detail: item[4], progress: null, icon: item[5]
      }}));
      if (mobileLayout) {{
        const spacing = config.mode === 'Application Architecture' ? 0.13 : 0.15;
        const start = config.mode === 'Application Architecture' ? 0.10 : 0.12;
        nodes.forEach((node, index) => {{
          node.xRatio = index % 2 === 0 ? 0.30 : 0.70;
          node.yRatio = start + index * spacing;
        }});
      }}
      edges = selected.edges;
    }}
  }}

  function setup() {{
    const host = document.getElementById('canvas');
    host.innerHTML = '';
    mobileLayout = host.clientWidth < 640;
    const canvas = createCanvas(Math.max(host.clientWidth, 300), mobileLayout ? 700 : 500);
    canvas.parent('canvas');
    pixelDensity(1);
    textFont('Arial');
    setupMode();
    for (let i = 0; i < 24; i++) {{
      particles.push({{ edge: i % Math.max(edges.length, 1), t: random(), speed: random(0.0015, 0.004) }});
    }}
  }}

  function windowResized() {{
    const host = document.getElementById('canvas');
    mobileLayout = host.clientWidth < 640;
    resizeCanvas(Math.max(host.clientWidth, 300), mobileLayout ? 700 : 500);
    setupMode();
  }}

  function nodePosition(node) {{
    return {{ x: node.xRatio * width, y: node.yRatio * height }};
  }}

  function projectIcon(id) {{
    if (id.includes('north') || id.includes('valles')) return 'map';
    if (id.includes('thesis') || id.includes('rock')) return 'graph';
    if (id.includes('processing')) return 'globe';
    if (id.includes('pondicherry') || id.includes('moho')) return 'waveform';
    if (id.includes('stock')) return 'app';
    if (id.includes('arcgis')) return 'capture';
    return 'progress';
  }}

  function drawNodeIcon(icon, x, y, size, active, gate) {{
    const half = size / 2;
    const ink = gate ? palette.red : palette.ink;
    stroke(ink);
    strokeWeight(active ? 3 : 2);
    fill(active ? '#eff6ff' : '#ffffff');
    rectMode(CENTER);
    rect(x, y, size, size, 12);
    rectMode(CORNER);

    push();
    translate(x, y);
    stroke(ink);
    strokeWeight(2);
    noFill();

    if (icon === 'files') {{
      rect(-17, -13, 25, 29, 3);
      rect(-9, -18, 25, 29, 3);
      line(-3, -8, 10, -8); line(-3, -2, 10, -2); line(-3, 4, 7, 4);
    }} else if (icon === 'capture' || icon === 'image') {{
      rect(-19, -15, 38, 30, 4);
      circle(10, -7, 5);
      beginShape(); vertex(-15, 10); vertex(-6, 0); vertex(0, 6); vertex(7, -2); vertex(16, 10); endShape();
      if (icon === 'capture') {{ line(-24, -19, -14, -19); line(-24, -19, -24, -9); line(24, 19, 14, 19); line(24, 19, 24, 9); }}
    }} else if (icon === 'code' || icon === 'app') {{
      rect(-20, -16, 40, 32, 4);
      line(-20, -7, 20, -7);
      circle(-13, -12, 3); circle(-7, -12, 3);
      if (icon === 'code') {{ line(-10, 3, -4, 8); line(-10, 3, -4, -2); line(10, 3, 4, 8); line(10, 3, 4, -2); }}
      else {{ rect(-13, -1, 9, 10, 2); line(1, 0, 13, 0); line(1, 6, 10, 6); }}
    }} else if (icon === 'map') {{
      beginShape(); vertex(-20, -14); vertex(-7, -19); vertex(7, -14); vertex(20, -19); vertex(20, 14); vertex(7, 19); vertex(-7, 14); vertex(-20, 19); endShape(CLOSE);
      line(-7, -19, -7, 14); line(7, -14, 7, 19);
      circle(4, -1, 6); line(4, 2, 4, 9);
    }} else if (icon === 'gate') {{
      line(-14, -19, -14, 19); line(14, -19, 14, 19); line(-14, -12, 14, -12);
      line(-7, 3, -1, 9); line(-1, 9, 10, -5);
    }} else if (icon === 'screen') {{
      rect(-21, -16, 42, 29, 4); line(-8, 19, 8, 19); line(0, 13, 0, 19);
      line(-12, -6, 11, -6); line(-12, 0, 6, 0); line(-12, 6, 13, 6);
    }} else if (icon === 'table') {{
      rect(-19, -17, 38, 34, 3);
      line(-19, -6, 19, -6); line(-19, 5, 19, 5); line(-6, -17, -6, 17); line(7, -17, 7, 17);
    }} else if (icon === 'layers') {{
      beginShape(); vertex(0, -18); vertex(21, -8); vertex(0, 2); vertex(-21, -8); endShape(CLOSE);
      beginShape(); vertex(-21, 1); vertex(0, 11); vertex(21, 1); endShape();
      beginShape(); vertex(-21, 10); vertex(0, 20); vertex(21, 10); endShape();
    }} else if (icon === 'cube') {{
      beginShape(); vertex(0, -20); vertex(18, -10); vertex(18, 11); vertex(0, 21); vertex(-18, 11); vertex(-18, -10); endShape(CLOSE);
      line(0, 0, 0, 21); line(0, 0, 18, -10); line(0, 0, -18, -10);
    }} else if (icon === 'motion' || icon === 'globe') {{
      circle(0, 0, 36); ellipse(0, 0, 15, 36); line(-18, 0, 18, 0);
      if (icon === 'motion') {{ circle(18, 0, 5); circle(-10, -15, 5); }}
    }} else if (icon === 'people') {{
      circle(-12, -8, 9); circle(12, -8, 9); circle(0, -13, 10);
      arc(-12, 12, 18, 20, PI, TWO_PI); arc(12, 12, 18, 20, PI, TWO_PI); arc(0, 10, 22, 24, PI, TWO_PI);
    }} else if (icon === 'graph') {{
      line(-16, 12, -5, -7); line(-5, -7, 7, 2); line(7, 2, 17, -14);
      circle(-16, 12, 6); circle(-5, -7, 6); circle(7, 2, 6); circle(17, -14, 6);
    }} else if (icon === 'waveform') {{
      beginShape(); vertex(-22, 2); vertex(-15, 2); vertex(-10, -10); vertex(-4, 15); vertex(3, -17); vertex(9, 9); vertex(15, 2); vertex(22, 2); endShape();
    }} else {{
      rect(-18, -14, 10, 28, 3); rect(-5, -5, 10, 19, 3); rect(8, -19, 10, 33, 3);
    }}
    pop();
  }}

  function drawConnection(from, to, feedback) {{
    const a = nodePosition(from);
    const b = nodePosition(to);
    stroke(feedback ? palette.orange : palette.line);
    strokeWeight(feedback ? 2.5 : 2);
    noFill();
    if (feedback) {{
      bezier(a.x, a.y + 28, a.x, height - 30, b.x, height - 30, b.x, b.y + 28);
    }} else {{
      line(a.x, a.y, b.x, b.y);
    }}
  }}

  function draw() {{
    background('#ffffff');
    noStroke();
    fill(palette.quiet);
    textSize(12);
    textAlign(LEFT, TOP);
    text(config.mode.toUpperCase(), 20, 16);

    if (config.mode !== 'Delivery Progress') {{
      edges.forEach((edge, index) => {{
        const from = nodes.find(node => node.id === edge[0]);
        const to = nodes.find(node => node.id === edge[1]);
        drawConnection(from, to, index === edges.length - 1 && config.mode === 'Research Flow');
      }});
      particles.forEach(particle => {{
        const edge = edges[particle.edge % edges.length];
        const from = nodes.find(node => node.id === edge[0]);
        const to = nodes.find(node => node.id === edge[1]);
        const a = nodePosition(from);
        const b = nodePosition(to);
        particle.t = (particle.t + particle.speed) % 1;
        noStroke();
        fill(config.mode === 'Research Flow' ? palette.orange : palette.blue);
        circle(lerp(a.x, b.x, particle.t), lerp(a.y, b.y, particle.t), 5);
      }});
    }}

    let hovered = null;
    nodes.forEach(node => {{
      const p = nodePosition(node);
      const touchRadius = mobileLayout ? 44 : 54;
      const isHover = dist(mouseX, mouseY, p.x, p.y) < touchRadius;
      if (isHover) hovered = node;
      const isGate = node.id === 'review';
      const active = isHover || heldNode === node;
      const tileSize = active ? (mobileLayout ? 62 : 72) : (mobileLayout ? 56 : 66);
      drawNodeIcon(node.icon || 'progress', p.x, p.y, tileSize, active, isGate);

      if (node.progress !== null) {{
        const barWidth = mobileLayout ? 54 : 64;
        noStroke(); fill('#e2e8f0'); rect(p.x - barWidth / 2, p.y + tileSize / 2 + 30, barWidth, 5, 3);
        fill(node.progress > 0.68 ? palette.green : node.progress > 0.45 ? palette.yellow : palette.gray);
        rect(p.x - barWidth / 2, p.y + tileSize / 2 + 30, barWidth * node.progress, 5, 3);
      }}

      noStroke();
      fill(palette.ink);
      textAlign(CENTER, TOP);
      textSize(mobileLayout ? 10 : 12);
      textStyle(BOLD);
      const label = node.label.length > 24 ? node.label.replace(' And ', '\\n').replace(' For ', '\\n') : node.label;
      const labelWidth = mobileLayout ? 84 : 108;
      text(label, p.x - labelWidth / 2, p.y + tileSize / 2 + 7, labelWidth, 32);
      textStyle(NORMAL);
      if (node.progress !== null) {{
        fill(palette.quiet);
        textSize(mobileLayout ? 10 : 11);
        text(Math.round(node.progress * 100) + '%', p.x, p.y + tileSize / 2 + 37);
      }}
    }});

    if (hovered && !heldNode) updateDetail(hovered);
    if (!hovered && !heldNode) {{
      document.getElementById('detail').innerHTML = '<strong>Interactive system map</strong>Move across a node to inspect it. Click to hold its description.';
    }}
  }}

  function updateDetail(node) {{
    document.getElementById('detail').innerHTML = '<strong>' + node.label + '</strong>' + node.detail;
  }}

  function mousePressed() {{
    const selected = nodes.find(node => {{
      const p = nodePosition(node);
      return dist(mouseX, mouseY, p.x, p.y) < (mobileLayout ? 44 : 54);
    }});
    heldNode = selected || null;
    if (heldNode) updateDetail(heldNode);
  }}
  </script>
</body>
</html>
        """,
        height=610,
        scrolling=False,
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


def render_ml_model_part_explainer(compact: bool = False) -> None:
    """Show the concrete meaning of OCR, UI, state, model, actions, and labels."""
    asset_path = project_asset("assets/topic_visuals/ml_ocr_ui_state_encoder.svg")
    asset_uri = asset_data_uri(asset_path, max_bytes=950_000)
    asset_html = (
        f"<img src='{asset_uri}' alt='OCR and UI state encoder diagram'>"
        if asset_uri
        else "<div class='mini-screen'><div class='mini-window-bar'></div><div class='mini-screen-row'></div><div class='mini-screen-row short'></div></div>"
    )
    compact_class = " compact" if compact else ""
    st.markdown(
        f"""
<div class="ml-part-explainer{compact_class}">
  <div class="ml-part-head">
    <div>
      <div class="ml-part-kicker">ML model parts / visual glossary</div>
      <h3>What OCR, UI state, and the model actually mean</h3>
      <p>
        These diagrams should show what the model sees before it acts. A GUI agent does not only
        "look at a screenshot." It turns screen text, interface controls, files, prior actions,
        and human labels into a state representation, then chooses an action that must be reviewed.
      </p>
    </div>
    <div class="ml-part-asset">{asset_html}</div>
  </div>
  <div class="ml-part-grid">
    <div class="ml-part-card">
      <strong>1. Raw screen</strong>
      <div class="part-mini">
        <div class="mini-screen">
          <div class="mini-window-bar"></div>
          <div class="mini-screen-row"></div>
          <div class="mini-screen-row short"></div>
        </div>
      </div>
      <p>The visible software state: map, panel, dialog, error, file tree, cursor, and output preview.</p>
    </div>
    <div class="ml-part-card">
      <strong>2. OCR text</strong>
      <div class="part-mini">
        <span class="ocr-token">Run tool</span>
        <span class="ocr-token">Layer panel</span>
        <span class="ocr-token">Output</span>
        <span class="ocr-token">Error</span>
      </div>
      <p>OCR reads letters and numbers from the screen so the model can use visible labels as tokens.</p>
    </div>
    <div class="ml-part-card">
      <strong>3. UI objects</strong>
      <div class="part-mini">
        <span class="ui-outline button">button</span>
        <span class="ui-outline menu">menu</span>
        <span class="ui-outline panel">panel</span>
      </div>
      <p>UI means user interface controls: buttons, fields, menus, panels, map regions, and alerts.</p>
    </div>
    <div class="ml-part-card">
      <strong>4. State encoder</strong>
      <div class="part-mini">
        <div class="state-vector">
          <span></span><span></span><span></span><span></span><span></span><span></span>
          <span></span><span></span><span></span><span></span><span></span><span></span>
        </div>
      </div>
      <p>The encoder compresses OCR, UI boxes, files, and action history into model-ready features.</p>
    </div>
    <div class="ml-part-card">
      <strong>5. Policy model</strong>
      <div class="part-mini">
        <div class="policy-core"><span></span><span></span><span></span><span></span><span></span><span></span></div>
      </div>
      <p>The policy chooses the next action: click, type, open file, run tool, inspect output, or stop.</p>
    </div>
    <div class="ml-part-card">
      <strong>6. Labels and gates</strong>
      <div class="part-mini">
        <div class="review-mini">
          <span class="pass">rubric pass</span>
          <span class="fail">correction needed</span>
          <span class="holdout">held-out replay</span>
        </div>
      </div>
      <p>Human review turns a demo into training data and blocks shortcuts, unsafe actions, or fake success.</p>
    </div>
  </div>
  <div class="ml-part-strip">
    <strong>Website rule:</strong> when a topic says ML model, show the evidence, the variables, the model part,
    the validation gate, and the human review step in the same visual path.
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_thesis_graph_model_visuals() -> None:
    """Use REE drawing close-ups to explain the NLP and graph-ML model choices."""
    graph_asset_path = project_asset("assets/topic_visuals/critical_minerals_nlp_graph_ml.svg")
    graph_asset_uri = asset_data_uri(graph_asset_path, max_bytes=950_000)
    graph_asset_html = (
        f"<img src='{graph_asset_uri}' alt='Critical minerals NLP to graph ML diagram'>"
        if graph_asset_uri
        else "<div class='mini-screen'><div class='mini-window-bar'></div><div class='mini-screen-row'></div><div class='mini-screen-row short'></div></div>"
    )

    def closeup_card(title: str, path_text: str, note: str, focus_class: str) -> str:
        uri = asset_data_uri(project_asset(path_text), max_bytes=950_000)
        image_html = (
            f"<img src='{uri}' alt='{escape(title)} close-up'>"
            if uri
            else "<div class='mini-screen'><div class='mini-window-bar'></div><div class='mini-screen-row'></div><div class='mini-screen-row short'></div></div>"
        )
        return f"""
<div class="adobe-closeup-card {focus_class}">
  {image_html}
  <div class="adobe-closeup-body">
    <strong>{escape(title)}</strong>
    <span>{escape(note)}</span>
  </div>
</div>
        """

    closeups = [
        closeup_card(
            "Deposit-shape close-up",
            "assets/project_visuals/ree_bayan_obo_main.png",
            "Use the Adobe drawing as the visual source for deposit, mineral, host, and process nodes.",
            "focus-center",
        ),
        closeup_card(
            "Host-context close-up",
            "assets/project_visuals/ree_host_context_bayan.png",
            "Crop the diagram around host rocks and context so the graph story starts from visible geology.",
            "focus-left",
        ),
        closeup_card(
            "Mineral relationship close-up",
            "assets/project_visuals/ree_dominant_minerals_bayan.png",
            "Show candidate mineral labels and relationships before any AI-suggested edge is trusted.",
            "focus-right",
        ),
    ]

    model_cards = [
        {
            "class": "science",
            "name": "SciBERT",
            "body": "A BERT-style language model trained on scientific text. Use it to tag scientific terms in papers, captions, and slide notes.",
            "why": "Why here: it gives the REE graph a text reader for minerals, processes, locations, and evidence phrases.",
            "href": "https://arxiv.org/abs/1903.10676",
        },
        {
            "class": "materials",
            "name": "MatSciBERT",
            "body": "A materials-domain language model trained on materials science literature.",
            "why": "Why here: mineral names, chemical formulas, phases, and materials jargon should be easier to tag than with a generic text model.",
            "href": "https://www.nature.com/articles/s41524-022-00784-w",
        },
        {
            "class": "sage",
            "name": "GraphSAGE",
            "body": "A graph neural network approach that samples neighbors and aggregates node features.",
            "why": "Why here: a new paper, deposit, or mineral node can inherit context from nearby reviewed graph nodes.",
            "href": "https://arxiv.org/abs/1706.02216",
        },
        {
            "class": "rgcn",
            "name": "R-GCN",
            "body": "A relational graph convolution model designed for graphs with many edge types.",
            "why": "Why here: contains, hosted-by, altered-by, and evidence-for edges should not be treated as the same relationship.",
            "href": "https://arxiv.org/abs/1703.06103",
        },
    ]
    model_html = "".join(
        f"""
<div class="graph-model-card {escape(card['class'])}">
  <strong>{escape(card['name'])}</strong>
  <span>{escape(card['body'])}</span>
  <span>{escape(card['why'])}</span>
  <a href="{escape(card['href'])}" target="_blank">Source paper</a>
</div>
        """
        for card in model_cards
    )
    st.markdown(
        f"""
<div class="thesis-graph-models">
  <div class="thesis-graph-head">
    <div>
      <div class="thesis-graph-kicker">Second topic / drawings and ideas close-up</div>
      <h3>Use Adobe sketches as the visible front door into graph ML</h3>
      <p>
        The topic should not start with abstract model names. First show close-ups of the real REE
        sketch language, then show how text encoders and graph models would convert those visible
        ideas into reviewed nodes, typed edges, and candidate links.
      </p>
    </div>
    <div class="graph-model-asset">{graph_asset_html}</div>
  </div>
  <div class="adobe-closeup-grid">{''.join(closeups)}</div>
  <div class="graph-model-grid">{model_html}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def detail_pills(items: list[str]) -> str:
    return "".join(f"<span class='detail-pill'>{escape(item)}</span>" for item in items)


def detail_text(items: list[str]) -> str:
    return "; ".join(items)


def render_research_sources() -> None:
    links = "".join(
        f"<a href='{escape(url)}' target='_blank'>{escape(title)}</a>"
        for title, url in RESEARCH_SOURCES
    )
    st.markdown(
        f"<div class='research-source-grid'>{links}</div>",
        unsafe_allow_html=True,
    )


def render_detailed_topic_plan(topic: dict, compact: bool = False) -> None:
    plan = DETAILED_TOPIC_PLANS.get(topic["slug"])
    if plan is None:
        return
    frames = "".join(
        f"<div class='story-frame'><b>Frame {idx}</b>{escape(frame)}</div>"
        for idx, frame in enumerate(plan["storyboard"], start=1)
    )
    title = plan["title"] if not compact else topic["title"]
    st.markdown(
        f"""
<div class="detail-card">
  <h3>{escape(title)}</h3>
  <div class="detail-question">{escape(plan["question"])}</div>
  <div class="detail-grid">
    <div class="detail-cell">
      <strong>Project anchor</strong>
      <span>{escape(plan["anchor"])}</span>
    </div>
    <div class="detail-cell">
      <strong>Conclusion</strong>
      <span>{escape(plan["conclusion"])}</span>
    </div>
    <div class="detail-cell">
      <strong>Modern ML/AI</strong>
      <div class="detail-pill-row">{detail_pills(plan["techniques"])}</div>
    </div>
    <div class="detail-cell">
      <strong>Data inputs</strong>
      <span>{escape(detail_text(plan["inputs"]))}</span>
    </div>
    <div class="detail-cell">
      <strong>Outputs</strong>
      <span>{escape(detail_text(plan["outputs"]))}</span>
    </div>
    <div class="detail-cell">
      <strong>Bottleneck</strong>
      <span>{escape(plan["bottleneck"])}</span>
    </div>
    <div class="detail-cell">
      <strong>Expert validates</strong>
      <span>{escape(plan["validate"])}</span>
    </div>
    <div class="detail-cell">
      <strong>Animation labels</strong>
      <div class="detail-pill-row">{detail_pills(plan["labels"])}</div>
    </div>
    <div class="detail-cell">
      <strong>Abstract animation</strong>
      <span>{escape(PROCESSING_SKETCH_PLANS.get(topic["slug"], {}).get("visual", ""))}</span>
    </div>
  </div>
  <div class="story-frames">{frames}</div>
  <div class="honesty-box"><strong>Do not claim:</strong> {escape(plan["do_not_claim"])}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_ai_workflow_panel(topic: dict, compact: bool = False) -> None:
    evidence = AI_WORKFLOW_EVIDENCE.get(topic["slug"])
    if evidence is None:
        return
    chips = "".join(
        f"<span class='ai-chip'>{escape(chip)}</span>"
        for chip in evidence["chips"]
    )
    title = "AI workflow evidence" if not compact else "Workflow evidence"
    st.markdown(
        f"""
<div class="ai-case-brief">
  <div class="ai-case-top">
    <div>
      <h3>{title}</h3>
      <p>{escape(evidence["description"])}</p>
    </div>
    <div class="ai-chip-row">{chips}</div>
  </div>
  <div class="ai-evidence-grid">
    <div class="ai-evidence-cell">
      <strong>Where AI helped</strong>
      <span>{escape(evidence["where"])}</span>
    </div>
    <div class="ai-evidence-cell">
      <strong>What I gave AI</strong>
      <span>{escape(evidence["gave"])}</span>
    </div>
    <div class="ai-evidence-cell">
      <strong>What AI produced</strong>
      <span>{escape(evidence["produced"])}</span>
    </div>
    <div class="ai-evidence-cell validation">
      <strong>Human validation</strong>
      <span>{escape(evidence["validated"])}</span>
    </div>
  </div>
  <div class="ai-future-line"><strong>Future ML version:</strong> {escape(evidence["future"])}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_source_backed_asset_panel(topic: dict) -> None:
    assets = SOURCE_BACKED_TOPIC_ASSETS.get(topic["slug"], [])
    if not assets:
        return
    st.subheader("Source images on deck")
    st.markdown(
        "<p class='source-panel-note'>Local screenshots, slide thumbnails, and exported visuals are shown here directly. "
        "External links stay in evidence leads only for provenance.</p>",
        unsafe_allow_html=True,
    )
    columns = st.columns(min(3, len(assets)))
    for idx, asset in enumerate(assets):
        with columns[idx % len(columns)]:
            with st.container(border=True):
                st.markdown(f"**{escape(asset['title'])}**")
                asset_path = project_asset(asset["path"])
                if asset_path.exists():
                    st.image(
                        str(asset_path),
                        caption=f"{asset['source']}: {asset['note']}",
                        use_container_width=True,
                    )
                else:
                    st.warning(f"Missing local source image: {asset_path.name}")
                    st.caption(f"{asset['source']}: {asset['note']}")


def ml_diagram_row(slug: str) -> pd.Series | None:
    match = ml_diagram_tracker[ml_diagram_tracker["topic_slug"] == slug]
    if match.empty:
        return None
    return match.iloc[0]


def compact_terms(value: str, limit: int = 3) -> list[str]:
    return [
        term.strip()
        for term in str(value).split(";")
        if term.strip()
    ][:limit]


def render_ml_visual_diagram(topic: dict, compact: bool = False) -> None:
    blueprint = ML_DIAGRAM_BLUEPRINTS.get(topic["slug"])
    if blueprint is None:
        return
    model_detail = ML_MODEL_DETAIL_DIAGRAMS.get(topic["slug"])
    row = ml_diagram_row(topic["slug"])
    tracker_validation = compact_terms(row["validation_gates"], 3) if row is not None else []
    tracker_next = str(row["next_action"]) if row is not None else "Build source-backed diagram."
    primary_source = str(row["primary_ml_source"]) if row is not None else "ML sources"
    secondary_source = str(row["secondary_ml_source"]) if row is not None else ""
    evidence_assets = SOURCE_BACKED_TOPIC_ASSETS.get(topic["slug"], [])
    evidence_html = workflow_icon_svg(topic["title"], 0)
    evidence_label = "project source"
    evidence_candidates = [
        (asset["title"], asset["path"])
        for asset in evidence_assets
    ]
    topic_visual = TOPIC_VISUALS.get(topic["slug"])
    if topic_visual:
        evidence_candidates.append(("topic sketch", topic_visual))
    for candidate_title, candidate_path in evidence_candidates:
        asset_path = project_asset(candidate_path)
        if asset_path.exists():
            asset_uri = asset_data_uri(asset_path, max_bytes=900_000)
            if asset_uri is not None:
                evidence_html = f"<img src='{asset_uri}' alt='{escape(candidate_title)}'>"
                evidence_label = candidate_title
                break

    source_chips = "".join(
        f"""
<div class="ml-source-ribbon">
  <strong>{escape(source['label'])}</strong>
  <span>{escape(source['short'])}</span>
</div>
        """
        for source in ML_SOURCE_RIBBONS
    )
    feature_chips = "".join(
        f"<span>{escape(feature)}</span>"
        for feature in blueprint["features"][:5]
    )
    risk_chips = "".join(
        f"<span>{escape(risk)}</span>"
        for risk in tracker_validation
    )
    model_label = (
        model_detail["main"]["name"]
        if model_detail is not None
        else blueprint["model"]
    )
    flow_nodes = [
        ("TARGET", blueprint["target"]),
        ("FEATURES", feature_chips),
        ("QC", blueprint["source_pattern"]),
        ("MODEL", model_label),
        ("VALIDATE", blueprint["validation"]),
        ("OUTPUT", blueprint["output"]),
    ]
    flow_html = ""
    for idx, (label, value) in enumerate(flow_nodes, start=1):
        value_html = value if label == "FEATURES" else escape(value)
        flow_html += f"""
<div class="ml-flow-node">
  <div class="ml-node-icon">{workflow_icon_svg(label, idx)}</div>
  <strong>{label}</strong>
  <span>{value_html}</span>
</div>
        """

    secondary_line = (
        f"<span>{escape(secondary_source)}</span>"
        if secondary_source and secondary_source.lower() != "nan"
        else "<span>Used as validation / monitoring layer</span>"
    )
    model_detail_html = ""
    if model_detail is not None and not compact:
        def model_stage_card(stage_key: str, stage_label: str) -> str:
            stage = model_detail[stage_key]
            return f"""
<div class="ml-model-card {stage_key}">
  <strong>{escape(stage_label)}</strong>
  <div class="ml-model-name">{escape(stage["name"])}</div>
  <div class="ml-model-row"><span>Target</span><p>{escape(stage["target"])}</p></div>
  <div class="ml-model-row"><span>Inputs</span><p>{escape(stage["input"])}</p></div>
  <div class="ml-model-row"><span>Training unit</span><p>{escape(stage["unit"])}</p></div>
</div>
            """

        metric_chips = "".join(
            f"<span>{escape(metric)}</span>"
            for metric in model_detail["metrics"]
        )
        validation_card = f"""
<div class="ml-model-card validation">
  <strong>Validation / Gate</strong>
  <div class="ml-model-row"><span>Split strategy</span><p>{escape(model_detail["validation"])}</p></div>
  <div class="ml-model-row"><span>Metrics</span><p class="ml-metric-chips">{metric_chips}</p></div>
  <div class="ml-model-row"><span>Human / risk gate</span><p>{escape(model_detail["gate"])}</p></div>
  <div class="ml-model-row"><span>Diagram wording</span><p>{escape(model_detail["diagram"])}</p></div>
</div>
        """
        model_detail_html = f"""
  <div class="ml-model-detail">
    <div class="ml-model-stack">
      {model_stage_card("reference", "Reference Model")}
      {model_stage_card("main", "Main Candidate")}
      {model_stage_card("challenger", "Challenger / Advanced")}
      {validation_card}
    </div>
  </div>
        """
    compact_class = " compact" if compact else ""
    st.markdown(
        f"""
<div class="ml-visual-diagram{compact_class}">
  <div class="ml-visual-head">
    <div>
      <div class="ml-kicker">ML diagram from the two source attachments</div>
      <h3>{escape(topic['title'])}: {escape(blueprint['objective'])}</h3>
    </div>
    <div class="ml-source-ribbons">{source_chips}</div>
  </div>
  <div class="ml-visual-board">
    <div class="ml-evidence-card">
      {evidence_html}
      <strong>{escape(evidence_label)}</strong>
      <span>real topic evidence</span>
    </div>
    <div class="ml-flow-track">{flow_html}</div>
    <div class="ml-gate-card">
      <strong>risk gate</strong>
      <div class="ml-risk-chips">{risk_chips}</div>
      <small>{escape(tracker_next)}</small>
    </div>
  </div>
  {model_detail_html}
  <div class="ml-source-map">
    <div><strong>Hydrate paper pattern</strong><span>Sgh target, log features, washout/GLOSS QC, transfer test.</span></div>
    <div><strong>Primary here</strong><span>{escape(primary_source)}</span></div>
    <div><strong>Validation notes</strong>{secondary_line}</div>
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def _diagram_chip_html(items: list[str], class_name: str = "") -> str:
    classes = f"diagram-chip {class_name}".strip()
    return "".join(f"<span class='{classes}'>{escape(item)}</span>" for item in items)


def _gate_box_html(label: str, detail: str) -> str:
    return f"<div class='gate-box'><strong>{escape(label)}</strong>{escape(detail)}</div>"


def _render_rich_manual_shell(manual: dict, body_html: str) -> None:
    st.markdown(
        f"""
<div class="manual-architecture priority rich-manual">
  <div class="rich-head">
    <div>
      <div class="rich-kicker">Visual-first manual / {escape(manual["kicker"])}</div>
      <h3>{escape(manual["name"])}</h3>
    </div>
    <div class="rich-output">Honest output: {escape(manual["output"])}</div>
  </div>
  {body_html}
</div>
        """,
        unsafe_allow_html=True,
    )


def render_priority_manual_visual_architecture(slug: str, manual: dict) -> bool:
    renderers = {
        "north_slope": render_hydrate_architecture_diagram,
        "ai_workflow": render_trace_factory_diagram,
        "thesis_graph": render_source_to_graph_diagram,
        "processing_earthquake": render_earthquake_feature_diagram,
        "seismic": render_seismic_qa_diagram,
        "rock_classification": render_rock_label_diagram,
        "valles": render_geophysical_disagreement_diagram,
        "near_surface": render_fen_fusion_diagram,
        "moho_ml": render_regional_transfer_diagram,
        "ambient_noise": render_ambient_noise_diagram,
        "stock_workflow": render_app_risk_diagram,
        "sem_petrography": render_sem_interpretation_diagram,
    }
    renderer = renderers.get(slug)
    if renderer is None:
        return False
    renderer(manual)
    return True


def render_hydrate_architecture_diagram(manual: dict) -> None:
    source_chips = _diagram_chip_html(
        ["public sources", "well IDs", "formation tops", "source library"],
        "source",
    )
    log_chips = "".join(
        f"<span>{escape(label)}</span>"
        for label in ["density", "porosity", "GR", "Rt", "Vp", "Vs"]
    )
    gates = "".join(
        [
            _gate_box_html("Leakage", "leakage barrier blocks NMR Sgh from feature transforms."),
            _gate_box_html("Split", "Random depth-row split blocked; use leave-well-out."),
            _gate_box_html("QC", "caliper washout and GLOSS outliers are removed before fit."),
            _gate_box_html("Claim", "low confidence intervals route to abstention and review."),
        ]
    )
    body_html = f"""
<div class="rich-diagram hydrate-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Source, log, and target lanes</h4>
      <div class="diagram-chip-row">{source_chips}</div>
      <div class="mini-table" style="margin-top:0.48rem;">
        <div><b>Training unit</b><span>depth point</span></div>
        <div><b>NMR target</b><span>Sgh saturation</span></div>
        <div><b>Review unit</b><span>complete well interval</span></div>
      </div>
      <div class="hydrate-log-grid">{log_chips}</div>
      <div class="borehole-sketch">
        <div class="borehole-track"></div>
        <div class="qc-stack">
          <div class="qc-tile"><b>Sgh</b>NMR-derived target interval, kept separate from features.</div>
          <div class="qc-tile"><b>caliper washout</b>Widened borehole segment is crossed out before training.</div>
        </div>
      </div>
    </div>
    <div class="leakage-wall">leakage barrier</div>
    <div class="rich-stage">
      <h4>QC and train-only feature work</h4>
      <div class="qc-stack">
        <div class="qc-tile"><b>CRS/depth QC</b>Align wells, depth rows, and public geology before feature rows exist.</div>
        <div class="qc-tile"><b>missing log gate</b>Rows without high-value logs are flagged or removed.</div>
        <div class="qc-tile"><b>train-only normalization</b>Min-max scaling is fit inside training wells only.</div>
      </div>
      <div class="gloss-points" aria-hidden="true">
        <span style="left:18%;top:26%;"></span>
        <span style="left:34%;top:42%;"></span>
        <span style="left:48%;top:32%;"></span>
        <span style="left:58%;top:55%;"></span>
        <span style="left:28%;top:62%;"></span>
        <span class="outlier" style="left:78%;top:20%;"></span>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["GLOSS outlier", "feature combinations", "GR + Vp", "Rt + Vp"], "target")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Models, validation, and review</h4>
      <div class="model-stack">
        <div class="model-block">Ridge / ElasticNet reference for Sgh</div>
        <div class="model-block main">
          Keras/TensorFlow ANN Sgh regressor
          <div class="ann-layer"><span></span><span></span><span></span><span></span></div>
          two hidden layers, 40 nodes each
        </div>
        <div class="model-block">XGBoost challenger for nonlinear interactions</div>
      </div>
      <div class="well-validation">
        <span>train well</span><span>train well</span><span>sealed test well</span>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["leave-well-out validation", "R2", "MAE", "RMSE"], "model")}
      </div>
      <div class="abstain-bin">calibration -> abstention bin -> geologist review</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_trace_factory_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("State", "Hidden state missing from video pauses labeling."),
            _gate_box_html("Shortcut", "Screen-layout memorization fails replay."),
            _gate_box_html("Rubric", "Ambiguous prompt/rubric goes to relabeling."),
            _gate_box_html("Unsafe", "Unsafe action gate blocks delete, upload, overwrite."),
        ]
    )
    body_html = f"""
<div class="rich-diagram trace-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Demonstration evidence</h4>
      <div class="trace-input-stack">
        <div class="qc-tile"><b>prompt/rubric</b>Task goal plus pass/fail label source.</div>
        <div class="qc-tile"><b>screen recording</b>Frames become observable states.</div>
        <div class="qc-tile"><b>file tree</b>Allowed project files and paths.</div>
      </div>
      <div class="trace-frame">
        <div class="screen-bar"></div>
        <span class="ui-token">button</span>
        <span class="ui-token">menu</span>
        <span class="ui-token">layer</span>
        <span class="ui-token">filepath</span>
        <span class="ui-token">CRS</span>
        <span class="ui-token">parameter</span>
        <span class="ui-token">output</span>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Trace encoder and policy</h4>
      <div class="trace-path">
        <div class="trace-step">t0 observe state</div>
        <div class="trace-step">t1 click/tool action</div>
        <div class="trace-step">t2 inspect output</div>
        <div class="trace-step">t3 correction reason</div>
      </div>
      <div class="encoder-grid" style="margin-top:0.5rem;">
        <div class="encoder-box">CLIP/OCR state encoder</div>
        <div class="encoder-box">UI tokens + file-tree metadata</div>
      </div>
      <div class="transformer-stack">behavior-cloning transformer predicts action, target, parameter, stop/review</div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Replay validation and stop gates</h4>
      <div class="replay-panel">
        <div class="diagram-chip-row">
          {_diagram_chip_html(["replay simulator", "scientific software task", "held-out project"], "source")}
        </div>
      </div>
      <div class="replay-score">
        <div class="score-box pass">held-out task score</div>
        <div class="score-box fail">unsafe action gate</div>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["action trace", "rubric label", "pass/fail", "human approval"], "review")}
      </div>
      <div class="abstain-bin">failed replay -> human review queue</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_source_to_graph_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Edge", "Hallucinated or unsupported edge is blocked."),
            _gate_box_html("Entity", "Duplicate entity names merge during ontology cleanup."),
            _gate_box_html("Leakage", "Graph leakage checked before link ranking."),
            _gate_box_html("Evidence", "Visually strong edge still needs source support."),
        ]
    )
    entity_nodes = "".join(
        f"<span class='entity-node'>{escape(label)}</span>"
        for label in ["mineral", "host rock", "deposit", "process", "location", "age"]
    )
    body_html = f"""
<div class="rich-diagram graph-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Source evidence entering the hub</h4>
      <div class="graph-source-stack">
        <div class="source-doc">papers + thesis chunks</div>
        <div class="source-doc">slides + figure captions</div>
        <div class="source-doc">CSV nodes and edge tables</div>
        <div class="source-doc">Gephi / Adobe graphics</div>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.48rem;">
        {_diagram_chip_html(["source-backed edge", "evidence source", "schema validity"], "source")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Entity, ontology, and relation layers</h4>
      <div class="entity-clusters">{entity_nodes}</div>
      <div class="ontology-merge">
        <span>ontology cleanup</span>
        <span>REE mineral + rare earth mineral -> mineral</span>
      </div>
      <div class="edge-visuals">
        <div class="edge-row">
          <div class="graph-dot">source</div><div class="edge-line"></div><div class="graph-dot">edge</div>
        </div>
        <div class="edge-row">
          <div class="graph-dot">AI idea</div><div class="edge-line dashed"></div><div class="graph-dot">review</div>
        </div>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["entity extraction", "relation cross-encoder", "source-backed edge", "inferred edge"], "target")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Retrieval, graph ML, and audit</h4>
      <div class="audit-chain">
        <div class="audit-node">GraphRAG retrieval: question node follows cited graph paths</div>
        <div class="audit-node">GraphSAGE / R-GCN ranks candidate relationships</div>
        <div class="audit-node review">human edge audit approves, edits, or rejects</div>
        <div class="audit-node gate">queryable graph publishes only reviewed evidence states</div>
      </div>
      <div class="graphrag-path">question -> graph path -> source chunks -> cited answer</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_earthquake_feature_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Look-ahead", "future windows are locked before feature generation."),
            _gate_box_html("Events", "duplicate or bad USGS events fail cleanup."),
            _gate_box_html("Imbalance", "rare anomaly labels need PR-AUC/F1 checks."),
            _gate_box_html("Claim", "no forecast language without future-window validation."),
        ]
    )
    body_html = f"""
<div class="rich-diagram earthquake-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>USGS event source</h4>
      <div class="globe-panel">
        <div class="globe-orb">
          <span class="event-dot shallow" style="left:62%;top:22%;"></span>
          <span class="event-dot mid" style="left:30%;top:46%;"></span>
          <span class="event-dot deep" style="left:52%;top:67%;"></span>
          <span class="event-dot shallow" style="left:41%;top:18%;"></span>
        </div>
        <div class="qc-stack">
          <div class="qc-tile"><b>globe/sound encoding</b>latitude, longitude, depth, magnitude, event time.</div>
          <div class="qc-tile"><b>flattening lens</b>visual marks become region-time feature rows.</div>
        </div>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.48rem;">
        {_diagram_chip_html(["USGS events", "magnitude bins", "depth bins", "lagged history"], "source")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Region-time feature table</h4>
      <div class="feature-row-grid">
        <div><span>region</span><span>window</span><span>count</span><span>lag</span></div>
        <div><span>A12</span><span>t-2</span><span>03</span><span>past only</span></div>
        <div><span>A12</span><span>t-1</span><span>07</span><span>past only</span></div>
        <div><span>A12</span><span>t</span><span>locked</span><span>target</span></div>
      </div>
      <div class="chronology-strip">
        <span>train older windows</span><span class="lock">time boundary</span><span>test newer windows</span>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["lagged feature", "chronological split", "spatial autocorrelation check"], "target")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Models and honest output</h4>
      <div class="model-stack">
        <div class="model-block">Poisson GLM event-count reference</div>
        <div class="model-block">negative-binomial model for overdispersed counts</div>
        <div class="model-block main">LightGBM anomaly ranker after target is defined</div>
      </div>
      <div class="abstain-bin">output: anomaly pattern view, not an unsupported earthquake forecast</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_seismic_qa_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Station", "station mismatch blocks pick propagation."),
            _gate_box_html("Signal", "weak waveform routes to QA, not interpretation."),
            _gate_box_html("Metadata", "bad channel or distance metadata fails ETL."),
            _gate_box_html("Review", "velocity table waits for human-reviewed picks."),
        ]
    )
    waveform_svg = """
<svg class="waveform-svg" viewBox="0 0 320 95" aria-hidden="true" fill="none">
  <path d="M5 50 C20 48 24 54 34 50 C44 43 52 58 62 50 C75 35 82 65 92 50 C106 25 116 76 128 50 C143 20 154 80 168 50 C184 35 194 61 210 50 C226 42 238 56 250 50 C270 47 288 53 315 50" stroke="currentColor" stroke-width="3"/>
  <rect x="116" y="10" width="34" height="75" fill="#fef3c7" stroke="#f59e0b"/>
  <line x1="132" y1="8" x2="132" y2="87" stroke="#dc2626" stroke-width="3"/>
  <line x1="214" y1="8" x2="214" y2="87" stroke="#2563eb" stroke-width="3"/>
</svg>
    """
    body_html = f"""
<div class="rich-diagram seismic-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Notebook and waveform evidence</h4>
      <div class="qc-stack">
        <div class="qc-tile"><b>catalog search</b>event id, magnitude, expected arrival window.</div>
        <div class="qc-tile"><b>station metadata</b>station, channel, distance, completeness.</div>
        <div class="qc-tile"><b>waveform windows</b>event-station-channel training unit.</div>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["ObsPy window", "SNR", "channel check", "notebook cell"], "source")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>QA model and pick proposal</h4>
      <div class="waveform-panel">{waveform_svg}</div>
      <div class="pick-band"><span>P pick band</span><span>S pick line</span></div>
      <div class="model-stack" style="margin-top:0.45rem;">
        <div class="model-block">LightGBM waveform QA classifier</div>
        <div class="model-block main">PhaseNet / EQTransformer pick proposal</div>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Uncertainty and reviewed output</h4>
      <div class="mini-table">
        <div><b>target</b><span>usable waveform / P-S pick</span></div>
        <div><b>split</b><span>held-out event or station</span></div>
        <div><b>metrics</b><span>pick-time error, precision/recall</span></div>
      </div>
      <div class="abstain-bin">uncertainty band -> human-reviewed velocity table</div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["uncertain manual pick", "reviewer mark", "caveat tag"], "review")}
      </div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_rock_label_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Leakage", "same-sample crops stay together in sample-held-out split."),
            _gate_box_html("Label", "weak labels and mixed definitions pause fusion."),
            _gate_box_html("Scale", "missing scale/context routes to ambiguous bucket."),
            _gate_box_html("Causation", "VIF/correlation gate blocks chemistry overclaim."),
        ]
    )
    body_html = f"""
<div class="rich-diagram rock-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Evidence and label audit</h4>
      <div class="diagram-chip-row">
        {_diagram_chip_html(["thin sections", "classification charts", "spider diagrams", "formation tables"], "source")}
      </div>
      <div class="mini-table" style="margin-top:0.5rem;">
        <div><b>training unit</b><span>sample / crop / mapped unit</span></div>
        <div><b>label state</b><span>strong, weak, ambiguous</span></div>
        <div><b>split</b><span>sample-held-out</span></div>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Separate model branches</h4>
      <div class="modality-grid">
        <div class="modality-card"><b>image branch</b>EfficientNet / ResNet embedding from thin-section or map crop.</div>
        <div class="modality-card"><b>chemistry branch</b>XGBoost / LightGBM on ratios, spider values, formation variables.</div>
        <div class="modality-card"><b>text branch</b>caption, source label, and formation context embedding.</div>
      </div>
      <div class="fusion-node">late-fusion label ranker only after metadata audit</div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["weak label", "VIF/correlation check", "ambiguous bucket"], "target")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Ranked labels and correction loop</h4>
      <div class="model-stack">
        <div class="model-block">logistic regression / linear SVM reference</div>
        <div class="model-block main">late-fusion MLP ranks rock or mineral label</div>
        <div class="model-block">CLIP retrieval challenger for similar reviewed examples</div>
      </div>
      <div class="abstain-bin">expert correction queue feeds revised training examples</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_geophysical_disagreement_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Registration", "shifted layers keep red offset warning."),
            _gate_box_html("Artifact", "acquisition artifact cannot become geologic signal."),
            _gate_box_html("Physics", "method physics stays visible by lane."),
            _gate_box_html("Consensus", "false consensus gate blocks smoothed overclaim."),
        ]
    )
    body_html = f"""
<div class="rich-diagram valles-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Method-specific evidence lanes</h4>
      <div class="method-lanes">
        <div class="method-lane"><span>gravity</span><span class="method-bar gravity"></span><span>density</span></div>
        <div class="method-lane"><span>EM/TEM</span><span class="method-bar em"></span><span>conductivity</span></div>
        <div class="method-lane"><span>ERT</span><span class="method-bar ert"></span><span>resistivity</span></div>
        <div class="method-lane"><span>seismic</span><span class="method-bar seismic"></span><span>velocity</span></div>
        <div class="method-lane"><span>field notes</span><span class="method-bar notes"></span><span>context</span></div>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Shared frame with conflict preserved</h4>
      <div class="agreement-zone">agreement zone: methods align in the same spatial frame</div>
      <div class="conflict-zone">conflict zone: striped method disagreement stays visible</div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["misregistration", "uncertainty ribbon", "conflict classifier"], "target")}
      </div>
      <div class="model-stack" style="margin-top:0.45rem;">
        <div class="model-block main">LightGBM conflict ranker</div>
        <div class="model-block">Gaussian Process uncertainty surfaces</div>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Expert disagreement board</h4>
      <div class="mini-table">
        <div><b>training unit</b><span>grid cell / zone / line intersection</span></div>
        <div><b>split</b><span>leave-area-out or leave-line-out</span></div>
        <div><b>output</b><span>review-priority rank</span></div>
      </div>
      <div class="abstain-bin">not final subsurface truth; review conflict zones first</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_fen_fusion_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Geometry", "wrong line intersection blocks feature row."),
            _gate_box_html("Context", "field-note loss creates missing-context status."),
            _gate_box_html("Unit", "possible unit cannot become asserted unit."),
            _gate_box_html("Validation", "leave-line-out failure routes to review."),
        ]
    )
    body_html = f"""
<div class="rich-diagram fen-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Line geometry and field evidence</h4>
      <div class="diagram-chip-row">
        {_diagram_chip_html(["hammer seismic", "ERT", "TEM", "field notes", "line intersections"], "source")}
      </div>
      <div class="cross-section" style="margin-top:0.52rem;">
        <div class="section-layer velocity">hammer seismic velocity lane</div>
        <div class="section-layer resistivity">ERT resistivity lane</div>
        <div class="section-layer conductivity">TEM conductivity lane</div>
        <div class="section-layer possible">possible unit labels + field-note context</div>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Agreement and conflict ranking</h4>
      <div class="feature-row-grid">
        <div><span>line</span><span>velocity</span><span>resistivity</span><span>conductivity</span></div>
        <div><span>L01</span><span>high</span><span>low</span><span>high</span></div>
        <div><span>L02</span><span>mid</span><span>mid</span><span>missing</span></div>
      </div>
      <div class="conflict-zone">striped conflict target, not clean fused geology</div>
      <div class="model-stack" style="margin-top:0.45rem;">
        <div class="model-block main">LightGBM method-conflict ranker</div>
        <div class="model-block">GP method-specific uncertainty</div>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Validation and review target</h4>
      <div class="mini-table">
        <div><b>training unit</b><span>line interval / intersection</span></div>
        <div><b>split</b><span>leave-line-out validation</span></div>
        <div><b>output</b><span>review target, not final unit</span></div>
      </div>
      <div class="abstain-bin">possible unit -> field review queue</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_regional_transfer_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Spatial", "nearby train/test cells trigger spatial leakage warning."),
            _gate_box_html("Boundary", "biased split boundary invalidates score."),
            _gate_box_html("Variables", "hidden variable mismatch checked before transfer claim."),
            _gate_box_html("Coordinates", "coordinate memorization is blocked or flagged."),
        ]
    )
    residual_points = "".join(
        f"<span class='{cls}'></span>"
        for cls in ["ok", "hot", "cold", "ok", "hot", "ok", "cold", "ok"]
    )
    body_html = f"""
<div class="rich-diagram moho-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Training region and features</h4>
      <div class="region-transfer">
        <div class="region-card"><b>Australia training</b>Moho target + gravity/topography/crustal features</div>
        <div class="rich-arrow"></div>
        <div class="region-card"><b>USA test region</b>sealed transfer geography</div>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["gravity anomaly", "topography", "crustal proxy", "region id"], "source")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Model ladder and transfer bridge</h4>
      <div class="model-stack">
        <div class="model-block">Ridge / GAM reference model</div>
        <div class="model-block main">LightGBM / XGBoost Moho regressor</div>
        <div class="model-block">ANN challenger after transfer design is credible</div>
      </div>
      <div class="chronology-strip">
        <span>train region</span><span class="lock">transfer bridge</span><span>held-out region</span>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["leave-region-out", "Australia-to-USA transfer", "coordinate memorization"], "target")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Residual map as the main output</h4>
      <div class="residual-map">{residual_points}</div>
      <div class="mini-table" style="margin-top:0.45rem;">
        <div><b>target</b><span>Moho depth</span></div>
        <div><b>metrics</b><span>RMSE, MAE, R2, residual bias</span></div>
        <div><b>output</b><span>failure zones + transfer score</span></div>
      </div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_ambient_noise_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Signal", "weak correlation is QC, not subsurface change."),
            _gate_box_html("Season", "seasonal noise gets a calendar flag."),
            _gate_box_html("Metadata", "station metadata error blocks alert."),
            _gate_box_html("Instrument", "instrument change pauses anomaly interpretation."),
        ]
    )
    body_html = f"""
<div class="rich-diagram ambient-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Continuous records to station pairs</h4>
      <div class="station-network">
        <span class="station-node" style="left:14%;top:26%;"></span>
        <span class="station-node" style="left:66%;top:22%;"></span>
        <span class="station-node" style="left:38%;top:68%;"></span>
        <span class="station-arc" style="left:22%;top:32%;transform:rotate(-7deg);"></span>
        <span class="station-arc" style="left:42%;top:55%;transform:rotate(-34deg);border-color:#d97706;"></span>
      </div>
      <div class="diagram-chip-row">
        {_diagram_chip_html(["continuous station records", "windows", "preprocessing", "station-pair CCF"], "source")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Stable stack and anomaly models</h4>
      <div class="ccf-stack">
        <div class="ccf-line weak"></div>
        <div class="ccf-line stable"></div>
        <div class="ccf-line stable"></div>
        <div class="ccf-line weak"></div>
      </div>
      <div class="agreement-zone">stable stack: repeatable station-pair CCF brightens</div>
      <div class="model-stack" style="margin-top:0.55rem;">
        <div class="model-block main">LightGBM CCF-quality classifier</div>
        <div class="model-block">Isolation Forest anomaly triage</div>
        <div class="model-block">SeisLM-style embedding challenger</div>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["stable CCF", "stack count", "change metric"], "target")}
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Freshness and alert review</h4>
      <div class="drift-gauge">
        <div class="gauge-track"><div class="gauge-fill"></div></div>
        <div class="diagram-chip-row" style="margin-top:0.42rem;">
          {_diagram_chip_html(["freshness check", "seasonal flag", "human alert review"], "review")}
        </div>
      </div>
      <div class="abstain-bin">reviewed monitoring alert with provenance</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_app_risk_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Future", "shift-before-rolling blocks current row leakage."),
            _gate_box_html("Refresh", "stale refresh timestamp triggers fallback path."),
            _gate_box_html("Baseline", "no persistence baseline means challenger cannot claim value."),
            _gate_box_html("Claim", "claim-language gate blocks investment overclaim."),
        ]
    )
    body_html = f"""
<div class="rich-diagram app-risk-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Saved data and past-only features</h4>
      <div class="mini-table">
        <div><b>source</b><span>saved ticker data</span></div>
        <div><b>freshness</b><span>refresh time</span></div>
        <div><b>feature rule</b><span>shift(1) before rolling</span></div>
      </div>
      <div class="diagram-chip-row" style="margin-top:0.45rem;">
        {_diagram_chip_html(["past-only feature window", "ticker universe", "stale-data flag"], "source")}
      </div>
    </div>
    <div class="leakage-wall">future leakage gate</div>
    <div class="rich-stage">
      <h4>Walk-forward model ladder</h4>
      <div class="walk-forward">
        <div class="walk-row"><span class="train">train past</span><span class="test">test future</span><span class="gate">gate</span></div>
        <div class="walk-row"><span class="train">train past + 1</span><span class="test">test next</span><span class="gate">gate</span></div>
      </div>
      <div class="model-stack" style="margin-top:0.55rem;">
        <div class="model-block">persistence / moving-average baseline</div>
        <div class="model-block main">ElasticNet / LightGBM challenger</div>
      </div>
      <div class="drift-gauge" style="margin-top:0.45rem;">
        <div class="gauge-track"><div class="gauge-fill"></div></div>
        <div class="diagram-chip-row" style="margin-top:0.42rem;">
          {_diagram_chip_html(["PSI drift", "KS drift", "segment monitoring"], "target")}
        </div>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Dashboard output control</h4>
      <div class="model-stack">
        <div class="model-block">fallback model when drift or staleness fails</div>
        <div class="model-block main">calibrated score only after walk-forward validation</div>
      </div>
      <div class="proxy-gate">claim-language gate: demo/research tool, not investment advice</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_sem_interpretation_diagram(manual: dict) -> None:
    gates = "".join(
        [
            _gate_box_html("Texture", "visible texture label cannot become proxy claim."),
            _gate_box_html("Scale", "missing scale blocks label confidence."),
            _gate_box_html("Origin", "detrital/authigenic interpretation needs extra evidence."),
            _gate_box_html("Literature", "proxy claim waits for expert and source support."),
        ]
    )
    body_html = f"""
<div class="rich-diagram sem-diagram">
  <div class="rich-stage-grid">
    <div class="rich-stage">
      <h4>Observation evidence</h4>
      <div class="sem-crop"><div class="scale-bar"></div></div>
      <div class="label-pins">
        <span>SEM crop</span><span>scale bar</span><span>sample metadata</span>
      </div>
      <div class="mini-table" style="margin-top:0.45rem;">
        <div><b>training unit</b><span>image crop</span></div>
        <div><b>split</b><span>sample-held-out</span></div>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Visible labels and model support</h4>
      <div class="diagram-chip-row">
        {_diagram_chip_html(["grain", "pore/fracture", "clay morphology", "mineral texture", "ambiguous crop"], "target")}
      </div>
      <div class="model-stack" style="margin-top:0.55rem;">
        <div class="model-block">linear SVM / logistic texture reference</div>
        <div class="model-block main">EfficientNet / ResNet patch classifier</div>
        <div class="model-block">U-Net / Mask R-CNN segmentation if masks exist</div>
        <div class="model-block">CLIP retrieval of similar expert-labeled examples</div>
      </div>
    </div>
    <div class="rich-arrow"></div>
    <div class="rich-stage">
      <h4>Interpretation gate</h4>
      <div class="mini-table">
        <div><b>visible label</b><span>observable texture</span></div>
        <div><b>interpretation label</b><span>detrital/authigenic, proxy</span></div>
        <div><b>support</b><span>expert correction + literature link</span></div>
      </div>
      <div class="proxy-gate">proxy claim gate blocks image-only climate or reservoir claims</div>
      <div class="abstain-bin">accepted observation or blocked interpretation</div>
    </div>
  </div>
  <div class="gate-strip">{gates}</div>
</div>
    """
    _render_rich_manual_shell(manual, body_html)


def render_manual_visual_architecture(topic: dict) -> None:
    manual = MANUAL_VISUAL_ARCHITECTURES.get(topic["slug"])
    if manual is None:
        return
    if render_priority_manual_visual_architecture(topic["slug"], manual):
        return
    source_items = "".join(
        f"<div class='manual-source-item'>{workflow_icon_svg(item, idx)}"
        f"<span>{escape(item)}</span></div>"
        for idx, item in enumerate(manual["source"], start=1)
    )
    flow_items = []
    for idx, item in enumerate(manual["flow"], start=1):
        gate_class = " gate" if any(
            token in item.lower()
            for token in ["validation", "score", "audit", "gate", "test", "review"]
        ) else ""
        flow_items.append(
            f"""
<div class="manual-flow-node{gate_class}">
  <div class="manual-node-icon">{workflow_icon_svg(item, idx)}</div>
  <strong>{escape(item)}</strong>
  <span>{escape(_manual_flow_caption(item))}</span>
</div>
            """
        )
    vocab_items = "".join(
        f"<span class='manual-vocab'>{escape(item)}</span>"
        for item in manual["vocab"]
    )
    gate_items = "".join(
        f"<div class='manual-gate-item'>{workflow_icon_svg(item, idx)}"
        f"<span>{escape(item)}</span></div>"
        for idx, item in enumerate(manual["gates"], start=1)
    )
    priority_class = (
        " priority"
        if topic["slug"] in {"north_slope", "ai_workflow", "thesis_graph"}
        else ""
    )
    st.markdown(
        f"""
<div class="manual-architecture{priority_class}">
  <div class="manual-head">
    <div>
      <div class="manual-kicker">Visual-first manual / {escape(manual["kicker"])}</div>
      <h3>{escape(manual["name"])}</h3>
    </div>
    <div class="manual-output"><strong>Honest output:</strong> {escape(manual["output"])}</div>
  </div>
  <div class="manual-board">
    <div class="manual-panel">
      <h4>Real source evidence</h4>
      <div class="manual-source-grid">{source_items}</div>
    </div>
    <div class="manual-panel">
      <h4>Architecture to build</h4>
      <div class="manual-model">{escape(manual["model"])}</div>
      <div class="manual-flow">{''.join(flow_items)}</div>
      <div class="manual-vocab-row">{vocab_items}</div>
    </div>
    <div class="manual-panel">
      <h4>Visible failure gates</h4>
      <div class="manual-gate-list">{gate_items}</div>
    </div>
  </div>
  <div class="manual-prompt"><strong>Execution instruction</strong>{escape(manual["prompt"])}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def _manual_flow_caption(value: str) -> str:
    lower_value = value.lower()
    if "qc" in lower_value or "g o" in lower_value:
        return "clean and block bad evidence"
    if "validation" in lower_value or "test" in lower_value or "score" in lower_value:
        return "prove it on held-out data"
    if "review" in lower_value or "audit" in lower_value:
        return "expert checkpoint stays visible"
    if "baseline" in lower_value or "reference" in lower_value:
        return "simple model before complexity"
    if "feature" in lower_value or "window" in lower_value:
        return "turn evidence into variables"
    if "classifier" in lower_value or "regressor" in lower_value or "ann" in lower_value:
        return "named model layer"
    if "gate" in lower_value:
        return "block unsafe claim"
    return "visual step in the workflow"


def render_ml_pipeline_contract(topic: dict) -> None:
    render_manual_visual_architecture(topic)
    render_ml_visual_diagram(topic)
    contract = ML_PIPELINE_CONTRACTS.get(topic["slug"])
    if contract is None:
        return

    def list_items(values: list[str]) -> str:
        return "".join(f"<li>{escape(value)}</li>" for value in values)

    def pipeline_cell(title: str, values: list[str]) -> str:
        return (
            "<div class=\"pipeline-cell\">"
            f"<strong>{escape(title)}</strong>"
            f"<ul>{list_items(values)}</ul>"
            "</div>"
        )

    source_context = ML_PIPELINE_SOURCE_CONTEXT.get(topic["slug"], {})
    model_detail = ML_MODEL_DETAIL_DIAGRAMS.get(topic["slug"])
    extra_cells = ""
    if model_detail is not None:
        extra_cells += pipeline_cell(
            "Named Models",
            [
                model_detail["reference"]["name"],
                model_detail["main"]["name"],
                model_detail["challenger"]["name"],
            ],
        )
        extra_cells += pipeline_cell("Model Metrics", model_detail["metrics"])
        extra_cells += pipeline_cell(
            "Split And Gate",
            [model_detail["validation"], model_detail["gate"]],
        )
    if source_context.get("keywords"):
        extra_cells += pipeline_cell("ML Source Keywords", source_context["keywords"])
    if source_context.get("sector_advance"):
        extra_cells += pipeline_cell("Sector Advance", source_context["sector_advance"])

    with st.expander("Detailed ML implementation notes"):
        st.markdown(
            f"""
<div class="pipeline-contract">
  <h3>{escape(contract["title"])}</h3>
  <p>{escape(contract["summary"])}</p>
  <div class="pipeline-grid">
    {pipeline_cell("Feature Set", contract["features"])}
    {pipeline_cell("Pipeline Changes", contract["pipeline"])}
    {pipeline_cell("Validation Gates", contract["validation"])}
    {pipeline_cell("Failure Modes", contract["failure_modes"])}
    {extra_cells}
  </div>
</div>
        """,
            unsafe_allow_html=True,
        )


def render_topic_signal(topic: dict, card: bool = False) -> str:
    if card:
        visual_path_text = CARD_VISUALS.get(topic["slug"]) or TOPIC_VISUALS.get(topic["slug"])
    else:
        visual_path_text = TOPIC_VISUALS.get(topic["slug"])
        if not visual_path_text:
            visual_path_text = CARD_VISUALS.get(topic["slug"])
    if visual_path_text:
        visual_path = project_asset(visual_path_text)
        if visual_path.exists():
            data_uri = asset_data_uri(visual_path, max_bytes=900_000 if card else None)
            if data_uri is None:
                data_uri = ""
            proof_html = ""
            if card:
                proof_path_text = CARD_VISUALS.get(
                    topic["slug"],
                    topic.get("hero", ""),
                )
                if proof_path_text == visual_path_text:
                    proof_path_text = topic.get("hero", "") or TOPIC_VISUALS.get(
                        topic["slug"],
                        "",
                    )
                proof_path = project_asset(proof_path_text)
                if proof_path.exists() and proof_path != visual_path:
                    proof_uri = asset_data_uri(proof_path, max_bytes=450_000)
                    if proof_uri is not None:
                        proof_label = (
                            "AI SKETCH"
                            if proof_path_text == TOPIC_VISUALS.get(topic["slug"])
                            else "REAL PROOF"
                        )
                        proof_html = (
                            "<div class='topic-proof-inset'>"
                            f"<img src='{proof_uri}' "
                            f"alt='Real project evidence for {escape(topic['title'])}'>"
                            f"<span>{proof_label}</span></div>"
                        )
                    else:
                        proof_html = (
                            "<div class='topic-proof-inset text-only'>"
                            f"{workflow_icon_svg(topic['title'], 0)}"
                            "<span>AI SKETCH</span></div>"
                        )
            if data_uri:
                keyword_html = ""
                if card:
                    frame = TOPIC_FRAMES.get(topic["slug"], {})
                    pattern = frame.get("pattern", ["input", "AI", "output", "review"])
                    chips = "".join(f"<span>{escape(term)}</span>" for term in pattern[:4])
                    keyword_html = f"<div class='topic-card-keywords'>{chips}</div>"
                visual_html = (
                    f"<img src='{data_uri}' "
                    f"alt='{escape(topic['title'])} workflow poster'>"
                    f"{keyword_html}"
                )
            else:
                frame = TOPIC_FRAMES.get(topic["slug"], {})
                pattern = frame.get("pattern", ["input", "AI", "output", "review"])
                chips = "".join(f"<span>{escape(term)}</span>" for term in pattern)
                visual_html = f"<div class='topic-pattern fallback-pattern'>{chips}</div>"
            visual_class = "card-visual" if card else "topic-room-visual"
            return (
                f"<div class='topic-poster topic-poster-composite {visual_class}'>"
                f"{visual_html}{proof_html}</div>"
            )
    frame = TOPIC_FRAMES.get(topic["slug"], {})
    pattern = frame.get("pattern", ["input", "AI", "output", "review"])
    chips = "".join(f"<span>{escape(term)}</span>" for term in pattern)
    return f"""
<div class="topic-signal">
  <div class="topic-pattern">{chips}</div>
</div>
    """


def project_status_label(status_row: pd.Series | None) -> tuple[str, str]:
    if status_row is None:
        return "Evidence assembled", "evidence"
    if str(status_row.get("interactive", "")).lower() == "complete":
        return "Working interactive", ""
    if str(status_row.get("published", "")).lower() == "partial":
        return "Published evidence", "evidence"
    return "Prototype", "prototype"


def render_think_card(
    topic: dict,
    status_row: pd.Series | None = None,
    compact: bool = False,
) -> str:
    frame = TOPIC_FRAMES.get(topic["slug"], {})
    question = frame.get("question", topic["question"])
    url = topic_url(topic["slug"]).replace("&", "&amp;")
    raise_prompt = TOPIC_AI_LEVERS.get(
        topic["slug"],
        frame.get("raise", "AI use: evidence becomes a reviewable workflow."),
    )
    return f"""
<a class="think-card-link" href="{url}" aria-label="Open {escape(topic['title'])}">
<div class="think-card">
  <p class="think-question">{escape(question)}</p>
  {render_topic_signal(topic, card=True)}
  <p class="think-title">{escape(topic['title'])}</p>
  <div class="think-raise">{escape(raise_prompt)}</div>
</div>
</a>
    """


def render_workflow_blueprint(topic: dict) -> None:
    blueprint = WORKFLOW_BLUEPRINTS.get(topic["slug"])
    if blueprint is None:
        return
    step_html = []
    for idx, (label, detail) in enumerate(blueprint["steps"], start=1):
        step_html.append(
            f"""
<div class="workflow-node">
  <div class="workflow-icon">{workflow_icon_svg(label, idx)}</div>
  <strong>{escape(label)}</strong>
  <span>{escape(detail)}</span>
</div>
            """
        )
    st.markdown(
        f"""
<div class="workflow-tree">
  <h3>{escape(blueprint["title"])}</h3>
  <div class="workflow-root">Project evidence + domain question</div>
  <div class="workflow-branches">{''.join(step_html)}</div>
  <div class="workflow-result"><strong>Product direction:</strong> {escape(blueprint["outcome"])}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_current_future_board(topic: dict, roadmap: pd.Series | None) -> None:
    evidence = AI_WORKFLOW_EVIDENCE.get(topic["slug"], {})
    current_steps = evidence.get("chips", topic["proof"][:3])
    if roadmap is not None:
        future_model = str(roadmap["model_or_method"]).split(";")[0].strip()
        future_output = str(roadmap["output"]).split(";")[0].strip()
    else:
        future_model = topic["future_ai"]
        future_output = topic["why_it_matters"]
    current_html = "".join(
        f"<div class='state-step'>{workflow_icon_svg(value, index)}"
        f"<span>{escape(value)}</span></div>"
        for index, value in enumerate(current_steps, start=1)
    )
    future_steps = [future_model, future_output]
    future_html = "".join(
        f"<div class='state-step future'>{workflow_icon_svg(value, index + 4)}"
        f"<span>{escape(value)}</span></div>"
        for index, value in enumerate(future_steps, start=1)
    )
    st.markdown(
        f"""
<div class="current-future-board">
  <div class="state-side current">
    <div class="state-kicker">USED NOW</div>
    <div class="state-flow">{current_html}</div>
  </div>
  <div class="guidance-gate">
    <div>{workflow_icon_svg("review", 0)}</div>
    <strong>DOMAIN<br>GUIDANCE</strong>
    <span>check · revise · approve</span>
  </div>
  <div class="state-side future">
    <div class="state-kicker">COULD BECOME</div>
    <div class="state-flow">{future_html}</div>
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_project_visual_stage(topic: dict) -> bool:
    slug = topic["slug"]
    if slug == "ai_workflow":
        qgis_path = project_asset(
            "assets/gmail_updates/2026-06-08/Screenshot 2026-05-17 233055.png"
        )
        qgis_uri = asset_data_uri(qgis_path, max_bytes=900_000)
        if qgis_uri is None:
            return False
        st.markdown(
            f"""
<div class="project-stage agent-stage" style="background-image:url('{qgis_uri}')">
  <div class="record-dot">RECORDING</div>
  <div class="stage-label" style="left:3%;top:5%">PROMPT + RUBRIC</div>
  <div class="action-marker" style="left:17%;top:31%">1</div>
  <div class="action-marker" style="left:39%;top:22%">2</div>
  <div class="action-marker" style="left:62%;top:39%">3</div>
  <div class="stage-label" style="right:5%;top:18%">SCREEN-RECORDED VIRTUAL ENV</div>
  <div class="stage-label failure" style="right:5%;top:31%">HUMAN REVIEW GATE</div>
  <div class="agent-lanes">
    <div class="agent-lane">HUMAN WORK<br>PROMPT - SCREEN RECORD</div>
    <div class="rubric-gate">SUPERVISED<br>ML LABELS</div>
    <div class="agent-lane">FUTURE AGENT<br>EXECUTES SOFTWARE</div>
  </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        return True

    if slug == "processing_earthquake":
        return render_fast_motion_video(
            USGS_GLOBE_VIDEO_PATH,
            "USGS 3D globe video",
            "Drive upload embedded locally and played faster so the globe motion reads immediately in the portfolio.",
            playback_rate=1.85,
        )

    if slug == "thesis_graph":
        drawing_uri = asset_data_uri(
            project_asset("assets/project_visuals/ree_bayan_obo_main.png"),
            max_bytes=500_000,
        )
        graph_uri = asset_data_uri(
            project_asset("assets/project_visuals/thesis_host_context_clean.png"),
            max_bytes=500_000,
        )
        if drawing_uri is None or graph_uri is None:
            return False
        st.markdown(
            f"""
<div class="project-stage" style="background:#eef2f4;padding:1rem;min-height:510px;">
  <div style="display:grid;grid-template-columns:1fr 150px 1fr;gap:0.9rem;align-items:center;">
    <div style="display:grid;gap:0.7rem;">
      <div class="chain-node" style="min-height:92px;"><strong>TABLES / CSVs</strong><span>many inputs and variables</span></div>
      <div class="chain-node" style="min-height:92px;"><strong>QUESTIONS / PROJECTS</strong><span>related variables and research goals</span></div>
      <div class="chain-node human" style="min-height:120px;"><img src="{drawing_uri}" alt="Bayan Obo drawing"><strong>DRAWINGS / IDEAS</strong><span>shapes, colors, polygons</span></div>
    </div>
    <div style="height:150px;border-radius:50%;background:#0b1f3a;color:#ffffff;display:grid;place-items:center;text-align:center;font-weight:900;border:6px solid #7ed6df;">
      <div>AI / ML<br><span style="font-size:0.78rem;color:#bfeff3;">sort + connect</span></div>
    </div>
    <div style="display:grid;gap:0.7rem;">
      <div class="chain-node" style="min-height:92px;"><strong>KNOWLEDGE GRAPH</strong><span>variables connect with evidence</span></div>
      <div class="chain-node" style="min-height:92px;"><strong>ML ARCHITECTURE</strong><span>inputs, model, validation gates</span></div>
      <div class="chain-node" style="min-height:120px;"><img src="{graph_uri}" alt="Graph export"><strong>ADOBE / GEPHI VISUAL</strong><span>architecture people can inspect</span></div>
    </div>
  </div>
  <div class="output-branches" style="padding:1rem 0 0;">
    <div>SOURCE-BACKED EDGES</div>
    <div class="question">AI-SUGGESTED LINKS<br>review first</div>
    <div class="question">HUMAN INTERPRETATION<br>kept visible</div>
  </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        return True

    if slug == "moho_ml":
        st.markdown(
            """
<div class="project-stage transfer-stage" style="grid-template-columns:1.15fr 1.3fr 1fr;">
  <div class="region-panel">
    <h4>NORTH SLOPE INPUTS</h4>
    <div class="property-chips">
      <span>DEPTH RAW</span><span>GR / DENSITY</span><span>RESISTIVITY</span>
      <span>VP / VS</span><span>CORE + QC</span>
    </div>
    <div class="small-note" style="margin-top:0.7rem;">Measured inputs, derived features, QC flags, and targets stay separate.</div>
  </div>
  <div>
    <div class="model-gate">BASELINE<br>FIRST</div>
    <div class="model-gate" style="margin-top:0.55rem;">CLASSIFY<br>OCCURRENCE</div>
    <div class="model-gate" style="margin-top:0.55rem;">REGRESS<br>SATURATION</div>
    <div class="leakage-gate">LEAKAGE GATE<br>NO TARGETS IN INPUTS</div>
  </div>
  <div class="region-panel">
    <h4>VALIDATION</h4>
    <div class="sample-field"></div>
    <div class="residual-dots"><i></i><i></i><i></i><i></i><i></i></div>
    <div class="small-note">Hold out complete wells before trusting model scores.</div>
  </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        return True

    if slug == "stock_workflow":
        stock_uri = asset_data_uri(
            project_asset("assets/project_visuals/stock_all_tickers_chart.svg"),
            max_bytes=600_000,
        )
        if stock_uri is None:
            return False
        st.markdown(
            f"""
<div class="project-stage pipeline-stage" style="grid-template-columns:1.35fr repeat(4,minmax(0,1fr));">
  <div class="pipeline-node">
    <div>
      <img src="{stock_uri}" alt="Current stock dashboard chart" style="width:100%;height:94px;object-fit:contain;margin-bottom:0.45rem;">
      <strong>CURRENT APP VISUAL</strong>
    </div>
  </div>
  <div class="pipeline-node">{workflow_icon_svg("Codex code", 2)}<strong>CODEX</strong></div>
  <div class="pipeline-node">{workflow_icon_svg("GitHub branches", 3)}<strong>GITHUB</strong></div>
  <div class="pipeline-node">{workflow_icon_svg("Streamlit dashboard", 4)}<strong>APP</strong></div>
  <div class="pipeline-node blocked">{workflow_icon_svg("review", 5)}<strong>UNSEEN TEST?</strong><span>reused data is blocked</span></div>
</div>
            """,
            unsafe_allow_html=True,
        )
        return True

    if slug == "rock_classification":
        map_uri = asset_data_uri(
            project_asset(
                "assets/project_visuals/rock_classification_slides/"
                "rock_raster_classification_map.png"
            ),
            max_bytes=700_000,
        )
        if map_uri is None:
            return False
        st.markdown(
            f"""
<div class="project-stage property-stage">
  <div class="property-inputs">
    <strong>SATELLITE / GIS VARIABLES</strong>
    <div class="property-chips">
      <span>BANDS</span><span>DEM</span><span>TEXTURE</span>
      <span>SLOPE</span><span>STRUCTURE</span>
    </div>
  </div>
  <div class="range-gate">FEATURE<br>GATES<br>down<br>GRAY = UNCERTAIN</div>
  <div class="map-output">
    <strong>REVIEWED ROCK-TYPE MAP</strong>
    <img src="{map_uri}" alt="Real raster classification map">
  </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        return True
    return False


def render_discussion_prompts(topic: dict) -> None:
    prompts = DISCUSSION_PROMPTS.get(topic["slug"], [])
    if not prompts:
        return
    st.subheader("Discussion prompts")
    st.markdown(
        "<div class='prompt-grid'>"
        + "".join(f"<div class='prompt-card'>{escape(prompt)}</div>" for prompt in prompts)
        + "</div>",
        unsafe_allow_html=True,
    )


def render_evidence_leads(topic: dict) -> None:
    leads = EVIDENCE_LEADS.get(topic["slug"], [])
    if not leads:
        return
    chips = []
    for label, path_text in leads:
        is_url = path_text.startswith(("http://", "https://"))
        path = Path(path_text)
        status = "deck" if is_url else ("found" if path.exists() else "missing")
        display_name = label if is_url else path.name
        chips.append(
            f"""
<a class="source-chip" href="{escape(source_href(path_text))}" target="_blank" rel="noopener noreferrer">
  <strong>{escape(label)}</strong>
  <span>{escape(status)} | {escape(display_name)}</span>
</a>
            """
        )
    st.subheader("Evidence leads")
    st.markdown(
        f"<div class='source-chip-grid'>{''.join(chips)}</div>",
        unsafe_allow_html=True,
    )


def render_processing_sketch_plan(topic: dict, compact: bool = False) -> None:
    plan = PROCESSING_SKETCH_PLANS.get(topic["slug"])
    if plan is None:
        return
    motion = "".join(
        f"<span class='motion-pill'>{escape(item)}</span>"
        for item in plan["motion"]
    )
    heading = "Processing abstract sketch" if not compact else topic["title"]
    st.markdown(
        f"""
<div class="sketch-card">
  <h3>{escape(heading)} <span class="small-note">/ {escape(plan["sketch"])}</span></h3>
  <div class="sketch-body">
    <div>
      <div class="sketch-panel">
        <strong>Visual concept</strong>
        <span>{escape(plan["visual"])}</span>
      </div>
      <div class="motion-strip">{motion}</div>
      <div class="sketch-panel">
        <strong>Processing build note</strong>
        <span>{escape(plan["processing_notes"])}</span>
      </div>
    </div>
    <div>
      <div class="sketch-panel">
        <strong>Conclusion it supports</strong>
        <span>{escape(plan["conclusion"])}</span>
      </div>
      <div class="sketch-panel" style="margin-top:0.55rem;">
        <strong>Future ML case</strong>
        <span>{escape(plan["future_ml"])}</span>
      </div>
    </div>
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_visual_wall(title: str, visual_rows: pd.DataFrame, limit: int = 4) -> None:
    if visual_rows.empty:
        return
    st.subheader(title)
    wall_cols = st.columns(2)
    for idx, visual in enumerate(visual_rows.head(limit).itertuples(index=False)):
        with wall_cols[idx % 2]:
            visual_path = project_asset(visual.asset_path)
            if visual_path.exists():
                st.image(str(visual_path), caption=visual.title, use_container_width=True)
            else:
                st.warning(f"Missing visual: {visual.title}")


@st.cache_data
def load_structural_surfaces() -> pd.DataFrame:
    return pd.read_parquet(
        MASTER_3D_PATH,
        columns=["x_3338", "y_3338", "lon", "lat", "depth_m", "surface_name"],
    )


@st.cache_data
def load_structural_context() -> pd.DataFrame:
    layers = pd.read_parquet(
        MASTER_2D_PATH,
        columns=[
            "layer_name",
            "feature_id",
            "vertex_order",
            "lon",
            "lat",
            "depth_m",
            "au_name",
        ],
    )
    return layers[
        layers["layer_name"].isin(["extent", "assessment_units", "wells"])
    ].copy()


def sample_structural_rows(df: pd.DataFrame, max_rows: int) -> pd.DataFrame:
    if len(df) <= max_rows:
        return df
    step = max(1, len(df) // max_rows)
    return df.iloc[::step].head(max_rows)


def grid_structural_surface(
    surface: pd.DataFrame,
    max_cells: int,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    stride = max(1, round((len(surface) / max_cells) ** 0.5))
    lon = surface.pivot(
        index="y_3338",
        columns="x_3338",
        values="lon",
    ).iloc[::stride, ::stride]
    lat = surface.pivot(
        index="y_3338",
        columns="x_3338",
        values="lat",
    ).iloc[::stride, ::stride]
    depth = surface.pivot(
        index="y_3338",
        columns="x_3338",
        values="depth_m",
    ).iloc[::stride, ::stride]
    return lon, lat, depth


def add_structural_context_line(
    figure: go.Figure,
    rows: pd.DataFrame,
    name: str,
    color: str,
    width: int,
    showlegend: bool = True,
) -> None:
    figure.add_trace(
        go.Scatter3d(
            x=rows["lon"],
            y=rows["lat"],
            z=[0] * len(rows),
            mode="lines",
            name=name,
            showlegend=showlegend,
            line={"color": color, "width": width},
            hovertemplate=(
                f"<b>{name}</b><br>Longitude: %{{x:.2f}}"
                "<br>Latitude: %{y:.2f}<extra></extra>"
            ),
        )
    )


def build_structural_figure(
    selected_surfaces: list[str],
    cells_per_surface: int,
    selected_overlays: list[str],
) -> go.Figure:
    surfaces = load_structural_surfaces()
    figure = go.Figure()

    for surface_name in selected_surfaces:
        surface = surfaces[surfaces["surface_name"] == surface_name]
        lon, lat, depth = grid_structural_surface(surface, cells_per_surface)
        metadata = SURFACE_CATALOG[surface_name]
        figure.add_trace(
            go.Surface(
                x=lon,
                y=lat,
                z=depth,
                name=metadata["label"],
                colorscale=[[0, metadata["color"]], [1, metadata["color"]]],
                opacity=0.72,
                showscale=False,
                showlegend=True,
                hovertemplate=(
                    f"<b>{metadata['label']}</b><br>"
                    "Longitude: %{x:.2f}<br>"
                    "Latitude: %{y:.2f}<br>"
                    "Depth: %{z:,.0f} m<extra></extra>"
                ),
            )
        )

    context = load_structural_context()
    if "North Slope study-area boundary" in selected_overlays:
        extent = context[context["layer_name"] == "extent"].sort_values(
            "vertex_order"
        )
        add_structural_context_line(
            figure,
            extent,
            "North Slope study-area boundary",
            "#111827",
            8,
        )

    if "Assessment-unit outlines" in selected_overlays:
        units = context[context["layer_name"] == "assessment_units"]
        for index, (_, rows) in enumerate(units.groupby("feature_id")):
            rows = sample_structural_rows(rows.sort_values("vertex_order"), 400)
            add_structural_context_line(
                figure,
                rows,
                "Assessment-unit outlines",
                "#f97316",
                4,
                showlegend=index == 0,
            )

    if "North Slope public wells" in selected_overlays:
        extent = context[context["layer_name"] == "extent"]
        wells = context[context["layer_name"] == "wells"].copy()
        wells = wells[
            wells["lon"].between(extent["lon"].min(), extent["lon"].max())
            & wells["lat"].between(extent["lat"].min(), extent["lat"].max())
        ]
        wells = sample_structural_rows(wells, 1400)
        figure.add_trace(
            go.Scatter3d(
                x=wells["lon"],
                y=wells["lat"],
                z=wells["depth_m"],
                mode="markers",
                name="North Slope public wells",
                marker={"size": 2.7, "color": "#111827", "opacity": 0.62},
                hovertemplate=(
                    "<b>Public well</b><br>Longitude: %{x:.2f}"
                    "<br>Latitude: %{y:.2f}<extra></extra>"
                ),
            )
        )

    figure.update_layout(
        height=680,
        margin={"l": 0, "r": 0, "t": 44, "b": 0},
        legend={"orientation": "h", "y": 1.04, "x": 0},
        scene={
            "xaxis_title": "Longitude",
            "yaxis_title": "Latitude",
            "zaxis_title": "Depth (m)",
            "zaxis": {"autorange": "reversed"},
            "aspectmode": "manual",
            "aspectratio": {"x": 1.8, "y": 1, "z": 0.55},
            "camera": {"eye": {"x": 1.55, "y": -1.75, "z": 1.05}},
        },
    )
    return figure


inventory = load_current_csv(INVENTORY_PATH)
drive_inventory = load_current_csv(DRIVE_INVENTORY_PATH)
notebook_inventory = load_current_csv(NOTEBOOK_INVENTORY_PATH)
case_studies = load_current_csv(CASE_STUDY_PATH)
project_visuals = load_current_csv(PROJECT_VISUALS_PATH)
linkedin_evidence = load_current_csv(LINKEDIN_EVIDENCE_PATH)
organized_folders = load_current_csv(ORGANIZED_FOLDERS_PATH)
ml_roadmap = load_current_csv(ML_ROADMAP_PATH)
ml_diagram_tracker = load_current_csv(ML_DIAGRAM_TRACKER_PATH)
project_status = load_current_csv(PROJECT_STATUS_PATH)
visual_audit = load_current_csv(VISUAL_AUDIT_PATH)
vision_board = load_current_csv(VISION_BOARD_PATH)
website_change_ideas = load_current_csv(WEBSITE_CHANGE_IDEAS_PATH)
drive_slide_sources = load_current_csv(DRIVE_SLIDE_SOURCES_PATH)
project_status_by_key = {
    row["project_key"]: row
    for _, row in project_status.iterrows()
}


PUBLIC_SECTIONS = [
    "Start",
    "Topics",
    "Interactives",
    "Visual Lab",
    "About",
    "Build Room",
]
PUBLIC_TO_INTERNAL = {
    "Start": "Overview",
    "Topics": "Think Tank Topics",
    "Interactives": "Structural Explorer",
    "Visual Lab": "Processing Visual Lab",
    "About": "Contact / Ideas",
}
BUILD_ROOM_SECTIONS = [
    "Vision Board",
    "System Map",
    "Evidence Library",
    "LinkedIn Evidence",
    "Notebook Explorer",
    "Code And Architecture",
    "Visual Gallery",
    "Visual Audit",
    "Update Inbox",
    "Build Plan",
    "Machine Learning Future",
    "Mobile View",
    "Case Studies",
]
ALL_INTERNAL_SECTIONS = list(PUBLIC_TO_INTERNAL.values()) + BUILD_ROOM_SECTIONS
PUBLIC_LABELS = {
    "Start": "Start · choose a question",
    "Topics": "Topics · evidence and future systems",
    "Interactives": "Interactives · working scientific tools",
    "Visual Lab": "Visual Lab · motion and Processing",
    "About": "About · share an idea or correction",
    "Build Room": "Build Room · sources, code, and review",
}
BUILD_ROOM_LABELS = {
    "Vision Board": "Vision Board / internal tracker",
    "System Map": "Architecture / System Map",
    "Evidence Library": "Sources and Evidence Library",
    "LinkedIn Evidence": "LinkedIn evidence",
    "Notebook Explorer": "Notebook Explorer",
    "Code And Architecture": "Code and architecture",
    "Visual Gallery": "Visual asset gallery",
    "Visual Audit": "Visual Audit",
    "Update Inbox": "Update Inbox",
    "Build Plan": "Build Plan",
    "Machine Learning Future": "ML research index",
    "Mobile View": "Mobile preview",
    "Case Studies": "Case-study inventory",
}
query_section = st.query_params.get("section", "Start")
if query_section == "Visual Contact Sheets":
    query_section = "Visual Gallery"
if query_section == "Project Rooms":
    query_section = "Think Tank Topics"
if query_section in PUBLIC_SECTIONS:
    query_public = query_section
    query_build = BUILD_ROOM_SECTIONS[0]
elif query_section in PUBLIC_TO_INTERNAL.values():
    query_public = next(
        public for public, internal in PUBLIC_TO_INTERNAL.items()
        if internal == query_section
    )
    query_build = BUILD_ROOM_SECTIONS[0]
elif query_section in BUILD_ROOM_SECTIONS:
    query_public = "Build Room"
    query_build = query_section
else:
    query_public = "Start"
    query_build = BUILD_ROOM_SECTIONS[0]


with st.sidebar:
    st.title("AI Think Tank")
    st.caption(f"Choose a room. Build {DEPLOY_BUILD_ID}")
    public_section = st.selectbox(
        "Public navigator",
        PUBLIC_SECTIONS,
        index=PUBLIC_SECTIONS.index(query_public),
        format_func=lambda item: PUBLIC_LABELS[item],
        key="public_section",
    )
    if public_section == "Build Room":
        section = st.selectbox(
            "Build Room tool",
            BUILD_ROOM_SECTIONS,
            index=BUILD_ROOM_SECTIONS.index(query_build),
            format_func=lambda item: BUILD_ROOM_LABELS[item],
            key="build_room_section",
        )
        st.caption("Behind the think tank: sources, code, audits, and backlog.")
    else:
        section = PUBLIC_TO_INTERNAL[public_section]
    st.divider()
    st.caption("Project claims separate current evidence, prototypes, and future ideas.")
    if DOWNLOAD_PACKAGE_PATH.exists():
        with DOWNLOAD_PACKAGE_PATH.open("rb") as package_file:
            st.download_button(
                "Download email package",
                package_file,
                file_name=DOWNLOAD_PACKAGE_PATH.name,
                mime="application/zip",
            )


if section == "Overview":
    st.markdown(
        """
<div class="portfolio-intro">
  <div class="portfolio-eyebrow">VISUAL AI THINK TANK</div>
  <h1>Pick a question. Let's talk.</h1>
  <p>Real project evidence anchors each idea. Domain guidance stays in the loop.</p>
</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-heading">
  <div class="section-heading-title">Discussion wall</div>
  <span>concept visual + real proof + open question</span>
</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        (
            "<div class='think-grid topic-wall'>"
            + "".join(
                render_think_card(
                    topic,
                    project_status_by_key.get(topic["project_key"]),
                )
                for topic in TOPIC_ROOMS
            )
            + "</div>"
        ),
        unsafe_allow_html=True,
    )
    render_public_system_legend()

    st.subheader("Explore the system")
    fast_cols = st.columns(5)
    fast_cols[0].link_button("Topics", "?section=Think%20Tank%20Topics")
    fast_cols[1].link_button("Structural Explorer", "?section=Structural%20Explorer")
    fast_cols[2].link_button("Visual Lab", "?section=Processing%20Visual%20Lab")
    fast_cols[3].link_button("Contact / Ideas", "?section=Contact%20%2F%20Ideas")
    fast_cols[4].link_button("Phone View", "?section=Mobile%20View")

    with st.expander("About this portfolio"):
        st.write(
            "These are evolving research, school, coding, and creative projects. "
            "The portfolio keeps the evidence visible while separating working prototypes "
            "from ideas that still need expert validation."
        )


elif section == "Vision Board":
    st.markdown(
        """
<div class="talk-hero">
  <div class="talk-kicker">Project direction</div>
  <h2>Vision board: what the portfolio is becoming</h2>
  <p>
    A living view of the immediate build, the next prototypes, and the longer-term
    platform direction. Each item links ambition to evidence and a concrete next move.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("New source updates to apply")
    st.caption(
        "Pulled from the self-sent Gmail attachments on June 10, 2026: website brand/design workflow and ML project reference notes."
    )
    render_gmail_source_update(compact=False)

    status_counts = vision_board["status"].value_counts()
    change_status_counts = website_change_ideas["status"].value_counts()
    vision_metrics = st.columns(4)
    vision_metrics[0].metric("Active now", int((vision_board["horizon"] == "Now").sum()))
    vision_metrics[1].metric("Next up", int((vision_board["horizon"] == "Next").sum()))
    vision_metrics[2].metric("In progress", int(status_counts.get("in_progress", 0)))
    unfinished_changes = website_change_ideas[
        ~website_change_ideas["status"].isin(["done", "complete"])
    ].copy()
    vision_metrics[3].metric(
        "Website changes left",
        int(len(unfinished_changes)),
        f"{int(change_status_counts.get('done', 0))} done",
    )

    if not unfinished_changes.empty:
        st.warning(
            "Not all vision-board changes are complete yet. The table below is the active implementation queue."
        )
        unfinished_priority_rank = {"P0": 0, "P1": 1, "P2": 2}
        unfinished_changes = unfinished_changes.assign(
            priority_rank=unfinished_changes["priority"].map(unfinished_priority_rank).fillna(9)
        ).sort_values(["priority_rank", "section", "change_id"])
        st.dataframe(
            unfinished_changes[
                ["priority", "status", "section", "change_id", "minimal_copy"]
            ].head(12),
            hide_index=True,
            use_container_width=True,
        )

    if not drive_slide_sources.empty:
        st.subheader("Drive slide and document sources now connected")
        st.caption(
            "These are the Drive decks/docs I found for new topic material, screenshots, "
            "and replacements for generic reused visuals. Open the Drive link for the "
            "native PowerPoint/Slides/Doc source; the North Slope source library also "
            "exists locally in the repo."
        )
        source_priority = {
            "active source": 0,
            "local source library": 1,
            "source candidate": 2,
        }
        source_cards_df = drive_slide_sources.assign(
            source_rank=drive_slide_sources["status"].map(source_priority).fillna(9)
        ).sort_values(["source_rank", "project_key", "deck_title"])
        source_cards = []
        for source in source_cards_df.head(12).itertuples(index=False):
            local_copy = str(source.local_copy)
            local_line = (
                f"<p><strong>Local:</strong> {escape(local_copy)}</p>"
                if local_copy and local_copy.lower() != "nan"
                else ""
            )
            source_cards.append(
                f"""
<div class="drive-source-card">
  <div class="source-status">{escape(str(source.status))}</div>
  <h3>{escape(str(source.deck_title))}</h3>
  <p><strong>Project:</strong> {escape(str(source.project_key))}</p>
  <p><strong>Use for:</strong> {escape(str(source.use_for))}</p>
  {local_line}
  <p>{escape(str(source.notes))}</p>
  <a href="{escape(str(source.drive_url))}" target="_blank">Open source</a>
</div>
                """
            )
        st.markdown(
            "<div class='drive-source-grid'>" + "".join(source_cards) + "</div>",
            unsafe_allow_html=True,
        )
        st.download_button(
            "Download Drive source inventory CSV",
            drive_slide_sources.to_csv(index=False),
            file_name=DRIVE_SLIDE_SOURCES_PATH.name,
            mime="text/csv",
        )

    vision_filters = st.columns([1, 1, 2])
    selected_horizon = vision_filters[0].selectbox(
        "Horizon",
        ["All", "Now", "Next", "Later"],
    )
    selected_vision_project = vision_filters[1].selectbox(
        "Project",
        ["All"] + sorted(vision_board["project_key"].dropna().unique().tolist()),
    )
    vision_search = vision_filters[2].text_input(
        "Search the vision",
        placeholder="interaction, PowerPoint, validation...",
    )

    filtered_vision = vision_board.copy()
    if selected_horizon != "All":
        filtered_vision = filtered_vision[
            filtered_vision["horizon"] == selected_horizon
        ]
    if selected_vision_project != "All":
        filtered_vision = filtered_vision[
            filtered_vision["project_key"] == selected_vision_project
        ]
    if vision_search:
        vision_haystack = (
            filtered_vision["focus"].fillna("")
            + " "
            + filtered_vision["outcome"].fillna("")
            + " "
            + filtered_vision["evidence"].fillna("")
            + " "
            + filtered_vision["next_action"].fillna("")
        ).str.lower()
        filtered_vision = filtered_vision[
            vision_haystack.str.contains(vision_search.lower(), regex=False)
        ]

    horizon_order = {"Now": 0, "Next": 1, "Later": 2}
    priority_order = {"P0": 0, "P1": 1, "P2": 2}
    filtered_vision = filtered_vision.assign(
        horizon_order=filtered_vision["horizon"].map(horizon_order).fillna(9),
        priority_order=filtered_vision["priority"].map(priority_order).fillna(9),
    ).sort_values(["horizon_order", "priority_order", "focus"])

    vision_cards = []
    for item in filtered_vision.itertuples(index=False):
        horizon_class = str(item.horizon).lower()
        vision_cards.append(
            f"""
<div class="vision-card {escape(horizon_class)}">
  <div class="horizon">{escape(str(item.horizon))}</div>
  <h3>{escape(str(item.focus))}</h3>
  <p>{escape(str(item.outcome))}</p>
  <p><strong>Evidence:</strong> {escape(str(item.evidence))}</p>
  <p class="vision-next">{escape(str(item.next_action))}</p>
  <div class="vision-meta">
    <span>{escape(str(item.priority))}</span>
    <span>{escape(str(item.status).replace("_", " "))}</span>
    <span>{escape(str(item.project_key))}</span>
  </div>
</div>
            """
        )
    if vision_cards:
        st.markdown(
            "<div class='vision-board'>" + "".join(vision_cards) + "</div>",
            unsafe_allow_html=True,
        )
    else:
        st.info("No vision items match the current filters.")

    st.subheader("Priority delivery queue")
    vision_queue = vision_board[
        vision_board["status"].isin(["in_progress", "planned"])
    ].copy()
    vision_queue["priority_order"] = vision_queue["priority"].map(priority_order).fillna(9)
    vision_queue["horizon_order"] = vision_queue["horizon"].map(horizon_order).fillna(9)
    vision_queue = vision_queue.sort_values(
        ["priority_order", "horizon_order", "focus"]
    )
    st.dataframe(
        vision_queue[
            ["priority", "horizon", "focus", "status", "next_action", "project_key"]
        ],
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Page-specific visual change plan")
    st.caption(
        "These concepts come from the 63-question interview and 55 follow-up "
        "answers. Each one records what the section looks like now, what should "
        "replace it, and why."
    )
    change_filters = st.columns(3)
    change_section = change_filters[0].selectbox(
        "Website section",
        ["All"] + sorted(website_change_ideas["section"].unique().tolist()),
        key="vision_change_section",
    )
    change_priority = change_filters[1].selectbox(
        "Change priority",
        ["All", "P0", "P1", "P2"],
        key="vision_change_priority",
    )
    change_status = change_filters[2].selectbox(
        "Change status",
        ["All"] + sorted(website_change_ideas["status"].unique().tolist()),
        key="vision_change_status",
    )
    filtered_changes = website_change_ideas.copy()
    if change_section != "All":
        filtered_changes = filtered_changes[
            filtered_changes["section"] == change_section
        ]
    if change_priority != "All":
        filtered_changes = filtered_changes[
            filtered_changes["priority"] == change_priority
        ]
    if change_status != "All":
        filtered_changes = filtered_changes[
            filtered_changes["status"] == change_status
        ]

    priority_rank = {"P0": 0, "P1": 1, "P2": 2}
    filtered_changes = filtered_changes.assign(
        priority_rank=filtered_changes["priority"].map(priority_rank).fillna(9)
    ).sort_values(["priority_rank", "section", "change_id"])
    change_cols = st.columns(2)
    for index, change in enumerate(filtered_changes.itertuples(index=False)):
        with change_cols[index % 2]:
            with st.container(border=True):
                st.caption(
                    f"{change.priority} · {change.section} · "
                    f"{str(change.status).replace('_', ' ')}"
                )
                st.markdown(f"**{str(change.change_id).replace('_', ' ').title()}**")
                st.markdown("**Current**")
                st.write(change.current_state)
                st.markdown("**Proposed visual**")
                st.write(change.proposed_visual)
                st.info(change.minimal_copy)
                st.markdown("**Why this change**")
                st.caption(change.why)

    st.download_button(
        "Download vision board CSV",
        vision_board.to_csv(index=False),
        file_name=VISION_BOARD_PATH.name,
        mime="text/csv",
    )
    st.download_button(
        "Download website change plan",
        website_change_ideas.to_csv(index=False),
        file_name=WEBSITE_CHANGE_IDEAS_PATH.name,
        mime="text/csv",
    )
    st.subheader("Questions for the next review")
    review_cols = st.columns(2)
    for index, question in enumerate(NEXT_REVIEW_QUESTIONS):
        with review_cols[index % 2]:
            st.info(question)
    st.link_button("Send a new update", "?section=Update%20Inbox")


elif section == "System Map":
    mobile_system_map = st.query_params.get("mobile", "0") == "1"
    st.markdown(
        """
<div class="talk-hero">
  <div class="talk-kicker">Architecture and delivery</div>
  <h2>How evidence becomes a reviewed system</h2>
  <p>
    This map separates the research workflow, the software that runs the portfolio,
    and the actual delivery progress of each project.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )

    mode = st.radio(
        "Map view",
        ["Research Flow", "Application Architecture", "Delivery Progress"],
        horizontal=True,
    )
    if mobile_system_map:
        render_mobile_system_map(mode, project_status)
        st.link_button("Open animated desktop map", "?section=System%20Map")
    else:
        render_system_map(mode, project_status)
        st.link_button(
            "Open phone-friendly map",
            "?section=System%20Map&mobile=1",
        )

    if mode == "Research Flow":
        st.caption(
            "Orange particles represent evidence moving through the workflow. "
            "The return path from expert validation makes revision part of the architecture."
        )
    elif mode == "Application Architecture":
        st.caption(
            "This is the current runtime, including the monolithic Streamlit entry point. "
            "The next refactor will isolate data services, content, components, and page renderers."
        )
    else:
        st.caption(
            "Progress is calculated across evidence, prototype, interaction, validation, and publication. "
            "It is a delivery signal, not a scientific-quality score."
        )
        st.dataframe(
            project_status[
                [
                    "title",
                    "evidence",
                    "prototype",
                    "interactive",
                    "validated",
                    "published",
                    "next_step",
                ]
            ],
            hide_index=True,
            use_container_width=True,
        )

    architecture_cols = st.columns([1, 1])
    with architecture_cols[0]:
        st.markdown("**Current implementation**")
        st.write(
            "Streamlit renders the portfolio from one main Python entry point, "
            "structured CSV manifests, visual assets, and Parquet structural datasets."
        )
    with architecture_cols[1]:
        st.markdown("**Next implementation step**")
        st.write(
            "Move cached data access and page renderers into focused modules, "
            "then add one interactive p5 study per high-priority scientific workflow."
        )

    if ARCHITECTURE_PATH.exists():
        st.download_button(
            "Download architecture document",
            ARCHITECTURE_PATH.read_text(encoding="utf-8"),
            file_name=ARCHITECTURE_PATH.name,
            mime="text/markdown",
        )


elif section == "Mobile View":
    st.title("AI Workflow Portfolio")
    st.caption("Tap a visual to open the full project.")
    st.link_button(
        "Open architecture and project progress",
        "?section=System%20Map&mobile=1",
    )

    mobile_topics = [
        topic for topic in TOPIC_ROOMS if topic["slug"] in MOBILE_TOPIC_SLUGS
    ]
    for topic in mobile_topics:
        with st.container(border=True):
            poster_path_text = TOPIC_VISUALS.get(topic["slug"])
            poster_path = project_asset(poster_path_text) if poster_path_text else None
            hero_path = project_asset(topic["hero"])
            if poster_path is not None and poster_path.exists():
                st.image(str(poster_path), use_container_width=True)
            elif hero_path.exists():
                st.image(str(hero_path), use_container_width=True)
            st.subheader(topic["title"])
            st.caption(TOPIC_FRAMES.get(topic["slug"], {}).get("question", topic["tagline"]))
            st.link_button("View full project", topic_url(topic["slug"]))
            if topic["slug"] == "north_slope":
                st.link_button(
                    "Open interactive Structural Explorer",
                    "?section=Structural%20Explorer",
                )

    st.subheader("Portfolio sections")
    st.link_button("Processing Visual Lab", "?section=Processing%20Visual%20Lab")
    st.link_button("Visual gallery", "?section=Visual%20Gallery")


elif section == "Structural Explorer":
    st.markdown(
        """
<div class="talk-hero">
  <div class="talk-kicker">Interactive project example</div>
  <h2>North Slope Structural Explorer</h2>
  <p>Select regional horizons, add public-data context, and rotate the basin in 3D.</p>
</div>
        """,
        unsafe_allow_html=True,
    )

    control_cols = st.columns([2, 1])
    selected_surfaces = control_cols[0].multiselect(
        "Visible horizons",
        STRUCTURAL_HORIZONS,
        default=["NStopo", "NSLCU", "NSshublik", "NSbasement"],
        format_func=lambda name: f"{name} - {SURFACE_CATALOG[name]['label']}",
    )
    cells_per_surface = control_cols[1].select_slider(
        "Surface detail",
        options=[1500, 3000, 6000],
        value=3000,
        format_func=lambda cells: f"{cells:,} cells / horizon",
    )
    selected_overlays = st.multiselect(
        "Context overlays",
        STRUCTURAL_OVERLAYS,
        default=[
            "North Slope study-area boundary",
            "Assessment-unit outlines",
        ],
    )

    if selected_surfaces:
        st.plotly_chart(
            build_structural_figure(
                selected_surfaces,
                cells_per_surface,
                selected_overlays,
            ),
            use_container_width=True,
        )
    else:
        st.info("Select at least one horizon.")

    label_cols = st.columns(2)
    for index, (code, metadata) in enumerate(SURFACE_CATALOG.items()):
        with label_cols[index % 2]:
            st.markdown(f"**{metadata['label']}**")
            st.caption(metadata["description"])

    with st.expander("Why this belongs in the portfolio"):
        st.write(
            "This is a stronger example than a static screenshot because the viewer "
            "can change structural layers, inspect depth, and connect the model to "
            "public wells and assessment units."
        )


elif section == "Think Tank Topics":
    topic_param = st.query_params.get("topic", TOPIC_ROOMS[0]["slug"])
    topic = topic_by_slug(topic_param)
    topic_frame = TOPIC_FRAMES.get(topic["slug"], {})

    st.markdown(
        f"""
<div class="talk-hero">
  <div class="talk-kicker">Think tank topic</div>
  <h2>{topic['title']}</h2>
  <p>{escape(topic_frame.get('question', topic['tagline']))}</p>
</div>
        """,
        unsafe_allow_html=True,
    )

    topic_roadmap = roadmap_row(topic["project_key"])
    if topic["slug"] == "north_slope":
        st.subheader("Working 3D structural explorer")
        st.caption(
            "Start with the live interaction: rotate the basin, inspect public structural context, "
            "then treat any output as a screening candidate that still needs expert review."
        )
        st.plotly_chart(
            build_structural_figure(
                ["NStopo", "NSLCU", "NSshublik", "NSbasement"],
                1500,
                [
                    "North Slope study-area boundary",
                    "Assessment-unit outlines",
                ],
            ),
            use_container_width=True,
            key="north_slope_topic_explorer",
        )
        render_north_slope_decision_board()
        render_current_future_board(topic, topic_roadmap)
        st.link_button(
            "Open full explorer controls",
            "?section=Structural%20Explorer",
        )
        source_library_manifest = project_asset(
            "assets/drive_sources/north_slope_source_library/source_manifest.csv"
        )
        source_library_index = project_asset(
            "assets/drive_sources/north_slope_source_library/source_index.md"
        )
        if source_library_manifest.exists():
            library_df = pd.read_csv(source_library_manifest)
            st.subheader("Local North Slope source-library index")
            source_cols = st.columns(3)
            source_cols[0].metric("Indexed source files", f"{len(library_df):,}")
            source_cols[1].metric(
                "Source categories",
                f"{library_df['Category'].nunique():,}",
            )
            source_cols[2].metric(
                "Indexed size",
                f"{library_df['Bytes'].sum() / 1_000_000:.1f} MB",
            )
            st.caption(
                "These are the curated source-library records copied into the local portfolio. "
                "Some rows still point to original laptop paths until the matching Drive files are exported."
            )
            with st.expander("Preview source-library manifest"):
                preview_cols = ["Category", "File", "Extension", "Bytes"]
                st.dataframe(
                    library_df[preview_cols].head(12),
                    hide_index=True,
                    use_container_width=True,
                )
            if source_library_index.exists():
                st.download_button(
                    "Download local source index",
                    source_library_index.read_bytes(),
                    file_name="north_slope_source_index.md",
                    mime="text/markdown",
                )
        render_north_slope_ml_update()
        render_source_backed_asset_panel(topic)
        render_ml_pipeline_contract(topic)
        render_slide_source_updates(topic["slug"])
    else:
        if topic["slug"] == "thesis_graph":
            render_thesis_graph_model_visuals()
        if not render_project_visual_stage(topic):
            st.markdown(render_topic_signal(topic), unsafe_allow_html=True)
        render_current_future_board(topic, topic_roadmap)
        render_source_backed_asset_panel(topic)
        if topic["slug"] == "ai_workflow":
            render_ml_model_part_explainer(compact=True)
        render_ml_pipeline_contract(topic)
        render_topic_update_panel(topic["slug"])
        render_slide_source_updates(topic["slug"])
    render_workflow_blueprint(topic)

    with st.expander("Switch think tank topic"):
        jump_cols = st.columns(4)
        for idx, room in enumerate(TOPIC_ROOMS):
            with jump_cols[idx % 4]:
                st.link_button(TOPIC_FRAMES.get(room["slug"], {}).get("question", room["title"]), topic_url(room["slug"]))

    with st.expander("How AI helped in this example"):
        render_ai_workflow_panel(topic)

    with st.expander("Processing concept and research plan"):
        render_processing_sketch_plan(topic)
        render_detailed_topic_plan(topic)

    current_visuals = project_visuals[
        project_visuals["project_key"].fillna("") == topic["project_key"]
    ].sort_values("sort_order")
    if topic["slug"] == "thesis_graph":
        ree_wall = current_visuals[
            current_visuals["visual_type"].fillna("").str.contains("Adobe|REE visualization|PowerPoint", case=False, regex=True)
        ]
        render_visual_wall("REE Adobe / Bayan Obo slide wall", ree_wall, limit=6)
    elif topic["slug"] == "rock_classification":
        rock_wall = current_visuals[
            current_visuals["visual_type"].fillna("").str.contains("slide|PowerPoint|presentation|classification|chart", case=False, regex=True)
        ]
        render_visual_wall("Rock classification maps and charts", rock_wall, limit=6)

    if topic_roadmap is not None:
        render_node_movement(topic_roadmap, title="Inputs -> variables -> AI/ML -> output")
        early_slide_visuals = project_visuals[
            (project_visuals["project_key"].fillna("") == topic["project_key"])
            & project_visuals["visual_type"].fillna("").str.contains("PowerPoint", case=False, regex=False)
        ].sort_values("sort_order")
        if not early_slide_visuals.empty:
            st.subheader("Featured slide exports")
            early_cols = st.columns(2)
            for idx, visual in enumerate(early_slide_visuals.head(2).itertuples(index=False)):
                with early_cols[idx % 2]:
                    visual_path = project_asset(visual.asset_path)
                    if visual_path.exists():
                        st.image(str(visual_path), caption=visual.title, use_container_width=True)

    hero_cols = st.columns([1.35, 1])
    with hero_cols[0]:
        hero_path = project_asset(topic["hero"])
        if topic["slug"] == "north_slope":
            render_external_app_embed(
                NORTH_SLOPE_WELL_SCAFFOLD_URL,
                "Embedded North Slope well-log scaffold",
                "This is the live Future Well-Log Engine from the North Slope Streamlit app, not a static screenshot.",
                height=760,
            )
            st.link_button("Open portfolio Structural Explorer", "?section=Structural%20Explorer")
            st.link_button("Open full North Slope app", NORTH_SLOPE_WELL_SCAFFOLD_URL)
            st.caption(
                "The portfolio structural explorer is embedded above on this page; this app embed shows the separate synthetic well-log scaffold."
            )
        elif topic["slug"] == "processing_earthquake":
            if hero_path.exists():
                st.image(str(hero_path), caption="Poster frame kept as secondary evidence.", use_container_width=True)
            st.link_button("Open original Drive video", USGS_GLOBE_DRIVE_URL)
        elif hero_path.exists():
            st.image(str(hero_path), caption=topic["theme"], use_container_width=True)
        else:
            st.warning("Hero image not found.")
    with hero_cols[1]:
        st.subheader("Example bottleneck")
        st.info(topic["bottleneck"])
        st.caption(topic["why_not_done"])

    if topic_roadmap is not None:
        st.subheader("Future use-case timeline")
        render_future_timeline(topic_roadmap)

    with st.expander("Technical notes for people who want to go deeper"):
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

    render_discussion_prompts(topic)
    render_evidence_leads(topic)

    with st.expander("Proof to show"):
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

    related_visuals = current_visuals
    if topic["slug"] == "north_slope":
        related_visuals = related_visuals[
            ~related_visuals["asset_path"].fillna("").str.contains(
                "north_slope_3d_streamlit_plotly_map",
                case=False,
                regex=False,
            )
        ]
    related_evidence = linkedin_evidence[
        linkedin_evidence["project_key"].fillna("") == topic["project_key"]
    ]
    related_folders = organized_folders[
        organized_folders["project_key"].fillna("") == topic["project_key"]
    ]

    slide_visuals = related_visuals[
        related_visuals["visual_type"].fillna("").str.contains("PowerPoint", case=False, regex=False)
    ]
    non_slide_visuals = related_visuals.drop(slide_visuals.index)

    if not slide_visuals.empty:
        st.subheader("PowerPoint / LinkedIn slide evidence")
        slide_cols = st.columns(2)
        for idx, visual in enumerate(slide_visuals.itertuples(index=False)):
            with slide_cols[idx % 2]:
                visual_path = project_asset(visual.asset_path)
                with st.container(border=True):
                    st.markdown(f"**{visual.title}**")
                    if visual_path.exists():
                        st.image(str(visual_path), use_container_width=True)
                    st.caption(visual.caption)

    st.subheader("Visual evidence")
    visual_cols = st.columns(3)
    if non_slide_visuals.empty:
        st.info("The source-backed image panel above is the primary visual evidence for this topic.")
    for idx, visual in enumerate(non_slide_visuals.itertuples(index=False)):
        with visual_cols[idx % 3]:
            visual_path = project_asset(visual.asset_path)
            with st.container(border=True):
                st.markdown(f"**{visual.title}**")
                if visual_path.exists():
                    st.image(str(visual_path), use_container_width=True)
                st.caption(visual.caption)

    st.subheader("Embedded or linked evidence")
    if related_evidence.empty:
        st.info("No separate LinkedIn manifest row is attached; use the local source images above as the primary evidence.")
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


elif section == "Processing Visual Lab":
    st.title("Processing Visual Lab")
    st.write(
        "This is the abstract visual layer for the think tank. The sketches should not recreate screenshots or PowerPoints. "
        "They should use dots, arrows, waves, clusters, fields, gates, and pulses to make the workflow idea easy to understand."
    )
    with st.expander("Visual redesign checklist"):
        st.markdown(
            """
1. **North Slope:** real four-horizon perspective, wells, assessment context, screening disclaimer.
2. **Earthquake globe:** depth legend, time arc, magnitude-driven pulses, sound response.
3. **Knowledge graph:** larger graph, three node types, one labeled relationship.
4. **Seismic:** dominant P-pick, confidence band, direct station/event output.
5. **Agent training:** larger final agent, visible failure example, animated action trace.
6. **Rock mapping:** connect satellite/GIS variables to reviewed classes and uncertainty overlap.
7. **Field geophysics:** add a combined interpretation panel and uncertainty bars.
8. **Hydrate ML:** emphasize feature lanes, leakage gate, and held-out complete wells.
9. **App pipeline:** use the current stock app visuals and put validation in the main path.
            """
        )
        if VISUAL_DESIGN_SPEC_PATH.exists():
            st.download_button(
                "Download full visual design specification",
                VISUAL_DESIGN_SPEC_PATH.read_text(encoding="utf-8"),
                file_name=VISUAL_DESIGN_SPEC_PATH.name,
                mime="text/markdown",
            )
    st.markdown(
        """
<div class="unfinished-note">
  Processing becomes the concept animation lab: static SVG mini-posters today, short looping sketches/GIFs next.
  The point is to visualize the idea behind each topic, not to prove the project is finished.
</div>
        """,
        unsafe_allow_html=True,
    )
    render_motion_priority_cards()

    st.subheader("Visual language")
    language_cols = st.columns(4)
    language_items = [
        ("dots", "files, examples, events, labels"),
        ("arrows", "workflow movement or AI transformation"),
        ("pulses", "attention, signal, confidence, activity"),
        ("gray clouds", "uncertainty or unresolved expert review"),
        ("grids", "maps, rasters, spatial data"),
        ("rings", "waves, time, depth, or spread"),
        ("color shifts", "classification or confidence"),
        ("gates", "validation, leakage checks, rubrics"),
    ]
    for idx, (label, meaning) in enumerate(language_items):
        with language_cols[idx % 4]:
            with st.container(border=True):
                st.markdown(f"**{label}**")
                st.caption(meaning)

    st.subheader("ML model parts")
    render_ml_model_part_explainer(compact=True)

    with st.expander("Research backbone for the visual lab"):
        st.write(
            "These sources support the direction of the sketches: knowledge graphs and GraphRAG for critical minerals, "
            "foundation models and uncertainty-aware workflows for seismic data, physics-informed ML for subsurface energy, "
            "spatial validation for geoscience ML, and agent evaluation for scientific software workflows."
        )
        render_research_sources()

    st.subheader("Visual studies")
    visual_cols = st.columns(3)
    for idx, topic in enumerate(TOPIC_ROOMS):
        with visual_cols[idx % 3]:
            st.markdown(render_topic_signal(topic), unsafe_allow_html=True)
            st.caption(topic["title"])

    st.subheader("Sketch plans by topic")
    sketch_cols = st.columns(3)
    for idx, topic in enumerate(TOPIC_ROOMS):
        with sketch_cols[idx % 3]:
            render_processing_sketch_plan(topic, compact=True)

    st.subheader("Four-frame animation storyboards")
    for topic in TOPIC_ROOMS:
        with st.expander(DETAILED_TOPIC_PLANS.get(topic["slug"], {}).get("title", topic["title"])):
            render_detailed_topic_plan(topic, compact=True)


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
        "Use this page as the high-level map: the same structure appears under each think tank topic, "
        "so the audience can see inputs, variables, models, and outputs without reading a wall of text."
    )
    render_ml_model_part_explainer()

    st.subheader("New ML and design source notes")
    st.caption(
        "Pulled from the latest Gmail source attachments and translated into portfolio update requirements."
    )
    render_gmail_source_update(compact=False)

    with st.expander("Research backbone for this roadmap", expanded=True):
        st.write(
            "The roadmap is intentionally exploratory. The sources below are included as direction markers, "
            "not proof that these prototypes are finished ML systems."
        )
        render_research_sources()

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
            topic_match = topic_for_project_key(row.project_key)
            if topic_match is not None:
                render_ml_visual_diagram(topic_match, compact=True)
                with st.expander("Detailed think-tank plan"):
                    render_detailed_topic_plan(topic_match)

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
    st.link_button("Open interactive System Map", "?section=System%20Map")

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
    st.title("Workflow Visual Gallery")
    st.write(
        "Visuals are grouped by the kind of AI workflow they help discuss: screenshots, maps, graphs, ML models, apps, and creative visualization."
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

    st.subheader("Visuals by workflow type")
    workflow_groups = {
        "AI + screenshots / agents": ["arcgis_raster_ml", "portfolio_profile"],
        "AI + maps / energy": ["north_slope", "valles_caldera", "moho_ml"],
        "AI + graphs / critical minerals": ["thesis_knowledge_graph"],
        "AI + classification": ["rock_classification"],
        "AI + app building": ["stock_dashboard", "stock_notebook"],
        "AI + creative visualization": ["processing_visuals", "pondicherry"],
    }
    selected_group = st.selectbox("Workflow type", list(workflow_groups.keys()))
    selected_visuals = project_visuals[
        project_visuals["project_key"].fillna("").isin(workflow_groups[selected_group])
    ].sort_values(["project_key", "sort_order"])

    if selected_visuals.empty:
        st.info("No individual visual has been selected for this workflow type yet.")
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


elif section == "Visual Audit":
    st.markdown(
        """
<div class="talk-hero">
  <div class="talk-kicker">Visual quality and roadmap</div>
  <h2>Review every visual against the portfolio vision</h2>
  <p>
    The audit connects each important visual to its purpose, evidence quality,
    mobile presentation, scientific review needs, and next design decision.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )

    open_audit = visual_audit[~visual_audit["status"].isin(["complete", "done"])]
    st.markdown(
        f"""
<div class="audit-summary">
  <div><span>Audited surfaces</span><strong>{len(visual_audit)}</strong></div>
  <div><span>P0 decisions</span><strong>{int((visual_audit["priority"] == "P0").sum())}</strong></div>
  <div><span>Mobile needs work</span><strong>{int((visual_audit["mobile_status"] == "needs_work").sum())}</strong></div>
  <div><span>Source blockers</span><strong>{int((visual_audit["status"] == "blocked_source").sum())}</strong></div>
</div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Next visual decisions")
    priority_order = {"P0": 0, "P1": 1, "P2": 2}
    status_order = {"in_progress": 0, "planned": 1, "blocked_source": 2}
    decision_queue = open_audit.copy()
    decision_queue["priority_order"] = decision_queue["priority"].map(priority_order).fillna(9)
    decision_queue["status_order"] = decision_queue["status"].map(status_order).fillna(9)
    decision_queue = decision_queue.sort_values(
        ["priority_order", "status_order", "visual_title"]
    ).head(6)

    decision_cols = st.columns(2)
    for index, item in enumerate(decision_queue.itertuples(index=False)):
        with decision_cols[index % 2]:
            with st.container(border=True):
                st.caption(f"{item.priority} · {item.page} · {item.status.replace('_', ' ')}")
                st.markdown(f"**{item.visual_title}**")
                st.write(item.current_issue)
                st.markdown(f"**Next change:** {item.recommended_change}")
                if valid_text(item.asset_path):
                    audit_asset = project_asset(item.asset_path)
                    if audit_asset.exists() and audit_asset.suffix.lower() in {
                        ".png",
                        ".jpg",
                        ".jpeg",
                        ".webp",
                        ".svg",
                    }:
                        st.image(str(audit_asset), use_container_width=True)

    st.subheader("Full audit")
    audit_filters = st.columns(3)
    selected_priority = audit_filters[0].selectbox(
        "Priority",
        ["All"] + sorted(visual_audit["priority"].dropna().unique().tolist()),
    )
    selected_status = audit_filters[1].selectbox(
        "Status",
        ["All"] + sorted(visual_audit["status"].dropna().unique().tolist()),
    )
    selected_project = audit_filters[2].selectbox(
        "Project",
        ["All"] + sorted(visual_audit["project_key"].dropna().unique().tolist()),
    )

    filtered_audit = visual_audit.copy()
    if selected_priority != "All":
        filtered_audit = filtered_audit[
            filtered_audit["priority"] == selected_priority
        ]
    if selected_status != "All":
        filtered_audit = filtered_audit[filtered_audit["status"] == selected_status]
    if selected_project != "All":
        filtered_audit = filtered_audit[
            filtered_audit["project_key"] == selected_project
        ]

    st.dataframe(
        filtered_audit[
            [
                "priority",
                "status",
                "page",
                "visual_title",
                "evidence_type",
                "desktop_status",
                "mobile_status",
                "scientific_review",
                "motion_opportunity",
                "current_issue",
                "recommended_change",
            ]
        ],
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        "Download visual audit CSV",
        visual_audit.to_csv(index=False),
        file_name=VISUAL_AUDIT_PATH.name,
        mime="text/csv",
    )


elif section == "Update Inbox":
    st.markdown(
        """
<div class="talk-hero">
  <div class="talk-kicker">Change intake</div>
  <h2>Package notes, screenshots, and a chat link</h2>
  <p>
    Turn a new idea or review message into one portable update package. The package
    keeps the original screenshots beside structured instructions for the next build pass.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("update_inbox_form"):
        request_title = st.text_input(
            "Update title",
            placeholder="Example: simplify the homepage and add new project visuals",
        )
        request_message = st.text_area(
            "Changes and new ideas",
            height=180,
            placeholder=(
                "Describe what should change, what should stay, and what outcome "
                "the updated page should create."
            ),
        )
        request_cols = st.columns(2)
        request_project = request_cols[0].selectbox(
            "Project area",
            ["Whole portfolio"]
            + sorted(vision_board["project_key"].dropna().unique().tolist()),
        )
        request_priority = request_cols[1].selectbox(
            "Priority",
            ["P1 - next", "P0 - urgent", "P2 - later"],
        )
        conversation_url = st.text_input(
            "Chat conversation link",
            placeholder="https://...",
        )
        screenshot_uploads = st.file_uploader(
            "Screenshots",
            type=["png", "jpg", "jpeg", "webp"],
            accept_multiple_files=True,
            help="Add the screenshots that show the current state or desired changes.",
        )
        submitted_update = st.form_submit_button(
            "Prepare update package",
            type="primary",
        )

    if submitted_update:
        errors = []
        if not request_title.strip():
            errors.append("Add an update title.")
        if not request_message.strip():
            errors.append("Describe the requested changes.")
        if conversation_url and not conversation_url.lower().startswith(
            ("http://", "https://")
        ):
            errors.append("The conversation link must start with http:// or https://.")

        if errors:
            for error in errors:
                st.error(error)
        else:
            package_bytes = build_update_handoff(
                request_title,
                request_message,
                conversation_url,
                request_project,
                request_priority,
                screenshot_uploads,
            )
            st.session_state["update_handoff"] = {
                "title": request_title.strip(),
                "package": package_bytes,
                "screenshots": [
                    {
                        "name": upload.name,
                        "bytes": upload.getvalue(),
                    }
                    for upload in screenshot_uploads
                ],
            }
            st.success(
                "Update package prepared. Review the screenshots and download the ZIP."
            )

    update_handoff = st.session_state.get("update_handoff")
    if update_handoff:
        preview_rows = update_handoff["screenshots"]
        if preview_rows:
            st.subheader("Screenshot review")
            preview_cols = st.columns(2)
            for index, screenshot in enumerate(preview_rows):
                with preview_cols[index % 2]:
                    st.image(
                        screenshot["bytes"],
                        caption=screenshot["name"],
                        use_container_width=True,
                    )
        st.download_button(
            "Download update handoff ZIP",
            update_handoff["package"],
            file_name="portfolio_update_handoff.zip",
            mime="application/zip",
            type="primary",
        )
        st.caption(
            "The ZIP contains update_request.json and the original screenshots. "
            "Keep approved work in the repository vision board and project files."
        )

    with st.expander("How updates move into the project"):
        st.markdown(
            """
1. Describe the requested change and attach visual evidence.
2. Export one handoff ZIP so the message, chat link, and screenshots stay together.
3. Review the request against the project charter and existing evidence.
4. Update the app, relevant data files, and `data/vision_board.csv`.
5. Test the affected desktop and mobile paths before publishing.
            """
        )


elif section == "Contact / Ideas":
    st.title("Contact / Ideas")
    st.markdown(
        """
<div class="talk-hero">
  <div class="talk-kicker">Why I am showing this</div>
  <h2>I am early in this, and I want the conversation.</h2>
  <p>
    I have been prompting since ChatGPT came out, but Codex, GitHub, screenshots,
    and Open Science Lab style workflows made me realize that a lot of manual project work
    can become a system. I am not trying to say these projects are finished. I am trying
    to learn how people with more experience would push them further.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("The ask")
    st.write(
        "I would love to hear your opinion, what you have seen work in industry or government, "
        "and how your experience changes these ideas. The best outcome is not applause; it is a better question."
    )
    render_feedback_cards()
    st.info(
        "I am showing unfinished systems because that is where expert feedback matters most. "
        "If you see a better validation test, a stronger dataset, a clearer visualization, "
        "or a false assumption, that is the conversation I want."
    )
    st.subheader("A little me")
    st.write(
        "I like cafes, geoscience, coding, art, markets, and conversations about how people are using AI. "
        "My projects are examples I can point to while asking bigger questions about workflows."
    )


elif section == "Build Plan":
    st.title("Build Plan")
    st.subheader("Next clean-up pass")
    st.markdown(
        """
1. Pick the best 12 to 20 individual screenshots from the contact sheets.
2. Refactor cached data loading and page rendering out of the main app entry point.
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
