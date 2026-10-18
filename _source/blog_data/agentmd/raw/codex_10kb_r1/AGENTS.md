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
