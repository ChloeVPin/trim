---
description: "Cursor rules for Next.js development with React and TypeScript integration."
globs: **/*
alwaysApply: false
---
You are an expert in Solidity, TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Shadcn UI, Radix UI, and Tailwind Aria.

Key Principles

- Write concise, technical responses with TypeScript examples.
- Use functional, declarative programming. Avoid classes.
- Use descriptive variable names with auxiliary verbs (e.g., isLoading).
- Use lowercase with dashes for directories (e.g., components/auth-wizard).
- Favor named exports for components.
- Use the Receive an Object, Return an Object (RORO) pattern.

JavaScript/TypeScript

- Use "function" keyword for pure functions. Omit semicolons.
- Use TypeScript for all code. Prefer interfaces over types. Avoid enums; use maps.
- File structure: exported component, subcomponents, helpers, static content, types.
- Omit curly braces for single-line conditionals, e.g. `if (condition) doSomething()`.

Error Handling and Validation

- Handle error and edge cases first, with guard clauses and early returns. Avoid else after return. Put the happy path last.
- Log errors and show user-friendly messages.
- Consider custom error types or error factories for consistent error handling.

React/Next.js

- Use functional components with TypeScript interfaces. Use `function`, not `const`, for components.
- Use declarative JSX.
- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Mobile-first responsive design with Tailwind CSS.
- Put static content in variables outside render functions.
- Optimize images: WebP format, size data, lazy loading.
- Wrap client components in Suspense with a fallback.
- Use dynamic loading for non-critical components.
- Minimize useEffect and setState. Favor RSC.
- Validate forms with Zod and react-hook-form, using useActionState.
- Use next-safe-action for all server actions:
  - Define input schemas with Zod.
  - Create actions with the action function from next-safe-action.
  - Return expected errors as values, not via try/catch. Use useActionState to show them.
  - Return the ActionResponse type from every server action, for success and error: `import type { ActionResponse } from '@/types/actions'`.
- Use error.tsx and global-error.tsx error boundaries with a fallback UI for unexpected errors.
- Code in services/ always throws user-friendly errors that tanStackQuery can catch and show to the user.

Key Conventions

1. Rely on Next.js App Router for state changes.
2. Prioritize Web Vitals (LCP, CLS, FID).
3. Minimize 'use client':
  - Prefer server components and Next.js SSR features.
  - Use 'use client' only for Web API access in small components.
  - Avoid 'use client' for data fetching or state management.
  - Refer to Next.js documentation for Data Fetching, Rendering, and Routing best practices: https://nextjs.org/docs
