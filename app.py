from pathlib import Path
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


inventory = load_current_csv(INVENTORY_PATH)
drive_inventory = load_current_csv(DRIVE_INVENTORY_PATH)
notebook_inventory = load_current_csv(NOTEBOOK_INVENTORY_PATH)
case_studies = load_current_csv(CASE_STUDY_PATH)
project_visuals = load_current_csv(PROJECT_VISUALS_PATH)
linkedin_evidence = load_current_csv(LINKEDIN_EVIDENCE_PATH)
organized_folders = load_current_csv(ORGANIZED_FOLDERS_PATH)


SECTIONS = [
    "Overview",
    "Presentation View",
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
    st.title("AI as a Research Operating System for Geoscience")
    st.write(
        "This site is built for a technical AI/geoscience audience: it shows how AI was used "
        "as a working partner for research planning, screenshots, code review, file discovery, "
        "notebooks, GIS, visualization, writing, and presentation assembly."
    )

    cols = st.columns(5)
    cols[0].metric("Case studies", len(case_studies))
    cols[1].metric("Notebooks indexed", len(notebook_inventory))
    cols[2].metric("Drive links", len(drive_inventory))
    cols[3].metric("High-priority sources", int((inventory["priority"] == "high").sum()))
    cols[4].metric("Visual assets", len(project_visuals))

    st.subheader("What AI actually did")
    ai_cols = st.columns(4)
    ai_steps = [
        ("Goal steering", "Screenshots, files, and messy questions were repeatedly brought to AI with the practical question: what is the next useful step?"),
        ("File access", "Codex in VS Code can inspect notebooks, CSVs, PDFs, decks, screenshots, folders, and app code so AI can reason over the actual project state."),
        ("Pipeline building", "Notebook experiments become Streamlit pages, evidence manifests, reusable folders, code snippets, and PowerPoint-ready sections."),
        ("Human supervision", "The Handshake/Vagon work shows why human demonstrations and rubric checks still matter for training reliable software-use agents."),
    ]
    for col, (label, body) in zip(ai_cols, ai_steps):
        with col:
            st.markdown(f"**{label}**")
            st.write(body)

    st.subheader("Why Codex, VS Code, and GitHub matter")
    tool_cols = st.columns(3)
    with tool_cols[0]:
        st.markdown("**VS Code + Codex**")
        st.write("AI can work inside the project folder, inspect code, organize files, update Streamlit, and verify changes in the browser.")
    with tool_cols[1]:
        st.markdown("**GitHub-ready workflow**")
        st.write("Once organized, the same app/data structure can become versioned, reviewed, shared, and extended as future projects grow.")
    with tool_cols[2]:
        st.markdown("**More file types for AI**")
        st.write("The workflow spans notebooks, PowerPoints, videos, screenshots, PDFs, GraphML, Gephi CSVs, QGIS/ArcGIS files, and manuscript drafts.")

    st.subheader("Geoscience background")
    bg_cols = st.columns([1.4, 1])
    with bg_cols[0]:
        for point in BACKGROUND_POINTS:
            st.write(f"- {point}")
    with bg_cols[1]:
        resume_path = Path("C:\\Users\\gargi\\Downloads\\AI_powerpoint_project_evidence\\01_profile_handshake_ai\\resume_geoscience_ai_onegeo.pdf")
        profile_path = Path("C:\\Users\\gargi\\Downloads\\AI_powerpoint_project_evidence\\01_profile_handshake_ai\\profile_rohan_nanda.pdf")
        if resume_path.exists():
            st.link_button("Open resume", local_file_uri(str(resume_path)))
        if profile_path.exists():
            st.link_button("Open LinkedIn profile PDF", local_file_uri(str(profile_path)))

    st.subheader("Machine learning value by project")
    st.dataframe(pd.DataFrame(ML_FUTURE_POINTS), hide_index=True, use_container_width=True)

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
