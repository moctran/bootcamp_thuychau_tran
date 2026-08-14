# Transaction Network Analysis

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
A large retail bank processes millions of customer transactions each month. Looking at transactions only as isolated rows can miss important relationship patterns between accounts. By representing accounts as nodes and transactions as edges, network analysis can reveal structural behaviors such as highly connected accounts, repeated reciprocal flows, concentrated counterparties, and tightly connected neighborhoods.

The project aims to build a scalable transaction-network analytics pipeline that converts raw transaction records into account-level and relationship-level graph features. These features can support downstream analytical tasks such as customer behavior analysis, anomaly detection, churn modeling, and credit-risk modeling.

## Stakeholder & User
- **Decision owner:** Data Science / Risk / Customer Analytics lead.
- **Tool/operator:** Data scientists and analysts working with large-scale transaction data.
- **Workflow context:** The pipeline is run on recurring transaction snapshots, such as monthly data, and produces reusable network features for downstream models and analysis.
- **Decision supported:** Determine which network-derived signals are useful enough to include in customer analytics or predictive models.

## Useful Answer & Decision
- **Type:** Primarily descriptive and predictive.
- **Descriptive goal:** Summarize how each account is positioned and behaves within the transaction network.
- **Predictive goal:** Test whether graph-derived features improve downstream prediction compared with using conventional customer and transaction features alone.
- **Core artifacts:** A reproducible graph-feature pipeline, processed feature tables, exploratory analysis, and model-ready datasets.
- **Example features:** Degree, weighted degree, reciprocity, neighbor entropy, neighborhood overlap, and other node/edge statistics.
- **Evaluation:** Feature stability, computational scalability, data quality, and incremental predictive performance in downstream models.

## Assumptions & Constraints
- Transaction records contain reliable sender, receiver, amount, and time information.
- Account identifiers can be consistently linked across the analysis period.
- The graph may contain millions of transaction records, so single-machine graph processing may be too slow or memory intensive.
- GPU/distributed tools such as cuGraph and Dask may be required for scalable computation.
- Transaction direction and repeated transactions carry useful behavioral information and should be preserved where appropriate.
- Sensitive customer information should not be exposed in outputs; analysis should rely on internal identifiers and approved data access.
- Network features should be calculated without leaking future information into predictive models.

## Known Unknowns / Risks
- Some network patterns may reflect normal high-volume activity rather than meaningful behavioral signals.
- Very large merchants or hub accounts may dominate degree-based metrics.
- Missing or filtered transactions may distort local network structure.
- Network features may change substantially across months, reducing stability.
- Feature computation may become expensive as graph size grows.
- Apparent predictive gains may come from temporal leakage if feature windows are not aligned correctly.
- The most useful graph features may differ across churn, credit-risk, and anomaly-detection tasks.

## Lifecycle Mapping
Goal → Stage → Deliverable

- Define the business and analytics question → **Problem Framing & Scoping (Stage 01)** → Project scope and README.
- Ingest and validate transaction data → **Data Preparation** → Clean edge list and account mapping.
- Build the transaction graph → **Network Construction** → Directed/weighted graph representation.
- Engineer graph features → **Feature Engineering** → Node- and edge-level feature tables.
- Explore network behavior → **EDA** → Summary statistics and visual diagnostics.
- Test downstream value → **Modeling & Evaluation** → Baseline-vs-network-feature comparison.
- Package reusable workflow → **Delivery** → Reproducible scripts, documentation, and reports.

## Repo Plan
- `data/raw/` — original or sample transaction inputs; sensitive production data should not be committed.
- `data/processed/` — cleaned edge lists and generated feature tables.
- `src/` — reusable graph construction and feature-engineering code.
- `notebooks/` — exploratory analysis and experiments.
- `docs/` — stakeholder notes, scope, data dictionary, and methodology.
- `reports/` — figures, summaries, and evaluation results.
- `model/` — saved downstream models or model metadata when applicable.

## Initial Technical Workflow
1. Load a monthly transaction snapshot.
2. Clean identifiers, timestamps, amounts, and transaction direction.
3. Aggregate records into an edge list where appropriate.
4. Construct a directed and/or weighted transaction graph.
5. Compute scalable graph features.
6. Join graph features back to account-level analytical datasets.
7. Evaluate feature distributions, stability, and usefulness.
8. Compare downstream models with and without network features.

## Success Criteria
The project is successful if it produces a reproducible and scalable network-feature pipeline and demonstrates which graph features provide stable, interpretable, and useful signals for downstream customer or risk analytics.