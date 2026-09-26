## Architecture Diagram

Shows all six agents and their connections, plus the external tools/APIs each one uses.

```mermaid
graph TD
    A[Alert Ingestion Agent] -->|normalized alert| B[Correlation Agent]
    B -->|incident context| C[Root-Cause Hypothesis Agent]
    C -->|remediation options| D[Runbook Execution Agent]
    D -->|high-risk action| E[Human Approval Gate]
    D -->|low-risk action, direct execution| F[Post-Incident Reporting Agent]
    E -->|approved| D
    E -->|rejected| C
    D -->|action executed| F
    F -->|updates| G[(Historical Incident DB / ChromaDB)]
    C -->|retrieves from| G

    A -.uses.-> H[Monitoring APIs: Prometheus / Datadog / PagerDuty]
    B -.uses.-> I[Log & Metrics Query API]
    D -.uses.-> J[Infrastructure API / Remediation Scripts]
    E -.uses.-> K[Slack / Email Notification]
```

---

## Agent Workflow Diagram

Shows the sequential pipeline as a linear process flow.

```mermaid
flowchart LR
    Start([Alert Fires]) --> S1[Alert Ingestion:\nnormalize & filter]
    S1 --> S2[Correlation:\ncorrelate logs/metrics/deployments]
    S2 --> S3[Root-Cause Hypothesis:\nretrieve similar incidents,\npropose cause]
    S3 --> S4[Runbook Execution:\nselect remediation]
    S4 --> S5[Post-Incident Reporting:\ncompile report, update DB]
    S5 --> End([Incident Closed])
```

---

## Flow Diagram (Decision Branch at Human Approval Gate)

Shows the branching logic specifically at the risk-classification decision point.

```mermaid
flowchart TD
    A[Runbook Execution Agent proposes action] --> B{Risk level?}
    B -->|Low risk| C[Execute immediately]
    B -->|High risk| D[Route to Human Approval Gate]
    D --> E{Engineer decision}
    E -->|Approve| C
    E -->|Reject| F[Return to Root-Cause Hypothesis Agent\nfor alternative remediation]
    C --> G[Post-Incident Reporting Agent]
    F --> G
```

---

## State Diagram (Incident Lifecycle)

Shows the incident's states across its lifecycle, matching Section 12's state description.

```mermaid
stateDiagram-v2
    [*] --> AlertReceived
    AlertReceived --> AlertNormalized: Alert Ingestion Agent
    AlertNormalized --> ContextCorrelated: Correlation Agent
    ContextCorrelated --> HypothesisProposed: Root-Cause Hypothesis Agent
    HypothesisProposed --> PendingApproval: high-risk action staged
    HypothesisProposed --> ActionExecuted: low-risk action, direct execution
    PendingApproval --> ActionExecuted: approved
    PendingApproval --> HypothesisProposed: rejected, re-propose
    ActionExecuted --> IncidentResolved
    IncidentResolved --> ReportCompiled: Post-Incident Reporting Agent
    ReportCompiled --> [*]
```