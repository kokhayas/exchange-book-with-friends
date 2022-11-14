import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

const LoginPage: React.FC = (): JSX.Element => {
	const { loginUser } = useContext(AuthContext);
	return (
		<>
		You are on Login Page
		<form onSubmit={loginUser}>
			<input type="text" name="username" placeholder="Enter Username"></input>
			<input type="password" name="password" placeholder="Enter Password"></input>
			<input type="submit"/>
		</form>
		</>
	)
}

export default LoginPage
