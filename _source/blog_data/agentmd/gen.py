import random, os
random.seed(7)
head = """# Project guide

This repository is a TypeScript monorepo for an online bookstore: a Next.js web app, a Node API and shared packages.
Read this file before making changes. Keep answers short and change only what the task needs.

## Commands
- Install: pnpm install
- Dev server: pnpm dev (web on :3000, api on :4000)
- Tests: pnpm test (Vitest), pnpm test:e2e (Playwright)
- Lint and types: pnpm lint && pnpm typecheck
"""
modules = ["auth", "billing", "catalog", "search", "cart", "checkout", "orders", "inventory", "shipping", "reviews", "recommendations", "notifications",
           "admin", "analytics", "i18n", "media", "accounts", "coupons", "wishlist", "returns", "payments", "tax", "gift-cards", "subscriptions",
           "feature-flags", "audit-log", "rate-limit", "webhooks", "sitemap", "seo", "email", "sms", "exports", "imports", "jobs", "cache",
           "storage", "logging", "metrics", "tracing", "health", "config", "permissions", "teams", "invoices", "refunds", "pricing", "bundles",
           "authors", "publishers", "series", "genres", "events", "newsletter", "support", "faq", "blog", "cms", "banners", "store-locator"]
rules = [
 "Put new {m} code under packages/{m}/src and export it through packages/{m}/src/index.ts; never import from another package's internal files.",
 "Every public function in {m} needs a JSDoc comment that states its inputs, its return value and the errors it can throw.",
 "Database access for {m} goes through the {m}Repository class; do not call Prisma directly from route handlers or React components.",
 "Write unit tests for {m} next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.",
 "Validate every request body that reaches the {m} API with the zod schema in packages/{m}/src/schema.ts before using it.",
 "Log {m} errors with logger.error({{ module: '{m}', err }}) and never log personal data such as emails, addresses or card numbers.",
 "Feature work in {m} must sit behind a flag named {m}.<feature> in feature-flags until product signs it off.",
 "The {m} module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().",
 "When {m} needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.",
 "Migrations for {m} live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.",
 "User-facing strings in {m} go through t('{m}.<key>') so they can be translated; do not hard-code English text in components.",
 "Keep {m} React components small: one component per file, props typed with an interface named <Component>Props.",
]
def build(n_bytes):
    out = [head]
    ms = modules[:]
    i = 0
    while len("\n".join(out).encode()) < n_bytes:
        m = ms[i % len(ms)]
        rs = random.sample(rules, 4)
        out.append(f"\n## Module: {m}\n" + "\n".join("- " + r.format(m=m) for r in rs))
        i += 1
    s = "\n".join(out)
    return s[:n_bytes].rsplit("\n", 1)[0] + "\n"
for kb in [1, 5, 10, 25, 50]:
    os.makedirs(f"files/{kb}kb", exist_ok=True)
    s = build(kb * 1024)
    open(f"files/{kb}kb/guide.md", "w").write(s)
    print(kb, len(s.encode()), len(s))
