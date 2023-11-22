'use client'

import { useEffect, useState } from "react";

const url = "http://127.0.0.1:8000/users";

type User = {
  name: string;
  lastname: string;
};

function Users() {
   
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");
  const [lastname, setLastName] = useState("");
  useEffect(()=>{
    async function getUsers(){
      const response =  await fetch(url);
      const users = await response.json();
      setUsers(users)
    }
    getUsers()
  }, [])

  console.log(users);
  return <div>
    <div>
      <input className="m-4 p-4" placeholder="name:" value={name} onChange={(e)=>{setName(e.target.value)}} type="text" />
      <input className="m-4 p-4" placeholder="lastname:"  value={lastname} onChange={(e)=>{setLastName(e.target.value)}} type="text" />

      <button onClick={()=>{
        fetch(url, {method: "POST", headers:{"Content-Type": "application/json"}, body: JSON.stringify({name: name, lastname: lastname})})

      }} >Add</button>
      </div>
  {users.map((user: User) => {
    return (
      <div
        className="bg-[#fff] cursor-pointer rounded-xl
         text-lg border-solid p-4 m-8 border-gray border-[1px]"
        key={user.name + user.lastname}
      >
        {user.name} {user.lastname}
      </div>
    );
  })}
  </div>
}

export default Users;
