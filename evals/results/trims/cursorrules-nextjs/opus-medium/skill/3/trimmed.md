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

- Use the "function" keyword for pure functions and for components, not const. Omit semicolons.
- Use TypeScript for all code. Prefer interfaces over types. Avoid enums, use maps.
- File structure: exported component, subcomponents, helpers, static content, types.
- Omit curly braces for single-line conditionals (e.g., if (condition) doSomething()).

Error Handling and Validation

- Handle errors, edge cases and preconditions at the start of functions with guard clauses and early returns; put the happy path last. Use if-return, not else.
- Implement proper error logging and user-friendly error messages.
- Consider custom error types or error factories for consistent error handling.

React/Next.js

- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Responsive design with Tailwind CSS, mobile-first.
- Use content variables for static content outside render functions.
- Favor RSC and Next.js SSR features. Minimize 'use client', 'useEffect', and 'setState'. Use 'use client' only for Web API access in small components, never for data fetching or state management.
- Rely on Next.js App Router for state changes.
- Use Zod for form validation, and useActionState with react-hook-form.
- Wrap client components in Suspense with fallback.
- Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Prioritize Web Vitals (LCP, CLS, FID).
- Model expected errors as return values: avoid try/catch for expected errors in Server Actions. Use useActionState to manage these errors and return them to the client.
- Handle unexpected errors with error boundaries in error.tsx and global-error.tsx, with a fallback UI.
- Code in services/ always throws user-friendly errors that TanStack Query can catch and show to the user.
- Use next-safe-action for all server actions:
  - Create actions with its action function.
  - Define input schemas with Zod.
  - import type { ActionResponse } from '@/types/actions'
  - All server actions return ActionResponse, for both errors and success.
