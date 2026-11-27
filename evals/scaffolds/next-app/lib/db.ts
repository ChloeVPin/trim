interface UserUpdate {
  where: { id: string }
  data: { displayName: string }
}

export const db = {
  user: {
    update: async (args: UserUpdate) => ({ id: args.where.id, ...args.data }),
  },
}
