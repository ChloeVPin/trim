import { readFileSync } from 'node:fs'

export function totalUnits(items) {
  return items.reduce((sum, item) => sum + item.qty, 0)
}

export function findBySku(items, sku) {
  return items.find((item) => item.sku === sku)
}

function legacyRestock(items, amount) {
  return items.map((item) => ({ ...item, qty: item.qty + amount }))
}

export function stockValue(items) {
  return items.reduce((sum, item) => sum + item.qty * item.unitCost, 0)
}
