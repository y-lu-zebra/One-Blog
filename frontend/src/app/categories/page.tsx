interface User {
  url: string
  username: string
  email: string
  is_staff: string
}

const fetchUsers: () => Promise<User[]> = async () => {
  const res: Response = await fetch(`${process.env.API_URL}/users/`)
  return (await res.json()) as Promise<User[]>
}

export default async function Page() {
  const users: User[] = await fetchUsers()
  console.log('users: ', users)
  return (
    <main>
      {process.env.APP_NAME} - {users[0].username}
    </main>
  )
}