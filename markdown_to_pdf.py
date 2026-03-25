from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor

def create_pdf(data, filename="Output.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=50, leftMargin=50,
                            topMargin=20, bottomMargin=20)
    styles = getSampleStyleSheet()
    story = []

    # Custom styles
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], alignment=TA_CENTER, fontSize=24, spaceAfter=10)
    section_style = ParagraphStyle('SectionStyle', parent=styles['Heading2'], alignment=TA_LEFT, textColor=HexColor('#6A0DAD'), spaceAfter=5)
    normal_style = styles['Normal']

    # Title
    story.append(Paragraph(data.get("title", "Project Title"), title_style))
    story.append(Spacer(1, 12))

    # Description
    story.append(Paragraph("Description", section_style))
    story.append(Paragraph(data.get("description", ""), normal_style))
    story.append(Spacer(1, 12))

    # Features
    features = data.get("features", [])
    if features:
        story.append(Paragraph("Features", section_style))
        feature_list = ListFlowable(
            [ListItem(Paragraph(f, normal_style)) for f in features],
            bulletType='bullet',
            leftIndent=20
        )
        story.append(feature_list)
        story.append(Spacer(1, 12))

    # Tech Stack
    tech_stack = data.get("tech_stack", [])
    if tech_stack:
        story.append(Paragraph("Tech Stack", section_style))
        tech_list = ListFlowable(
            [ListItem(Paragraph(t, normal_style)) for t in tech_stack],
            bulletType='bullet',
            leftIndent=20
        )
        story.append(tech_list)
        story.append(Spacer(1, 12))

    # Advantages
    advantages = data.get("advantages", [])
    if advantages:
        story.append(Paragraph("Advantages", section_style))
        advantages_list = ListFlowable(
            [ListItem(Paragraph(a, normal_style)) for a in advantages],
            bulletType='bullet',
            leftIndent=20
        )
        story.append(advantages_list)
        story.append(Spacer(1, 12))

    # Future Improvements
    improvements = data.get("future_improvements", [])
    if improvements:
        story.append(Paragraph("Future Improvements", section_style))
        improvements_list = ListFlowable(
            [ListItem(Paragraph(i, normal_style)) for i in improvements],
            bulletType='bullet',
            leftIndent=20
        )
        story.append(improvements_list)
        story.append(Spacer(1, 12))

    # Build PDF
    doc.build(story)
    print(f"PDF generated: {filename}")