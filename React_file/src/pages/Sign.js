import { Button } from 'react-bootstrap';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import { Footerone } from "../Footer/Footern";
import { Navbarcom } from "../Navbar/Navbar";

function Signform() {
  return (
    <>
    <Navbarcom/>
   
    <Form className='bg-light container my-4 p-4 align-items-center' size="sm" style={{width:'550px'}}>
      <h1 className='text-center'>Sign in</h1>
      <hr></hr>
      <Form.Group as={Row} className="mb-3" controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Email
        </Form.Label>
        <Col sm="10">
          <Form.Control type="text" placeholder="Enter email" />
        </Col>
      </Form.Group>
      <Form.Group as={Row} className="mb-3" controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Password
        </Form.Label>
        <Col sm="10">
          <Form.Control type="password" placeholder="Enter password" />
        </Col>
      </Form.Group>
      <Row className="justify-content-end">
        <Button className='me-2' type='submit' style={{width:'120px'}}>Sign in</Button>
      </Row>
    </Form>
    <Footerone/>
    </>
  );
}

export default Signform;