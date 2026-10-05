import { useEffect, useMemo, useState } from "react";
import {
  AlertTriangle,
  Bell,
  CheckCircle2,
  Clock3,
  RefreshCw,
  Search,
  ShieldAlert,
  XCircle,
} from "lucide-react";
import { getAlerts, updateAlertStatus } from "../services/api";

export default function Alerts() {
  const [alerts, setAlerts] = useState([]);
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("ALL");
  const [severityFilter, setSeverityFilter] = useState("ALL");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [updatingId, setUpdatingId] = useState(null);

  async function loadAlerts() {
    try {
      setLoading(true);
      setError("");

      const data = await getAlerts();

      setAlerts(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error("Failed to load alerts:", err);
      setError("Unable to load security alerts.");
      setAlerts([]);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    async function fetchAlerts() {
      await loadAlerts();
    }

    fetchAlerts();
  }, []);

  const filteredAlerts = useMemo(() => {
    const query = search.trim().toLowerCase();

    return alerts.filter((alert) => {
      const matchesSearch =
        !query ||
        String(alert.alert_id || "")
          .toLowerCase()
          .includes(query) ||
        String(alert.threat_id || "")
          .toLowerCase()
          .includes(query) ||
        String(alert.alert_type || "")
          .toLowerCase()
          .includes(query) ||
        String(alert.description || "")
          .toLowerCase()
          .includes(query);

      const matchesStatus =
        statusFilter === "ALL" ||
        String(alert.status || "").toUpperCase() === statusFilter;

      const matchesSeverity =
        severityFilter === "ALL" ||
        String(alert.severity || "").toUpperCase() === severityFilter;

      return matchesSearch && matchesStatus && matchesSeverity;
    });
  }, [alerts, search, statusFilter, severityFilter]);

  const newCount = alerts.filter(
    (x) => String(x.status || "").toUpperCase() === "NEW"
  ).length;

  const investigatingCount = alerts.filter(
    (x) => String(x.status || "").toUpperCase() === "INVESTIGATING"
  ).length;

  const monitoringCount = alerts.filter(
    (x) => String(x.status || "").toUpperCase() === "MONITORING"
  ).length;

  const resolvedCount = alerts.filter(
    (x) => String(x.status || "").toUpperCase() === "RESOLVED"
  ).length;

  const getSeverityClass = (severity) => {
    const value = String(severity || "").toLowerCase();

    if (value === "critical") return "critical";
    if (value === "high") return "high";
    if (value === "medium") return "medium";
    return "low";
  };

  const getStatusClass = (status) => {
    const value = String(status || "").toLowerCase();

    if (value === "new") return "new";
    if (value === "investigating") return "investigating";
    if (value === "monitoring") return "monitoring";
    if (value === "resolved") return "resolved";
    if (value === "false_positive") return "false-positive";

    return "monitoring";
  };

  async function handleStatusChange(alertId, status) {
    try {
      setUpdatingId(alertId);

      await updateAlertStatus(alertId, status);

      setAlerts((current) =>
        current.map((alert) =>
          alert.alert_id === alertId
            ? { ...alert, status }
            : alert
        )
      );
    } catch (err) {
      console.error("Failed to update alert status:", err);
      setError("Unable to update alert status.");
    } finally {
      setUpdatingId(null);
    }
  }

  return (
    <div className="page">
      {/* HEADER */}
      <div className="page-head">
        <div>
          <div className="eyebrow">SOC ALERT MANAGEMENT</div>

          <h2>Security Alerts</h2>

          <p>
            Correlated security alerts requiring analyst triage and
            defensive review.
          </p>
        </div>

        <div className="page-head-actions">
          <button
            type="button"
            className="icon-button"
            onClick={loadAlerts}
            title="Refresh alerts"
          >
            <RefreshCw
              size={16}
              className={loading ? "spin" : ""}
            />
          </button>

          <span className="badge amber">
            {alerts.length} ALERTS
          </span>
        </div>
      </div>

      {/* SUMMARY */}
      <div className="stats-grid">
        <div className="panel stat-card">
          <div className="stat-icon danger">
            <Bell size={18} />
          </div>

          <div>
            <span>New</span>
            <strong>{newCount}</strong>
          </div>
        </div>

        <div className="panel stat-card">
          <div className="stat-icon warning">
            <ShieldAlert size={18} />
          </div>

          <div>
            <span>Investigating</span>
            <strong>{investigatingCount}</strong>
          </div>
        </div>

        <div className="panel stat-card">
          <div className="stat-icon info">
            <Clock3 size={18} />
          </div>

          <div>
            <span>Monitoring</span>
            <strong>{monitoringCount}</strong>
          </div>
        </div>

        <div className="panel stat-card">
          <div className="stat-icon success">
            <CheckCircle2 size={18} />
          </div>

          <div>
            <span>Resolved</span>
            <strong>{resolvedCount}</strong>
          </div>
        </div>
      </div>

      {/* FILTERS */}
      <div className="panel filter-panel">
        <div className="search-box">
          <Search size={17} />

          <input
            type="text"
            placeholder="Search alert ID, threat ID or description..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </div>

        <select
          value={severityFilter}
          onChange={(event) =>
            setSeverityFilter(event.target.value)
          }
          aria-label="Filter alerts by severity"
        >
          <option value="ALL">All Severities</option>
          <option value="CRITICAL">Critical</option>
          <option value="HIGH">High</option>
          <option value="MEDIUM">Medium</option>
          <option value="LOW">Low</option>
        </select>

        <select
          value={statusFilter}
          onChange={(event) =>
            setStatusFilter(event.target.value)
          }
          aria-label="Filter alerts by status"
        >
          <option value="ALL">All Statuses</option>
          <option value="NEW">New</option>
          <option value="INVESTIGATING">Investigating</option>
          <option value="MONITORING">Monitoring</option>
          <option value="RESOLVED">Resolved</option>
          <option value="FALSE_POSITIVE">False Positive</option>
        </select>
      </div>

      {/* ERROR */}
      {error && (
        <div className="panel error-panel">
          <AlertTriangle size={18} />
          <span>{error}</span>

          <button type="button" onClick={loadAlerts}>
            Retry
          </button>
        </div>
      )}

      {/* LOADING */}
      {loading && (
        <div className="panel empty-state">
          <RefreshCw size={23} className="spin" />

          <h3>Loading security alerts...</h3>

          <p>
            Retrieving correlated defensive intelligence.
          </p>
        </div>
      )}

      {/* EMPTY */}
      {!loading &&
        !error &&
        filteredAlerts.length === 0 && (
          <div className="panel empty-state">
            <CheckCircle2 size={26} />

            <h3>No alerts found</h3>

            <p>
              No alerts match the current filters.
            </p>
          </div>
        )}

      {/* ALERT LIST */}
      {!loading && filteredAlerts.length > 0 && (
        <div className="alert-list">
          {filteredAlerts.map((alert) => {
            const severityClass = getSeverityClass(
              alert.severity
            );

            const statusClass = getStatusClass(alert.status);

            return (
              <div
                className="panel alert-card"
                key={alert.alert_id}
              >
                <div className="alert-main">
                  <div className="alert-icon">
                    <AlertTriangle size={18} />
                  </div>

                  <div className="alert-content">
                    <div className="alert-title-row">
                      <div>
                        <span className="alert-id">
                          {alert.alert_id}
                        </span>

                        <h3>
                          {alert.alert_type ||
                            "Security Intelligence Alert"}
                        </h3>
                      </div>

                      <span
                        className={`severity ${severityClass}`}
                      >
                        {String(
                          alert.severity || "LOW"
                        ).toUpperCase()}
                      </span>
                    </div>

                    <p>
                      {alert.description ||
                        "Correlated synthetic security observation requiring analyst review."}
                    </p>

                    <div className="alert-meta">
                      <span>
                        Threat:{" "}
                        <b>{alert.threat_id || "—"}</b>
                      </span>

                      <span>
                        Risk:{" "}
                        <b>{alert.risk_score ?? "—"}</b>
                      </span>

                      <span>
                        Confidence:{" "}
                        <b>
                          {alert.confidence_score ?? "—"}%
                        </b>
                      </span>

                      <span>
                        Created:{" "}
                        <b>
                          {alert.timestamp ||
                            alert.created_at ||
                            "—"}
                        </b>
                      </span>
                    </div>
                  </div>
                </div>

                <div className="alert-actions">
                  <span
                    className={`alert-status ${statusClass}`}
                  >
                    {String(
                      alert.status || "NEW"
                    ).replace("_", " ")}
                  </span>

                  <select
                    value={alert.status || "NEW"}
                    disabled={
                      updatingId === alert.alert_id
                    }
                    onChange={(event) =>
                      handleStatusChange(
                        alert.alert_id,
                        event.target.value
                      )
                    }
                    aria-label={`Update status for ${alert.alert_id}`}
                  >
                    <option value="NEW">NEW</option>
                    <option value="INVESTIGATING">
                      INVESTIGATING
                    </option>
                    <option value="MONITORING">
                      MONITORING
                    </option>
                    <option value="RESOLVED">
                      RESOLVED
                    </option>
                    <option value="FALSE_POSITIVE">
                      FALSE POSITIVE
                    </option>
                  </select>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* FOOTER NOTE */}
      <div className="panel alert-info">
        <ShieldAlert size={16} />

        <div>
          <strong>Analyst-first alerting</strong>

          <p>
            Alerts represent prioritized defensive intelligence.
            They do not by themselves establish a confirmed
            security incident.
          </p>
        </div>
      </div>
    </div>
  );
}