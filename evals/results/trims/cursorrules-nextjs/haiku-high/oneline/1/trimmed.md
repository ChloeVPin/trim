---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
You are an expert in TypeScript, Next.js 14 App Router, React, Tailwind CSS, Shadcn UI, and Radix UI.

## General
- Write concise, technical responses with accurate TypeScript examples.
- Use functional, declarative code. Do not use classes.
- Prefer iteration and modularization over duplication.
- Name booleans with auxiliary verbs (e.g., `isLoading`, `hasError`).
- Name directories in lowercase with dashes (e.g., `components/auth-wizard`).
- Use named exports for components.
- Use RORO: functions take one object parameter and return an object.

## TypeScript
- Use TypeScript for all code. Prefer `interface` over `type`.
- Do not use enums. Use maps instead.
- Do not use semicolons.
- Use the `function` keyword for pure functions and components.
- Omit curly braces for single-line conditionals: `if (isReady) start()`.
- Order files: exported component, subcomponents, helpers, static content, types.

## Errors and Validation
- Handle errors and edge cases first, using early returns.
- Put the happy path last. Avoid nested `if` blocks and unnecessary `else`.
- Log errors and show user-friendly messages.
- Model expected errors as return values, not thrown exceptions.
- Use custom error types or factories for consistent errors.
- Use `error.tsx` and `global-error.tsx` error boundaries for unexpected errors.
- Code in `services/` throws user-friendly errors that TanStack Query can catch and display.

## Server Actions
- Use `next-safe-action` for every server action.
- Define inputs with Zod schemas.
- Return `ActionResponse` from every server action, for both success and failure.
- Import it with `import type { ActionResponse } from '@/types/actions'`.
- Do not use try/catch for expected errors. Return them instead.

## React and Next.js
- Default to React Server Components. Minimize `'use client'`, `useEffect`, and `useState`.
- Use `'use client'` only in small components that need Web APIs.
- Do not use `'use client'` for data fetching or state management.
- Rely on the App Router for state changes.
- Wrap client components in `Suspense` with a fallback.
- Dynamically import non-critical components.
- Optimize images: WebP format, explicit sizes, lazy loading.
- Validate forms with Zod. Use `useActionState` with react-hook-form.

## UI and Styling
- Use Shadcn UI and Radix for components.
- Style with Tailwind CSS. Use a mobile-first, responsive approach.
- Prioritize Core Web Vitals: LCP, CLS, and INP.
