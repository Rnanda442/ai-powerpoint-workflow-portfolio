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
DEPLOY_BUILD_ID = "0a824ca / 2026-06-09"
INVENTORY_PATH = ROOT / "data" / "source_inventory.csv"
DRIVE_INVENTORY_PATH = ROOT / "data" / "google_drive_inventory.csv"
NOTEBOOK_INVENTORY_PATH = ROOT / "data" / "notebook_inventory.csv"
CASE_STUDY_PATH = ROOT / "data" / "case_studies.csv"
PROJECT_VISUALS_PATH = ROOT / "data" / "project_visuals.csv"
LINKEDIN_EVIDENCE_PATH = ROOT / "data" / "linkedin_evidence.csv"
ORGANIZED_FOLDERS_PATH = ROOT / "data" / "organized_project_folders.csv"
ML_ROADMAP_PATH = ROOT / "data" / "ml_future_roadmap.csv"
PROJECT_STATUS_PATH = ROOT / "data" / "project_status.csv"
VISUAL_AUDIT_PATH = ROOT / "data" / "visual_audit.csv"
VISION_BOARD_PATH = ROOT / "data" / "vision_board.csv"
WEBSITE_CHANGE_IDEAS_PATH = ROOT / "data" / "website_change_ideas.csv"
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
        "slug": "stock_workflow",
        "title": "AI-Assisted App Building And Data Pipelines",
        "tagline": "A stock dashboard example for discussing Codex, GitHub, cloud workflows, automation, and how young people think about AI-driven opportunity.",
        "project_key": "stock_dashboard",
        "hero": "assets/project_visuals/stock_all_tickers_chart.svg",
        "theme": "Codex + local files + GitHub + Streamlit + model-evaluation honesty.",
        "bottleneck": "People can build useful tools faster now, but AI can also make confident mistakes unless the user understands testing, leakage, and what the model is allowed to know.",
        "why_not_done": "Before Codex, building an app from notebook screenshots meant repetitive copying, local debugging, and scattered files. The new workflow can organize existing work, track changes, and push more of the build into GitHub/cloud-style systems.",
        "ai_used": "Codex organized local downloads, inspected existing notebook/app outputs, built Streamlit structure, helped debug charts, and made the workflow feel less like copy-paste and more like a system.",
        "future_ai": "A future version would separate training and unseen evaluation data, keep GitHub-tracked pipelines, automate refreshes, and use cloud/virtual desktop workflows so local storage and CPU are less of a bottleneck.",
        "why_it_matters": "This opens a bigger discussion: if jobs and markets are changing, what practical AI skills help young people build tools, test ideas, and maybe create value without pretending the model is magic?",
        "proof": ["stockprediction2025 dashboard", "GitHub Actions pipeline", "Streamlit charts", "model-baseline notes"],
        "question": "How can Codex-style tools help people build real apps without hiding model risk or data leakage?",
    },
]

MOBILE_TOPIC_SLUGS = [
    "ai_workflow",
    "thesis_graph",
    "processing_earthquake",
    "north_slope",
    "seismic",
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
    "moho_ml": {
        "question": "Did it transfer or memorize?",
        "example": "The Australia-to-USA gravity/Moho supervised ML project is the example.",
        "raise": "Raise your hand if you want to talk about leakage, transfer tests, and honest model scoring.",
        "pattern": ["train", "test", "transfer", "residual"],
    },
    "stock_workflow": {
        "question": "Build faster. Test honestly.",
        "example": "The stock dashboard and GitHub/cloud workflow are the example.",
        "raise": "Raise your hand if you want to talk about AI, money, app building, and model risk.",
        "pattern": ["files", "Codex", "GitHub", "app"],
    },
}

TOPIC_VISUALS = {
    "ai_workflow": "assets/topic_visuals/agent_training.svg",
    "thesis_graph": "assets/topic_visuals/knowledge_graph.svg",
    "processing_earthquake": "assets/topic_visuals/earthquake_globe.svg",
    "seismic": "assets/topic_visuals/seismic_processing.svg",
    "north_slope": "assets/topic_visuals/north_slope_energy.svg",
    "rock_classification": "assets/topic_visuals/rock_resource_map.svg",
    "valles": "assets/topic_visuals/field_geophysics.svg",
    "moho_ml": "assets/topic_visuals/moho_transfer.svg",
    "stock_workflow": "assets/topic_visuals/app_pipeline.svg",
}

CARD_VISUALS = {
    "ai_workflow": "assets/gmail_updates/2026-06-08/Screenshot 2026-05-18 001002.png",
    "thesis_graph": "assets/project_visuals/linkedin_powerpoint_slides/ree_slide_system_overview.png",
    "processing_earthquake": "assets/project_visuals/processing_earthquake_linkedin_poster.jpg",
    "north_slope": "assets/project_visuals/north_slope_alaska_geology_well_map.png",
    "rock_classification": "assets/gmail_updates/2026-06-08/Screenshot 2026-05-16 203029.png",
    "seismic": "assets/gmail_updates/2026-06-08/Screenshot 2025-07-01 101445.png",
    "valles": "assets/project_visuals/linkedin_powerpoint_slides/sage_valles_deck_image_03.jpg",
    "moho_ml": "assets/project_visuals/valles_moho.png",
    "stock_workflow": "assets/project_visuals/stock_saved_data_chart.svg",
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
    "moho_ml": [
        "What is the cleanest way to test regional transfer?",
        "Which model family would you try before an ANN today?",
        "How should residual maps guide geology review?",
    ],
    "stock_workflow": [
        "What AI skills help young people build practical tools?",
        "How do we keep model testing honest?",
        "What belongs in GitHub/cloud instead of a laptop folder?",
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
    "moho_ml": {
        "sketch": "transfer_residual_loop",
        "visual": "A training cluster on the left feeds a neural-node chain. Predictions land on a new region, then residual dots flash where transfer fails.",
        "motion": ["train pulse", "network propagation", "test-region reveal", "residual flash"],
        "conclusion": "A high ML score is not enough; the model has to transfer honestly to new geography.",
        "future_ml": "Spatial cross-validation, transfer learning, residual mapping, uncertainty estimates, and model-family comparison.",
        "processing_notes": "Use two point clouds, a simple node network, and red/blue residual particles after prediction.",
    },
    "stock_workflow": {
        "sketch": "codex_pipeline_risk_gate_loop",
        "visual": "Chaotic file dots fall into a Codex node, split into GitHub branches and dashboard panels, then pass through a leakage-check gate.",
        "motion": ["file rain", "pipeline sorting", "branch split", "risk gate"],
        "conclusion": "AI helps people build tools quickly, but useful apps need honest model testing and visible risk checks.",
        "future_ml": "Pipeline automation, model monitoring, leakage detection, cloud refreshes, and human-reviewed decision support.",
        "processing_notes": "Animate falling particles into lanes, branch lines, mini dashboard rectangles, and a red gate that blocks bad scores.",
    },
}

RESEARCH_SOURCES = [
    ("USGS Earth MRI", "https://www.usgs.gov/special-topics/earth-mri"),
    ("DOE AI for Energy report", "https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf"),
    ("Geoscience knowledge graph pipeline", "https://www.mdpi.com/2075-163X/14/12/1296"),
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
    "moho_ml": {
        "description": "A real supervised ML example becomes a discussion about transfer, leakage, and reproducibility.",
        "chips": ["Gravity inputs", "ANN-style model", "Transfer test"],
        "where": "AI can now help recover, explain, document, and stress-test a past machine-learning project instead of leaving it as a hidden class notebook.",
        "gave": "aus.moho.ipynb, australian.moho, australian.py, machinelearningreport.docx, gravity/Moho variables, and the Australia-to-USA transfer goal.",
        "produced": "A new topic room that separates actual past ML from future speculative AI workflows.",
        "validated": "Train/test boundaries, model leakage, whether R2 means anything on unseen geography, and whether the prediction makes geologic sense.",
        "future": "A current version would compare ANN, tree ensembles, Gaussian/process-style uncertainty, spatial cross-validation, and residual maps before claiming it works.",
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
}

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
        padding: 0.35rem 0 1rem;
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
        font-size: 2.65rem;
        line-height: 1.06;
        margin: 0 0 0.75rem;
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
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.9rem;
        margin: 1rem 0;
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
        padding: 0.85rem;
        min-height: 315px;
        display: flex;
        flex-direction: column;
        gap: 0.65rem;
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
        object-fit: contain;
        background: #f8fafc;
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
        font-size: 0.88rem;
        font-weight: 850;
        line-height: 1.22;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }
    .think-question {
        font-size: 1.02rem;
        line-height: 1.34;
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
        padding: 0.48rem 0.6rem;
        font-size: 0.84rem;
        font-weight: 750;
        line-height: 1.3;
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
        .ml-strip, .future-timeline, .node-lane, .storyboard-grid, .ai-case-top, .ai-evidence-grid, .think-grid, .vision-board, .blueprint-steps, .workflow-branches, .prompt-grid, .source-chip-grid, .sketch-body, .sketch-grid, .research-source-grid, .detail-grid, .story-frames, .current-future-board, .evidence-chain, .transfer-stage, .pipeline-stage, .property-stage { grid-template-columns: 1fr; }
        .chain-node:not(:last-child)::after,
        .pipeline-node:not(:last-child)::after { display: none; }
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
            radial-gradient(circle at 8% 0%, rgba(20,184,166,0.20), transparent 30%),
            radial-gradient(circle at 92% 8%, rgba(249,115,22,0.16), transparent 28%),
            linear-gradient(145deg, #07111f 0%, #111827 48%, #0f172a 100%) !important;
        color: #e5edf7 !important;
    }
    section[data-testid="stSidebar"] {
        background: #07111f !important;
        border-right: 1px solid rgba(148, 163, 184, 0.22);
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
        background: rgba(15, 23, 42, 0.82) !important;
        border: 1px solid rgba(148, 163, 184, 0.28) !important;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.22);
    }
    .portfolio-intro {
        max-width: none;
        border-radius: 18px;
        padding: 1.35rem 1.45rem 1.45rem;
        margin-bottom: 1rem;
    }
    .talk-hero {
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.92), rgba(15, 118, 110, 0.28)) !important;
    }
    .portfolio-eyebrow,
    .talk-kicker { color: #5eead4 !important; letter-spacing: 0.08em; }
    .portfolio-intro h1,
    .talk-hero h2,
    .section-heading-title,
    .think-title,
    .think-question,
    h1, h2, h3, h4 { color: #f8fafc !important; }
    .portfolio-intro p,
    .talk-hero p,
    .section-heading span,
    .small-note,
    .ml-body,
    .timeline-node em,
    .vision-card p { color: #cbd5e1 !important; }
    .think-grid.topic-wall {
        border-radius: 18px;
        background:
            radial-gradient(circle at 12% 16%, rgba(20,184,166,0.20), transparent 20%),
            radial-gradient(circle at 88% 22%, rgba(249,115,22,0.18), transparent 22%),
            radial-gradient(circle at 50% 95%, rgba(96,165,250,0.20), transparent 24%),
            linear-gradient(135deg, rgba(15,23,42,0.92) 0%, rgba(30,41,59,0.88) 100%) !important;
    }
    .think-card,
    .vision-card,
    .ml-stage,
    .future-timeline .timeline-node,
    .node-cluster,
    .source-chip,
    div[data-testid="stMetric"],
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(15, 23, 42, 0.84) !important;
        border-color: rgba(148, 163, 184, 0.28) !important;
        color: #e5edf7 !important;
    }
    .think-card { border-radius: 14px; }
    .think-card-link:hover .think-card,
    .think-card-link:focus .think-card {
        border-color: #5eead4 !important;
        box-shadow: 0 16px 42px rgba(20, 184, 166, 0.24);
    }
    .topic-poster {
        background: #020617 !important;
        border-color: rgba(94, 234, 212, 0.28) !important;
    }
    .topic-poster-composite.card-visual > img,
    .topic-room-visual > img,
    .topic-pattern.fallback-pattern { background: #020617 !important; }
    .think-raise {
        background: rgba(20, 184, 166, 0.12) !important;
        color: #ccfbf1 !important;
        border-left-color: #5eead4 !important;
    }
    .project-status,
    .portfolio-proof span,
    .vision-meta span,
    .topic-pattern span,
    .node-pill,
    .ai-chip,
    .motion-pill {
        background: rgba(15, 23, 42, 0.92) !important;
        border-color: rgba(94, 234, 212, 0.30) !important;
        color: #e0f2fe !important;
    }
    .stAlert {
        background: rgba(15, 23, 42, 0.88) !important;
        color: #e5edf7 !important;
    }
    .stAlert p,
    .stAlert li,
    div[data-testid="stMarkdownContainer"] p {
        color: #dbeafe;
    }
    .future-timeline .timeline-node span { color: #5eead4 !important; }
    .future-timeline .timeline-node strong { color: #f8fafc !important; }
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


def render_topic_signal(topic: dict, card: bool = False) -> str:
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
                proof_path = project_asset(proof_path_text)
                if proof_path.exists() and proof_path != visual_path:
                    proof_uri = asset_data_uri(proof_path, max_bytes=450_000)
                    if proof_uri is not None:
                        proof_html = (
                            "<div class='topic-proof-inset'>"
                            f"<img src='{proof_uri}' "
                            f"alt='Real project evidence for {escape(topic['title'])}'>"
                            "<span>REAL PROOF</span></div>"
                        )
                    else:
                        proof_html = (
                            "<div class='topic-proof-inset text-only'>"
                            f"{workflow_icon_svg(topic['title'], 0)}"
                            "<span>REAL PROOF</span></div>"
                        )
            if data_uri:
                visual_html = (
                    f"<img src='{data_uri}' "
                    f"alt='{escape(topic['title'])} workflow poster'>"
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
    workflow = AI_WORKFLOW_EVIDENCE.get(topic["slug"], {})
    question = frame.get("question", topic["question"])
    url = topic_url(topic["slug"]).replace("&", "&amp;")
    raise_prompt = frame.get("raise", "Raise your hand if you want to discuss this project.")
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
  <div class="stage-label" style="left:3%;top:5%">PROMPT</div>
  <div class="action-marker" style="left:17%;top:31%">1</div>
  <div class="action-marker" style="left:39%;top:22%">2</div>
  <div class="action-marker" style="left:62%;top:39%">3</div>
  <div class="stage-label failure" style="right:5%;top:18%">FAILED ACTION ↩ HUMAN</div>
  <div class="agent-lanes">
    <div class="agent-lane">HUMAN LANE<br>DEMO → TRACE</div>
    <div class="rubric-gate">SAME OUTPUT<br>RUBRIC</div>
    <div class="agent-lane">AGENT LANE<br>REPLAY → REVIEW</div>
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
<div class="project-stage">
  <div class="evidence-chain">
    <div class="chain-node">{workflow_icon_svg("prompt", 1)}<strong>PROMPT</strong><span>What connects?</span></div>
    <div class="chain-node human"><img src="{drawing_uri}" alt="Real Bayan Obo Adobe drawing"><strong>ADOBE</strong><span>orange = geologist</span></div>
    <div class="chain-node">
      <div class="mini-table"><span>mineral</span><span>stage</span><span>host</span><span>source</span><span>fluid</span><span>deposit</span></div>
      <strong>EXCEL</strong><span>real fields</span>
    </div>
    <div class="chain-node">{workflow_icon_svg("csv nodes", 3)}<strong>NODES</strong><span>solid = source</span></div>
    <div class="chain-node"><img src="{graph_uri}" alt="Real thesis graph export"><strong>GEPHI</strong><span>dotted = AI suggestion</span></div>
    <div class="chain-node question-node">{workflow_icon_svg("review", 5)}<strong>UNKNOWN?</strong><span>expert review</span></div>
  </div>
  <div class="output-branches">
    <div>EVIDENCE SUMMARY</div>
    <div class="question">RELATIONSHIP GAP<br>question, not discovery</div>
    <div class="question">EXTRACTION HYPOTHESIS<br>question, not discovery</div>
  </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        return True

    if slug == "moho_ml":
        moho_uri = asset_data_uri(
            project_asset("assets/project_visuals/valles_moho.png"),
            max_bytes=500_000,
        )
        if moho_uri is None:
            return False
        st.markdown(
            f"""
<div class="project-stage transfer-stage">
  <div class="region-panel">
    <h4>AUSTRALIA · TRAIN</h4>
    <div class="sample-field"></div>
    <div class="small-note">gravity + Moho points</div>
  </div>
  <div>
    <div class="model-gate">ANN<br>BASELINE</div>
    <div class="leakage-gate">LEAKAGE?<br>BLOCK INVALID SPLITS</div>
  </div>
  <div class="region-panel">
    <h4>USA · TRANSFER FIRST</h4>
    <img src="{moho_uri}" alt="Real Moho mapping evidence">
    <div class="residual-dots"><i></i><i></i><i></i><i></i><i></i></div>
    <div class="small-note">residuals before score</div>
  </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        return True

    if slug == "stock_workflow":
        st.markdown(
            f"""
<div class="project-stage pipeline-stage">
  <div class="pipeline-node"><div><div class="file-rain"><span></span><span></span><span></span><span></span><span></span></div><strong>FILES</strong></div></div>
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
    <strong>MEASURED SIGNALS</strong>
    <div class="property-chips">
      <span>DENSITY</span><span>VELOCITY</span><span>RESISTIVITY</span>
      <span>CHEMISTRY</span><span>FORMATION</span>
    </div>
  </div>
  <div class="range-gate">RANGE<br>GATES<br>↓<br>GRAY = UNCERTAIN</div>
  <div class="map-output">
    <strong>CLASSIFIED GIS ZONES</strong>
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
        path = Path(path_text)
        status = "found" if path.exists() else "missing"
        chips.append(
            f"""
<div class="source-chip">
  <strong>{escape(label)}</strong>
  <span>{escape(status)} | {escape(path.name)}</span>
</div>
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
project_status = load_current_csv(PROJECT_STATUS_PATH)
visual_audit = load_current_csv(VISUAL_AUDIT_PATH)
vision_board = load_current_csv(VISION_BOARD_PATH)
website_change_ideas = load_current_csv(WEBSITE_CHANGE_IDEAS_PATH)
project_status_by_key = {
    row["project_key"]: row
    for _, row in project_status.iterrows()
}


PUBLIC_SECTIONS = [
    "Start",
    "Topics",
    "Interactives",
    "Visual Lab",
    "Vision",
    "About",
    "Build Room",
]
PUBLIC_TO_INTERNAL = {
    "Start": "Overview",
    "Topics": "Think Tank Topics",
    "Interactives": "Structural Explorer",
    "Visual Lab": "Processing Visual Lab",
    "Vision": "Vision Board",
    "About": "Contact / Ideas",
}
BUILD_ROOM_SECTIONS = [
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
    "Presentation View",
    "Mobile View",
    "Case Studies",
]
ALL_INTERNAL_SECTIONS = list(PUBLIC_TO_INTERNAL.values()) + BUILD_ROOM_SECTIONS
PUBLIC_LABELS = {
    "Start": "Start · choose a question",
    "Topics": "Topics · evidence and future systems",
    "Interactives": "Interactives · working scientific tools",
    "Visual Lab": "Visual Lab · motion and Processing",
    "Vision": "Vision · now, next, and later",
    "About": "About · share an idea or correction",
    "Build Room": "Build Room · sources, code, and review",
}
BUILD_ROOM_LABELS = {
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
    "Presentation View": "Presentation system",
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

    st.subheader("Explore the system")
    fast_cols = st.columns(6)
    fast_cols[0].link_button("System Map", "?section=System%20Map")
    fast_cols[1].link_button("Vision Board", "?section=Vision%20Board")
    fast_cols[2].link_button("Structural Explorer", "?section=Structural%20Explorer")
    fast_cols[3].link_button("Presentation View", "?section=Presentation%20View")
    fast_cols[4].link_button("Visual Audit", "?section=Visual%20Audit")
    fast_cols[5].link_button("Phone View", "?section=Mobile%20View")

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

    status_counts = vision_board["status"].value_counts()
    vision_metrics = st.columns(4)
    vision_metrics[0].metric("Active now", int((vision_board["horizon"] == "Now").sum()))
    vision_metrics[1].metric("Next up", int((vision_board["horizon"] == "Next").sum()))
    vision_metrics[2].metric("In progress", int(status_counts.get("in_progress", 0)))
    vision_metrics[3].metric("P0 priorities", int((vision_board["priority"] == "P0").sum()))

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
        project_options = featured_visuals["project_key"].drop_duplicates().tolist()
        selected_visual_project = st.selectbox(
            "Evidence project",
            project_options,
            format_func=lambda key: next(
                (
                    topic["title"]
                    for topic in TOPIC_ROOMS
                    if topic["project_key"] == key
                ),
                key.replace("_", " ").title(),
            ),
            key="presentation_visual_project",
        )
        project_visual_options = featured_visuals[
            featured_visuals["project_key"] == selected_visual_project
        ]
        visual_titles = project_visual_options["title"].tolist()
        selected_visual_title = st.selectbox(
            "Visual from this project",
            visual_titles,
            key="presentation_visual",
        )
        selected_visual = project_visual_options[
            project_visual_options["title"] == selected_visual_title
        ].iloc[0]
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
    if not render_project_visual_stage(topic):
        st.markdown(render_topic_signal(topic), unsafe_allow_html=True)
    render_current_future_board(topic, topic_roadmap)
    if topic["slug"] == "north_slope":
        st.subheader("Working 3D structural explorer")
        st.caption(
            "This interaction is part of the North Slope project, not separate evidence. "
            "Rotate the basin and inspect the public-data structural context here."
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
        st.info("No extra visual has been selected for this topic yet.")
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
6. **Rock mapping:** connect input ranges to classified zones and uncertainty overlap.
7. **Field geophysics:** add a combined interpretation panel and uncertainty bars.
8. **Moho ML:** emphasize geographic transfer, leakage gate, and residual map.
9. **App pipeline:** put validation in the main path and loop results back to Codex.
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
            topic_match = next(
                (topic for topic in TOPIC_ROOMS if topic["project_key"] == row.project_key),
                None,
            )
            if topic_match is not None:
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
    idea_cols = st.columns(3)
    with idea_cols[0]:
        with st.container(border=True):
            st.markdown("**Tell me what breaks**")
            st.caption("Where would this workflow fail in a real organization, dataset, basin, or software environment?")
    with idea_cols[1]:
        with st.container(border=True):
            st.markdown("**Tell me what to learn**")
            st.caption("Neo4j, cloud hosting, Linux sandboxes, agents, model validation, data engineering, or something older that still matters.")
    with idea_cols[2]:
        with st.container(border=True):
            st.markdown("**Tell me what is useful**")
            st.caption("Which topic could actually help energy, geoscience, finance, or scientific software work if it was built correctly?")
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
