#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate a clean, modern, ATS-friendly resume PDF with ReportLab."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
    HRFlowable, KeepTogether,
)
from reportlab.lib.styles import ParagraphStyle

ACCENT = HexColor("#0a7ea4")   # calm professional blue
DARK = HexColor("#1a1a1a")
GREY = HexColor("#555555")
LIGHTGREY = HexColor("#888888")

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19,
                           leading=22, textColor=DARK, spaceAfter=1),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8.5,
                              leading=11, textColor=GREY),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=10.5,
                              leading=11.5, textColor=ACCENT, spaceBefore=5,
                              spaceAfter=1),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9.5,
                           leading=11, textColor=DARK, spaceBefore=2.5),
    "meta": ParagraphStyle("meta", fontName="Helvetica-Oblique", fontSize=8,
                           leading=10, textColor=GREY, spaceAfter=1),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.4,
                             leading=10.0, textColor=DARK, leftIndent=10,
                             bulletIndent=2, spaceAfter=0.5),
    "skillhead": ParagraphStyle("skillhead", fontName="Helvetica-Bold", fontSize=9,
                                leading=12, textColor=DARK),
}


def hr():
    return HRFlowable(width="100%", thickness=0.8, color=ACCENT,
                      spaceBefore=1, spaceAfter=4)


def bullets(items):
    return [Paragraph(f"<bullet>&bull;</bullet> {t}", styles["bullet"])
            for t in items]


def P(text, style):
    return Paragraph(text, styles[style])


def link(url, text=None):
    """Wrap a URL in a real, clickable PDF hyperlink (accent-coloured)."""
    label = text or url.replace("https://", "").replace("mailto:", "")
    return f'<a href="{url}" color="#0a7ea4"><u>{label}</u></a>'


def skill_line(label, values):
    return Paragraph(
        '<font color="#0a7ea4"><b>' + label + ':</b></font> ' + values,
        styles["bullet"])


story = [
    P("Amoako Benedict Acheampong", "name"),
    P(f"Accra, Ghana &nbsp;|&nbsp; (+233) 50 572 2027 &nbsp;|&nbsp; "
      f'{link("mailto:amoakoben40@gmail.com")}', "contact"),
    P(f'{link("https://benedictamoako.vercel.app")} &nbsp;|&nbsp; '
      f'{link("https://linkedin.com/in/amoakoben")} &nbsp;|&nbsp; '
      f'{link("https://github.com/primeyloa")}', "contact"),
    Spacer(1, 2),
    hr(),

    P("SUMMARY", "section"),
    Paragraph("Computer Science student (B.Sc., University of Ghana) focused on AI/ML "
              "and systems engineering. Hands-on experience fine-tuning and deploying "
              "ML models (LLMs, computer vision, NLP), leading backend development of "
              "production-style web platforms (Django REST Framework), and publishing "
              "first-author research on bias in content-moderation classifiers. "
              "Comfortable owning problems end-to-end &mdash; from data curation and "
              "pipeline design through evaluation and deployment.", styles["bullet"]),

    P("SKILLS", "section"),
    skill_line("Languages", "Python, TypeScript/JavaScript, Java, C#, SQL"),
    skill_line("ML / AI", "Fine-tuning (LoRA/Unsloth), MedGemma, scikit-learn, NLTK, "
                  "computer vision, NLP & sentiment analysis, evaluation & error analysis"),
    skill_line("Backend & Data", "Django REST Framework, MongoDB, PostgreSQL, Redis, Celery, "
              "JWT auth, REST APIs, Postman"),
    skill_line("Frontend & Mobile", "React (Vite), React Native/Expo"),

    P("EXPERIENCE", "section"),

    KeepTogether([
        P("Backend Engineer Intern (Remote)", "role"),
        P("Scholafrik &nbsp;-> Apr 2026 &ndash; Sep 2026", "meta"),
        *bullets([
            "Shipped backend features in a TypeScript codebase with strict type safety; wrote and maintained tests and managed database queries across releases.",
            "Collaborated in a remote agile team to integrate new product features end-to-end, from design review to production.",
        ]),
    ]),

    KeepTogether([
        P("Machine Learning Research Intern", "role"),
        P("Data Intelligence & Swarm Analytics (DISAL), Accra &nbsp;-> Sep 2025 &ndash; Dec 2025", "meta"),
        *bullets([
            "Built and fine-tuned vision-language models (Google MedGemma 4B with LoRA "
            "via Unsloth) to classify tropical skin diseases, optimised for dark skin "
            "tones to reduce diagnostic bias in an underserved group.",
            "Curated and enhanced the training dataset (bulk image processing, quality "
            "filtering) under tight memory constraints; ran systematic evaluation of "
            "fine-tuned checkpoints before deployment.",
            "Integrated the trained model with a mobile app, demonstrating the full "
            "research-to-deployment loop.",
        ]),
    ]),

    KeepTogether([
        P("NLP Scientist &mdash; Tourism Review Sentiment & Quality Analytics", "role"),
        P("Independent research project &nbsp;-> 2025 &ndash; 2026", "meta"),
        *bullets([
            "Designed an end-to-end NLP pipeline (tokenisation, Bag-of-Words, preprocessing) over large-scale public review datasets using NLTK, scikit-learn and Pandas.",
            "Performed rigorous error analysis to align model predictions with service-quality metrics, turning raw reviews into actionable insights.",
        ]),
    ]),

    KeepTogether([
        P("IT Business Analyst (Pro-bono)", "role"),
        P("Agyaben Skin Clinic, Accra &nbsp;-> Nov 2025", "meta"),
        *bullets([
            "Analysed patient intake-to-consultation workflows with a small team; "
            "identified bottlenecks and implemented a hybrid scheduling system that "
            "reduced congestion and queueing.",
        ]),
    ]),

    P("SELECTED PROJECTS", "section"),

    KeepTogether([
        P("CauseHive &mdash; donation management platform", "role"),
        P("Django REST Framework, React (Vite), PostgreSQL, Celery, Redis, Paystack "
          f'&nbsp;-> {link("https://github.com/primeyloa/CauseHive-front")}',
          "meta"),
        *bullets([
            "Led full backend development in an agile team; later consolidated four "
            "microservices into a deployable Django monolith with per-domain "
            "databases and a custom database router.",
            "Implemented JWT auth, rate limiting, Celery background jobs and the "
            "Paystack payment gateway, supporting donations across multiple African "
            "countries.",
        ]),
    ]),

    KeepTogether([
        P("twicorpus &mdash; Twi (Akan) NLP corpus package", "role"),
        P(f'Python, pip &nbsp;-> {link("https://github.com/primeyloa/twicorpus")}', "meta"),
        *bullets([
            "Authored and published an installable Python package providing "
            "NLTK-style word lists and corpora for Twi, lowering the barrier to "
            "NLP research in a low-resource Ghanaian language; open-sourced with "
            "attribution to the GhanaNLP community dataset.",
        ]),
    ]),

    KeepTogether([
        P("Service Hub &mdash; campus service-operations optimiser", "role"),
        P("Java, SQLite, Java Swing (joint university project) &nbsp;-> "
          f'{link("https://github.com/primeyloa/Service-Hub")}', "meta"),
        *bullets([
            "Co-built a smart service-request dispatcher for the University of Ghana "
            "campus, implementing custom data structures (heaps, red-black trees, "
            "graphs) and classic algorithms (Dijkstra, MST, knapsack) with a "
            "simulation GUI and an empirical benchmarker.",
        ]),
    ]),

    KeepTogether([
        P("Preprint &mdash; Crisis-Driven Bias in Social Media Flagging", "role"),
        P(f'{link("https://doi.org/10.13140/RG.2.2.24694.36165")}', "meta"),
        *bullets([
            "Quantified topic sensitivity and crisis-driven bias in content-moderation "
            "classifiers &mdash; a first-author research contribution at the "
            "intersection of NLP and algorithmic fairness.",
        ]),
    ]),

    KeepTogether([
        P("Flail &mdash; AI agent for animated videos", "role"),
        P(f"JavaScript &nbsp;-> {link('https://github.com/primeyloa/flail')}", "meta"),
        *bullets([
            "AI agent that creates short animated videos from a brief; user approves "
            "each step and every video stays as editable files based on ICMs.",
        ]),
    ]),

    KeepTogether([
        P("Cevin &mdash; financial literacy platform", "role"),
        P(f"TypeScript &nbsp;-> {link('https://github.com/primeyloa/cevin')}", "meta"),
        *bullets([
            "Hackathon project helping users find reliable financial literacy and "
            "investment platforms.",
        ]),
    ]),

    KeepTogether([
        P("Ferlance &mdash; business intelligence for small businesses", "role"),
        P(f"TypeScript &nbsp;-> {link('https://ferlance.onrender.com')}", "meta"),
        *bullets([
            "Business intelligence platform for Ghanaian small businesses; turns sales "
            "sheets, Mobile Money alerts and stock counts into clear numbers, honest "
            "insights and actionable answers. Features AI agent 'Lance' for instant "
            "business questions and supports 5 file formats including CSV and Excel.",
        ]),
    ]),

    P("EDUCATION", "section"),
    KeepTogether([
        P("B.Sc. Computer Science", "role"),
        P("University of Ghana, Legon &nbsp;-> Expected 2027", "meta"),
        *bullets([
            "Relevant coursework: Data Structures & Algorithms, AI, Machine "
            "Learning, Databases, Software Engineering, Operating Systems.",
        ]),
    ]),

    P("LEADERSHIP & COMMUNITY", "section"),
    Paragraph("<b>Claude Campus Ambassador, University of Ghana:</b> 2026 &ndash; present, "
              "Representative for Claude AI, guiding students and faculty on effective "
              "AI tool usage and responsible implementation.", styles["bullet"]),
    Paragraph("<b>Founder &mdash; dotBAC (.BAC) Community:</b> student tech community "
              "mentoring young enthusiasts through real-world projects, with "
              "documented success stories.", styles["bullet"]),
    Paragraph("<b>HealthTrust (Alle-AI Hackathon):</b> used Alle AI's NLP to "
              "analyse public health data and produce vaccination education content.", styles["bullet"]),


]


def build(path):
    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=17 * mm, rightMargin=17 * mm,
                          topMargin=14 * mm, bottomMargin=14 * mm,
                          title="Amoako Benedict Acheampong - Resume",
                          author="Amoako Benedict Acheampong")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
                  id="main")
    doc.addPageTemplates([PageTemplate(id="page", frames=[frame])])
    doc.build(story)


if __name__ == "__main__":
    build("Benedict_Acheampong_Resume.pdf")
    print("built resume pdf")