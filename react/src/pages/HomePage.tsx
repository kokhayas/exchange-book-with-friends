import { useContext, useEffect, useState } from "react";
import { AuthContext } from "../context/AuthContext";

const HomePage = () => {
	const {logoutUser} = useContext(AuthContext)
	const {authTokens} = useContext(AuthContext);
	type Note = {
		id: number,
		body: string,
		user: string,
	}

	const [notes, setNotes] = useState<Note[]>([])
	useEffect(()=>{
		getNotes()
	}, [])

		const getNotes = async() =>{
        const response = await fetch('http://localhost:8000/api/v1/notes/', {
            method:'GET',
            headers:{
                'Content-Type':'application/json',
                'Authorization': 'Bearer ' + String(authTokens?.access)
            }
        })
		const notes: Note[] = await response.json()
		console.log('authTokens', authTokens)
		if (response.status===200){
			setNotes(notes)
		}
	}
	return (
		<div>
			<p>You are on home page</p>
			notes list
			<ul>
				{ notes?.map(note => {
					return (<li key={note.id}>{note.body}</li>)
				})}
			</ul>
		</div>
	)
}

export default HomePage

// curl --header "Content-Type: application/json" --header "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4NjU3NDgxLCJqdGkiOiJlNDRiNDlkYTViMDE0MzlmYjE4YmRjZjdkOTUzNWJmNCIsInVzZXJfaWQiOjIsInVzZXJuYW1lIjoidXNlcm5hbWUifQ.__NaOwqNdggBKqG4yuzr5aplwFxMGjAXH5AD7a1UTYg"  -X GET http://localhost:8000/api/v1/notes/

// curl --request GET
//    --header "Authorization: Bearer "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4NjU3MDY4LCJqdGkiOiIyZmIzZWMxZmViMWU0ZTBmODk0ZjNkMTkxNWY3YTEyNiIsInVzZXJfaWQiOjIsInVzZXJuYW1lIjoidXNlcm5hbWUifQ.WQy6AH4atlbWTIb73bwClc39zfEEsQcQHR5sfsgUogM"
// "http://localhost:8000/api/v1/notes/"


// curl \
//   -X POST \
//   -H "Content-Type: application/json" \
//   -d '{"username": "username", "password": "password"}' \
//   http://localhost:8000/api/v1/api/token/


// curl \
//   -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4NjYxNDYwLCJqdGkiOiI4MTQxNGIwMmE0YmE0NTBhYWQyZmE4NDQ2NjA0YWZkOCIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoidXNlcm5hbWUifQ.9A9ex-0_-hptWXRi8vBao3mWAGliDFbyV41BBRtQtiQ" \
//   http://localhost:8000/api/v1/notes/