---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
Stack: Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, Tailwind CSS.

## Code style
- TypeScript everywhere. Functional and declarative; no classes. Extract shared logic rather than duplicating it.
- Use the `function` keyword for components and pure functions. No semicolons.
- Prefer interfaces over types. Use maps instead of enums.
- Name booleans with auxiliary verbs (`isLoading`, `hasError`). Directories are kebab-case (`components/auth-wizard`). Use named exports for components.
- Functions take one object and return one object (RORO).
- File order: exported component, subcomponents, helpers, static content, types/interfaces.
- Write simple conditionals on one line without braces: `if (condition) doSomething()`.

## Error handling
- Handle errors and invalid states first with guard clauses and early returns. Put the happy path last, and use if-return instead of `else`.
- Log errors properly and show users clear, friendly messages. Use custom error types or error factories so errors stay consistent.
- Server actions: return expected errors as values instead of using try/catch, and surface them with `useActionState`. Handle unexpected errors with `error.tsx` and `global-error.tsx` boundaries.
- Code in `services/` throws user-friendly errors that TanStack Query catches and shows to the user.

## React / Next.js
- Favor React Server Components. Use `'use client'` only for small components that need Web APIs, never for data fetching or state management. Keep `useEffect` and `setState` to a minimum. Let the App Router drive state changes.
- Wrap client components in `Suspense` with a fallback. Load non-critical components dynamically.
- Build UI with Shadcn UI, Radix, and Tailwind, mobile-first and responsive.
- Define static content in variables outside render functions.
- Images: WebP, explicit dimensions, lazy loading.
- Prioritize Web Vitals (LCP, CLS, INP).
- Forms: validate with Zod, using react-hook-form together with `useActionState`.

## Server actions
- Create every server action with next-safe-action, using a Zod input schema.
- Every action returns `ActionResponse` (`import type { ActionResponse } from '@/types/actions'`) for both success and error results.
