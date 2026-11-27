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

- Use the "function" keyword for pure functions and components, not const. Omit semicolons.
- Use TypeScript for all code. Prefer interfaces over types. Avoid enums; use maps.
- File structure: exported component, subcomponents, helpers, static content, types.
- Omit curly braces in conditionals when the body is a single statement. Use one-line syntax for simple conditionals (e.g., if (condition) doSomething()).

Error Handling and Validation

- Prioritize error handling and edge cases:
  - Handle errors and edge cases at the beginning of functions with guard clauses and early returns, to avoid deeply nested if statements.
  - Place the happy path last in the function.
  - Avoid unnecessary else statements; use the if-return pattern instead.
  - Implement proper error logging and user-friendly error messages.
  - Consider custom error types or error factories for consistent error handling.

React/Next.js

- Use functional components with TypeScript interfaces, and declarative JSX.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Use mobile-first responsive design with Tailwind CSS.
- Place static content and interfaces at the end of the file. Use content variables for static content outside render functions.
- Minimize 'use client', 'useEffect', and 'setState'. Favor RSC.
- Use Zod for form validation.
- Wrap client components in Suspense with a fallback.
- Use dynamic loading for non-critical components.
- Optimize images: WebP format, size data, lazy loading.
- Model expected errors as return values. In Server Actions, avoid try/catch for expected errors; use useActionState to manage them and return them to the client.
- Use error boundaries for unexpected errors: implement error.tsx and global-error.tsx to handle them and provide a fallback UI.
- Use useActionState with react-hook-form for form validation.
- Code in services/ always throws user-friendly errors that tanStackQuery can catch and show to the user.
- Use next-safe-action for all server actions:
  - Use the action function from next-safe-action to create actions, with input schemas defined in Zod.
  - Import the type with `import type { ActionResponse } from '@/types/actions'`.
  - Ensure every server action returns ActionResponse, with consistent error handling and success responses.

Key Conventions

1. Rely on Next.js App Router for state changes.
2. Prioritize Web Vitals (LCP, CLS, FID).
3. Minimize 'use client' usage. Use it only for Web API access in small components, not for data fetching or state management. Prefer server components and Next.js SSR features.
   Refer to the Next.js documentation for data fetching, rendering, and routing best practices: https://nextjs.org/docs
