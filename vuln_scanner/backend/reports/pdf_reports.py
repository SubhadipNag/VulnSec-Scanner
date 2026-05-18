from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

import os
from datetime import datetime

def generate_pdf_report(target, results):

    # Create reports folder if not exists

    os.makedirs("generated_reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"generated_reports/report_{timestamp}.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        f"<b>Web Vulnerability Scan Report</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    target_text = Paragraph(
        f"<b>Target:</b> {target}",
        styles['BodyText']
    )

    elements.append(target_text)

    elements.append(Spacer(1, 20))

    # Ports

    ports = Paragraph(
        f"<b>Port Scan Results:</b><br/>{results.get('ports')}",
        styles['BodyText']
    )

    elements.append(ports)

    elements.append(Spacer(1, 20))

    # Headers

    headers = Paragraph(
        f"<b>Header Analysis:</b><br/>{results.get('headers')}",
        styles['BodyText']
    )

    elements.append(headers)

    elements.append(Spacer(1, 20))

    # XSS

    xss = Paragraph(
        f"<b>XSS Scan:</b><br/>{results.get('xss')}",
        styles['BodyText']
    )

    elements.append(xss)

    elements.append(Spacer(1, 20))

    doc.build(elements)

    return filename
