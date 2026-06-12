# Branching 15 Minute Website Script - June 12, 2026

Use this as a flexible talk track. Do **not** read every topic branch in one run. The point is:

- 2 minutes: introduce the website.
- 1 minute: ask the room which topic they want.
- 10 to 11 minutes: cover 3 or 4 topic branches.
- 1 minute: close with the main message.

Each branch is written in a casual read-aloud voice. Keep the pauses. The word "like" is included on purpose so it sounds more like a real explanation and less like a technical paper.

## 0:00-2:00 - Opening

Hi, so this is my AI portfolio website, but I do not really want to present it like a normal portfolio where it is just, like, here are projects and here are screenshots.

[pause]

The idea is more like a visual think tank. It is showing how different science and software projects can become AI or machine-learning workflows, but without pretending that every model is already finished.

So as I go through it, I want you to look for three things.

First, the source evidence. Like, what is the actual project, slide, notebook, image, or data source behind the topic?

Second, the ML diagram. That is where I am trying to show what goes into the model, what the model is actually doing, and what comes out.

Third, the review gate. This is really important. A lot of AI presentations sound too confident. I am trying to show the part where a human still checks the model, or where the model is not allowed to make a claim yet.

[pause]

The website is organized by topics. So instead of me forcing one linear path, I can ask: which room do you want to go into? If we pick one topic, I can explain the real project, the machine-learning terms in plain English, and then how the same idea transfers to other sectors like energy, banking, startups, agriculture, public-sector work, marketing, or operations.

The main sentence for the whole website is: AI should help turn scattered work into systems people can inspect, question, and improve.

## 2:00-3:00 - Audience Choice Setup

[show the topic wall]

So these are the topic rooms. Each one has a current project, but the bigger question is what reusable AI workflow it teaches.

For example, one room is about AI agents learning scientific software from screenshots and task recordings. Another one is about knowledge graphs for critical minerals. Another one is about public energy data and hydrate screening. There are also topics on seismic notebooks, rock classification, Valles field geophysics, near-surface methods, ambient-noise monitoring, SEM petrography, and even a stock app workflow for model-risk discipline.

[pause]

Pick one that sounds interesting, and I will go into that avenue.

If nobody picks, I would start with: AI workflow, critical minerals graph, North Slope energy screening, and one image/geophysics topic.

## Universal Transition Into Any Topic

Use this when you click into a topic:

Okay, so this topic has three layers. The first layer is the actual evidence from the project. The second layer is the ML diagram, which is like the architecture of the future version. The third layer is the transfer idea: where this same pattern could matter outside this one project.

[pause]

I am going to explain the model terms in plain English, not as math first.

## Branch 1 - AI Agents Learn Scientific Software

[click: How AI Agents Learn Scientific Software]

This one is about how AI agents could learn real scientific software work. Not just chat answers, but actual workflow steps. Like opening QGIS, checking layers, using files, making mistakes, fixing them, and exporting something that a human says is acceptable.

The ML diagram is basically: screen recording plus prompt plus rubric goes into UI tokens and action traces. A UI token is just a screen element the model can understand, like a button, menu, layer name, file path, or error message.

The first model term is OCR or UI state encoder. In plain English, that means the model reads what is on the screen and turns it into structured pieces.

Then behavior-cloning transformer means the model watches a human sequence and learns the next action. Like: observe the screen, click the tool, inspect the result, correct if needed.

Replay simulator means you do not just trust the final screenshot. You rerun the task and see if the agent can actually do it again on a held-out task.

[pause]

The other-sector use cases are pretty direct. In energy project drafting, an agent could help prepare public-source maps and reports. In banking operations QA, it could watch a workflow and check if the analyst followed the right steps. In startup app delivery, it could help repeat build-test-debug cycles. In commerce back-office automation, it could learn order, inventory, or dashboard workflows.

The boundary is: the agent should not just do risky file actions silently. It needs a human approval gate.

## Branch 2 - Critical Minerals Knowledge Graph

[click: AI + Knowledge Graphs For Critical Minerals]

This topic is about turning critical-mineral research into a graph. Like, papers and slides have a lot of useful relationships, but they are trapped in paragraphs. A graph makes the relationships visible: deposit, mineral, host rock, process, source, and evidence.

The ML diagram starts with sources: thesis slides, Gephi exports, node tables, edge tables, captions, and figures. Then AI helps extract entities and rank relationships.

SciBERT or MatSciBERT is basically a science-language reader. It is better at terms like minerals, formulas, phases, and technical captions than a generic text model.

Relation cross-encoder means the model looks at two things, like a mineral and a host rock, plus the source sentence, and asks: is this relationship actually supported?

GraphRAG means the answer comes through a graph path and then pulls the source text behind it. So it is not just a fluent answer. It is an answer with traceable evidence.

GraphSAGE or R-GCN means nearby graph nodes help each other, but relation types stay separate. Like "hosted by" is not the same thing as "evidence for."

[pause]

The same pattern transfers to critical-mineral targeting, banking risk maps, startup knowledge bases, and marketing relationship graphs. Anywhere there are documents and relationships, this matters.

The careful line is: this is not AI discovering minerals by itself. It is AI helping organize relationships for expert review.

## Branch 3 - Processing Earthquake Globe

[click: First AI Visualization: Earthquake Globe]

This one is the origin-story topic. It is about using Processing to turn earthquake data into a globe visualization. So the project starts as creative coding, but the future ML idea is: can a visual become a reproducible feature table?

Like, earthquakes have latitude, longitude, depth, magnitude, and time. A globe makes that intuitive. But a model needs rows and features. So the diagram shows event points becoming region-time windows.

Poisson or negative-binomial GLM is the simple baseline. It is basically asking: how many events happened in this region and time window, and is that count unusual?

LightGBM anomaly ranker is the more flexible challenger. It can rank unusual windows from lagged counts, depth bins, magnitude bins, and cluster features.

Hawkes process or ST-DBSCAN is about clustering events in space and time. So if one event changes the likelihood of nearby events, that is the type of pattern it is thinking about.

[pause]

The multi-sector transfer is hazard communication, logistics anomaly windows, finance volatility windows, and equipment monitoring. Like, the same idea is: events happen over space and time, and we need a visual plus a reviewable model, not just a dramatic animation.

The gate here is no forecast claim unless future-window validation is defined.

## Branch 4 - Seismic Notebooks And Pondicherry

[click: Seismic Notebooks And Pondicherry]

This topic is about seismic notebooks becoming a cleaner QA pipeline. The current evidence is notebooks, waveform visuals, field or training images, and seismic processing figures.

The ML diagram is: catalog search, station metadata, waveform windows, quality checks, model-assisted picks, uncertainty, and human review.

SeisLM is a seismic foundation model. In plain English, it is a pretrained waveform model. It learns useful waveform representations before being adapted to tasks like event detection or phase picking.

PhaseNet or EQTransformer are phase-picking models. They propose P-wave and S-wave arrival times. But the key word is propose.

LightGBM waveform QA is simpler. It uses features like signal-to-noise ratio, missing channels, metadata, and station quality to rank what needs review.

[pause]

The use cases transfer to energy cloud processing, agriculture remote sensing, insurance geohazard triage, and research collaboration. The common pattern is noisy data going into a QA workflow before anyone trusts the output.

The sentence I would use is: the model proposes, uncertainty stays visible, and the human reviews.

## Branch 5 - North Slope Energy Screening

[click: AI For Energy Screening Workflows]

This is one of the strongest energy-sector topics. It is about public geology, source libraries, maps, well-log ideas, and a future hydrate screening workflow.

The ML diagram is not just "predict hydrates." It is more like: public sources and well-style features go into a feature table, then the model has to pass leakage checks and leave-well-out validation.

Ridge or ElasticNet baseline is the simple starting point. It gives a transparent first estimate. If a fancy model cannot beat that, the fancy model is not useful.

Keras ANN hydrate model is a neural network that could learn nonlinear combinations of log curves like resistivity, porosity, gamma ray, Vp, and Vs.

XGBoost or LightGBM challenger is a tree-based model. It asks lots of split questions and combines them.

Leave-well-out validation means you train on some wells and test on a different well. That matters because random depth rows from the same well can make the model look way better than it really is.

[pause]

Other-sector use cases are energy source libraries, real-estate due diligence, supply-chain site intelligence, and public-sector data portals. So the broader pattern is not just geology. It is: collect public sources, structure them, screen options, and keep uncertainty visible.

The careful claim is: this is a screening scaffold, not a final production hydrate model.

## Branch 6 - Rock Classification

[click: AI For Visual Geoscience Classification]

This topic is about visual and chemical classification. The evidence is thin-section slides, chemical diagrams, formation maps, raster outputs, and labels.

The ML diagram shows separate evidence branches. Images go one way, chemistry goes another way, and text or source metadata goes another way. Then a fusion model can combine them.

EfficientNet or ResNet is the image branch. It learns visual patterns from image crops, like textures or map patches.

XGBoost or LightGBM chemistry branch is the tabular branch. It learns from chemical values, ratios, spider diagrams, or formation variables.

Late-fusion MLP means the branches stay separate first, then a small model combines them into one ranked label.

CLIP or SigLIP retrieval means the system can find similar labeled examples instead of immediately saying, "this is definitely the class."

[pause]

The transfer examples are resource mapping, precision agriculture soil classes, construction material screening, and environmental land-cover QA. Like, this same pattern works any time images plus measurements plus labels need to become a review queue.

The risk is weak labels or same-sample leakage. A nice-looking classification is not enough.

## Branch 7 - Valles Caldera Field Geophysics

[click: SAGE / Valles Caldera Geophysics]

This topic is about field geophysics and uncertainty. The current project has SAGE/Valles evidence, maps, line data, field photos, and different geophysical methods.

The ML diagram is really a disagreement board. It is not trying to force all methods into one perfect answer. It shows where methods agree, where they conflict, and where review is needed.

LightGBM conflict ranker is a model that ranks zones as agreement, conflict, insufficient evidence, or needs review.

Gaussian Process uncertainty means the model gives a smooth estimate but also shows where it is uncertain.

U-Net segmentation is an image-like model that could mark zones in gridded geophysical panels, but only if labeled examples exist.

Survey graph model means survey lines, zones, and method intersections become nodes and edges.

[pause]

The multi-sector use cases are geothermal surveys, infrastructure corridor risk, water-resource screening, and site-remediation planning. The broad pattern is comparing imperfect methods without hiding disagreement.

The important phrase is: do not let AI make the map cleaner than the evidence.

## Branch 8 - Near-Surface Geophysics

[click: AI For Near-Surface Geophysics]

This topic is close to Valles, but more focused on shallow field methods. The evidence includes hammer seismic, ERT, TEM, field notes, line intersections, and geologic units.

The ML diagram starts with line geometry. That just means the model needs to know where each field line was actually measured. If the geometry is wrong, the comparison is wrong.

LightGBM method-conflict classifier ranks intervals as agreement, conflict, missing context, or review target.

Gaussian Process or Bayesian surface means uncertainty is part of the output, not a footnote.

Leave-line-out validation means train on some survey lines and test on a different line. Like, can the method transfer across the field area, or did it memorize one line?

[pause]

The transfer examples are near-surface engineering, farm drainage mapping, utility siting, and wetland monitoring. So this is not only a geophysics story. It is a field-decision story.

The gate is: possible unit labels should not become asserted unit claims unless the field evidence supports it.

## Branch 9 - Moho ML / Transfer Testing

[click: Supervised ML For Moho Depth Mapping]

This is the cleanest validation topic. The question is: if a model trains on one region, can it transfer to another region?

The diagram is basically Australia training data going into gravity and crustal features, then simple baselines, then tree or neural models, then a USA transfer test.

Ridge or GAM reference is the simple benchmark. It gives you a sanity check.

LightGBM or XGBoost regressor predicts a continuous value, like Moho depth, from geophysical features.

Keras ANN is the neural network challenger. It can learn nonlinear patterns, but it is less transparent.

Gaussian Process residuals means the error map matters. Where the model is wrong may reveal missing geology, bad features, or transfer limits.

[pause]

The cross-sector examples are hydrate screening, reservoir analog ranking, carbon-storage review, and energy decision support. The wider lesson is that a model is not trustworthy just because it scores well where it was trained.

The plain-English line is: transfer is the honesty test.

## Branch 10 - Ambient-Noise Seismology

[click: AI For Ambient-Noise Seismology]

This topic is about continuous seismic data. The hard part is scale. Continuous records become station pairs, cross-correlations, stacks, monitoring windows, and QC decisions.

The ML diagram is a monitoring ladder. Signals move through preprocessing, station-pair CCFs, stable stacks, quality classification, anomaly triage, freshness checks, and human alert review.

SeisLM-style embedding means a pretrained waveform model turns messy signal windows into useful features.

LightGBM CCF-quality classifier scores whether a station-pair cross-correlation looks reliable.

Isolation Forest is an anomaly model. It finds unusual windows without needing every bad case labeled ahead of time.

Freshness or seasonal gate checks whether the data are current and whether the change could be seasonal or instrument-related.

[pause]

The transfer use cases are volcano monitoring, infrastructure vibration alerts, industrial equipment monitoring, and city-scale subsurface sensing. The broader point is continuous monitoring with review gates.

The careful line is: weak correlations should go to QC, not directly to alerts.

## Branch 11 - Stock Workflow / Model Risk

[click: AI App Building, Automation, And Model Risk]

This topic is not here because stock prediction is the same as geoscience. It is here because the workflow discipline transfers.

The ML diagram is saved data, refresh time, past-only features, baseline model, challenger model, walk-forward validation, drift monitor, fallback path, and claim-language gate.

Persistence baseline means a simple rule: assume the next value acts like the recent past. A fancy model has to beat that.

ElasticNet is a cautious linear model that shrinks weak signals.

LightGBM challenger is the more flexible nonlinear model.

Walk-forward validation means train on the past, test on the next time window, move forward, and repeat. Like, no peeking into the future.

[pause]

The transfer examples are finance dashboards, sales forecasting, inventory planning, and marketing spend monitoring. This is basically the business-app version of the same rule: build fast, but validate honestly.

The gate is: do not let a polished dashboard hide weak assumptions.

## Branch 12 - SEM Petrography

[click: AI For SEM Petrography And Climate Proxies]

This topic is about image-based scientific labeling. SEM images can show tiny mineral textures, grains, pores, and clay morphology. But interpretation is the dangerous part.

The diagram separates observation from claim. Image crops and scale bars go into visible label proposals. Then expert correction and literature links come before any proxy interpretation.

EfficientNet or ResNet patch classifier labels visible image patterns.

U-Net or Mask R-CNN segmentation outlines grains, pores, fractures, or clay patches if reviewed masks exist.

CLIP retrieval finds similar expert-labeled images and captions.

Proxy claim gate is the most important term. It blocks the jump from "this texture is visible" to "this proves a climate or reservoir interpretation."

[pause]

The multi-sector use cases are petrography review, materials QA, agriculture soil microscopy, and manufacturing defect triage. The shared pattern is image labels with expert review before high-stakes claims.

My simple line is: visible label first, proxy claim later.

## If You Need A Fast 30 Second Version Of Any Branch

Use this template:

This topic starts with real evidence, not a generic AI idea. The ML diagram shows what enters the model, what the model does, what output it proposes, and what gate blocks overclaiming. The model terms are here so the audience can see them visually instead of just hearing vocabulary. The same pattern transfers to other sectors because the basic workflow is the same: messy evidence becomes structured inputs, a model ranks or labels something, and a human reviews the risky part.

## Closing - Last 60 Seconds

So the point of the website is not that every model is already trained. The point is that each project can be turned into a more serious AI workflow if the source evidence, model inputs, definitions, outputs, and review gates are visible.

[pause]

Like, if someone disagrees with the diagram, that is actually good. That means the website gave them something concrete to question.

The final message I want to leave is: AI should not hide the scientific reasoning. It should make the reasoning easier to inspect.

Thank you. I would really want feedback on which topic felt clearest and which diagram still needs to be simplified.

## Backup Lines For Questions

**If someone asks, "Are these models already trained?"**

Not all of them. The site separates current project evidence from future ML architecture. The value right now is making the model plan and validation gates explicit.

**If someone asks, "Why so many topics?"**

Because the website is testing one reusable idea across different evidence types: screenshots, graphs, waveforms, maps, well logs, images, and dashboards.

**If someone asks, "What did AI actually do here?"**

AI and Codex helped organize evidence, build the Streamlit site, generate diagrams, clean topic structure, write code, and turn scattered files into a reviewable system.

**If someone asks, "What is the strongest next step?"**

The strongest next step is to pick two or three topics and make the diagrams even more interactive, so people can move from source evidence to model input to review gate without needing as much explanation.

