import { useEffect, useState } from 'react';
import ListUser from '../components/ListUser';
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
	  {users.map((user, index) => {
		return (
			<ListUser key={index} user={user} />
			)
	  })}
	</div>
  );
};

export default UsersListPage;
