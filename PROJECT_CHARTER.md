# AI Workflow Portfolio Charter

This file is the durable source of truth for the project's goals, vision,
design direction, constraints, and current priorities. Read this before making
substantial changes to the website, visuals, PowerPoint, or repository.

Last updated: June 8, 2026

## Project In One Sentence

Build a visual AI think tank where unfinished geoscience, coding, research, and
creative projects serve as evidence for discussing how prompting, domain
knowledge, emerging ML workflows, and human review can create useful systems.

## Core Thesis

The site is not mainly a finished-project portfolio, recruiting site, or a
collection of products presented as flawless work.

The larger argument is:

- AI becomes useful when it can work with actual files, screenshots, code,
  notebooks, maps, research sources, and project history.
- Domain knowledge, curiosity, and human review determine whether the output is
  meaningful.
- AI can reduce repetitive work and help turn scattered evidence into software,
  visualizations, research structures, and presentations.
- A trustworthy portfolio must distinguish working evidence, prototypes,
  future ideas, and claims that still require validation.

## Primary Outcomes

1. A public Streamlit portfolio that works on desktop and mobile.
2. A PowerPoint presentation built from the same story and visual system.
3. A curated visual library containing maps, diagrams, Processing-style motion
   studies, screenshots, videos, charts, and project evidence.
4. Clear project rooms that connect each example to a larger AI, ML, or
   scientific-workflow question.
5. A maintainable repository where future work can continue across the laptop,
   desktop, GitHub, Drive, and Streamlit without losing context.
6. A living vision board and structured update handoff so new notes,
   screenshots, and conversation links become trackable project decisions.

## Intended Audience

The site should be understandable to:

- DOE and energy managers working near the front of AI integration.
- AI, ML, software, and scientific-workflow professionals.
- Geoscientists, GIS specialists, visualization experts, and energy researchers.
- Experienced practitioners who can challenge, correct, or extend the ideas.
- Curious builders looking for workflows they can adapt to their own projects.

The site is not optimized for recruiter conversion. Its primary outcome is
discussion, learning, collaboration, and useful disagreement.

## Desired Visitor Experience

A visitor should be able to:

1. Understand the portfolio's main idea within 15 seconds.
2. Choose a visual topic rather than navigate a file inventory.
3. See strong evidence before reading long explanations.
4. Interact with at least a few real working examples.
5. Understand what AI did, what the user contributed, and what an expert still
   needs to validate.
6. Leave with one or two memorable project stories.

## Non-Negotiable Direction

These principles should remain stable unless the project owner explicitly
changes them.

### Visual First

- Lead with posters, maps, diagrams, motion, or interactive tools.
- Do not lead with long paragraphs or large data tables.
- Every major topic needs a recognizable hero visual.
- Important visuals should link directly to their project.

### Real Evidence

- Prefer actual project outputs over generic AI-generated decoration.
- Use real maps, slide exports, screenshots, notebooks, graphs, and code.
- Processing-style visuals may abstract a concept, but they must connect to a
  real workflow or research question.

### Honest Claims

- Clearly distinguish completed work, prototypes, plans, and speculative ML.
- Do not present screening as prediction.
- Keep uncertainty, model leakage, source provenance, and expert review visible.
- Do not imply that AI replaces scientific judgment.

### Concise Default Experience

- Default pages should be scannable and visual.
- Technical depth belongs in expanders, dedicated pages, or linked evidence.
- Avoid repeating the same explanation in multiple sections.
- Keep body paragraphs under roughly 55 words when possible.

### Mobile Matters

- The public site must remain useful from a phone.
- Mobile views should use fewer stages, larger tap targets, and shorter labels.
- Heavy interactive elements need sensible default detail levels.

## Evolving Vision

These ideas are important but can change as the portfolio develops.

- Grow from a portfolio into an AI workflow think tank.
- Use the projects as conversation starters about scientific agents, knowledge
  graphs, energy screening, model transfer, and visual reasoning.
- Rebuild older Processing concepts as modern web or Processing animations.
- Connect the website and PowerPoint through one shared visual language.
- Potentially migrate beyond Streamlit when the story and interaction design
  are stable enough to justify a custom website.

## Key Project Stories

### AI Agent Training

Human demonstrations, screenshots, screen recordings, and rubrics can become
training and evaluation material for scientific software agents.

### Critical-Mineral Knowledge Graph

Thesis notes, drawings, CSV nodes, Gephi, and future graph databases show how
research synthesis can become a queryable visual system.

### Processing Earthquake Globe

USGS events, a 3D globe, depth and magnitude encoding, and sound form the
creative-coding origin story for the portfolio.

### Pondicherry Seismic Workflow

Catalog search, station matching, waveform processing, P-wave picking, mapping,
and velocity analysis demonstrate notebook-to-application potential.

### North Slope Gas Hydrates

Public GIS layers, structural horizons, wells, assessment units, and future
wireline features demonstrate energy screening and interactive 3D reasoning.

### Rock Classification And Resource Mapping

Rock properties, geochemistry, thin sections, formation labels, and instrument
signals can become visual classes and future supervised-learning examples.

### Valles / Field Geophysics

Gravity, seismic, EM/ERT/TEM, field constraints, and uncertainty show why AI
must compare methods without flattening expert judgment.

### Moho ML Transfer

Training on Australia and testing on the USA makes model transfer, leakage, and
spatial validation concrete.

### Codex App Pipeline

Existing files, Codex, GitHub, testing, and Streamlit show how scattered work
can become a tracked application rather than repeated copy-and-paste.

## Visual Language

The shared visual system should use:

- Dots for events, files, examples, labels, or observations.
- Arrows for workflow movement and transformation.
- Pulses for magnitude, attention, confidence, or activity.
- Grids and surfaces for spatial data.
- Rings and waves for time, depth, propagation, or sound.
- Gates for validation, rubric checks, and leakage prevention.
- Gray or hatching for uncertainty and unresolved review.
- One dominant accent color per visual, with supporting elements quieter.

Refer to `docs/VISUAL_DESIGN_SPEC.md` for specific changes to each poster.
Use `data/visual_audit.csv` to track visual purpose, evidence quality,
desktop/mobile presentation, scientific review, motion opportunities, priority,
and implementation status.

## Typography And Composition

- Page title: 38-44 px desktop, 30-34 px mobile.
- Section title: 26-30 px desktop, 22-26 px mobile.
- Poster headline: 30-36 px, maximum six words.
- Poster stage labels: 18-22 px.
- Poster supporting details: 14-16 px.
- Use one dominant focal object per poster.
- Give the final output more visual weight than the input.
- Keep important text within a 40 px safe margin.
- Use bold only for the main claim, project name, or decision.

## Interaction Priorities

Highest-value interactions:

1. North Slope Structural Explorer.
2. Clickable topic posters.
3. Processing earthquake motion or video.
4. Knowledge-graph exploration.
5. Seismic waveform and pick inspection.

Interactions must clarify the project. Avoid interaction that exists only as
decoration.

## Technical Direction

- Current public frontend: Streamlit.
- Source control and deployment source: GitHub `main`.
- Public deployment: Streamlit Community Cloud.
- Primary app entry point: `app.py`.
- Structured content: CSV manifests under `data/`.
- Visual assets: `assets/project_visuals/` and `assets/topic_visuals/`.
- Interactive structural data: `assets/structural_data/`.
- Project documentation: `docs/`.

Prefer:

- Reusable helper functions over repeated page code.
- Structured manifests over hardcoded file lists when practical.
- Lightweight SVG for concept posters.
- Plotly for meaningful interactive scientific views.
- Expanders for technical detail.

Avoid:

- Reintroducing the obsolete 17 MB North Slope HTML scene.
- Depending on laptop-only `C:\Users\gargi\...` paths for public functionality.
- Adding heavy assets without a clear visitor-facing benefit.
- Duplicating the same narrative across Overview, topic rooms, and presentation
  pages.

## Source And Device Reality

- The desktop workspace and laptop do not automatically share local files.
- GitHub is the authoritative source for code and committed public-safe assets.
- Google Drive can hold source references and larger working materials.
- Original Processing sketches and the verified earthquake video may still live
  only on the laptop until intentionally synced.
- Local Windows paths are evidence references, not reliable public links.

## Safety And Boundaries

- Never commit credentials, tokens, private account data, or `.env` files.
- Do not place classified, controlled, restricted, or proprietary data in the
  public repository or Streamlit deployment.
- Public North Slope content must remain public-source.
- Future approved well-log data must be loaded only in its authorized runtime.
- Confirm that personal media is appropriate for public display before adding it.

## Current Priorities

1. Improve the nine topic visuals using the visual design specification.
2. Recover or export the correct Processing earthquake video and sketches.
3. Make the North Slope Structural Explorer visually polished on mobile.
4. Reduce remaining repeated or overly long copy.
5. Improve the knowledge-graph and seismic interactive examples.
6. Build a PowerPoint from the same concise story and visual hierarchy.

## Decisions Already Made

- The portfolio and North Slope atlas are separate repositories, but the best
  Structural Explorer is embedded directly in the portfolio.
- Overview posters must be clickable.
- Mobile View is a first-class surface.
- The old static/heavy North Slope HTML scene should not be the primary example.
- Processing visuals are central to the portfolio's identity, not a side note.
- The site should be more visual and less wordy.
- Technical plans and research details should not dominate the default view.

## Definition Of Done For A Topic

A topic is presentation-ready when it has:

1. A strong hero visual with clear hierarchy.
2. A one-sentence project question.
3. A concise explanation of what AI did.
4. Real evidence or a working interaction.
5. A clear human-validation or uncertainty statement.
6. A future direction that does not overclaim.
7. A mobile-readable layout.

## Working Practice For Future Changes

Before implementing a substantial change:

1. Read this charter.
2. Identify whether the change supports a non-negotiable goal or an evolving
   idea.
3. Check whether the same content already exists elsewhere.
4. Prefer improving evidence and visual hierarchy over adding more prose.
5. Test Overview, Mobile View, and the affected project route.
6. Commit and push to GitHub only after validation.

## Questions Still Open

- What should the final portfolio name and personal brand be?
- Which three projects should dominate the eventual PowerPoint?
- Should the long-term website remain Streamlit or move to a custom frontend?
- Which Processing sketches are worth rebuilding first after the earthquake
  globe?
- What personal contact and profile information should be public?
- How much unfinished work should remain visible versus archived?
