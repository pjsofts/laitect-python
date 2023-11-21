const url = "http://127.0.0.1:5000/users";

type User = {
  name: string;
  lastname: string;
};

async function Users() {
  const response = await fetch(url, {cache: 'no-store'});
  const users = await response.json();
  console.log(users);
  return users.map((user: User) => {
    return (
      <div
        className="bg-[#fff] cursor-pointer rounded-xl
         text-lg border-solid p-4 m-8 border-gray border-[1px]"
        key={user.name}
      >
        {user.name} {user.lastname}
      </div>
    );
  });
}

export default Users;
