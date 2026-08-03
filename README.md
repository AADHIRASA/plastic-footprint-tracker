# plastic-footprint-tracker
Plastic Footprint Tracker
About this project

The Plastic Footprint Tracker is a tool that estimates a person's daily single-use plastic footprint. Based on a few quick questions about everyday usage — plastic bottles, bags, straws, cups/cutlery, and packets/wrappers — it calculates an estimated CO2 footprint, total plastic weight, and the longest decomposition time among the items used, then generates a readable summary (with the option to save it as a text report).

The project includes a CLI (command-line) version (project.py), a browser version (index.html), and a printable awareness poster (plastic-awareness-poster.pptx).

This project was originally built as a CS50x Final Project, and was developed with the help of AI (Claude, by Anthropic) as a guided learning exercise — the logic, testing, and documentation were built and reviewed personally, with step-by-step explanation and support from the AI tool throughout the development process.

Problem Statement

Public awareness campaigns on single-use plastics are often limited to a single event — a talk, a poster, or a pledge signed on the day — with little follow-through afterward, and little way for individuals to see, in concrete terms, how much plastic waste they personally generate. Without a simple way to quantify personal plastic usage, awareness messages tend to stay abstract and rarely translate into a measurable understanding of individual impact.

There was a need for a simple, accessible tool that lets a person enter their everyday plastic usage and immediately see a concrete, personalised estimate of their footprint — items used, estimated CO2 impact, plastic weight, and how long that plastic would take to decompose — making the abstract idea of "reducing plastic use" tangible and personal.

Purpose

This tool was developed to support a public awareness campaign on:

"Single-Use Plastics: Towards a Sustainable Future"

held on the occasion of International Plastic Bag Free Day, at a primary health center, by the

Department of Community Medicine Chettinad Hospital and Research Institute Chennai, India

Why This Tool Was Used

The Plastic Footprint Tracker was used at this event because it:

Converts an abstract awareness message into concrete, personal numbers — estimated CO2 (grams), plastic weight (grams), and decomposition time (years) — based on a participant's own daily usage
Requires no technical knowledge to use — a participant simply answers a few quick questions about their day
Projects the yearly impact of daily habits (e.g., "if repeated every day, this adds up to X kg of CO2 in a year"), making the long-term consequence of small daily choices visible
Made the awareness session interactive, rather than a one-way talk
Was accompanied by a printed/visual awareness poster used alongside the tool during the event
Served as a practical, hands-on demonstration of how simple computational tools can support public health and environmental awareness initiatives
Usage

This tool was piloted and utilised by over 50 participants during the awareness event, who used it to calculate and reflect on their personal single-use plastic footprint.

How it works
The user is asked how many of each item (bottles, bags, straws, cups/cutlery, packets/wrappers) they used that day
Each item has an associated average CO2 footprint, plastic weight, and decomposition time (simplified, rounded, publicly known averages — used for educational/awareness purposes, not scientific measurement)
The tool calculates per-item and total values, and generates a readable summary, including a projected yearly CO2 impact if the same habits were repeated daily
The user can optionally save this summary as a text report
Project structure
File	Purpose
project.py	Core CLI tool — collects usage, calculates footprint, generates and optionally saves a summary
test_project.py	Automated unit tests for the calculation logic (run with pytest)
index.html	Browser-based version of the tool
plastic-awareness-poster.pptx	Printable awareness poster used alongside the tool at the event
requirements.txt	Python dependencies

Run the CLI version with:

python project.py

Run the automated tests with:

pytest test_project.py
Project status

This is a pilot/educational awareness tool, built and used as part of the above community awareness event. The impact figures used are simplified, rounded, publicly available averages, intended to make plastic usage tangible for awareness purposes — not a scientifically validated environmental measurement instrument.

Acknowledgement

Originally built as a CS50x Final Project, and developed as a learning exercise with AI-assisted guidance (Claude, Anthropic), under the personal supervision, review, and testing of the project author.
