# Transaction Network Risk Analysis
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Financial institutions process large volumes of transactions, making it difficult for risk teams to understand how accounts are connected and where potentially unusual patterns are concentrated. This project represents transaction activity as a network, where accounts are nodes and transaction relationships are edges, and applies descriptive network analysis to summarize account relationships and structural patterns.

The project supports transaction risk management by identifying accounts or groups with unusual network characteristics that may deserve additional review. It is descriptive rather than predictive or causal: network indicators are used as interpretable screening signals, not as proof that an account is fraudulent.

## Stakeholder & User
- Decision owner: Transaction Risk Management / Financial Crime Risk Management
- Primary users: Risk analysts and transaction investigators
- Supporting users: Data analysts, data scientists, and data engineers
- Decision: Which accounts or groups should be investigated first?

## Useful Answer & Decision
- Framing: Descriptive
- Output: Interpretable network metrics, account/group summaries, and selected visualizations
- Decision supported: Investigation prioritization
- Important caveat: Unusual structure is a screening signal, not proof of misconduct

## Assumptions & Constraints
- Sender and receiver accounts can be identified consistently.
- The selected observation window reasonably represents transaction activity.
- Data is sensitive and must be protected.
- Large graphs may require scalable processing.
- Investigator capacity limits how many cases can be surfaced.
- Metrics must remain understandable to business users.

## Known Unknowns / Risks
- Normal network behavior differs by customer type.
- Results depend on the selected time window.
- External transactions may be unobserved.
- Unusual structures can produce false positives.
- Historical labels may be incomplete.

## Lifecycle Mapping
- Clarify risk decision → Problem Framing & Scoping → Scoping document
- Understand transactions → Data Understanding → Data dictionary and summaries
- Build account graph → Data Preparation → Node and edge tables
- Describe relationships → Network Analysis → Network features and summaries
- Prioritize review → Analysis → Interpretable shortlist of accounts/groups
- Communicate findings → Communication → Risk report/dashboard

## Repo Plan
`data/`, `src/`, `notebooks/`, `docs/`

Real confidential transaction data will not be committed to the repository.
