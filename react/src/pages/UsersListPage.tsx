import React, { useEffect, useState } from 'react';
import type { User } from '../types/index';

const UsersListPage: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
  	getUsers()
  }, [])

  const getUsers = async () => {
	const response = await fetch('http://127.0.0.1:8000/api/v1/users');
	const data = await response.json();
	console.log(data)
	setUsers(data);
  }

  return (
	<div>
	  <h1>Users</h1>
	  <ul>
		{users.map(user => (
		  <>
		    <li key={user.id}>{user.username}</li>
		    <li key={user.id}>{user.password} </li>
			<li key={user.id}>{user.id} </li>

		  </>
		))}
	  </ul>
	</div>
  );
};

export default UsersListPage;
