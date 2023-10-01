import React from "react";
import "./App.css";
import { BrowserRouter, createBrowserRouter, Route, RouterProvider } from "react-router-dom";
import LoginPage from  './pages/LoginPage';
import AdminHomePage from  './pages/AdminHomePage';


function App() {
  return (
    <div className="App">
      <LoginPage/>
    </div>
  );
}

export default App;
