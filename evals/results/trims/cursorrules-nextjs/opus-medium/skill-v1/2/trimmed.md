---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
Stack: Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, Tailwind Aria.

Key Principles

- Write concise, technical responses with TypeScript examples.
- Use functional, declarative programming. Avoid classes.
- Prefer iteration and modularization over duplication.
- Use descriptive variable names with auxiliary verbs (e.g., isLoading).
- Use lowercase with dashes for directories (e.g., components/auth-wizard).
- Favor named exports for components.
- Use the Receive an Object, Return an Object (RORO) pattern.

JavaScript/TypeScript

- Use TypeScript for all code. Prefer interfaces over types. Avoid enums; use maps.
- Use the "function" keyword for pure functions and for components (not const).
- Omit semicolons.
- Omit curly braces for single-statement conditionals; write them on one line (e.g., if (condition) doSomething()).
- File order: exported component, subcomponents, helpers, static content, types/interfaces.

Error Handling and Validation

- Handle errors, edge cases and invalid preconditions first, with guard clauses and early returns; put the happy path last.
- Avoid nesting and unnecessary else statements; use if-return.
- Log errors properly and show user-friendly error messages.
- Consider custom error types or error factories for consistency.

React/Next.js

- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Responsive design with Tailwind CSS, mobile-first.
- Keep static content in variables outside render functions.
- Favor React Server Components and Next.js SSR features. Minimize 'use client', useEffect and setState; use 'use client' only for Web API access in small components, never for data fetching or state management.
- Rely on the Next.js App Router for state changes.
- Wrap client components in Suspense with a fallback.
- Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Prioritize Web Vitals (LCP, CLS, FID).
- Use Zod for form validation, and useActionState with react-hook-form.
- Model expected errors as return values: don't use try/catch for expected errors in Server Actions; manage them with useActionState and return them to the client.
- Handle unexpected errors with error boundaries in error.tsx and global-error.tsx, with a fallback UI.
- Code in the services/ dir always throws user-friendly errors that TanStack Query can catch and show to the user.
- Use next-safe-action for all server actions:
  - Create actions with its action function.
  - Define input schemas with Zod.
  - Import the response type with `import type { ActionResponse } from '@/types/actions'`.
  - Every server action returns ActionResponse, for both errors and success.

For data fetching, rendering and routing, follow the Next.js docs: https://nextjs.org/docs
