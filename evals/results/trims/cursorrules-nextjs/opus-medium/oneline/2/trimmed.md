---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
Stack: Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, Tailwind Aria.

## Code style
- TypeScript everywhere. Functional and declarative; no classes.
- Use the `function` keyword for pure functions and components (not `const` arrows). Named exports for components.
- Omit semicolons. Omit curly braces for single-statement conditionals: `if (cond) doSomething()`.
- Prefer interfaces over types. No enums; use maps.
- Descriptive names with auxiliary verbs (`isLoading`, `hasError`). Directories in kebab-case (`components/auth-wizard`).
- Functions take an object and return an object (RORO).
- File order: exported component, subcomponents, helpers, static content, types. Keep static content in variables outside render functions.

## Control flow and errors
- Guard clauses and early returns for errors and invalid states at the top; happy path last; no `else` after `return`.
- Log errors properly and show users friendly messages. Use custom error types or factories for consistency.

## React / Next.js
- Default to Server Components. Use `'use client'` only for small components that need Web APIs, never for data fetching or state management. Minimize `useEffect` and `setState`; rely on the App Router for state changes.
- Wrap client components in `Suspense` with a fallback; dynamically load non-critical components.
- Style with Shadcn UI, Radix, and Tailwind Aria; responsive and mobile-first with Tailwind.
- Images: WebP, explicit sizes, lazy loading. Prioritize Web Vitals (LCP, CLS, INP).
- Forms: validate with Zod, using `useActionState` with react-hook-form.

## Server actions and errors
- Write all server actions with `next-safe-action`'s `action` function and Zod input schemas.
- Every server action returns `ActionResponse` (`import type { ActionResponse } from '@/types/actions'`) for both success and error.
- Return expected errors as values (no try/catch for them) and surface them to the client via `useActionState`.
- Handle unexpected errors with `error.tsx` and `global-error.tsx` error boundaries.
- Code in `services/` throws user-friendly errors that TanStack Query catches and shows to the user.
