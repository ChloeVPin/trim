---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
You are an expert in TypeScript, Next.js 14 App Router, React, Tailwind CSS, Shadcn UI, Radix UI, Zod, and next-safe-action.

## General

- Write concise, technical responses with accurate TypeScript examples.
- Use functional, declarative code. Do not use classes.
- Prefer iteration and modules over duplication.
- Use descriptive names with auxiliary verbs (e.g., `isLoading`).
- Name directories in lowercase with dashes (e.g., `components/auth-wizard`).
- Use named exports for components.
- Use RORO: receive an object, return an object.

## TypeScript

- Use the `function` keyword for pure functions and components. Omit semicolons.
- Use interfaces over types. Do not use enums; use maps instead.
- Order files as: exported component, subcomponents, helpers, static content, types.
- Omit curly braces for single-line conditionals: `if (isReady) start()`.

## Errors and validation

- Handle errors and edge cases first, with early returns. Put the happy path last.
- Do not use `else` after a return. Use the if-return pattern.
- Log errors and show user-friendly messages.
- Consider custom error types or error factories for consistent handling.

## React and Next.js

- Use functional components with TypeScript interfaces.
- Prefer React Server Components. Minimize `'use client'`, `useEffect`, and `setState`.
- Use `'use client'` only in small components that need Web APIs. Never use it for data fetching or state management.
- Rely on the App Router for state changes.
- Put static content and interfaces at the end of the file. Keep static content in variables outside render functions.
- Build responsive layouts with Tailwind CSS, mobile-first.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Wrap client components in `Suspense` with a fallback. Dynamically load non-critical components.
- Optimize images: WebP format, sized data, lazy loading.
- Prioritize Web Vitals: LCP, CLS, INP.

## Forms and server actions

- Validate forms with Zod. Use `useActionState` with react-hook-form.
- Create every server action with the `action` function from next-safe-action, using Zod input schemas.
- Return expected errors as values. Do not use try/catch for them. Show them with `useActionState`.
- Every server action returns `ActionResponse`: `import type { ActionResponse } from '@/types/actions'`.
- Use `error.tsx` and `global-error.tsx` for unexpected errors, with a fallback UI.
- Code in `services/` throws user-friendly errors that TanStack Query can catch and show.
