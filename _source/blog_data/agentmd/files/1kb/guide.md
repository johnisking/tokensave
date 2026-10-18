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
