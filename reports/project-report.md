# Cybersecurity Awareness & Threat Intelligence Dashboard — Project Report

## Abstract

This project presents a defensive cybersecurity platform that combines synthetic cyber threat intelligence with security-awareness training. The system validates and enriches indicators, separates risk from confidence, correlates related observations, maps supported behavior to MITRE ATT&CK, prioritizes synthetic vulnerabilities, generates SOC alerts, and provides awareness modules and a quiz. The default deployment is offline and uses 2,000 synthetic records.

## Introduction

Modern security teams need both technical intelligence and informed users. Raw indicators alone can be noisy, while awareness content without current context can feel disconnected. This project brings these two areas together in one SOC-style interface.

## Problem Statement

Separate threat feeds, vulnerability lists, analyst notes and awareness material make it difficult to move from observation to action. The proposed system provides a common defensive workflow with context and prioritization.

## Objectives

- Normalize threat intelligence.
- Validate and enrich IOCs.
- Score risk and confidence separately.
- Correlate observations and reduce alert fatigue.
- Provide vulnerability awareness.
- Visualize ATT&CK context.
- Provide SOC and executive views.
- Deliver cybersecurity awareness learning.
- Validate the implementation with automated tests.

## Cybersecurity Awareness

The awareness component teaches phishing, passwords, MFA, social engineering, safe browsing, ransomware, privacy, mobile/Wi-Fi safety and incident reporting.

## Cyber Threat Intelligence

CTI provides contextual information that supports defensive decisions. This implementation emphasizes technical and tactical intelligence.

## Threat Intelligence Types

- Strategic: high-level business/leadership context.
- Tactical: adversary behaviors and defensive patterns.
- Operational: campaign/activity context.
- Technical: IOCs and machine-oriented artifacts.

## IOC and IOA Concepts

An IOC is an artifact such as an IP, domain or hash that may be associated with compromise. An Indicator of Attack/Behavior describes behavior or activity rather than only an artifact. The system treats both as contextual evidence rather than automatic proof.

## Threat Intelligence Lifecycle

Observed → Validated → Enriched → Scored → Investigated → Monitored → Expired/Closed.

## Proposed System

The proposed system consists of a synthetic data generator, validation/enrichment services, scoring/correlation engines, SQLite storage, FastAPI APIs and a React dashboard with awareness modules.

## Architecture

```text
Synthetic Data → Normalize → Validate → Enrich → Score → Correlate
                                                        ↓
                                  Threat DB ← Alerts ← SOC Dashboard
                                                        ↓
                                              Awareness + Executive View
```

## Synthetic Dataset

The generator creates 2,000 records across ten threat categories, multiple indicator types, synthetic sources, confidence, risk, status, timestamps, campaign IDs and optional ATT&CK/CVE context.

## IOC Validation

Validation checks IPv4/IPv6, domain, URL, MD5, SHA-1, SHA-256 and CVE syntax. It explicitly does not determine maliciousness.

## Threat Enrichment

Local records provide category, confidence, severity, risk, timestamps, related records and contextual mappings.

## Risk Scoring

The weighted model combines severity, confidence, recency, observation frequency, source reliability and context/correlation.

## Confidence Scoring

Confidence represents the strength of the intelligence evidence. It remains independent of risk.

## Source Reliability

The project uses synthetic reliability levels A–D, from highly reliable to unknown. Source reliability is distinct from item-level confidence.

## Threat Correlation

Campaign and observation context are used to group related records. Correlation indicates relationship but does not prove attribution.

## MITRE ATT&CK

Supported synthetic records can be mapped to recognized tactics and techniques such as Phishing, Valid Accounts, Command and Scripting Interpreter and Data Encrypted for Impact.

## Vulnerability Awareness

Synthetic CVE-style records demonstrate contextual prioritization using CVSS, asset criticality, exposure, exploitation evidence and business context.

## Alert Management

High-risk/high-confidence observations can generate analyst-review alerts. Repeated observations can be correlated to reduce alert fatigue.

## SOC Workflow

Threat Feed → Detection → Validation → Enrichment → Risk/Confidence → Alert → Triage → Correlation → Investigation → Resolution/Monitoring/False Positive → Documentation.

## Awareness Center

The awareness center provides concise defensive lessons and concrete micro-actions.

## Quiz System

The project includes 35 questions with category scores, overall score bands, weak-area identification and learning recommendations.

## Executive Dashboard

The executive view converts technical signals into high-level threat counts, awareness trends, weaknesses and defensive priorities.

## Testing

The automated suite contains 35 tests and covers validation, scoring, enrichment, correlation, alerts, API behavior, filtering, sorting, awareness, quiz scoring and persistence.

## Security

The system avoids suspicious network interaction and file execution. Inputs are validated, analyst changes are auditable, environment variables are supported and production guidance calls for HTTPS, RBAC and rate limiting.

## Results

The completed implementation provides a local defensive CTI/SOC learning platform with 2,000 synthetic records, multiple dashboards, investigation workflows, awareness training and automated tests.

## Limitations

The data is synthetic, SQLite is local-scale, live feeds are disabled by default and production identity/infrastructure controls require additional hardening.

## Future Scope

Authorized STIX/TAXII, SIEM/SOAR, CISA KEV, CVE/EPSS-style prioritization, endpoint/cloud telemetry, ATT&CK Navigator, Docker, CI/CD and centralized logging can be added defensively.

## Conclusion

The project demonstrates how threat intelligence, SOC workflows and security awareness can be combined into a practical defensive platform. Its strongest design principle is that intelligence provides evidence and context while analysts remain responsible for interpretation and action.
