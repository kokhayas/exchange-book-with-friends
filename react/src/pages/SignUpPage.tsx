import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

const SignUpPage: React.FC = (): JSX.Element => {
	const { signUpUser } = useContext(AuthContext);
	return (
		<>
		You are on SignUp Page
		<form onSubmit={signUpUser}>
			<input type="text" name="username" placeholder="Enter Username"></input>
			<input type="password" name="password" placeholder="Enter Password"></input>
			<input type="submit"/>
		</form>
		</>
	)
}

export default SignUpPage