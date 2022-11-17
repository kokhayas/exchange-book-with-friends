import jwt_decode from 'jwt-decode';
import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export interface User {
	'exp': number,
	'jti': string,
	'user_id': number,
	'username': string
}
export type AuthTokens =
	{
		access: string,
		refresh: string,
	} | null

export interface AuthContextInterface {
	loginUser: (event: React.FormEvent<HTMLFormElement>) => void;
	logoutUser: () => void;
//   checkingSession: boolean;
     authTokens: AuthTokens
//   idToken: string | null;
//   expiresAt: number | null;
//   isAuthenticated: boolean;
//   handleAuthentication: () => void;
//   login: () => void;
//   logout: () => void;
	user: User | null;
}

export const authContextDefaults: AuthContextInterface = {
	// eslint-disable-next-line @typescript-eslint/no-empty-function
	loginUser: () => {},
	// eslint-disable-next-line @typescript-eslint/no-empty-function
	logoutUser: () => {},
//   checkingSession: false,
//   expiresAt: null,
     authTokens: null,
//   idToken: null,
//   isAuthenticated: false,
//   handleAuthentication: () => null,
//   login: () => null,
//   logout: () => null,
  user: null,
};

export const AuthContext = React.createContext<AuthContextInterface>(
  authContextDefaults
);


// eslint-disable-next-line react/prop-types
export const AuthProvider = ({children}:{children: React.ReactNode}) => {
	const [loading, setLoading] = React.useState<boolean>(true);
	const navigate = useNavigate();
	// localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens') || '{}'): null;
	// const [user, setUser] = React.useState<User | null>(null);
	//   const [isAuthenticated, setIsAuthenticated] = React.useState<boolean>(false);
	  const [authTokens, setAuthTokens] = React.useState<AuthTokens>(() => localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens') || '{}'): JSON.parse('{}'));
	  const [user, setUser] = React.useState<User | null>(() => localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens') || '{}'): null)
	  const loginUser = async (event: React.FormEvent<HTMLFormElement>) => {
		event.preventDefault();
		const target = event.target as typeof event.target & {
			username: { value: string };
			password: { value: string };
		}
		const response = await fetch('http://localhost:8000/api/v1/api/token/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({'username': target.username.value, 'password': target.password.value})
		})
		const data: AuthTokens = await response.json();

		if (response.status === 200 && data) {
			setAuthTokens(data);
			// console.log('AuthTokens is set', data);
			setUser(jwt_decode(data.access))
			localStorage.setItem('authTokens', JSON.stringify(data))
			navigate('/');
		} else {
			alert("Something went wrong!")
		}
		console.log('response', response)
		console.log('data', data)
	}
	const logoutUser = () => {
			setAuthTokens(null);
			setUser(null);
			localStorage.removeItem('authTokens');
			navigate('/login')
	}

	const updateToken = async () => {
		console.log('Update token')
		if (authTokens ) {
		const response = await fetch('http://localhost:8000/api/v1/api/token/refresh/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({'refresh': authTokens?.refresh}),
		})
		const data = await response.json();
		if (response.status === 200) {
			setAuthTokens(data);
			setUser(jwt_decode(data.access))
			localStorage.setItem('authTokens', JSON.stringify(data))
			navigate('/');
		} else {
			logoutUser();
		}
		if (loading) {setLoading(false);}
	}
	}

	  const contextData: AuthContextInterface = {
		loginUser: loginUser,
		logoutUser: logoutUser,
		user: user,
		authTokens: authTokens,
	  }
	  useEffect(() => {
		if (loading) {
			updateToken();
		}
		const fourMinutes = 1000*60*4;
		const twoSeconds = 2000
		const interval = setInterval(()=>{
			if (authTokens) {
				updateToken()
			}
		}, fourMinutes)
		return () => clearInterval(interval)
	  }, [authTokens, loading])

	return(
		//  write a type
		<AuthContext.Provider value={contextData}>
			{children}
		</AuthContext.Provider>
	)
}

