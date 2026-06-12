# Presentation Script - AI Think Tank Portfolio

## Goal

Use the site as a discussion tool, not as a finished trophy case. The main message is:

> I am using AI to turn scattered scientific work into visual systems people can inspect, question, and improve.

## 0:00-0:45 - Opening

Hi, my project is a visual AI think tank. It is built around one question: what changes when AI can help organize scientific work, not just write text?

The site is not meant to say every model is complete. It separates current evidence, future ML ideas, and the review gates that keep the claims honest.

What I want you to look for is whether the diagrams make the research easier to criticize.

## 0:45-1:45 - Start Page

On the start page, each tile is a discussion topic. The project is the example, but the question is the point.

For example, one topic asks how agents could learn scientific software from screenshots and recordings. Another asks whether knowledge graphs can explain critical-mineral research architecture. Another asks how public energy data could become a 3D screening workspace.

The design choice is intentional: I am trying to move away from a normal portfolio grid and toward a seminar-style wall of ideas.

## 1:45-3:15 - Topic Two: Critical Minerals Knowledge Graph

This is the second topic, and it is the clearest example of what I changed.

Originally, the graph images were too small and repeated. Now the page starts with one source graph and one readable redraw. The redraw shows the same idea in a way a visitor can actually read: Bayan Obo in the center, minerals, host rock, fluid events, and source evidence around it.

The main AI question is: how do we move from papers, captions, and Adobe sketches into a graph that a geologist can review?

SciBERT is a scientific text encoder. I would use it to tag scientific words in papers and captions.

MatSciBERT is similar, but it is trained for materials science language. That matters because mineral names, chemical formulas, phases, and materials terms are more specialized than normal English.

GraphSAGE is a graph neural network method. The simple way to explain it is: a new node learns from its neighbors. If I add a new mineral, deposit, or paper node, GraphSAGE can aggregate information from nearby reviewed nodes.

R-GCN is useful because not every edge means the same thing. A graph edge that says "contains" is different from one that says "hosted by" or "evidence for." R-GCN uses relation-specific weights, so the model does not flatten all relationships into one generic connection.

The important claim is not "AI discovered the answer." The claim is: AI can suggest entities and relationships, but the geologist accepts, edits, or rejects the edge before it becomes part of the graph.

## 3:15-4:30 - How Models Are Explained Across Topics

Every topic now has a "How the model works" panel.

The agent topic shows UI tokens, OCR, state encoding, and action traces.

The North Slope topic shows well-log features moving into an ANN-style hydrate model with leakage gates.

The seismic topic shows waveform windows, pick proposals, uncertainty bands, and human review.

The rock classification and SEM topics show image branches, source labels, and expert correction.

The point is to make ML vocabulary visible. If I say "model," I need to show what enters it, what moves inside it, what comes out, and what gate prevents overclaiming.

## 4:30-5:45 - North Slope / Energy Screening

The North Slope topic is about public data and energy screening.

The future ML architecture is not just "predict hydrates." It is: collect public geologic sources, align well-log style features, separate target data from feature generation, use well-held-out validation, and route low-confidence intervals to review.

This is where the site connects AI to real workflow value. The useful product is not a flashy map alone. It is a workspace where public sources, provenance, uncertainty, and expert review are visible.

## 5:45-6:45 - Software Agents And Visual Workflows

The agent topic is about how future AI systems could learn scientific software tasks.

If an agent only sees a final screenshot, it cannot reliably learn the work. It needs the prompt, rubric, files, OCR text, UI boxes, action sequence, mistakes, corrections, and final accepted output.

That becomes an action trace. The model can then be evaluated on held-out software tasks instead of just sounding right in a chat.

## 6:45-7:45 - Honest Failure Gates

A theme across the site is that every AI output needs a visible failure gate.

For time series, the gate is future leakage and walk-forward validation.

For maps, the gate is spatial leakage or false visual agreement.

For seismic, the gate is weak signal, bad metadata, or unreviewed picks.

For SEM images, the gate is proxy overclaim: a visible texture label is not automatically a climate or reservoir interpretation.

These gates are what make the project more serious than just "AI made a diagram."

## 7:45-8:30 - Closing

The final message is that AI can help convert scattered project evidence into visual, reviewable systems.

But the human part is still essential: choosing variables, checking sources, rejecting weak claims, and deciding what the model is actually allowed to say.

What I want feedback on is whether these diagrams make the ML ideas easier to criticize. If someone can point to a node, edge, feature, or gate and say "I disagree with that," then the website is doing its job.

## Backup Lines

If someone asks if the models are already trained:
No. The site separates current evidence from future model architecture. The value right now is making the data, model objective, and validation gates explicit.

If someone asks why graphs:
Because graphs let relationships stay visible. Papers are linear text, but geologic systems are connected: minerals, host rocks, processes, locations, sources, and uncertainty.

If someone asks what you built with AI:
I used AI and Codex to organize project evidence, build the Streamlit app, create visual diagrams, structure ML architecture ideas, and push the changes through GitHub.

If someone asks what needs work:
The strongest next step is replacing remaining abstract sections with more source-specific visuals and testing which diagrams people understand without explanation.
