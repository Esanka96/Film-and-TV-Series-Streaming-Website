import React from "react";
import { Button, Form, Nav, Navbar, Container } from "react-bootstrap";
import { Link, Outlet } from "react-router-dom";


export const Navbarcom = () => {
  return (
    <>
      <Navbar className="px-5" expand="lg" bg="dark" variant="dark" sticky="top">
        <Container fluid>
          <Navbar.Brand as={Link} to="/">Home</Navbar.Brand>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Nav className="me-auto my-2 my-lg-0" style={{ maxHeight: '100px' }} navbarScroll>
              <Nav.Link as={Link} to="/get">All Movies</Nav.Link>
              <Nav.Link as={Link} to="/create">TV Shows</Nav.Link>
            </Nav>
          </Navbar.Collapse>

          {/* This section is aligned to the right */}
          <Navbar.Collapse className="justify-content-end">
            <Form className="d-flex me-4">
              <Form.Control
                style={{width:'280px'}}
                type="search"
                placeholder="Find movies, TV shows and more"
                aria-label="Search"
              />
                 <Button className="mx-2" variant="danger">Search</Button>
            </Form>
            <Nav>
              <Link className="mx-2 btn btn-light" as={Link} to="/register">Register</Link>
              <Link className="btn btn-primary" as={Link} to="/sign" >Sign In</Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <Outlet />
    </>
  );
};
