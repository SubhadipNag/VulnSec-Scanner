from flask import Blueprint, request, jsonify, send_file

from scanners.port_scanner import run_port_scan
from scanners.header_scanner import analyze_headers
from scanners.xss_scanner import scan_xss

from reports.pdf_reports import generate_pdf_report

scan_bp = Blueprint("scan", __name__)

@scan_bp.route("/scan", methods=["POST"])
def scan_target():

    try:

        data = request.get_json()

        target = data.get("target")

        results = {
            "ports": run_port_scan(target),
            "headers": analyze_headers(target),
            "xss": scan_xss(target)
        }

        # Generate PDF

        pdf_file = generate_pdf_report(target, results)

        return jsonify({
            "results": results,
            "report": pdf_file
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# Download Route

@scan_bp.route("/download-report/<path:filename>")
def download_report(filename):

    return send_file(
        filename,
        as_attachment=True
    )
