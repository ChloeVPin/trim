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
- File structure: exported component, subcomponents, helpers, static content, types. Keep static content in variables outside render functions.
- Omit curly braces for single-line conditionals and write simple ones on one line (e.g., if (condition) doSomething()).

Error Handling and Validation

- Handle errors, edge cases and invalid preconditions at the start of functions with guard clauses and early returns. Put the happy path last; use if-return instead of else.
- Implement proper error logging and user-friendly error messages.
- Consider using custom error types or error factories for consistent error handling.

React/Next.js

- Use function, not const, for components.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Implement responsive design with Tailwind CSS, mobile-first.
- Favor RSC and Next.js SSR features. Minimize 'use client', 'useEffect', and 'setState'. Use 'use client' only for Web API access in small components, not for data fetching or state management.
- Rely on Next.js App Router for state changes.
- Wrap client components in Suspense with fallback.
- Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Prioritize Web Vitals (LCP, CLS, FID).
- For form validation, use Zod with react-hook-form and useActionState.
- Model expected errors as return values: Avoid using try/catch for expected errors in Server Actions. Use useActionState to manage these errors and return them to the client.
- Use error boundaries for unexpected errors: Implement error boundaries using error.tsx and global-error.tsx files to handle unexpected errors and provide a fallback UI.
- Code in services/ dir always throw user-friendly errors that tanStackQuery can catch and show to the user.
- Use next-safe-action for all server actions:
  - Create actions with the action function from next-safe-action.
  - Define input schemas using Zod.
  - Use import type { ActionResponse } from '@/types/actions'
  - Ensure all server actions return the ActionResponse type, for both success and error responses.

Refer to Next.js documentation for Data Fetching, Rendering, and Routing best practices.
- https://nextjs.org/docs
