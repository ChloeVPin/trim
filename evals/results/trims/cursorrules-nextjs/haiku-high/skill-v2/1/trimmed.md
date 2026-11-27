---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
You are an expert in Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, and Tailwind Aria.

Key Principles

- Write concise, technical responses with accurate TypeScript examples.
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
- Avoid unnecessary curly braces. For single-line conditionals, use one-line syntax, e.g. `if (condition) doSomething()`.

Error Handling and Validation

- Prioritize error handling and edge cases:
  - Handle errors and edge cases at the beginning of functions with guard clauses and early returns, not nested if statements.
  - Place the happy path last in the function for improved readability.
  - Avoid unnecessary else statements; use if-return pattern instead.
  - Implement proper error logging and user-friendly error messages.
  - Consider using custom error types or error factories for consistent error handling.

React/Next.js

- Use functional components and TypeScript interfaces. Declare components with `function`, not `const`.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Use mobile-first responsive design with Tailwind CSS.
- Use content variables for static content outside render functions.
- Minimize 'use client', 'useEffect', and 'setState'. Favor RSC.
- Use Zod for form validation.
- Wrap client components in Suspense with fallback.
- Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Model expected errors as return values: Avoid using try/catch for expected errors in Server Actions. Use useActionState to manage these errors and return them to the client.
- Use error boundaries for unexpected errors: error.tsx and global-error.tsx files that provide a fallback UI.
- Use useActionState with react-hook-form for form validation.
- Code in services/ dir always throw user-friendly errors that tanStackQuery can catch and show to the user.
- Use next-safe-action for all server actions:
  - Define input schemas using Zod for robust type checking and validation.
  - Ensure all server actions return the ActionResponse type, with consistent error handling and success responses.
  - Use import type { ActionResponse } from '@/types/actions'

Key Conventions

1. Rely on Next.js App Router for state changes.
2. Prioritize Web Vitals (LCP, CLS, FID).
3. Minimize 'use client' usage:
  - Use 'use client' only for Web API access in small components.
  - Avoid using 'use client' for data fetching or state management.
  Refer to Next.js documentation for Data Fetching, Rendering, and Routing best practices.
  - https://nextjs.org/docs
