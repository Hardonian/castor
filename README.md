# Podcast Analytics & Sponsorship Platform

**Turn your podcast into a revenue-generating machine with enterprise-grade analytics, automated sponsor matching, and real-time attribution tracking.**

> **YC Readiness:** Comprehensive YC application and interview prep materials available in [`/yc/`](yc/README.md) directory.

---

## What This Is

A complete, production-ready platform that solves the hardest problems in podcast monetization. We've built everything you need to track listener behavior, match with sponsors, measure campaign performance, and prove ROI—all in one unified system.

Most podcasters are flying blind. They don't know who's listening, when campaigns actually convert, or how to price their inventory. This platform fixes that. It's the infrastructure that turns podcasts into measurable, scalable businesses.

---

## Why This Exists

Podcast monetization is broken. Here's what's wrong:

- **No visibility**: You can't see who's listening, where they're coming from, or what drives conversions
- **Manual matching**: Finding sponsors is a time-consuming, relationship-dependent process
- **Attribution chaos**: Proving ROI means cobbling together data from multiple sources, and it's still guesswork
- **Pricing blind spots**: You're either leaving money on the table or pricing yourself out of deals

We built this because we needed it. After running podcast operations at scale, we realized the tools don't exist. So we built them.

---

## What You Get

### 📊 **Real-Time Analytics That Actually Matter**

Track listener behavior, episode performance, and audience demographics. Not just downloads—actual insights that help you make decisions. See which episodes drive engagement, which topics resonate, and how your audience grows over time.

### 🎯 **Intelligent Sponsor Matching**

Stop cold-emailing sponsors. Our AI-powered matching engine analyzes advertiser needs against podcast content, audience, and performance data to surface perfect-fit opportunities automatically.

### 💰 **Attribution That Proves ROI**

Multiple attribution models (first-touch, last-touch, linear, time-decay, position-based) let you show sponsors exactly how campaigns perform. Cross-platform tracking connects podcast listens to website visits, purchases, and conversions.

### 📈 **Automated Campaign Management**

From insertion orders to performance reports, automate the entire campaign lifecycle. Set up automated workflows that create IOs when deals close, recalculate matches when data changes, and generate reports on schedule.

### 🔒 **Enterprise-Grade Security & Multi-Tenancy**

Built for agencies, networks, and platforms that manage multiple podcasts. Tenant isolation, role-based access control, and comprehensive audit logs ensure data security and compliance.

### 🤖 **AI-Powered Insights**

Content analysis, anomaly detection, and predictive analytics help you understand what's working and what's not. Get recommendations on episode topics, optimal ad placement, and audience growth strategies.

---

## Real-World Use Cases

**Solo Podcaster**: Track which episodes drive the most engagement, prove value to sponsors with attribution data, and automate campaign reporting so you can focus on creating content.

**Podcast Network**: Manage dozens of shows, match advertisers across your entire inventory, and provide unified reporting to sponsors while maintaining show-level autonomy.

**Agency**: Onboard new podcast clients quickly, demonstrate ROI with cross-platform attribution, and scale operations without hiring more account managers.

**Enterprise Platform**: White-label the entire platform, offer it to your podcast creators, and monetize through revenue sharing while maintaining full control over the experience.

**Advertiser**: Find podcasts that match your target audience, track campaign performance across multiple shows, and optimize spend based on real attribution data.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend (Next.js)                      │
│         Dashboard | Analytics | Campaign Management         │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│                   API Layer (FastAPI)                        │
│  REST APIs | Authentication | Authorization | Webhooks      │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
┌───────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐
│  PostgreSQL  │ │  TimescaleDB │ │    Redis    │
│  (Relational)│ │ (Time-Series)│ │   (Cache)  │
└──────────────┘ └─────────────┘ └────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│              Background Processing Layer                      │
│  RSS Ingestion | Analytics Aggregation | Workflow Engine   │
└─────────────────────────────────────────────────────────────┘
```

**Key Components:**
- **Ingestion**: RSS feed polling, episode metadata extraction, host API integrations
- **Analytics Store**: Time-series data storage, listener metrics, attribution events
- **Campaign Management**: CRUD operations, sponsor relationships, lifecycle management
- **Attribution Engine**: Multiple models, cross-platform tracking, ROI calculations
- **AI Framework**: Content analysis, predictive analytics, anomaly detection
- **Orchestration**: Workflow engine, intelligent automation, event-driven processes

---

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 15+ (with TimescaleDB extension for time-series data)
- Redis 7+
- Node.js 20+ (for frontend)
- PostgreSQL client tools (`psql`) for migrations

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/podcast-analytics-platform.git
cd podcast-analytics-platform

# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration (see Database Setup below)

# Start local database (using Docker Compose)
docker-compose up -d postgres redis

# Run database migrations
./scripts/db-migrate-local.sh

# Start the backend API
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# In another terminal, start the frontend
cd frontend
npm install
npm run dev
```

### Database Setup

#### Local Development

1. **Start PostgreSQL with TimescaleDB**:
   ```bash
   docker-compose up -d postgres
   ```

2. **Apply migrations**:
   ```bash
   ./scripts/db-migrate-local.sh
   ```

   Or manually:
   ```bash
   psql postgresql://postgres:postgres@localhost:5432/podcast_analytics \
     -f db/migrations/99999999999999_master_schema.sql
   ```

#### Production / Hosted Database

**Recommended: Supabase** (see `docs/backend-options-and-costs.md` for analysis)

1. **Get connection string** from your database provider
2. **Set environment variable**:
   ```bash
   export DATABASE_URL="postgresql://user:password@host:5432/database"
   ```
3. **Apply migration**:
   ```bash
   ./scripts/db-migrate-hosted.sh
   ```

**Important**: Always create a backup before applying migrations to production!

For detailed migration instructions, see [`docs/migrations-workflow.md`](docs/migrations-workflow.md).

#### Environment Variables

Configure database connection in `.env`:

```bash
# Option 1: Use DATABASE_URL (recommended)
DATABASE_URL=postgresql://user:password@host:5432/database

# Option 2: Use individual variables (for backward compatibility)
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=podcast_analytics
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

See [`.env.example`](.env.example) for all available configuration options.

### Your First 10 Minutes

1. **Start the services**: Follow the installation steps above
2. **Create a tenant**: `POST /api/v1/tenants` with your organization details
3. **Add a podcast**: `POST /api/v1/podcasts` with your RSS feed URL
4. **View analytics**: Navigate to `/dashboard` to see listener metrics
5. **Set up attribution**: Configure tracking URLs for your campaigns

---

## Project Structure

```
podcast-analytics-platform/
├── src/                          # Backend source code
│   ├── api/                      # FastAPI route handlers
│   ├── analytics/                 # Analytics store and ROI calculator
│   ├── attribution/              # Attribution models and engine
│   ├── campaigns/                # Campaign management
│   ├── database/                 # Database connections (Postgres, Redis, Timescale)
│   ├── ingestion/                # RSS feed ingestion
│   ├── ai/                       # AI framework and content analysis
│   ├── orchestration/            # Workflow engine and automation
│   ├── telemetry/                # Metrics and event logging
│   └── main.py                   # Application entry point
│
├── frontend/                     # Next.js frontend application
│   ├── app/                      # Next.js app router pages
│   ├── components/               # React components
│   └── public/                   # Static assets
│
├── tests/                        # Test suite
│   ├── unit/                     # Unit tests
│   ├── integration/               # Integration tests
│   └── e2e/                      # End-to-end tests
│
├── db/                           # Database migrations
│   └── migrations/               # Master migration file
│       └── 99999999999999_master_schema.sql
├── migrations_archive/           # Legacy migrations (archived)
├── scripts/                      # Utility scripts
│   ├── db-migrate-local.sh       # Local migration script
│   └── db-migrate-hosted.sh      # Hosted migration script
├── docs/                         # Additional documentation
│   ├── backend-discovery.md      # Backend infrastructure discovery
│   ├── data-model-overview.md    # Database schema overview
│   ├── backend-options-and-costs.md  # Backend hosting analysis
│   └── migrations-workflow.md    # Migration workflow guide
└── README.md                     # This file
```

---

## Key Features in Detail

### Multi-Tenant Architecture
Every organization gets isolated data, custom branding, and independent configuration. Perfect for agencies managing multiple clients or platforms offering white-label solutions.

### Advanced Attribution Models
Choose the attribution model that fits your needs:
- **First Touch**: Credit the first interaction
- **Last Touch**: Credit the final interaction before conversion
- **Linear**: Distribute credit evenly across all touchpoints
- **Time Decay**: Give more credit to recent interactions
- **Position Based**: Weight first and last touchpoints more heavily

### Automated Workflows
Define workflows that trigger on events. Examples:
- Auto-create insertion orders when deals reach "won" stage
- Recalculate matches when advertiser or podcast data changes
- Generate and email reports on a schedule
- Send alerts when campaigns underperform

### Cost Tracking & Optimization
Track resource usage and costs per tenant. Monitor API calls, database queries, storage, and compute. Set budgets and get alerts when thresholds are exceeded.

### Security & Compliance
- OAuth2 authentication with JWT tokens
- Multi-factor authentication (MFA)
- Role-based access control (RBAC)
- Attribute-based access control (ABAC)
- API key management
- Comprehensive audit logs

---

## Development

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_analytics.py -v
```

### Code Quality

```bash
# Lint code
ruff check src/ tests/

# Format code
ruff format src/ tests/

# Type checking
mypy src/
```

### Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install
```

---

## CI/CD

This project uses GitHub Actions for continuous integration. The CI pipeline:

1. **Lints** backend (ruff) and frontend (ESLint)
2. **Type checks** backend (mypy) and frontend (TypeScript)
3. **Runs tests** with coverage reporting
4. **Builds** Docker images for deployment

See `.github/workflows/ci.yml` for details.

To run CI checks locally:

```bash
make ci          # Run all CI checks
make lint        # Lint code
make type-check  # Type check
make test        # Run tests
make build       # Build artifacts
```

---

## Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`pytest tests/`)
6. Run linting and type checking
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Documentation

### YC Readiness
- **[YC Readiness Documentation](yc/README.md)** - Comprehensive YC application and interview prep materials
- [YC Product Overview](yc/YC_PRODUCT_OVERVIEW.md) - Product narrative for YC application
- [YC Interview Cheat Sheet](yc/YC_INTERVIEW_CHEATSHEET.md) - Interview prep with answers
- [YC Gap Analysis](yc/YC_GAP_ANALYSIS.md) - Gaps vs YC expectations

### Getting Started
- [Local Development Guide](docs/local-dev.md) - Set up your local development environment
- [Stack Discovery](docs/stack-discovery.md) - Complete technology stack overview
- [Environment Variables & Secrets](docs/env-and-secrets.md) - Environment configuration guide
- [Quick Setup Script](scripts/setup-local.sh) - One-command local setup

### Architecture & Strategy
- [Backend Strategy](docs/backend-strategy.md) - Backend architecture and database hosting
- [Frontend Hosting Strategy](docs/frontend-hosting-strategy.md) - Frontend deployment and Vercel setup
- [CI/CD Overview](docs/ci-overview.md) - CI workflows and branch protection
- [System Architecture](architecture/system-architecture.md) - Detailed architecture diagrams
- [Tech Overview](yc/YC_TECH_OVERVIEW.md) - Technical architecture for YC

### Operations
- [Cost & Limits](docs/cost-and-limits.md) - Hosting costs and usage limits
- [Demo Script](docs/demo-script.md) - Step-by-step demo guide
- [Migrations Workflow](docs/migrations-workflow.md) - How to run database migrations

### Additional Documentation
- [Backend Discovery](docs/backend-discovery.md) - Database infrastructure and migration framework
- [Data Model Overview](docs/data-model-overview.md) - Complete database schema documentation
- [Backend Options & Costs](docs/backend-options-and-costs.md) - Hosting analysis (Supabase vs alternatives)
- [Pricing Plan](monetization/pricing-plan.md) - Pricing tiers and conversion logic
- [API Documentation](http://localhost:8000/api/docs) - Interactive API docs (when running locally)
- [User Personas](research/user-persona-matrix.md) - Target user profiles
- [Analytics Events](validation/analytics-events.md) - Event tracking reference
- [Metrics API](http://localhost:8000/api/v1/metrics/dashboard) - Metrics endpoints (when running locally)

---

## License

See [LICENSE](LICENSE) file for details.

---

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/podcast-analytics-platform/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/podcast-analytics-platform/discussions)
- **Email**: scottrmhardie@gmail.com
- **Founder/CEO**: Scott Hardie
- **LinkedIn**: www.linkedin.com/in/scottrmhardie

---

## Star This Repo

If this project helps you, please give it a star ⭐. It helps others discover the project and motivates continued development.

---

**Built with ❤️ for podcasters who want to build real businesses.**

*Last Updated: 2024*


## Repository Operations Standards

- Squash-only merges
- Auto-delete merged branches
- Weekly dependency update windows
- Security scanning in CI
