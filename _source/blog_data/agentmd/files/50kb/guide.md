# Project guide

This repository is a TypeScript monorepo for an online bookstore: a Next.js web app, a Node API and shared packages.
Read this file before making changes. Keep answers short and change only what the task needs.

## Commands
- Install: pnpm install
- Dev server: pnpm dev (web on :3000, api on :4000)
- Tests: pnpm test (Vitest), pnpm test:e2e (Playwright)
- Lint and types: pnpm lint && pnpm typecheck

## Module: auth
- Put new auth code under packages/auth/src and export it through packages/auth/src/index.ts; never import from another package's internal files.
- Write unit tests for auth next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in auth must sit behind a flag named auth.<feature> in feature-flags until product signs it off.
- Migrations for auth live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.

## Module: billing
- Log billing errors with logger.error({ module: 'billing', err }) and never log personal data such as emails, addresses or card numbers.
- When billing needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep billing React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for billing goes through the billingRepository class; do not call Prisma directly from route handlers or React components.

## Module: catalog
- User-facing strings in catalog go through t('catalog.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in catalog needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the catalog API with the zod schema in packages/catalog/src/schema.ts before using it.
- The catalog module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().

## Module: search
- Write unit tests for search next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in search must sit behind a flag named search.<feature> in feature-flags until product signs it off.
- Migrations for search live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new search code under packages/search/src and export it through packages/search/src/index.ts; never import from another package's internal files.

## Module: cart
- When cart needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep cart React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for cart goes through the cartRepository class; do not call Prisma directly from route handlers or React components.
- Log cart errors with logger.error({ module: 'cart', err }) and never log personal data such as emails, addresses or card numbers.

## Module: checkout
- Every public function in checkout needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the checkout API with the zod schema in packages/checkout/src/schema.ts before using it.
- The checkout module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in checkout go through t('checkout.<key>') so they can be translated; do not hard-code English text in components.

## Module: orders
- Feature work in orders must sit behind a flag named orders.<feature> in feature-flags until product signs it off.
- Migrations for orders live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new orders code under packages/orders/src and export it through packages/orders/src/index.ts; never import from another package's internal files.
- Write unit tests for orders next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.

## Module: inventory
- Keep inventory React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for inventory goes through the inventoryRepository class; do not call Prisma directly from route handlers or React components.
- Log inventory errors with logger.error({ module: 'inventory', err }) and never log personal data such as emails, addresses or card numbers.
- When inventory needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.

## Module: shipping
- Validate every request body that reaches the shipping API with the zod schema in packages/shipping/src/schema.ts before using it.
- The shipping module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in shipping go through t('shipping.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in shipping needs a JSDoc comment that states its inputs, its return value and the errors it can throw.

## Module: reviews
- Migrations for reviews live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new reviews code under packages/reviews/src and export it through packages/reviews/src/index.ts; never import from another package's internal files.
- Write unit tests for reviews next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in reviews must sit behind a flag named reviews.<feature> in feature-flags until product signs it off.

## Module: recommendations
- Database access for recommendations goes through the recommendationsRepository class; do not call Prisma directly from route handlers or React components.
- Log recommendations errors with logger.error({ module: 'recommendations', err }) and never log personal data such as emails, addresses or card numbers.
- When recommendations needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep recommendations React components small: one component per file, props typed with an interface named <Component>Props.

## Module: notifications
- The notifications module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in notifications go through t('notifications.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in notifications needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the notifications API with the zod schema in packages/notifications/src/schema.ts before using it.

## Module: admin
- Put new admin code under packages/admin/src and export it through packages/admin/src/index.ts; never import from another package's internal files.
- Write unit tests for admin next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in admin must sit behind a flag named admin.<feature> in feature-flags until product signs it off.
- Migrations for admin live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.

## Module: analytics
- Log analytics errors with logger.error({ module: 'analytics', err }) and never log personal data such as emails, addresses or card numbers.
- When analytics needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep analytics React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for analytics goes through the analyticsRepository class; do not call Prisma directly from route handlers or React components.

## Module: i18n
- User-facing strings in i18n go through t('i18n.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in i18n needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the i18n API with the zod schema in packages/i18n/src/schema.ts before using it.
- The i18n module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().

## Module: media
- Write unit tests for media next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in media must sit behind a flag named media.<feature> in feature-flags until product signs it off.
- Migrations for media live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new media code under packages/media/src and export it through packages/media/src/index.ts; never import from another package's internal files.

## Module: accounts
- When accounts needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep accounts React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for accounts goes through the accountsRepository class; do not call Prisma directly from route handlers or React components.
- Log accounts errors with logger.error({ module: 'accounts', err }) and never log personal data such as emails, addresses or card numbers.

## Module: coupons
- Every public function in coupons needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the coupons API with the zod schema in packages/coupons/src/schema.ts before using it.
- The coupons module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in coupons go through t('coupons.<key>') so they can be translated; do not hard-code English text in components.

## Module: wishlist
- Feature work in wishlist must sit behind a flag named wishlist.<feature> in feature-flags until product signs it off.
- Migrations for wishlist live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new wishlist code under packages/wishlist/src and export it through packages/wishlist/src/index.ts; never import from another package's internal files.
- Write unit tests for wishlist next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.

## Module: returns
- Keep returns React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for returns goes through the returnsRepository class; do not call Prisma directly from route handlers or React components.
- Log returns errors with logger.error({ module: 'returns', err }) and never log personal data such as emails, addresses or card numbers.
- When returns needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.

## Module: payments
- Validate every request body that reaches the payments API with the zod schema in packages/payments/src/schema.ts before using it.
- The payments module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in payments go through t('payments.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in payments needs a JSDoc comment that states its inputs, its return value and the errors it can throw.

## Module: tax
- Migrations for tax live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new tax code under packages/tax/src and export it through packages/tax/src/index.ts; never import from another package's internal files.
- Write unit tests for tax next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in tax must sit behind a flag named tax.<feature> in feature-flags until product signs it off.

## Module: gift-cards
- Database access for gift-cards goes through the gift-cardsRepository class; do not call Prisma directly from route handlers or React components.
- Log gift-cards errors with logger.error({ module: 'gift-cards', err }) and never log personal data such as emails, addresses or card numbers.
- When gift-cards needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep gift-cards React components small: one component per file, props typed with an interface named <Component>Props.

## Module: subscriptions
- The subscriptions module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in subscriptions go through t('subscriptions.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in subscriptions needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the subscriptions API with the zod schema in packages/subscriptions/src/schema.ts before using it.

## Module: feature-flags
- Put new feature-flags code under packages/feature-flags/src and export it through packages/feature-flags/src/index.ts; never import from another package's internal files.
- Write unit tests for feature-flags next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in feature-flags must sit behind a flag named feature-flags.<feature> in feature-flags until product signs it off.
- Migrations for feature-flags live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.

## Module: audit-log
- Log audit-log errors with logger.error({ module: 'audit-log', err }) and never log personal data such as emails, addresses or card numbers.
- When audit-log needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep audit-log React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for audit-log goes through the audit-logRepository class; do not call Prisma directly from route handlers or React components.

## Module: rate-limit
- User-facing strings in rate-limit go through t('rate-limit.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in rate-limit needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the rate-limit API with the zod schema in packages/rate-limit/src/schema.ts before using it.
- The rate-limit module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().

## Module: webhooks
- Write unit tests for webhooks next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in webhooks must sit behind a flag named webhooks.<feature> in feature-flags until product signs it off.
- Migrations for webhooks live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new webhooks code under packages/webhooks/src and export it through packages/webhooks/src/index.ts; never import from another package's internal files.

## Module: sitemap
- When sitemap needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep sitemap React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for sitemap goes through the sitemapRepository class; do not call Prisma directly from route handlers or React components.
- Log sitemap errors with logger.error({ module: 'sitemap', err }) and never log personal data such as emails, addresses or card numbers.

## Module: seo
- Every public function in seo needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the seo API with the zod schema in packages/seo/src/schema.ts before using it.
- The seo module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in seo go through t('seo.<key>') so they can be translated; do not hard-code English text in components.

## Module: email
- Feature work in email must sit behind a flag named email.<feature> in feature-flags until product signs it off.
- Migrations for email live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new email code under packages/email/src and export it through packages/email/src/index.ts; never import from another package's internal files.
- Write unit tests for email next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.

## Module: sms
- Keep sms React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for sms goes through the smsRepository class; do not call Prisma directly from route handlers or React components.
- Log sms errors with logger.error({ module: 'sms', err }) and never log personal data such as emails, addresses or card numbers.
- When sms needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.

## Module: exports
- Validate every request body that reaches the exports API with the zod schema in packages/exports/src/schema.ts before using it.
- The exports module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in exports go through t('exports.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in exports needs a JSDoc comment that states its inputs, its return value and the errors it can throw.

## Module: imports
- Migrations for imports live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new imports code under packages/imports/src and export it through packages/imports/src/index.ts; never import from another package's internal files.
- Write unit tests for imports next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in imports must sit behind a flag named imports.<feature> in feature-flags until product signs it off.

## Module: jobs
- Database access for jobs goes through the jobsRepository class; do not call Prisma directly from route handlers or React components.
- Log jobs errors with logger.error({ module: 'jobs', err }) and never log personal data such as emails, addresses or card numbers.
- When jobs needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep jobs React components small: one component per file, props typed with an interface named <Component>Props.

## Module: cache
- The cache module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in cache go through t('cache.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in cache needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the cache API with the zod schema in packages/cache/src/schema.ts before using it.

## Module: storage
- Put new storage code under packages/storage/src and export it through packages/storage/src/index.ts; never import from another package's internal files.
- Write unit tests for storage next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in storage must sit behind a flag named storage.<feature> in feature-flags until product signs it off.
- Migrations for storage live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.

## Module: logging
- Log logging errors with logger.error({ module: 'logging', err }) and never log personal data such as emails, addresses or card numbers.
- When logging needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep logging React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for logging goes through the loggingRepository class; do not call Prisma directly from route handlers or React components.

## Module: metrics
- User-facing strings in metrics go through t('metrics.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in metrics needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the metrics API with the zod schema in packages/metrics/src/schema.ts before using it.
- The metrics module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().

## Module: tracing
- Write unit tests for tracing next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in tracing must sit behind a flag named tracing.<feature> in feature-flags until product signs it off.
- Migrations for tracing live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new tracing code under packages/tracing/src and export it through packages/tracing/src/index.ts; never import from another package's internal files.

## Module: health
- When health needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep health React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for health goes through the healthRepository class; do not call Prisma directly from route handlers or React components.
- Log health errors with logger.error({ module: 'health', err }) and never log personal data such as emails, addresses or card numbers.

## Module: config
- Every public function in config needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the config API with the zod schema in packages/config/src/schema.ts before using it.
- The config module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in config go through t('config.<key>') so they can be translated; do not hard-code English text in components.

## Module: permissions
- Feature work in permissions must sit behind a flag named permissions.<feature> in feature-flags until product signs it off.
- Migrations for permissions live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new permissions code under packages/permissions/src and export it through packages/permissions/src/index.ts; never import from another package's internal files.
- Write unit tests for permissions next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.

## Module: teams
- Keep teams React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for teams goes through the teamsRepository class; do not call Prisma directly from route handlers or React components.
- Log teams errors with logger.error({ module: 'teams', err }) and never log personal data such as emails, addresses or card numbers.
- When teams needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.

## Module: invoices
- Validate every request body that reaches the invoices API with the zod schema in packages/invoices/src/schema.ts before using it.
- The invoices module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in invoices go through t('invoices.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in invoices needs a JSDoc comment that states its inputs, its return value and the errors it can throw.

## Module: refunds
- Migrations for refunds live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new refunds code under packages/refunds/src and export it through packages/refunds/src/index.ts; never import from another package's internal files.
- Write unit tests for refunds next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in refunds must sit behind a flag named refunds.<feature> in feature-flags until product signs it off.

## Module: pricing
- Database access for pricing goes through the pricingRepository class; do not call Prisma directly from route handlers or React components.
- Log pricing errors with logger.error({ module: 'pricing', err }) and never log personal data such as emails, addresses or card numbers.
- When pricing needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep pricing React components small: one component per file, props typed with an interface named <Component>Props.

## Module: bundles
- The bundles module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in bundles go through t('bundles.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in bundles needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the bundles API with the zod schema in packages/bundles/src/schema.ts before using it.

## Module: authors
- Put new authors code under packages/authors/src and export it through packages/authors/src/index.ts; never import from another package's internal files.
- Write unit tests for authors next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in authors must sit behind a flag named authors.<feature> in feature-flags until product signs it off.
- Migrations for authors live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.

## Module: publishers
- Log publishers errors with logger.error({ module: 'publishers', err }) and never log personal data such as emails, addresses or card numbers.
- When publishers needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep publishers React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for publishers goes through the publishersRepository class; do not call Prisma directly from route handlers or React components.

## Module: series
- User-facing strings in series go through t('series.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in series needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the series API with the zod schema in packages/series/src/schema.ts before using it.
- The series module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().

## Module: genres
- Write unit tests for genres next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in genres must sit behind a flag named genres.<feature> in feature-flags until product signs it off.
- Migrations for genres live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new genres code under packages/genres/src and export it through packages/genres/src/index.ts; never import from another package's internal files.

## Module: events
- When events needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep events React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for events goes through the eventsRepository class; do not call Prisma directly from route handlers or React components.
- Log events errors with logger.error({ module: 'events', err }) and never log personal data such as emails, addresses or card numbers.

## Module: newsletter
- Every public function in newsletter needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the newsletter API with the zod schema in packages/newsletter/src/schema.ts before using it.
- The newsletter module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in newsletter go through t('newsletter.<key>') so they can be translated; do not hard-code English text in components.

## Module: support
- Feature work in support must sit behind a flag named support.<feature> in feature-flags until product signs it off.
- Migrations for support live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new support code under packages/support/src and export it through packages/support/src/index.ts; never import from another package's internal files.
- Write unit tests for support next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.

## Module: faq
- Keep faq React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for faq goes through the faqRepository class; do not call Prisma directly from route handlers or React components.
- Log faq errors with logger.error({ module: 'faq', err }) and never log personal data such as emails, addresses or card numbers.
- When faq needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.

## Module: blog
- Validate every request body that reaches the blog API with the zod schema in packages/blog/src/schema.ts before using it.
- The blog module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in blog go through t('blog.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in blog needs a JSDoc comment that states its inputs, its return value and the errors it can throw.

## Module: cms
- Migrations for cms live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new cms code under packages/cms/src and export it through packages/cms/src/index.ts; never import from another package's internal files.
- Write unit tests for cms next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in cms must sit behind a flag named cms.<feature> in feature-flags until product signs it off.

## Module: banners
- Database access for banners goes through the bannersRepository class; do not call Prisma directly from route handlers or React components.
- Log banners errors with logger.error({ module: 'banners', err }) and never log personal data such as emails, addresses or card numbers.
- When banners needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep banners React components small: one component per file, props typed with an interface named <Component>Props.

## Module: store-locator
- The store-locator module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in store-locator go through t('store-locator.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in store-locator needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the store-locator API with the zod schema in packages/store-locator/src/schema.ts before using it.

## Module: auth
- Put new auth code under packages/auth/src and export it through packages/auth/src/index.ts; never import from another package's internal files.
- Write unit tests for auth next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in auth must sit behind a flag named auth.<feature> in feature-flags until product signs it off.
- Migrations for auth live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.

## Module: billing
- Log billing errors with logger.error({ module: 'billing', err }) and never log personal data such as emails, addresses or card numbers.
- When billing needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep billing React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for billing goes through the billingRepository class; do not call Prisma directly from route handlers or React components.

## Module: catalog
- User-facing strings in catalog go through t('catalog.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in catalog needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the catalog API with the zod schema in packages/catalog/src/schema.ts before using it.
- The catalog module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().

## Module: search
- Write unit tests for search next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in search must sit behind a flag named search.<feature> in feature-flags until product signs it off.
- Migrations for search live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new search code under packages/search/src and export it through packages/search/src/index.ts; never import from another package's internal files.

## Module: cart
- When cart needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep cart React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for cart goes through the cartRepository class; do not call Prisma directly from route handlers or React components.
- Log cart errors with logger.error({ module: 'cart', err }) and never log personal data such as emails, addresses or card numbers.

## Module: checkout
- Every public function in checkout needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the checkout API with the zod schema in packages/checkout/src/schema.ts before using it.
- The checkout module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in checkout go through t('checkout.<key>') so they can be translated; do not hard-code English text in components.

## Module: orders
- Feature work in orders must sit behind a flag named orders.<feature> in feature-flags until product signs it off.
- Migrations for orders live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new orders code under packages/orders/src and export it through packages/orders/src/index.ts; never import from another package's internal files.
- Write unit tests for orders next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.

## Module: inventory
- Keep inventory React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for inventory goes through the inventoryRepository class; do not call Prisma directly from route handlers or React components.
- Log inventory errors with logger.error({ module: 'inventory', err }) and never log personal data such as emails, addresses or card numbers.
- When inventory needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.

## Module: shipping
- Validate every request body that reaches the shipping API with the zod schema in packages/shipping/src/schema.ts before using it.
- The shipping module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in shipping go through t('shipping.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in shipping needs a JSDoc comment that states its inputs, its return value and the errors it can throw.

## Module: reviews
- Migrations for reviews live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new reviews code under packages/reviews/src and export it through packages/reviews/src/index.ts; never import from another package's internal files.
- Write unit tests for reviews next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in reviews must sit behind a flag named reviews.<feature> in feature-flags until product signs it off.

## Module: recommendations
- Database access for recommendations goes through the recommendationsRepository class; do not call Prisma directly from route handlers or React components.
- Log recommendations errors with logger.error({ module: 'recommendations', err }) and never log personal data such as emails, addresses or card numbers.
- When recommendations needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep recommendations React components small: one component per file, props typed with an interface named <Component>Props.

## Module: notifications
- The notifications module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in notifications go through t('notifications.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in notifications needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the notifications API with the zod schema in packages/notifications/src/schema.ts before using it.

## Module: admin
- Put new admin code under packages/admin/src and export it through packages/admin/src/index.ts; never import from another package's internal files.
- Write unit tests for admin next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in admin must sit behind a flag named admin.<feature> in feature-flags until product signs it off.
- Migrations for admin live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.

## Module: analytics
- Log analytics errors with logger.error({ module: 'analytics', err }) and never log personal data such as emails, addresses or card numbers.
- When analytics needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep analytics React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for analytics goes through the analyticsRepository class; do not call Prisma directly from route handlers or React components.

## Module: i18n
- User-facing strings in i18n go through t('i18n.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in i18n needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the i18n API with the zod schema in packages/i18n/src/schema.ts before using it.
- The i18n module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().

## Module: media
- Write unit tests for media next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in media must sit behind a flag named media.<feature> in feature-flags until product signs it off.
- Migrations for media live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new media code under packages/media/src and export it through packages/media/src/index.ts; never import from another package's internal files.

## Module: accounts
- When accounts needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep accounts React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for accounts goes through the accountsRepository class; do not call Prisma directly from route handlers or React components.
- Log accounts errors with logger.error({ module: 'accounts', err }) and never log personal data such as emails, addresses or card numbers.

## Module: coupons
- Every public function in coupons needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the coupons API with the zod schema in packages/coupons/src/schema.ts before using it.
- The coupons module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in coupons go through t('coupons.<key>') so they can be translated; do not hard-code English text in components.

## Module: wishlist
- Feature work in wishlist must sit behind a flag named wishlist.<feature> in feature-flags until product signs it off.
- Migrations for wishlist live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new wishlist code under packages/wishlist/src and export it through packages/wishlist/src/index.ts; never import from another package's internal files.
- Write unit tests for wishlist next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.

## Module: returns
- Keep returns React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for returns goes through the returnsRepository class; do not call Prisma directly from route handlers or React components.
- Log returns errors with logger.error({ module: 'returns', err }) and never log personal data such as emails, addresses or card numbers.
- When returns needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.

## Module: payments
- Validate every request body that reaches the payments API with the zod schema in packages/payments/src/schema.ts before using it.
- The payments module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in payments go through t('payments.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in payments needs a JSDoc comment that states its inputs, its return value and the errors it can throw.

## Module: tax
- Migrations for tax live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new tax code under packages/tax/src and export it through packages/tax/src/index.ts; never import from another package's internal files.
- Write unit tests for tax next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in tax must sit behind a flag named tax.<feature> in feature-flags until product signs it off.

## Module: gift-cards
- Database access for gift-cards goes through the gift-cardsRepository class; do not call Prisma directly from route handlers or React components.
- Log gift-cards errors with logger.error({ module: 'gift-cards', err }) and never log personal data such as emails, addresses or card numbers.
- When gift-cards needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep gift-cards React components small: one component per file, props typed with an interface named <Component>Props.

## Module: subscriptions
- The subscriptions module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in subscriptions go through t('subscriptions.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in subscriptions needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the subscriptions API with the zod schema in packages/subscriptions/src/schema.ts before using it.

## Module: feature-flags
- Put new feature-flags code under packages/feature-flags/src and export it through packages/feature-flags/src/index.ts; never import from another package's internal files.
- Write unit tests for feature-flags next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in feature-flags must sit behind a flag named feature-flags.<feature> in feature-flags until product signs it off.
- Migrations for feature-flags live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.

## Module: audit-log
- Log audit-log errors with logger.error({ module: 'audit-log', err }) and never log personal data such as emails, addresses or card numbers.
- When audit-log needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep audit-log React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for audit-log goes through the audit-logRepository class; do not call Prisma directly from route handlers or React components.

## Module: rate-limit
- User-facing strings in rate-limit go through t('rate-limit.<key>') so they can be translated; do not hard-code English text in components.
- Every public function in rate-limit needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the rate-limit API with the zod schema in packages/rate-limit/src/schema.ts before using it.
- The rate-limit module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().

## Module: webhooks
- Write unit tests for webhooks next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.
- Feature work in webhooks must sit behind a flag named webhooks.<feature> in feature-flags until product signs it off.
- Migrations for webhooks live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new webhooks code under packages/webhooks/src and export it through packages/webhooks/src/index.ts; never import from another package's internal files.

## Module: sitemap
- When sitemap needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.
- Keep sitemap React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for sitemap goes through the sitemapRepository class; do not call Prisma directly from route handlers or React components.
- Log sitemap errors with logger.error({ module: 'sitemap', err }) and never log personal data such as emails, addresses or card numbers.

## Module: seo
- Every public function in seo needs a JSDoc comment that states its inputs, its return value and the errors it can throw.
- Validate every request body that reaches the seo API with the zod schema in packages/seo/src/schema.ts before using it.
- The seo module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
- User-facing strings in seo go through t('seo.<key>') so they can be translated; do not hard-code English text in components.

## Module: email
- Feature work in email must sit behind a flag named email.<feature> in feature-flags until product signs it off.
- Migrations for email live in packages/db/migrations with a timestamp prefix; never edit a migration that has already shipped.
- Put new email code under packages/email/src and export it through packages/email/src/index.ts; never import from another package's internal files.
- Write unit tests for email next to the source as *.test.ts; aim for the happy path plus one failure case for each exported function.

## Module: sms
- Keep sms React components small: one component per file, props typed with an interface named <Component>Props.
- Database access for sms goes through the smsRepository class; do not call Prisma directly from route handlers or React components.
- Log sms errors with logger.error({ module: 'sms', err }) and never log personal data such as emails, addresses or card numbers.
- When sms needs to call another service, use the typed client in packages/clients and add a timeout of at most 5 seconds.

## Module: exports
- Validate every request body that reaches the exports API with the zod schema in packages/exports/src/schema.ts before using it.
- The exports module uses money values in integer cents; convert to a display string only in the UI layer with formatMoney().
