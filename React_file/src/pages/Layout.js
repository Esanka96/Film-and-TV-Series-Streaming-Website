import { Outlet, Link } from "react-router-dom";
import { Nav, NavItem,Navbar,NavDropdown,Form,Button,Container } from "react-bootstrap";
import React from "react";
import { Footerone } from "../Footer/Footern";
import { Navbarcom } from "../Navbar/Navbar";

const Layout = () => {
  return (
    <>
    <Navbarcom/>
    <Footerone/>
    </>
  );
};

export default Layout;
