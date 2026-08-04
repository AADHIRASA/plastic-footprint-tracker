
Plastic Receipt



Plastic Footprint Tracker
Community Health Awareness Programme
International Plastic Bag Free Day — 10 July 2026
Semmencheri, Chennai
 
Table of Contents
1. Background
2. Methodology — Calculations & References
3. Impact — Campaign Reach & Metrics
 
1. Background
The Plastic Receipt was created for a community health awareness programme on single-use plastics, held on International Plastic Bag Free Day (10 July 2026) at the satellite centre in Semmencheri, Chennai.

The tool was built with AI assistance in GitHub as a CS50x learning project. It generates an itemized receipt showing estimated CO₂ footprint, plastic weight, and decomposition time based on 5 quick questions about daily plastic use.

What It Does
Answer 5 questions about daily plastic use → get an itemized receipt showing:
Estimated CO₂ footprint (grams)
Total plastic weight (grams)
Decomposition time (years)
Yearly projection if habits continue

Interfaces
Version	File	Use Case
Web	index.html	Browser-based receipt — works offline
Flyer	plastic-receipt-flyer.png	Printed handout with scannable QR code

Live Access
Web tool: tinyurl.com/yh59y4x5
Source code: github.com/AADHIRASA/plastic-footprint-tracker
 
2. Methodology — Calculations & References
The figures used are simplified, rounded, publicly known averages for educational purposes. They are not precise scientific measurements. However, Peer-reviewed literature supports them as conservative, educationally valid estimates.

Calculation Model
Per-Item Impact = Count × Average per Unit
Total Impact    = Sum across all categories
Yearly CO₂ (kg) = Daily CO₂ (g) × 365 ÷ 1000

Impact Data
Category	Material	CO₂ (g/unit)	Weight (g)	Decomposition
Bottles	PET	82.8	25	450 years
Bags	LDPE	10.0	5	20 years
Straws	PP	1.5	0.4	200 years
Cups / Cutlery	PS/PP	15.0	8	50 years
Packets / Wrappers	Mixed / LDPE	6.0	3	100 years

Source of Each Value
Decomposition Times
Oliveira et al. (2020) — Frontiers in Marine Science (PMC)
Directly confirms three values:
PET bottles: 450 years
PE grocery bags: 20 years
PS cups: 50 years
The remaining values (straws: 200 years; wrappers: 100 years) fall within the "hundreds of years" persistence range reported by Gallo et al. (2018) (Environ Sci Pollut Res, PMCID: PMC5918521) and Mohanan et al. (2020) (Front Microbiol, PMID: 33324366) for petroleum-based polymers in environmental conditions.


Why Conservative Estimates?
Lower-bound, rounded figures are ethically preferable for public health education. They convey the correct order of magnitude without risking overstatement.

References 
1. Oliveira M, Almeida M, Miguel I. Marine environmental plastic pollution: mitigation by microorganism degradation and recycling valorization. Front Mar Sci. 2020;7:565. doi:10.3389/fmars.2020.00565
2. Sun Y, et al. Evaluating scenarios for carbon reduction using different tableware in China. Sci Total Environ. 2021;792:147903. doi:10.1016/j.scitotenv.2021.147903. PMID: 34118672
3. Gallo F, Fossi C, Weber R, Santillo D, Sousa J, Ingram I, et al. Marine litter plastics and microplastics and their toxic chemicals components: the need for urgent preventive measures. Environ Sci Pollut Res Int. 2018;25(13):12941-12943. doi:10.1007/s11356-017-9913-z. PMCID: PMC5918521
4. Eleni K, et al. Environmental and economic impacts of substituting single-use plastic straws: a life-cycle assessment for Greece. Polymers (Basel). 2025;17(6):935. doi:10.3390/polym17060935. PMID: 40363017
5. Mohanan N, Montazer Z, Sharma PK, Levin DB. Microbial and enzymatic degradation of synthetic plastics. Front Microbiol. 2020;11:580. doi:10.3389/fmicb.2020.00580. PMID: 33324366
 
3. Impact — Campaign Reach & Metrics
Campaign
Programme: Single-Use Plastics: Towards a Sustainable Future
Date: 10 July 2026 (International Plastic Bag Free Day)
Venue: Satellite centre, Semmencheri, Chennai
Organizer: Department of Community Medicine, Chettinad Hospital and Research Institute

Reach
Metric	Value
On-site participants (event)	50+
Extended reach (friends, family, QR sharing)	50+
Total users reached	100+

Deployment Channels
Channel	Method	Users
Printed code display	Code printout displayed at the booth with QR code for scanning	Walk-in participants
QR-code flyer	Printed handout with scannable QR code linking to tinyurl.com/yh59y4x5	Participants who took flyers
WhatsApp sharing	TinyURL link shared directly on WhatsApp	Friends, family, extended network

The flyer (plastic-receipt-flyer.png) was printed and distributed at the event. It features a scannable QR code linking directly to the live web tool. The code printout was displayed at the booth so attendees could scan and access the tool immediately on their phones.

Event Activities
Delivered a public address to over 50 attendees on the health and environmental impact of single-use plastics
Coordinated awareness materials and engaged the audience throughout the session
Guided participants through the Plastic Receipt exercise in person, helping them understand and reflect on their own plastic usage in real time
Displayed the code printout with QR code for attendees to scan
Distributed printed flyers and shared the TinyURL link on WhatsApp

Post-Event Sharing
After the campaign, the tool and flyer were shared via:
WhatsApp groups within the medical college community
Direct sharing of the TinyURL link
Reuse of the flyer template for a subsequent World Environment Day session
 


