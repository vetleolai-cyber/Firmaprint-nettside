# Firmaprint.no PRD

## Original Problem Statement
Norsk nettbutikk for profilklær med logo (Firmaprint.no) med fokus på brodering og trykk. Målgruppe: bedrifter, lag/foreninger, arrangementer, håndverkere, SMB.

## Architecture
- **Frontend**: React 19 + Tailwind CSS + Shadcn UI
- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **Payments**: Stripe (kort) + Faktura for bedrifter
- **Auth**: JWT-basert autentisering

## User Personas
1. **Bedriftskunde**: SMB som trenger profilklær til ansatte
2. **Eventarrangør**: Trenger t-skjorter til events/konkurranser
3. **Håndverker**: Arbeidsklær med logo for teamet
4. **Lag/forening**: Capser og hoodies med logo

## Core Requirements (Static)
- [ ] Produktkatalog med kategorier
- [ ] Logo-customizer med drag-and-drop
- [ ] Handlekurv og checkout
- [ ] Stripe-betaling + faktura
- [ ] Bedriftsportal med rabatttrinn
- [ ] Tilbudsskjema
- [ ] Brodyr vs Trykk informasjon
- [ ] FAQ, kontakt, om oss

## What's Been Implemented (January 28, 2025)

### Backend (server.py)
- ✅ Auth endpoints (register, login, me)
- ✅ Product CRUD with categories/filters
- ✅ Cart management (session-based)
- ✅ Order creation with Stripe checkout
- ✅ Quote/contact forms
- ✅ Logo upload endpoint
- ✅ Price calculation for print/embroidery
- ✅ Seed data with 8 products

### Frontend Pages
- ✅ Homepage (hero, categories, bestsellers, reviews, CTA)
- ✅ Products page with filters
- ✅ Product page with customizer canvas
- ✅ Cart page
- ✅ Checkout page (Stripe + faktura)
- ✅ Business page (rabatttrinn, tilbudsskjema)
- ✅ Print vs Embroidery comparison
- ✅ FAQ page
- ✅ Contact page
- ✅ About page
- ✅ Privacy + Terms pages
- ✅ Login/Register pages

### Features
- ✅ Canvas-basert logo-plassering
- ✅ Trykkområde-visualisering
- ✅ Farge- og størrelsesvalg
- ✅ Prisberegning basert på trykk/brodyr
- ✅ Session-basert handlekurv
- ✅ Responsive design (mobil-først)

## Prioritized Backlog

### P0 (Critical)
- [ ] Stripe webhook for order confirmation
- [ ] Order confirmation email
- [ ] Logo preview in cart items

### P1 (High Priority)
- [ ] AI-genererte produktmockups
- [ ] PDF/AI filstøtte for logo
- [ ] Min ordre historikk
- [ ] Admin dashboard

### P2 (Medium Priority)
- [ ] Vipps-integrasjon
- [ ] Prøvebestilling
- [ ] Produktanbefalinger
- [ ] Lagerstatuss

### P3 (Nice to have)
- [ ] Multi-logo per produkt
- [ ] Lagre designs
- [ ] Gjenbruk av tidligere designs
- [ ] Export til print-ready PDF

## Next Tasks
1. Test Stripe checkout flow end-to-end
2. Implement order confirmation page
3. Add logo preview to cart items
4. Connect AI image generation for mockups
