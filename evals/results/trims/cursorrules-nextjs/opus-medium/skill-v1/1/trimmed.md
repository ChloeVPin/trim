---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
Stack: Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, and Tailwind Aria.

Key Principles

- Write concise, technical responses with TypeScript examples.
- Use functional, declarative programming. Avoid classes.
- Prefer iteration and modularization over duplication.
- Use descriptive variable names with auxiliary verbs (e.g., isLoading).
- Use lowercase with dashes for directories (e.g., components/auth-wizard).
- Favor named exports for components.
- Use the Receive an Object, Return an Object (RORO) pattern.

JavaScript/TypeScript

- Use "function" keyword for pure functions. Omit semicolons.
- Use TypeScript for all code. Prefer interfaces over types. Avoid enums, use maps.
- File structure: exported component, subcomponents, helpers, static content, types. Static content and interfaces go at the end of the file.
- Write simple conditionals on one line without curly braces (e.g., if (condition) doSomething()).

Error Handling and Validation

- Handle errors, edge cases and invalid preconditions at the start of functions with guard clauses and early returns; put the happy path last. Use if-return instead of unnecessary else.
- Log errors properly and show users friendly error messages.
- Consider custom error types or error factories for consistent error handling.

React/Next.js

- Use declarative JSX and TypeScript interfaces.
- Use function, not const, for components.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Use Tailwind CSS for responsive design, mobile-first.
- Use content variables for static content outside render functions.
- Use Zod for form validation.
- Wrap client components in Suspense with fallback.
- Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Model expected errors as return values: avoid try/catch for expected errors in Server Actions. Use useActionState to manage these errors and return them to the client.
- Handle unexpected errors with error boundaries in error.tsx and global-error.tsx files that provide a fallback UI.
- Use useActionState with react-hook-form for form validation.
- Code in the services/ dir always throws user-friendly errors that TanStack Query can catch and show to the user.
- Use next-safe-action for all server actions:
  - Create actions with its action function, with input schemas defined in Zod.
  - Every server action returns the ActionResponse type (import type { ActionResponse } from '@/types/actions'), for both success and error responses.

Key Conventions

1. Rely on Next.js App Router for state changes.
2. Prioritize Web Vitals (LCP, CLS, FID).
3. Minimize 'use client', 'useEffect' and 'setState'; favor React Server Components and Next.js SSR features. Use 'use client' only for Web API access in small components, not for data fetching or state management.
