import React from "react";
import { Spinner, Container, Table,Nav,Navbar,Form,Button } from "react-bootstrap";
import Carousel from "react-multi-carousel";
import { FcStart } from "react-icons/fc";
import { Link, Outlet } from "react-router-dom";
import { Footerone } from "../Footer/Footern";


export const Footer = () => {
  const responsive = {
    superLargeDesktop: {
      breakpoint: { max: 4000, min: 3000 },
      items: 5,
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 3,
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 2,
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1,
    },
  };
  return (
    <>
    <Footerone/>
    <Navbar expand="lg" bg="dark" data-bs-theme="dark" sticky="top">
    <Container fluid>
    <Navbar.Brand as={Link} to="/">Home</Navbar.Brand>
      <Navbar.Toggle aria-controls="navbarScroll" />
      <Navbar.Collapse id="navbarScroll">
        <Nav
          className="me-auto my-2 my-lg-0"
          style={{ maxHeight: '100px' }}
          navbarScroll
        >
          <Nav.Link as={Link} to="/get">All Movies</Nav.Link>
          <Nav.Link as={Link} to="/create">TV Shows</Nav.Link>
        </Nav>
        <Form className="d-flex">
          <Form.Control
            type="search"
            placeholder="Search"
            className="me-2"
            aria-label="Search"
          />
          <Button variant="outline-success">Search</Button>
        </Form>
      </Navbar.Collapse>
    </Container>
  </Navbar>
    <Outlet />
    </>
  );
};
