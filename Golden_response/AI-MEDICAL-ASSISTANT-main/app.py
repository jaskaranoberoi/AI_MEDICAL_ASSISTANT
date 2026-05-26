from flask import Flask, request, jsonify
from orchestrator import MedicalAIOrchestrator

app = Flask(__name__)

# Initialize orchestrator ONCE
orchestrator = MedicalAIOrchestrator()


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})


@app.route("/analyze", methods=["POST"])
def analyze_patient():
    """
    Expected JSON payload:
    {
        "intake": {...},
        "image_path": "data/images/example.png",   # optional
        "reports": [
            {"id": "r1", "text": "...", "source": "report.pdf"}
        ],                                          # optional
        "user_query": "What does the report mention?"
    }
    """

    try:
        data = request.get_json(force=True)

        result = orchestrator.run({
            "intake": data.get("intake"),
            "image_path": data.get("image_path"),
            "reports": data.get("reports", []),
            "user_query": data.get("user_query")
        })

        return jsonify({
            "success": True,
            "data": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
