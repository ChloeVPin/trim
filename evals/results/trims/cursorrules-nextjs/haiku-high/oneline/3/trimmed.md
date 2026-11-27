# Project rules

Stack: TypeScript, Node.js, Next.js 14 App Router, React, Vite, Viem v2, Wagmi v2, Solidity, Shadcn UI, Radix UI, Tailwind.

## General

- Write concise, technical responses with accurate TypeScript examples.
- Use functional, declarative code. Do not use classes.
- Prefer iteration and modules over duplicated code.
- Use descriptive names. Prefix booleans with auxiliary verbs (e.g., `isLoading`, `hasError`).
- Name directories in lowercase with dashes (e.g., `components/auth-wizard`).
- Use named exports for components.
- Use RORO: functions take one object parameter and return one object.

## TypeScript

- Use TypeScript for all code.
- Prefer interfaces over type aliases.
- Do not use enums. Use maps instead.
- Use the `function` keyword for pure functions.
- Omit semicolons.
- Omit curly braces for single-line conditionals (e.g., `if (condition) doSomething()`).
- Order files as: exported component, subcomponents, helpers, static content, types.

## Errors and validation

- Handle errors and edge cases first, at the top of the function.
- Use early returns and guard clauses. Do not use `else` or deep nesting.
- Put the happy path last.
- Log errors. Show users friendly error messages.
- Consider custom error types or error factories for consistent handling.

## React and Next.js

- Declare components with `function`, not `const`. Use TypeScript interfaces for props.
- Use declarative JSX.
- Default to server components. Use `'use client'` only in small components that need Web APIs.
- Never use `'use client'` for data fetching or state management.
- Minimize `useEffect` and `useState`. Rely on the App Router for state changes.
- Wrap client components in `Suspense` with a fallback.
- Use dynamic imports for non-critical components.
- Optimize images: WebP format, sized data, lazy loading.
- Put static content in variables outside render functions. Put static content and interfaces at the end of the file.
- Prioritize Web Vitals: LCP, CLS, INP.
- Refer to https://nextjs.org/docs for data fetching, rendering, and routing.

## UI and styling

- Use Shadcn UI, Radix, and Tailwind Aria for components and styling.
- Build responsive layouts with Tailwind, mobile-first.

## Forms

- Validate forms with Zod.
- Use `useActionState` with react-hook-form for form validation.

## Server actions and services

- Use next-safe-action for every server action. Define each action's input with a Zod schema.
- Do not use try/catch for expected errors in server actions. Return them as values, and surface them to the client with `useActionState`.
- Every server action returns the `ActionResponse` type: `import type { ActionResponse } from '@/types/actions'`.
- Handle unexpected errors with `error.tsx` and `global-error.tsx` boundaries.
- Code in `services/` throws user-friendly errors so TanStack Query can catch and show them.
