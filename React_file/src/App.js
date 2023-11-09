import React, { useEffect, useState } from "react";
import axios from "axios";
import { Button, Card, Container, Row, Col } from "react-bootstrap";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/Layout";
import { Footer } from "./pages/Home";
import TVseries from "./pages/AllTV";
import Allfilms from "./pages/AllFilms";
import Singleview from "./pages/Singleview";
import Singletv from "./pages/SingleTV";
import Registerform from "./pages/Register";
import Signform from "./pages/Sign";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />} />
        {/* <Route path="home" element={<Footer />} /> */}
        <Route path="create" element={<TVseries />} />
        <Route path="get" element={<Allfilms />} />
        <Route path="single/:id" element={<Singleview />} />
        <Route path="singletv/:id" element={<Singletv />} />
        <Route path="register" element={<Registerform/>} />
        <Route path="sign" element={<Signform/>}/>
        {/* </Route> */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
