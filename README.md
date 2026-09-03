# portfolio-site

Portfolio site, resume and CV for **Amoako Benedict Acheampong**.

## Structure

```
site/                    ← portfolio site (static, GitHub Pages–ready)
  index.html               single-page site, dark theme, no dependencies
resume/                  ← generated documents + generators
  make_resume.py           ReportLab script → Benedict_Acheampong_Resume.pdf
  make_cv.py               ReportLab script → Benedict_Acheampong_CV.pdf
  Benedict_Acheampong_Resume.pdf   (1 page, ATS-friendly)
  Benedict_Acheampong_CV.pdf       (2 pages, academic style)
resume_resources/        ← original source material provided by Benedict
```

## Regenerating the documents

Requires Python with `reportlab` (and `pypdf` to verify page counts):

```powershell
cd resume
python make_resume.py   # → Benedict_Acheampong_Resume.pdf
python make_cv.py       # → Benedict_Acheampong_CV.pdf
```

## Deploying the site

The site is a single static file. Easiest options:

- **GitHub Pages**: create a repo (e.g. `primeyloa.github.io` or `portfolio`),
  push the contents of `site/` to the default branch, enable Pages.
- Any static host (Netlify, Vercel, Cloudflare Pages): drag-and-drop `site/`.

## Editing content

All content lives directly in `site/index.html` (sections: hero, about,
experience, projects, research, contact). Update `resume/make_*.py` and rerun
to change the PDFs.

## Notes

- Replace the `.avatar` fallback block in `index.html` with a real photo when
  available (an `<img>` inside `.avatar`).
- Phone/email used across documents: amoakoben@gmail.com · +233 50 572 2027.
