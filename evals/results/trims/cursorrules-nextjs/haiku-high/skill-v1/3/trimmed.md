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

- Use the "function" keyword for pure functions. Omit semicolons.
- Use TypeScript for all code. Prefer interfaces over types. Avoid enums; use maps.
- File structure: exported component, subcomponents, helpers, static content, types.
- Avoid unnecessary curly braces in conditionals. Use one-line syntax for simple ones, e.g., `if (condition) doSomething()`.

Error Handling and Validation

- Handle errors and edge cases first, using guard clauses and early returns to avoid deeply nested if statements. Place the happy path last in the function.
- Avoid else; use the if-return pattern instead.
- Implement proper error logging and user-friendly error messages.
- Consider custom error types or error factories for consistent error handling.

React/Next.js

- Use functional components and TypeScript interfaces. Use `function`, not `const`, for components. Use declarative JSX.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Implement mobile-first responsive design with Tailwind CSS.
- Use content variables for static content outside render functions.
- Use Zod for form validation, with useActionState and react-hook-form.
- Wrap client components in Suspense with a fallback. Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Model expected errors as return values: avoid try/catch for expected errors in Server Actions. Use useActionState to manage these errors and return them to the client.
- Use error boundaries for unexpected errors: implement error.tsx and global-error.tsx to handle them and provide a fallback UI.
- Code in services/ always throws user-friendly errors that TanStack Query can catch and show to the user.
- Use next-safe-action for all server actions:
  - Use the action function from next-safe-action to create actions.
  - Define input schemas using Zod for type checking and validation.
  - Ensure all server actions return the ActionResponse type, with consistent error and success responses. Use `import type { ActionResponse } from '@/types/actions'`.

Key Conventions

1. Rely on Next.js App Router for state changes.
2. Prioritize Web Vitals (LCP, CLS, FID).
3. Minimize 'use client' usage:
  - Prefer server components and Next.js SSR features.
  - Use 'use client' only for Web API access in small components.
  - Avoid using 'use client' for data fetching or state management.
  - Minimize 'useEffect' and 'setState'. Favor RSC.

  Refer to the Next.js documentation for data fetching, rendering, and routing best practices: https://nextjs.org/docs
