# Site Review After June 10 Push

## Deployment Status

- Latest commit pushed to GitHub `main`: `aa1f508 Integrate Gmail source updates`.
- The project charter says GitHub `main` is the Streamlit Community Cloud deployment source, so the pushed commit is now available for Streamlit Cloud to redeploy.
- Local verification was done at `http://localhost:8501` from the pushed code.
- I could not confirm the public Streamlit URL from the repo or likely URL guesses. The tested guesses returned 404:
  - `https://ai-powerpoint-workflow-portfolio.streamlit.app`
  - `https://ai-workflow-think-tank.streamlit.app`
  - `https://rnanda442-ai-powerpoint-workflow-portfolio-app.streamlit.app`

## Vision Lens Used

The review used the project charter and `docs/PROJECT_VISION_AND_GOALS.md` as the target.

The site should feel like a visual AI think tank, not a finished-project catalog. The correct page order is:

1. Question worth discussing.
2. Visual or motion concept.
3. Real project example.
4. What AI/tools did.
5. What the human supplied or validated.
6. Bottleneck.
7. Plausible future ML workflow.
8. Visible output or decision.
9. Audience challenge prompt.

The key design rule is still: visuals before prose, real evidence before decoration, and visible validation before claims.

## Current Overall State

The site now looks much closer to the intended direction than before the June 10 update. The full-page black background problem is fixed locally: pages now use a light technical studio background, while dark visuals remain contained inside posters, videos, and technical scenes.

The strongest current surfaces are:

- Start page topic wall.
- North Slope topic and Structural Explorer.
- REE / critical-minerals topic because it has many real slide exports.
- Rock classification topic because it has real slide/image evidence.
- Vision Board as a source/control page.

The weakest current surfaces are:

- Presentation View, because it is still a dashboard of talk assets instead of a controlled presentation rail.
- Processing Visual Lab, because it explains the sketch language but does not yet show enough finished motion/sketch outputs.
- Contact / Ideas, because the wording is honest but could be more visually tied to the rest of the think tank.
- Some topic pages still have too many downstream sections and expanders before the viewer gets one clean story.

## Page-By-Page Review

### Start

What is there:

- Opens with "Pick a question. Let's talk."
- Shows a clickable discussion wall of nine topic cards.
- Each card leads with a topic question, proof label, and "raise your hand" invitation.
- The page has 12 visible images and 9 topic cards in the local audit.

How it looks:

- This is the closest page to the vision. It does feel like a topic wall rather than a ranked project portfolio.
- The lighter background makes the cards easier to read.
- The topic cards still feel somewhat separate from each other.

What it needs:

- Add subtle connecting routes between cards so the wall reads as one AI workflow system.
- Add a small "current evidence / future idea / validation" legend.
- Keep the overview concise; do not add more explanatory paragraphs.

Specific next idea:

- Build a background route layer behind the cards:
  - files/screenshots -> Codex app pipeline
  - public data -> North Slope
  - papers/slides -> REE graph
  - waveforms -> seismic
  - uncertainty gates -> Moho/validation

### Vision Board

What is there:

- Hero explains the portfolio direction.
- New Gmail source cards are visible:
  - design tokens
  - lighter theme
  - ML baseline-first principle
  - chronological/spatial validation
  - data quality monitoring
  - CreditScoreV4 production/fairness case thinking
- Drive slide and document source cards are connected.
- Vision-board metrics and implementation queues remain visible.

How it looks:

- It is useful as a build-control room.
- It is still more operational than visual.
- The new source cards are clear and readable.

What it needs:

- Convert the Vision Board from a table/control page into a visual Now / Next / Later canvas.
- Keep the tables downloadable or in expanders, but lead with three zones:
  - Now: topic wall, North Slope explorer, source intake, lighter design.
  - Next: slide-to-site sections, Processing sketches, presentation rail.
  - Later: modular app and possible custom frontend.

Specific next idea:

- Build a "Vision map" with three columns connected by arrows:
  - Now = evidence and readability.
  - Next = visual/motion proof.
  - Later = platform and reusable presentation system.

### Structural Explorer

What is there:

- Working Plotly 3D North Slope structural explorer.
- Horizon controls and overlays.
- Uses public wells/boundaries/assessment context.

How it looks:

- This is one of the strongest concrete interactions.
- It proves the site is not just screenshots.
- It still opens as a technical control surface, not as a guided story.

What it needs:

- Add a short visual legend above or beside the plot:
  - horizon surfaces
  - public wells
  - assessment units
  - what can/cannot be concluded
- Add a "why this matters" panel after the plot:
  - public source reuse
  - energy screening
  - not a resource estimate
  - needs expert review

Specific next idea:

- Add an initial "guided view" mode before advanced controls:
  1. Show topographic + basement surface.
  2. Add wells.
  3. Add assessment outlines.
  4. Ask: "Where would a human inspect next?"

### North Slope Topic

What is there:

- Strong dark workflow poster.
- Current/future split: 3D Plotly map, source library, wireline ML scaffold -> feature engineering, ranked hydrate intervals.
- Working 3D structural explorer embedded in topic context.
- Local source-library index.
- New validation panel from Gmail ML notes:
  - inputs to make visible
  - model families
  - validation gates
  - monitoring story
- Embedded well-log scaffold link/section later in the page.

How it looks:

- The dark poster is appropriate because it is contained.
- This is currently the most complete topic.
- The page still has many sections, so the viewer may not immediately understand the one best story path.

What it needs:

- Make the 3D explorer the dominant hero for this topic, not only an embedded section after the poster.
- Add the synchronized vertical well panel idea from `website_change_ideas.csv`:
  - gamma ray
  - resistivity
  - density
  - rock unit
  - hydrate clue
  - uncertainty
- Replace generic "ranked hydrate intervals" language with "review queue" or "screening candidates" to avoid overclaiming.

Specific sketch idea:

- "Public data -> 3D decision space":
  - Left: public maps, papers, wells, wireline logs, geology.
  - Center: structural block with vertical wells.
  - Right: three branches: investigate, need more data, low priority.
  - Gate over the branch point: provenance + stratigraphy + leakage + expert review.

Slide-source opportunity:

- Use `VISUAL UPDATED North Slope Gas Hydrate Reservoir Characterization Research Overview Slides` as the primary source for the topic hero/value story.
- Add one deck-derived section called "How the North Slope deck becomes the app":
  - slide concept
  - source library
  - 3D explorer
  - well-log scaffold
  - validation gates

### REE / Critical Minerals Topic

What is there:

- Strong source-to-graph visual: prompt, Adobe sketch, Excel fields, Gephi, unknown/question outputs.
- Many real PowerPoint slide exports:
  - system overview
  - map and spider diagram
  - Bayan Obo interpretation
  - deposit model
  - trace-element model
  - summary model
- Clear "question, not discovery" language.

How it looks:

- This is one of the strongest visual evidence pages because it has many real slide-derived assets.
- The current/future distinction is understandable.
- It still needs clearer separation between source-supported edges, AI suggestions, and geologist reasoning.

What it needs:

- Add a compact "edge legend":
  - solid = source-supported
  - dotted = AI-suggested
  - orange = geologist reasoning
  - gray = unresolved
- Add one query-beam sketch showing GraphRAG/Neo4j value:
  - query enters graph
  - evidence summary
  - relationship gap
  - extraction hypothesis
  - expert review

Slide-source opportunity:

- The REE slide exports are already strong. The next pass should crop each slide to one key evidence region rather than showing full slides when labels are too small.

### Seismic / Pondicherry Topic

What is there:

- Current/future story around ObsPy notebook, waveform QA, velocity maps, arrival-picking ML, and review.
- EarthScope slide evidence appears.
- The future workflow mentions pick timing, distance, velocity, and uncertainty.

How it looks:

- It has the right ingredients, but it is less visually immediate than North Slope, REE, or Rock.
- It needs one dominant waveform interaction or sketch.

What it needs:

- Add a synchronized three-panel visual:
  - waveform trace with pick
  - confidence band
  - event/station or velocity map
- Make "override" visible: AI suggests, human accepts/edits/rejects.

Specific sketch idea:

- "PICK | CONFIDENCE | OVERRIDE":
  - scrolling trace
  - vertical pick line with confidence halo
  - small map updates when pick changes
  - gray zone for noisy/uncertain arrivals

Slide-source opportunity:

- Use `Exploration Seismology FInal Land data`, `EarthScope` deck images, and possibly `NoisePy` as new section sources:
  - seismic training context
  - notebook workflow
  - ambient-noise workflow candidate
  - uncertainty review

Possible new section:

- "From waveform notebook to reviewable seismic assistant."

### Rock Classification Topic

What is there:

- Strong concept poster: measured signals -> range gates -> classified GIS zones.
- Real visuals:
  - chemical classification reference
  - thin-section slide
  - formation classification outputs
  - Moho depth formation map
  - raster classification map
  - chemical classification chart

How it looks:

- This is visually strong because it has real images and the concept is easy to understand.
- It still needs clearer scientific validation: what labels mean, what uncertainty means, and what is only a future ML idea.

What it needs:

- Add a "label quality" gate:
  - known rock/mineral class
  - uncertain/mixed class
  - needs human petrography/geochemistry review
- Add an extended 3D resource-model sketch:
  - public data -> classified cells -> uncertain cells stay gray.

Slide-source opportunity:

- Use `SEM petrography` as a new petrography subsection.
- Use the existing thin-section and classification slide assets as the real proof layer.

Specific wording change:

- Replace "resource maps" in some headings with "resource-mapping questions" or "candidate map layers" unless the output is actually validated.

### Valles / Field Geophysics Topic

What is there:

- Current/future story around gravity maps, SAGE slides, uncertainty review, data fusion, interpretation dashboard.
- Real slide evidence from SAGE/Valles deck.

How it looks:

- It is credible but still reads as a collection of methods.
- It needs the strongest visual concept: methods overlap but do not collapse into false certainty.

What it needs:

- Add the four-panel/fusion visual:
  - gravity
  - EM/ERT/TEM
  - seismic
  - fused interpretation with unresolved gray areas
- Add visible "conflict" markers where methods disagree.

Specific sketch idea:

- "Combine evidence, not certainty":
  - translucent fields slide onto common geometry
  - agreement glows
  - disagreement stays gray
  - clicking/hovering a conflict reveals acquisition limits or method sensitivity

Slide-source opportunity:

- Use `Alaska Seismotech portfolio` and `SAGE / Valles` slide images to expand the field/geophysics topic.

### Processing Visual Lab

What is there:

- Explains dots, arrows, pulses, gray clouds, gates, grids, rings, and color shifts.
- Shows static SVG visual studies and topic sketch plans.
- Includes storyboard concepts.

How it looks:

- It is useful as a planning page.
- It is not yet a showcase page.
- It explains "what sketches should do" more than it demonstrates finished sketches.

What it needs:

- Promote one or two finished motion studies to the top.
- Add short loop assets or embedded video/GIF:
  - earthquake globe
  - North Slope decision space
  - seismic pick confidence
  - app pipeline leakage gate

Specific next sketch priority:

1. Earthquake globe motion/video.
2. Seismic pick-confidence loop.
3. Valles uncertainty fusion.
4. North Slope source-to-decision loop.

Wording change:

- Reduce the opening explanation. Lead with a motion grid, then put the visual-language glossary below.

### Machine Learning Future

What is there:

- ML Future page now includes new Gmail source notes.
- It has baseline/validation/data-quality/fairness concepts.
- It maps each project into inputs, variables, methods, and outputs.

How it looks:

- Better after the Gmail update.
- Still a build-room page, not a public-first page.
- It can become overwhelming because it covers every project.

What it needs:

- Convert it into a "validation room" with fewer, stronger gates:
  - baseline
  - split
  - leakage
  - drift
  - fairness/segment check
  - expert review
- Move detailed project rows into expanders or secondary cards.

Specific new section:

- "ML claims checklist":
  - What is the baseline?
  - What is held out?
  - What could leak?
  - What data quality changed?
  - Which segment could fail?
  - What would an expert reject?

### Presentation View

What is there:

- Talk view with core argument, workflow architecture, evidence selectors, expert questions, talk path, and folder table.

How it looks:

- It is useful for the builder, but it does not yet feel like the final presentation mode.
- It is too much like a dashboard of presentation assets.

What it needs:

- Replace with a seven-frame presentation rail:
  1. Question.
  2. Proof.
  3. AI action.
  4. Working output.
  5. Human review.
  6. Future product.
  7. Audience challenge.
- Each frame should use one dominant visual and one short sentence.

Specific slide/web alignment:

- The web Presentation View should become the source for the eventual PowerPoint.
- The strongest first deck should probably use:
  1. AI think tank opener.
  2. North Slope public-data screening.
  3. REE knowledge graph.
  4. Seismic or rock classification.
  5. Scientific agent/Codex workflow.
  6. Validation gates.
  7. Ask/challenge.

### Mobile View

What is there:

- A simplified list of major topics with visual cards.
- Links into topic pages and Structural Explorer.

How it looks:

- It supports the "mobile matters" requirement.
- It is simpler than desktop, which is good.
- It still feels like a list rather than a mobile-native visual wall.

What it needs:

- Larger tap areas and fewer topics above the fold.
- Add "Start with North Slope / Start with REE / Start with Seismic" quick picks.
- Consider hiding build-room navigation on mobile unless explicitly opened.

### Contact / Ideas

What is there:

- Honest explanation that the owner is early, wants conversation, and is asking for experienced people to challenge the work.

How it looks:

- Tone is aligned with the vision.
- It is text-heavy and not visually tied to the rest of the system.

What it needs:

- Add three visual prompt cards:
  - "Correct a claim"
  - "Suggest a method"
  - "Share a workflow"
- Add a short list of best feedback types:
  - ML validation
  - geoscience interpretation
  - energy workflow value
  - scientific agent evaluation
  - slide/story clarity

Wording suggestion:

> I am showing unfinished systems because that is where expert feedback matters most. If you see a better validation test, a stronger dataset, a clearer visualization, or a false assumption, that is the conversation I want.

## Slide / PowerPoint Source Opportunities

Current source inventory suggests these additions:

1. North Slope updated deck:
   - Use as the primary North Slope narrative and visual source.
   - Add a section connecting deck slides to the app: source library -> 3D explorer -> well-log scaffold -> validation gates.

2. Thesis Ch.1 / REE deck:
   - Already has the strongest slide exports.
   - Next step is better crops and edge legends, not more full-slide galleries.

3. ADVGIS Final:
   - Candidate for Moho / GIS / spatial ML transfer section.
   - Could support a stronger "spatial validation and leakage" visual.

4. Exploration Seismology Final Land Data and EarthScope deck:
   - Candidate for seismic workflow expansion.
   - Use to replace any generic seismic imagery with slide-derived training/method evidence.

5. Near-Surface Dwellers Presentation:
   - Could become a new near-surface geophysics topic if it has enough distinct value from Valles/seismic.

6. Alaska Seismotech portfolio:
   - Candidate source for field/geophysics visuals.
   - Could strengthen Valles or a broader applied geophysics topic.

7. SEM petrography:
   - Candidate for a petrography subsection inside Rock Classification.
   - Good for visual ML/multimodal classification discussion.

8. NoisePy:
   - Candidate for a new ambient-noise/seismic software topic, or a subsection under Seismic.

9. Older Portfolio / Professional Profile:
   - Use only for identity and framing.
   - Do not let it pull the site back into a generic personal portfolio.

## Highest Priority Next Changes

1. Build the Presentation View rail.
   - This directly supports the upcoming presentation and the eventual PowerPoint.

2. Make North Slope more visually decisive.
   - 3D explorer as hero.
   - Vertical well-log panel.
   - Investigate / more data / low priority branches.

3. Add one finished motion/sketch study.
   - Earthquake globe if the video is available.
   - Otherwise seismic pick-confidence or North Slope decision loop.

4. Convert Vision Board into Now / Next / Later canvas.
   - Keep tables as implementation details.

5. Strengthen validation language everywhere.
   - Use "screening candidate", "review target", "question", and "workflow" more often than "prediction", "resource map", or "discovery".

## Questions For Owner Review

1. What is the real public Streamlit URL?
2. For the presentation, which three topics should dominate: North Slope, REE, Seismic, Rock, Agent Training, or Codex pipeline?
3. Should North Slope be the first topic visitors see, or should the topic wall remain neutral?
4. Can the updated North Slope slide deck be exported into clean slide images for the site?
5. Is `NoisePy` important enough to become its own topic, or should it support the existing seismic topic?
6. Should `Near-Surface Dwellers` become a new near-surface geophysics topic?
7. What personal photo/profile information is approved for the public About page?
8. Which Processing sketch should be rebuilt first if the original earthquake globe files are still missing?
9. Are there any North Slope data or claims that must stay out of the public Streamlit repo?
10. For the final PowerPoint, should the tone be more technical, more personal, or more DOE/energy-management focused?
