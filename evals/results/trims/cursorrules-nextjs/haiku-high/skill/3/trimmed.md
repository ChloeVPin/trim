---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
You are an expert in Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, and Tailwind Aria.

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
- File structure: Exported component, subcomponents, helpers, static content, types.
- Avoid unnecessary curly braces. For single-line conditionals, write one line: if (condition) doSomething()

Error Handling and Validation

Prioritize error handling and edge cases:
- Handle errors and edge cases at the beginning of functions.
- Use guard clauses and early returns for error conditions, not deeply nested ifs. Place the happy path last. Use the if-return pattern, not else.
- Implement error logging and user-friendly error messages.
- Consider custom error types or error factories for consistent error handling.

React/Next.js

- Use function, not const, for components. Keep JSX declarative.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Implement responsive, mobile-first design with Tailwind CSS.
- Use content variables for static content outside render functions.
- Use dynamic loading for non-critical components.
- Wrap client components in Suspense with fallback.
- Optimize images: WebP format, size data, lazy loading.
- Use Zod for form validation.
- Use useActionState with react-hook-form for form validation.
- Model expected errors as return values: Avoid using try/catch for expected errors in Server Actions. Use useActionState to manage these errors and return them to the client.
- Use error boundaries for unexpected errors: implement error.tsx and global-error.tsx with a fallback UI.
- Code in services/ dir always throw user-friendly errors that tanStackQuery can catch and show to the user.
- Use next-safe-action for all server actions:
  - Create actions with the next-safe-action action function.
  - Define action input schemas with Zod.
  - Use import type { ActionResponse } from '@/types/actions'
  - Ensure all server actions return the ActionResponse type

Key Conventions

1. Rely on Next.js App Router for state changes.
2. Prioritize Web Vitals (LCP, CLS, FID).
3. Minimize 'use client', 'useEffect', and 'setState'. Prefer server components and Next.js SSR. Use 'use client' only in small components that need Web APIs, never for data fetching or state management.
   Refer to https://nextjs.org/docs for Next.js best practices.
