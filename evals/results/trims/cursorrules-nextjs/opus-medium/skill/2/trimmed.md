---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
Stack: Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, Tailwind Aria.

Key Principles

- Write concise, technical responses with accurate TypeScript examples.
- Use functional, declarative programming. Avoid classes.
- Use descriptive variable names with auxiliary verbs (e.g., isLoading).
- Use lowercase with dashes for directories (e.g., components/auth-wizard).
- Favor named exports for components.
- Use the Receive an Object, Return an Object (RORO) pattern.

JavaScript/TypeScript

- Use "function" keyword for pure functions. Omit semicolons.
- Use TypeScript for all code. Prefer interfaces over types. Avoid enums, use maps.
- File structure: Exported component, subcomponents, helpers, static content, types.
- Omit curly braces for single-line conditionals: if (condition) doSomething()

Error Handling and Validation

- Handle errors and preconditions first with guard clauses and early returns; put the happy path last. Use if-return instead of else.
- Implement proper error logging and user-friendly error messages.
- Consider custom error types or error factories for consistent error handling.

React/Next.js

- Use function, not const, for components.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Responsive design with Tailwind CSS, mobile-first.
- Use content variables for static content outside render functions.
- Favor RSC and Next.js SSR. Minimize 'use client', 'useEffect', and 'setState'; use 'use client' only for Web API access in small components, never for data fetching or state management.
- Validate forms with Zod, using useActionState with react-hook-form.
- Wrap client components in Suspense with fallback.
- Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Server Actions: return expected errors as values (no try/catch) and manage them with useActionState on the client.
- Handle unexpected errors with error boundaries in error.tsx and global-error.tsx, with a fallback UI.
- Code in services/ dir always throw user-friendly errors that tanStackQuery can catch and show to the user.
- Use next-safe-action for all server actions:
  - Create actions with its action function, with Zod input schemas.
  - Use import type { ActionResponse } from '@/types/actions'
  - All server actions return ActionResponse, for both success and error responses.

Key Conventions

1. Rely on Next.js App Router for state changes.
2. Prioritize Web Vitals (LCP, CLS, FID).
