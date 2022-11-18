import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

const Header: React.FC = () => {
	const {user, logoutUser} = useContext(AuthContext)
	// const {name} = useContext(AuthContext);
	  return (
	<div className="text-sky-500">
		<h1>My App</h1>
		<Link to ="/">Home</Link>
		<span>  |  </span>
		{user ? (
			<p onClick={logoutUser}>Logout</p>
		): (
			<>
			<Link to ="/login">Login</Link>
			<span> | </span>
			<Link to ="/signup">Sign up</Link>
			</>
		)}
		{user && <p>hello {user.username}</p>}
	</div>
  );
};

export default Header


