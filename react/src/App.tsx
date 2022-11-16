import { Route, Routes } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import { AuthProvider } from './context/AuthContext';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import PrivateRoutes from './utils/PrivateRoutes';

// これから実現するMVPの機能
// 1. サインアップ
// 2. サインイン
// 3. 自分の本の登録
// 4. 自分の本の一覧
// 5. 他人の本の一覧

const App: React.FC = (): JSX.Element => {
  return(
  		<>
			<AuthProvider>
				<Header/>

				<Routes>
					<Route element={< PrivateRoutes />}>
						<Route element={<HomePage/>} path="/"/>
					</Route>
					<Route element={<LoginPage/>} path="/login"/>

				</Routes>
			</AuthProvider>
		</>
		)
}

export default App;
