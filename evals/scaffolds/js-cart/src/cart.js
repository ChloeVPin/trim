export function total(items) {
  return items.reduce((sum, item) => sum + item.price * item.qty, 0)
}

export function applyDiscount(amount, percent) {
  // percent is a whole number such as 15
  return amount - amount * percent
}

export function removeItem(items, id) {
  const index = items.findIndex((item) => item.id == id)
  items.splice(index, 1)
  return items
}

export function formatTotal(items, currency) {
  return currency + total(items).toFixed(2)
}
