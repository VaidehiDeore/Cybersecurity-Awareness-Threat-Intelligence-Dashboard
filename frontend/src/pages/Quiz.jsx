import { useEffect, useState } from "react";
import {
  BrainCircuit,
  Check,
  ArrowRight,
  RotateCcw,
  AlertTriangle,
  Loader2,
} from "lucide-react";
import { getQuiz, submitQuiz } from "../services/api";

export default function Quiz() {
  const [q, setQ] = useState([]);
  const [a, setA] = useState({});
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");
  const [validationMessage, setValidationMessage] = useState("");

  useEffect(() => {
    async function loadQuiz() {
      try {
        setLoading(true);
        setError("");

        const data = await getQuiz();

        setQ(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error("Failed to load quiz:", err);
        setError("Unable to load the awareness quiz.");
      } finally {
        setLoading(false);
      }
    }

    loadQuiz();
  }, []);

  const answeredCount = Object.keys(a).length;
  const totalQuestions = q.length;

  const finish = async () => {
    setValidationMessage("");
    setError("");

    if (totalQuestions === 0) {
      setError("No quiz questions are available.");
      return;
    }

    if (answeredCount < totalQuestions) {
      const remaining = totalQuestions - answeredCount;

      setValidationMessage(
        `Please answer all ${totalQuestions} questions before submitting. ${remaining} question${remaining === 1 ? "" : "s"} remaining.`
      );

      return;
    }

    try {
      setSubmitting(true);

      const response = await submitQuiz(a);

      setResult(response);
    } catch (err) {
      console.error("Quiz submission failed:", err);

      setError(
        err?.message ||
          "Unable to submit the assessment. Please try again."
      );
    } finally {
      setSubmitting(false);
    }
  };

  const retakeQuiz = () => {
    setA({});
    setResult(null);
    setError("");
    setValidationMessage("");

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  if (loading) {
    return (
      <div className="page">
        <div className="panel empty-state">
          <Loader2 className="spin" size={26} />

          <h3>Loading awareness assessment...</h3>

          <p>
            Preparing your cybersecurity knowledge check.
          </p>
        </div>
      </div>
    );
  }

  if (result) {
    return (
      <div className="page quiz-result">
        <div className="result-card panel">
          <div className="result-icon">
            <Check size={26} />
          </div>

          <div className="eyebrow">
            ASSESSMENT COMPLETE
          </div>

          <h2>
            {result.overall_score}
            <span>/100</span>
          </h2>

          <b>{result.level}</b>

          <p>
            Educational awareness score — not an employee
            fitness or competency judgment.
          </p>

          <div className="category-results">
            {Object.entries(result.category_scores || {}).map(
              ([category, score]) => (
                <div
                  className="category-result"
                  key={category}
                >
                  <div className="category-result-head">
                    <span>{category}</span>
                    <b>{score}%</b>
                  </div>

                  <div className="scorebar">
                    <i
                      style={{
                        width: `${score}%`,
                      }}
                    />
                  </div>
                </div>
              )
            )}
          </div>

          <div className="recommendations">
            <h4>Learning recommendations</h4>

            {result.recommendations?.length ? (
              result.recommendations.map(
                (recommendation, index) => (
                  <p key={`${recommendation}-${index}`}>
                    → {recommendation}
                  </p>
                )
              )
            ) : (
              <p>
                Strong coverage. Keep practicing and review
                modules periodically.
              </p>
            )}
          </div>

          <button
            className="primary"
            type="button"
            onClick={retakeQuiz}
          >
            <RotateCcw size={14} />
            Retake quiz
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="page">
      {/* HEADER */}
      <div className="page-head">
        <div>
          <div className="eyebrow">
            AWARENESS / KNOWLEDGE CHECK
          </div>

          <h2>Cybersecurity Awareness Quiz</h2>

          <p>
            {q.length} questions across phishing, passwords,
            MFA, privacy and defensive habits.
          </p>
        </div>

        <div className="quiz-count">
          <BrainCircuit size={17} />

          {answeredCount}/{totalQuestions}
        </div>
      </div>

      {/* ERROR */}
      {error && (
        <div className="quiz-message error-message">
          <AlertTriangle size={17} />

          <span>{error}</span>
        </div>
      )}

      {/* VALIDATION MESSAGE */}
      {validationMessage && (
        <div className="quiz-message warning-message">
          <AlertTriangle size={17} />

          <span>{validationMessage}</span>
        </div>
      )}

      {/* PROGRESS */}
      <div className="quiz-progress panel">
        <div className="quiz-progress-head">
          <span>Assessment progress</span>

          <b>
            {answeredCount} / {totalQuestions}
          </b>
        </div>

        <div className="quiz-progress-track">
          <div
            className="quiz-progress-fill"
            style={{
              width:
                totalQuestions > 0
                  ? `${(answeredCount / totalQuestions) * 100}%`
                  : "0%",
            }}
          />
        </div>

        {answeredCount < totalQuestions && (
          <small>
            Answer all questions to submit your assessment.
          </small>
        )}
      </div>

      {/* QUESTIONS */}
      <div className="quiz-list">
        {q.map((x, i) => (
          <div
            className="panel question"
            key={x.id}
          >
            <div className="q-meta">
              <span>Q{i + 1}</span>

              <small>{x.category}</small>
            </div>

            <h3>{x.question}</h3>

            <div className="options">
              {x.options.map((option, j) => {
                const selected = a[x.id] === j;

                return (
                  <button
                    type="button"
                    className={
                      selected
                        ? "option selected"
                        : "option"
                    }
                    key={option}
                    onClick={() => {
                      setA((current) => ({
                        ...current,
                        [x.id]: j,
                      }));

                      setValidationMessage("");
                    }}
                  >
                    <span>
                      {String.fromCharCode(65 + j)}
                    </span>

                    {option}
                  </button>
                );
              })}
            </div>
          </div>
        ))}
      </div>

      {/* SUBMIT */}
      <div className="quiz-submit-area">
        <button
          className="primary finish"
          type="button"
          onClick={finish}
          disabled={submitting}
        >
          {submitting ? (
            <>
              <Loader2
                size={15}
                className="spin"
              />

              Submitting...
            </>
          ) : (
            <>
              Submit assessment
              <ArrowRight size={15} />
            </>
          )}
        </button>

        {answeredCount < totalQuestions && (
          <p className="submit-hint">
            {totalQuestions - answeredCount} question
            {totalQuestions - answeredCount === 1
              ? ""
              : "s"} remaining
          </p>
        )}
      </div>
    </div>
  );
}