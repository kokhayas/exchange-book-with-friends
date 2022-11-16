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

	const getNotes = async() => {
		const response = await fetch('http://localhost:8000/api/v1/notes', {
			method: "GET",
			headers: {
				'Content-Type': 'application/json',
				'Authorization': 'Bearer ' + String(authTokens && authTokens.access)
			}
		})
		const notes: Note[] = await response.json()
		if (response.status==200){
			setNotes(notes)
		} else if (response.statusText ==="Unauthorized") {
			logoutUser();
		}
		}
	return (
		<div>
			<p>You are on home page</p>
			<ul>
				{ notes.map(note => {
					return (<li key={note.id}>{note.body}</li>)
				})}
			</ul>
		</div>
	)
}

export default HomePage