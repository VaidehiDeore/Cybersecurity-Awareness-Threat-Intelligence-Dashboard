import { useEffect, useMemo, useState } from "react";
import {
  TriangleAlert,
  ShieldCheck,
  Search,
  RefreshCw,
  ExternalLink,
} from "lucide-react";
import { getVulnerabilities } from "../services/api";

export default function Vulnerabilities() {
  const [vulnerabilities, setVulnerabilities] = useState([]);
  const [search, setSearch] = useState("");
  const [severityFilter, setSeverityFilter] = useState("ALL");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  async function loadVulnerabilities() {
    try {
      setLoading(true);
      setError("");

      const data = await getVulnerabilities();

      setVulnerabilities(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error("Failed to load vulnerabilities:", err);
      setError("Unable to load vulnerability data.");
      setVulnerabilities([]);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadVulnerabilities();
  }, []);

  const filteredVulnerabilities = useMemo(() => {
    const query = search.trim().toLowerCase();

    return vulnerabilities.filter((item) => {
      const matchesSearch =
        !query ||
        String(item.cve_id || "")
          .toLowerCase()
          .includes(query) ||
        String(item.description || "")
          .toLowerCase()
          .includes(query) ||
        String(item.product_category || "")
          .toLowerCase()
          .includes(query);

      const matchesSeverity =
        severityFilter === "ALL" ||
        String(item.severity || "").toUpperCase() === severityFilter;

      return matchesSearch && matchesSeverity;
    });
  }, [vulnerabilities, search, severityFilter]);

  const criticalCount = vulnerabilities.filter(
    (x) => String(x.severity || "").toUpperCase() === "CRITICAL"
  ).length;

  const highCount = vulnerabilities.filter(
    (x) => String(x.severity || "").toUpperCase() === "HIGH"
  ).length;

  const patchAvailableCount = vulnerabilities.filter(
    (x) =>
      x.patch_available === true ||
      String(x.patch_available).toLowerCase() === "true"
  ).length;

  const getSeverityClass = (severity) => {
    const value = String(severity || "LOW").toLowerCase();

    if (value === "critical") return "critical";
    if (value === "high") return "high";
    if (value === "medium") return "medium";
    return "low";
  };

  const isPatchAvailable = (value) => {
    return value === true || String(value).toLowerCase() === "true";
  };

  return (
    <div className="page">
      {/* PAGE HEADER */}
      <div className="page-head">
        <div>
          <div className="eyebrow">VULNERABILITY MANAGEMENT</div>

          <h2>Vulnerability Awareness</h2>

          <p>
            Contextual prioritization — CVSS alone does not determine patch
            priority.
          </p>
        </div>

        <div className="page-head-actions">
          <button
            type="button"
            className="icon-button"
            onClick={loadVulnerabilities}
            title="Refresh vulnerability data"
          >
            <RefreshCw size={16} className={loading ? "spin" : ""} />
          </button>

          <span className="badge amber">
            {vulnerabilities.length} TRACKED
          </span>
        </div>
      </div>

      {/* SUMMARY CARDS */}
      <div className="stats-grid">
        <div className="panel stat-card">
          <div className="stat-icon danger">
            <TriangleAlert size={19} />
          </div>

          <div>
            <span>Critical</span>
            <strong>{criticalCount}</strong>
          </div>
        </div>

        <div className="panel stat-card">
          <div className="stat-icon warning">
            <TriangleAlert size={19} />
          </div>

          <div>
            <span>High Severity</span>
            <strong>{highCount}</strong>
          </div>
        </div>

        <div className="panel stat-card">
          <div className="stat-icon success">
            <ShieldCheck size={19} />
          </div>

          <div>
            <span>Patch Available</span>
            <strong>{patchAvailableCount}</strong>
          </div>
        </div>

        <div className="panel stat-card">
          <div className="stat-icon info">
            <ShieldCheck size={19} />
          </div>

          <div>
            <span>Total Tracked</span>
            <strong>{vulnerabilities.length}</strong>
          </div>
        </div>
      </div>

      {/* FILTER BAR */}
      <div className="panel filter-panel">
        <div className="search-box">
          <Search size={17} />

          <input
            type="text"
            placeholder="Search CVE, product category or description..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </div>

        <select
          value={severityFilter}
          onChange={(event) => setSeverityFilter(event.target.value)}
          aria-label="Filter by severity"
        >
          <option value="ALL">All Severities</option>
          <option value="CRITICAL">Critical</option>
          <option value="HIGH">High</option>
          <option value="MEDIUM">Medium</option>
          <option value="LOW">Low</option>
        </select>
      </div>

      {/* ERROR */}
      {error && (
        <div className="panel error-panel">
          <TriangleAlert size={18} />
          <span>{error}</span>

          <button type="button" onClick={loadVulnerabilities}>
            Retry
          </button>
        </div>
      )}

      {/* LOADING */}
      {loading && (
        <div className="panel empty-state">
          <RefreshCw size={22} className="spin" />
          <h3>Loading vulnerability intelligence...</h3>
          <p>Retrieving contextual vulnerability records.</p>
        </div>
      )}

      {/* EMPTY */}
      {!loading && !error && filteredVulnerabilities.length === 0 && (
        <div className="panel empty-state">
          <ShieldCheck size={26} />

          <h3>No vulnerabilities found</h3>

          <p>
            Try changing your search term or severity filter.
          </p>
        </div>
      )}

      {/* VULNERABILITY GRID */}
      {!loading && filteredVulnerabilities.length > 0 && (
        <div className="vuln-grid">
          {filteredVulnerabilities.map((item) => {
            const severityClass = getSeverityClass(item.severity);

            return (
              <div
                className="panel vuln"
                key={item.vulnerability_id || item.cve_id}
              >
                {/* CARD HEADER */}
                <div className="vuln-top">
                  <span className={`severity ${severityClass}`}>
                    {String(item.severity || "LOW").toUpperCase()}
                  </span>

                  <TriangleAlert size={18} />
                </div>

                {/* CVE */}
                <div className="vuln-title-row">
                  <div>
                    <h3>{item.cve_id || "Unknown CVE"}</h3>

                    {item.product_category && (
                      <span className="vuln-product">
                        {item.product_category}
                      </span>
                    )}
                  </div>

                  <span className="synthetic-pill">
                    SYNTHETIC
                  </span>
                </div>

                {/* DESCRIPTION */}
                <p className="vuln-description">
                  {item.description ||
                    "No vulnerability description available."}
                </p>

                {/* METRICS */}
                <div className="vuln-metrics">
                  <div>
                    <span>CVSS</span>
                    <b>{item.cvss_score ?? "—"}</b>
                  </div>

                  <div>
                    <span>Priority</span>
                    <b>{item.priority_score ?? "—"}</b>
                  </div>

                  <div>
                    <span>Patch</span>
                    <b>
                      {isPatchAvailable(item.patch_available)
                        ? "Available"
                        : "No"}
                    </b>
                  </div>
                </div>

                {/* PRIORITY BAR */}
                <div className="priority-section">
                  <div className="priority-label">
                    <span>Contextual Priority</span>

                    <strong>
                      {item.priority_score ?? 0}/100
                    </strong>
                  </div>

                  <div className="priority-bar">
                    <i
                      style={{
                        width: `${Math.min(
                          Math.max(Number(item.priority_score) || 0,
                          0),
                          100
                        )}%`,
                      }}
                    />
                  </div>
                </div>

                {/* STATUS */}
                <div className="vuln-footer">
                  <div className="vuln-status">
                    {isPatchAvailable(item.patch_available) ? (
                      <ShieldCheck size={14} />
                    ) : (
                      <TriangleAlert size={14} />
                    )}

                    <span>
                      {item.exploitation_status_demo ||
                        "Demo intelligence record"}
                    </span>
                  </div>

                  <button
                    type="button"
                    className="vuln-action"
                    title="View defensive details"
                  >
                    <ExternalLink size={14} />
                  </button>
                </div>

                <small className="demo-note">
                  Synthetic defensive record — no exploitation activity.
                </small>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}