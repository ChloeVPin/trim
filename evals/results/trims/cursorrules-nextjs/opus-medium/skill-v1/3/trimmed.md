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
- Use the "function" keyword for pure functions and for components, not const.
- Omit semicolons.
- Omit curly braces for single-line conditionals; write them on one line (e.g., if (condition) doSomething()).
- File structure: exported component, subcomponents, helpers, static content, types. Static content and interfaces go at the end of the file.

Error Handling and Validation

- Handle errors, edge cases and preconditions at the start of functions with guard clauses and early returns; put the happy path last. Use if-return instead of unnecessary else.
- Implement proper error logging and user-friendly error messages.
- Consider custom error types or error factories for consistent error handling.

React/Next.js

- Use declarative JSX.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling. Build responsive layouts with Tailwind CSS, mobile-first.
- Put static content in variables outside render functions.
- Favor React Server Components and Next.js SSR features. Minimize 'use client', 'useEffect' and 'setState'; use 'use client' only for Web API access in small components, never for data fetching or state management.
- Rely on the Next.js App Router for state changes.
- Wrap client components in Suspense with a fallback.
- Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Prioritize Web Vitals (LCP, CLS, FID).
- Forms: validate with Zod, and use useActionState with react-hook-form.
- Expected errors in Server Actions: model them as return values, not try/catch, and use useActionState to return them to the client.
- Unexpected errors: use error boundaries via error.tsx and global-error.tsx with a fallback UI.
- Code in the services/ dir always throws user-friendly errors that TanStack Query can catch and show to the user.
- Use next-safe-action for all server actions:
  - Create actions with the action function from next-safe-action.
  - Define input schemas with Zod.
  - Use import type { ActionResponse } from '@/types/actions'
  - All server actions return the ActionResponse type, for both success and error responses.
