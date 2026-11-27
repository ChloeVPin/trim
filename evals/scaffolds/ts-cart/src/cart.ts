export type CartItem = {
  id: string
  name: string
  priceCents: number
  qty: number
}

export type Cart = {
  items: CartItem[]
}

export function total(cart: Cart): number {
  return cart.items.reduce((sum, item) => sum + item.priceCents * item.qty, 0)
}

export function applyDiscount(amountCents: number, percent: number): number {
  // percent is a whole number such as 15
  return amountCents - amountCents * percent
}
