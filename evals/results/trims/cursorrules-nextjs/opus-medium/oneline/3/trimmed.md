---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
Stack: Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, Tailwind Aria.

Responses: concise and technical, with TypeScript examples.

## Code style
- TypeScript everywhere. Functional and declarative; no classes. Modularize rather than duplicate.
- Use the `function` keyword for components and pure functions. Omit semicolons.
- Prefer interfaces over types; use maps instead of enums.
- Name booleans with auxiliary verbs (`isLoading`, `hasError`). Directories are lowercase-with-dashes (`components/auth-wizard`). Named exports for components.
- Functions take an object and return an object (RORO).
- File order: exported component, subcomponents, helpers, static content, types/interfaces. Keep static content in variables outside render functions.
- Omit braces for single-line conditionals: `if (condition) doSomething()`.

## Error handling
- Handle errors, edge cases, and invalid preconditions first with guard clauses and early returns; put the happy path last; no `else` after a return.
- Log errors properly and show users friendly messages. Use custom error types or factories for consistency.
- Server Actions: return expected errors as values (no try/catch for them) and surface them with `useActionState`.
- Unexpected errors: use `error.tsx` and `global-error.tsx` boundaries with a fallback UI.
- Code in `services/` throws user-friendly errors that TanStack Query can catch and display.

## React / Next.js
- Favor React Server Components and Next.js SSR. Use `'use client'` only for small components that need Web APIs, not for data fetching or state management. Minimize `useEffect` and `setState`; rely on the App Router for state changes.
- Wrap client components in `Suspense` with a fallback; dynamically load non-critical components.
- UI: Shadcn UI, Radix, Tailwind Aria. Tailwind CSS, mobile-first responsive design.
- Images: WebP, explicit sizes, lazy loading.
- Prioritize Web Vitals (LCP, CLS, INP).
- Forms: Zod validation, `useActionState` with react-hook-form.
- Server actions: use next-safe-action for all of them, with Zod input schemas. Every action returns `ActionResponse` (`import type { ActionResponse } from '@/types/actions'`) for consistent success and error responses.
