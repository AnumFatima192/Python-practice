# 🗺️ DESIGN: GKS Undergraduate Info Hub

Based on early profile building for the **Global Korea Scholarship (GKS) 2029 Undergraduate Intake**. This document outlines the structural layout and architectural choices for a static informational web platform.

---

## 1. Screen Layout & Navigation

### 🌍 Shared Layout (All Pages)
- **Header (Sticky)**: Site branding on the left ("GKS-UG Portal") with clean desktop navigation links on the right (Home / UG Guidelines / Life in Korea). Converts to a responsive hamburger menu on mobile devices.
- **Footer**: A professional single-line text displaying an unofficial disclaimer (not affiliated with NIIED or the Korean Government) alongside a dynamic "Last Updated" timestamp.

### 🏠 Home Screen (`/`)
- **Hero Section**: A bold, welcoming headline explaining the purpose of the platform: *Empowering Pakistani ICS/FSc students to crack the GKS Undergraduate Scholarship.*
- **Navigation Grid**: Two high-contrast interactive cards positioned side-by-side on desktop and stacked vertically on mobile:
  - **Card 1** ➡️ Navigates directly to `/undergrad-info`
  - **Card 2** ➡️ Navigates directly to `/korea-life`

### 🎓 Undergraduate Info Screen (`/undergrad-info`)
- **Page Title**: "GKS Undergraduate Track Guidelines"
- **Structured Content (Clean Bullet Lists)**:
  1. **Eligibility Rules:** Clear GPA/Percentage requirements (80%+ threshold).
  2. **Document Checklist:** Attestation requirements for Matric and Intermediate degrees.
  3. **Application Strategy:** Step-by-step breakdown of University Track vs. Embassy Track.

### 🍁 Life in Korea Info Screen (`/korea-life`)
- **Page Title**: "Student Life & Cultural Insights"
- **Structured Content (Clean Bullet Lists)**:
  1. **Financial Allowances:** Monthly stipend breakdowns and settling-in grants.
  2. **The Language Year:** What to expect during the mandatory 1-year Korean training program.
  3. **The Survival Guide:** Managing academic pressure and cold winters in regional areas like Gwangju.

---

## 2. Static Data Flow Architect

This application operates as a high-performance **Static Site**. It intentionally bypasses external databases or user authentication to guarantee ultra-fast loading speeds on slower internet connections.

- **Data Input:** Zero forms or data entry. The system responds exclusively to routing requests triggered by navigation clicks.
- **Data Processing:** Content is fully hardcoded directly into the system's core architecture as immutable plain text or structured code arrays.
- **Data Output:** Pre-rendered HTML is instantly served to the client browser, maximizing security and accessibility.

---

## 3. Technology Stack Choices

| Technology | Architectural Purpose (Plain Language) |
| :--- | :--- |
| **Next.js / Python** | Serves as the core core architecture. Next.js creates lightning-fast static routing, ensuring seamless page-to-page transitions. |
| **Tailwind CSS** | Used for rapid layout design, using responsive utilities directly in code to maintain a clean, trustworthy blue-and-white color palette. |
| **Vercel** | The target cloud deployment infrastructure, hosting the live website globally on a fast CDN for free. |
