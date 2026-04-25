# Cookie Consent Management Guide

**Document ID:** PIMS-SUP-015  
**Version:** 1.0 | **Date:** 2025-01-01  
**Owner:** DPO | **Classification:** Internal

---

## 1. Purpose

This guide defines the organisation's approach to cookie consent management in compliance with the Privacy and Electronic Communications Regulations 2003 (PECR), UK GDPR, and EU ePrivacy Directive. It supports the Consent Management Procedure (PIMS-OPS-005) for digital channels.

---

## 2. Cookie Categories

### 2.1 Strictly Necessary Cookies
- **Consent required?** NO — may be set without consent
- **Purpose:** Essential for the website to function (session management, shopping cart, security tokens, load balancing, authentication)
- **Examples:** Session ID, CSRF tokens, load balancer cookies, login state cookies
- **Retention:** Session or short duration (typically 24 hours or less)

### 2.2 Performance / Analytics Cookies
- **Consent required?** YES
- **Purpose:** Measure how visitors use the website (page views, traffic sources, time on page)
- **Examples:** Google Analytics (_ga, _gid), Hotjar, Pendo, Mixpanel
- **Retention:** Typically 13 months
- **Default state in CMP:** OFF (must be actively enabled by user)

### 2.3 Functional / Preference Cookies
- **Consent required?** YES (some jurisdictions allow without consent if strictly necessary for user-requested feature)
- **Purpose:** Remember user preferences (language, region, accessibility settings, chat widget state)
- **Examples:** Language preference cookie, currency selection, accessibility settings
- **Default state in CMP:** OFF (unless essential for service)

### 2.4 Marketing / Targeting Cookies
- **Consent required?** YES — explicit opt-in required
- **Purpose:** Track users across websites; personalised advertising; retargeting
- **Examples:** Facebook Pixel (fbp, fbclid), Google Ads (_gcl_au), LinkedIn Insight Tag, DoubleClick
- **Default state in CMP:** OFF — user must actively opt in
- **Note:** These cookies have highest risk profile; require most prominent disclosure

### 2.5 Social Media Cookies
- **Consent required?** YES
- **Purpose:** Enable social media sharing; track engagement with social content on site
- **Examples:** Twitter pixel, LinkedIn tracking, YouTube embedded video cookies
- **Default state in CMP:** OFF

---

## 3. Consent Management Platform (CMP) Requirements

### 3.1 Mandatory CMP Features

Your CMP must include:

| Feature | Requirement |
|---------|------------|
| **Cookie banner** | Displayed on first visit before any non-essential cookies are set |
| **Accept all button** | Prominently displayed |
| **Reject all button** | Equally prominent as Accept All — same size, colour, position |
| **Manage preferences** | Allow granular category-level consent |
| **Pre-ticked boxes** | PROHIBITED — no pre-ticked boxes for non-essential cookies |
| **Implied consent** | PROHIBITED — silence, scrolling, or continued use is not valid consent |
| **Re-visit preferences** | Accessible link/icon at all times (footer) to change preferences |
| **Consent record** | Capture timestamp, version of notice, IP address (where permitted), choices made |
| **Consent withdrawal** | User can withdraw consent as easily as they gave it |

### 3.2 CMP Design Best Practices

| Element | Best Practice |
|---------|--------------|
| **Banner text** | Clear, plain language; avoid legal jargon |
| **Colour scheme** | Reject/Decline button must be same visual prominence as Accept |
| **No dark patterns** | Do not make rejection harder than acceptance; do not use misleading UI |
| **Mobile-responsive** | CMP must work correctly on mobile and tablet |
| **Layered approach** | Banner summary + detailed preference centre available |
| **Cookie policy link** | Always link to full cookie policy from the banner |

### 3.3 Cookie Policy Content Requirements

Your cookie policy must include:
- What cookies are used and why (category + specific cookie name, provider, purpose, expiry)
- How to manage or delete cookies
- How to withdraw consent
- How to complain to the ICO
- Date of last update

---

## 4. Cookie Audit Process

Conduct a cookie audit **at least annually** and when significant website changes occur:

| Step | Action |
|------|--------|
| 1 | Use a cookie scanning tool (e.g., OneTrust, Cookiebot, CookieYes) to discover all cookies set by the website |
| 2 | Categorise each cookie (Strictly Necessary / Analytics / Functional / Marketing / Social) |
| 3 | Verify the CMP is correctly blocking non-essential cookies before consent |
| 4 | Verify all cookies are disclosed in the cookie policy |
| 5 | Test that Reject All correctly blocks all non-essential cookies |
| 6 | Test that Accept All correctly allows all non-essential cookies |
| 7 | Test that granular preferences work correctly (e.g., accepting Analytics but rejecting Marketing) |
| 8 | Test on mobile devices |
| 9 | Document audit results and any remediation actions |
| 10 | Update cookie policy to reflect current cookie inventory |

---

## 5. Third-Party Scripts and Tag Management

| Risk | Control |
|------|---------|
| Third-party scripts setting cookies before consent | Use a Tag Manager (e.g., Google Tag Manager) configured to fire tags only after consent granted |
| New cookies introduced by third parties without notice | Include cookie audit in change management process; audit after any new script deployment |
| Consent not passed to third-party platforms | Configure CMP to pass consent signals via Consent Mode (Google) or equivalent |

---

## 6. Consent Records

For each user interaction with the CMP, capture and retain:

| Field | Description |
|-------|------------|
| Consent ID | Unique identifier |
| Date / timestamp | Exact datetime of consent interaction |
| Consent action | Accepted all / Rejected all / Custom preferences |
| Preference details | Which categories were accepted/rejected |
| CMP version | Version of cookie notice at time of consent |
| User agent | Browser type (not individual ID) |
| Retention period | 3 years from consent date |

---

## 7. Compliance Checklist

| # | Check | Status |
|---|-------|--------|
| 1 | CMP deployed on all web properties | ☐ |
| 2 | Non-essential cookies blocked before consent | ☐ |
| 3 | Reject All button as prominent as Accept All | ☐ |
| 4 | No pre-ticked boxes | ☐ |
| 5 | Granular category preferences available | ☐ |
| 6 | Cookie policy updated and accurate | ☐ |
| 7 | Consent records captured and stored | ☐ |
| 8 | Preference centre accessible at all times | ☐ |
| 9 | Annual cookie audit conducted | ☐ |
| 10 | Tag Manager configured for consent-based firing | ☐ |

---

## 8. Key References

- UK ICO Cookie Guidance (ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/)
- EU ePrivacy Directive and national implementations
- GDPR Article 7 (conditions for consent)
- PIMS-OPS-005 (Consent Management Procedure)

---

*ISO/IEC 27701:2025 PIMS Toolkit | Cookie Consent Management Guide | PIMS-SUP-015*
