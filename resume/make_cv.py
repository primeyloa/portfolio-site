#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate a fuller academic-style CV PDF with ReportLab."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
    HRFlowable, KeepTogether,
)
from reportlab.lib.styles import ParagraphStyle

ACCENT = HexColor("#0a7ea4")
DARK = HexColor("#1a1a1a")
GREY = HexColor("#555555")

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19,
                           leading=22, textColor=DARK, spaceAfter=1),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8.5,
                              leading=11, textColor=GREY),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=11,
                              leading=13, textColor=ACCENT, spaceBefore=10,
                              spaceAfter=2),
    "entry": ParagraphStyle("entry", fontName="Helvetica-Bold", fontSize=9.5,
                            leading=12, textColor=DARK, spaceBefore=4),
    "meta": ParagraphStyle("meta", fontName="Helvetica-Oblique", fontSize=8.5,
                           leading=11, textColor=GREY, spaceAfter=1),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9,
                           leading=11.5, textColor=DARK, leftIndent=10,
                           spaceAfter=2),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9,
                              leading=11.5, textColor=DARK, leftIndent=12,
                              bulletIndent=4, spaceAfter=1.5),
}


def hr():
    return HRFlowable(width="100%", thickness=0.8, color=ACCENT,
                      spaceBefore=1, spaceAfter=4)


def P(text, style):
    return Paragraph(text, styles[style])


def link(url, text=None):
    """Wrap a URL in a real, clickable PDF hyperlink (accent-coloured)."""
    label = text or url.replace("https://", "").replace("mailto:", "")
    return f'<a href="{url}" color="#0a7ea4"><u>{label}</u></a>'


def bullets(items):
    return [Paragraph(f"<bullet>&bull;</bullet> {t}", styles["bullet"])
            for t in items]


def entry(title, meta, items):
    return KeepTogether([
        P(title, "entry"),
        P(meta, "meta"),
        *bullets(items),
    ])


story = [
    P("Amoako Benedict Acheampong", "name"),
    P(f"Accra, Ghana &nbsp;|&nbsp; (+233) 50 572 2027 &nbsp;|&nbsp; "
      f'{link("mailto:amoakoben40@gmail.com")}', "contact"),
    P(f'{link("https://benedictamoako.vercel.app")} &nbsp;|&nbsp; '
      f'{link("https://linkedin.com/in/amoakoben")} &nbsp;|&nbsp; '
      f'{link("https://github.com/primeyloa")} &nbsp;|&nbsp; '
      f'{link("https://x.com/yloa_nyame")} &nbsp;|&nbsp; '
      f'{link("https://yloa.substack.com")} (essays)', "contact"),
    Spacer(1, 2),
    hr(),

    P("PROFILE", "section"),
    P("Computer Science student and researcher with a focus on applied machine "
      "learning &mdash; particularly vision-language models, NLP for low-resource "
      "languages, and fairness in automated classification systems. Combines "
      "research experience (model fine-tuning, dataset curation, systematic "
      "evaluation) with production engineering (backend platforms, payment "
      "integration, deployment). First-author preprint on bias in "
      "content-moderation classifiers; author of an open-source NLP corpus package "
      "for Twi. Founder of a student tech community in Accra.", "body"),

    P("EDUCATION", "section"),
    entry(
        "B.Sc. Computer Science",
        "University of Ghana, Legon &nbsp;-> 2024 &ndash; 2027 (expected)",
        [
            "Relevant coursework: Data Structures & Algorithms, Artificial "
            "Intelligence, Machine Learning, Database Fundamentals, Object-Oriented "
            "Programming, Human-Computer Interaction, Operating Systems, Discrete "
            "Mathematics, Calculus, Software Engineering.",
        ]),

    P("RESEARCH & PUBLICATIONS", "section"),
    entry(
        "Crisis-Driven Bias in Social Media Flagging: Quantifying Topic "
        "Sensitivity in Content Moderation Classifiers",
        "Preprint (solo author), 2026 &nbsp;-> "
        f'{link("https://doi.org/10.13140/RG.2.2.24694.36165")}',
        [
            "Investigates how content-moderation classifiers exhibit heightened "
            "topic sensitivity during crisis periods, and quantifies the resulting "
            "flagging bias across topics.",
            "Contributes methods for measuring topic-sensitivity in moderation "
            "systems at the intersection of NLP and algorithmic fairness.",
        ]),
    entry(
        "Fine-tuning Vision-Language Models for Tropical Skin Disease "
        "Classification on Dark Skin Tones",
        "Data Intelligence & Swarm Analytics (DISAL), Accra &nbsp;-> "
        "2025 &ndash; 2026",
        [
            "Fine-tuned Google MedGemma 4B with Low-Rank Adaptation (LoRA, via "
            "Unsloth) under memory constraints for tropical skin-disease "
            "classification optimised for dark (Fitzpatrick V&ndash;VI) skin tones.",
            "Built the data pipeline: bulk image processing, quality enhancement "
            "and filtering of medical imagery; systematic evaluation of "
            "checkpoints; deployment integrated with a mobile application.",
        ]),
    entry(
        "Tourism Review Sentiment & Service-Quality Analytics",
        "Independent research project, 2025 &ndash; 2026",
        [
            "End-to-end NLP pipeline (NLTK, scikit-learn, Pandas) over "
            "large-scale public review datasets: tokenisation, Bag-of-Words, "
            "preprocessing, error analysis aligned with service-quality metrics.",
        ]),
    entry(
        "twicorpus &mdash; word lists and corpora for Twi (Akan) NLP",
        "Open-source Python package &nbsp;-> "
        f'{link("https://github.com/primeyloa/twicorpus")} &nbsp;-> pip install twicorpus',
        [
            "Authored an NLTK-style Python package exposing Twi word lists and "
            "corpora (derived from the GhanaNLP community&rsquo;s Twi "
            "Speech-Text Parallel Dataset), lowering the barrier to NLP research "
            "in a low-resource Ghanaian language.",
        ]),

    P("PROFESSIONAL EXPERIENCE", "section"),
    entry(
        "Backend Engineer Intern (Remote)",
        "Scholafrik &nbsp;-> Apr 2026 &ndash; Sep 2026",
        [
            "Shipped backend features in a TypeScript codebase with strict type "
            "safety; wrote and maintained tests and managed database queries.",
            "Collaborated in a remote agile team to integrate new product features "
            "end-to-end, from design review to production.",
        ]),
    entry(
        "Machine Learning Research Intern",
        "Data Intelligence & Swarm Analytics (DISAL), Accra &nbsp;-> "
        "Sep 2025 &ndash; Dec 2025",
        [
            "Conducted research into building and fine-tuning LLMs for predicting "
            "specific classes of skin disease, with a focus on tropical diseases "
            "prevalent in Africa.",
            "Deployed a model optimised for dark skin tones, reducing prediction "
            "bias for an underserved population.",
        ]),
    entry(
        "IT Business Analyst (Pro-bono)",
        "Agyaben Skin Clinic, Accra &nbsp;-> Nov 2025",
        [
            "Analysed patient intake-to-consultation workflows; identified "
            "operational pain points and implemented a hybrid scheduling and "
            "management system to reduce congestion and queueing.",
        ]),
    entry(
        "Co-founder",
        "Umbrella (insurtech), Accra &nbsp;-> 2025",
        [
            "Developed and managed the technology vision for weather-based "
            "index-insurance solutions for farmers (B2C model).",
        ]),

    P("SELECTED ENGINEERING PROJECTS", "section"),
    entry(
        "CauseHive &mdash; donation management platform",
        "Django REST Framework, React (Vite), PostgreSQL, Celery, Redis, Paystack "
        f'&nbsp;-> {link("https://github.com/primeyloa/CauseHive-front")}',
        [
            "Led full backend development in an agile team; consolidated four "
            "microservices into a deployable Django monolith with per-domain "
            "databases and a custom database router.",
            "Implemented JWT auth, rate limiting, Celery background jobs and the "
            "Paystack payment gateway supporting donations across multiple "
            "African countries.",
        ]),
    entry(
        "Service Hub &mdash; campus service-operations optimiser",
        "Java, SQLite, Java Swing (joint university project) "
        f'&nbsp;-> {link("https://github.com/primeyloa/Service-Hub")}',
        [
            "Co-built a smart service-request dispatcher for the University of "
            "Ghana campus: custom data structures (heaps, red-black trees, graphs) "
            "and algorithms (Dijkstra, MST, knapsack) with a simulation GUI and "
            "empirical benchmarker.",
        ]),
    entry(
        "Twi ASR &mdash; automatic speech recognition prototype",
        "React Native/Expo, TypeScript, SQLite "
        f'&nbsp;-> {link("https://github.com/primeyloa/asr")}',
        [
            "Prototype mobile app for Twi speech transcription with simulated "
            "realtime streaming, dialect switching, transcript history and "
            "export &mdash; architecture wired for a real inference backend.",
        ]),
    entry(
        "spindle &mdash; agent harness for local LLMs",
        f'TypeScript, Vite, Supabase &nbsp;-> {link("https://github.com/primeyloa/spindle")}',
        [
            "Early-stage framework for running AI agents on locally hosted LLMs, "
            "with a focus on cross-model compatibility and an extensible "
            "skills/tools marketplace.",
        ]),
    entry(
        "Flail &mdash; AI agent for animated videos",
        f'JavaScript &nbsp;-> {link("https://github.com/primeyloa/flail")}',
        [
            "AI agent that creates short animated videos from a brief; user approves "
            "each step and every video stays as editable files based on ICMs.",
        ]),
    entry(
        "Cevin &mdash; financial literacy platform",
        f"TypeScript &nbsp;-> {link('https://github.com/primeyloa/cevin')}",
        [
            "Hackathon project helping users find reliable financial literacy and "
            "investment platforms.",
        ]),
    entry(
        "Ferlance &mdash; business intelligence for small businesses",
        f"TypeScript &nbsp;-> {link('https://ferlance.onrender.com')}",
        [
            "Business intelligence platform for Ghanaian small businesses; turns sales "
            "sheets, Mobile Money alerts and stock counts into clear numbers, honest "
            "insights and actionable answers. Features AI agent 'Lance' for instant "
            "business questions and supports 5 file formats including CSV and Excel.",
        ]),

    P("LEADERSHIP & COMMUNITY", "section"),
    # Claude Campus Ambassador comes FIRST, as requested
    entry(
        "Claude Campus Ambassador, University of Ghana",
        "2026 &ndash; present",
        [
            "Representative for Claude AI on campus, guiding students and faculty "
            "on effective AI tool usage, responsible implementation, and best "
            "practices for integrating AI into academic and personal projects.",
        ]),
    entry(
        "Founder & Community Lead &mdash; dotBAC (.BAC)",
        "Accra &nbsp;-> ongoing",
        [
            "Founded and lead a student tech community guiding young enthusiasts "
            "toward building meaningful real-world projects; featured and "
            "supported several notable community projects with documented "
            "success stories.",
        ]),
    entry(
        "HealthTrust &mdash; Alle-AI Hackathon",
        "2026",
        [
            "Built a solution leveraging Alle AI&rsquo's NLP capabilities to "
            "analyse public health data, surface insights, recommend preventive "
            "health actions and produce verified educational content on vaccines "
            "and vaccination worldwide.",
        ]),

    P("TECHNICAL SKILLS", "section"),
    P("<b>Languages:</b> Python, TypeScript/JavaScript, Java, C#, SQL, "
      "Prolog (exposure)", "body"),
    P("<b>ML / AI:</b> LoRA fine-tuning, Unsloth, MedGemma, scikit-learn, NLTK, "
      "computer vision, sentiment analysis, topic modeling, evaluation & "
      "error analysis", "body"),
    P("<b>Backend & data:</b> Django REST Framework, MongoDB, PostgreSQL, "
      "Redis, Celery, JWT auth, REST API design, Postman", "body"),
    P("<b>Frontend & mobile:</b> React (Vite), React Native/Expo, HTML/CSS, "
      "Tailwind, Bootstrap", "body"),
    P("<b>Tools & practice:</b> Git/GitHub, Docker, Railway, Google Colab, "
      "Linux, agile teamwork, technical writing", "body"),

    P("SPOKEN LANGUAGES", "section"),
    P("English (fluent), Twi (native)", "body"),
]


def build(path):
    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=17 * mm, rightMargin=17 * mm,
                          topMargin=14 * mm, bottomMargin=14 * mm,
                          title="Amoako Benedict Acheampong - Curriculum Vitae",
                          author="Amoako Benedict Acheampong")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
                  id="main")
    doc.addPageTemplates([PageTemplate(id="page", frames=[frame])])
    doc.build(story)


if __name__ == "__main__":
    build("Benedict_Acheampong_CV.pdf")
    print("built cv pdf")
