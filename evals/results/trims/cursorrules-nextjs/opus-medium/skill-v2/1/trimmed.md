---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
Stack: Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, and Tailwind Aria.

Key Principles

- Write concise, technical responses with TypeScript examples.
- Use functional, declarative programming. Avoid classes.
- Use descriptive variable names with auxiliary verbs (e.g., isLoading).
- Use lowercase with dashes for directories (e.g., components/auth-wizard).
- Favor named exports for components.
- Use the Receive an Object, Return an Object (RORO) pattern.

JavaScript/TypeScript

- Use TypeScript for all code. Prefer interfaces over types. Avoid enums, use maps.
- Use the "function" keyword for pure functions and for components, not const.
- Omit semicolons.
- Omit curly braces for single-line conditionals; write simple ones on one line (e.g., if (condition) doSomething()).
- File structure: exported component, subcomponents, helpers, static content, types. Static content and interfaces go at the end of the file.

Error Handling and Validation

- Handle errors, edge cases and invalid preconditions at the start of functions with guard clauses and early returns; put the happy path last. Use if-return instead of else.
- Implement proper error logging and user-friendly error messages.
- Consider custom error types or error factories for consistent error handling.

React/Next.js

- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Responsive design with Tailwind CSS, mobile-first.
- Use content variables for static content outside render functions.
- Minimize 'use client', 'useEffect', and 'setState'. Favor React Server Components and Next.js SSR features. Use 'use client' only for Web API access in small components, not for data fetching or state management.
- Rely on Next.js App Router for state changes.
- Wrap client components in Suspense with fallback.
- Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Prioritize Web Vitals (LCP, CLS, FID).
- Use Zod for form validation, and useActionState with react-hook-form.
- Model expected errors as return values: don't use try/catch for expected errors in Server Actions; manage them with useActionState and return them to the client.
- Handle unexpected errors with error boundaries in error.tsx and global-error.tsx, providing a fallback UI.
- Code in services/ always throws user-friendly errors that TanStack Query can catch and show to the user.
- Use next-safe-action for all server actions:
  - Create actions with its action function, with input schemas defined in Zod.
  - Use import type { ActionResponse } from '@/types/actions'
  - All server actions return the ActionResponse type, for both errors and success responses.

Refer to the Next.js documentation for Data Fetching, Rendering, and Routing best practices: https://nextjs.org/docs
