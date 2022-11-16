import { Link } from "react-router-dom"
import { User } from "../types/index"

const getUsername = (user: User) => {
	return user.username
}

const getTime = (user: User) => {
	return new Date(user.date_joined).toLocaleDateString()
}

const ListUser = ({ user }: {user: User}) => {
	return (
		<Link to={`/users/${user.id}`}>
			<div>
				<h3>{getUsername(user)}</h3>
				<p>{getTime(user)}</p>
			</div>
		</Link>
	)
}

export default ListUser