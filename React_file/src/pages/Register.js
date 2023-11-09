import { Button } from 'react-bootstrap';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import { Footerone } from "../Footer/Footern";
import { Navbarcom } from "../Navbar/Navbar";
import { useState } from 'react';
import axios from "axios";

function Registerform() {

  const [firstname, setFirstname]= useState("");
  const [lastname, setLastname]= useState("");
  const [email, setEmail]= useState("");
  const [password, setPassword]= useState("");

  const handlefirstname = (e) =>{
    setFirstname(e.target.value);
  }

  const handlelastname = (e) =>{
    setLastname(e.target.value)
  }

  const handleemail = (e) =>{
    setEmail(e.target.value)
  }

  const handlepassword = (e) =>{
    setPassword(e.target.value)
  }

  const handlesubmit = (e) =>{
    e.preventDefault();

    const formData = new FormData();
    formData.append("First_name",firstname)
    formData.append("Last_name",lastname)
    formData.append("Email",email)
    formData.append("Password",password)

    axios.post("http://127.0.0.1:8000/api/register/",formData,{
      headers:{
        "Content-Type":"multipart/form-data"
      },
    })
    .then((response)=>{
      alert("Data sent successfully");
      setFirstname("")
      setLastname("")
      setEmail("")
      setPassword("")
    })
    .catch((error)=>{
      alert("Fail to send data", error)
    })
  }

  return (
    <>
        <Navbarcom/>
   
    <Form className='bg-light container my-4 p-5 align-items-center' style={{width:'700px'}} onSubmit={handlesubmit}>
      <h1 className='text-center'>Register Here</h1>
      <hr></hr>
      <Form.Group as={Row} className="mb-3" controlId="firstname" >
        <Form.Label column sm="2">
          First name
        </Form.Label>
        <Col sm="10">
          <Form.Control type="text" 
          placeholder="Enter first name" 
          value={firstname}
          onChange={handlefirstname}/>
        </Col>
      </Form.Group>
      <Form.Group as={Row} className="mb-3" controlId="lastname">
        <Form.Label column sm="2">
          Last name
        </Form.Label>
        <Col sm="10">
          <Form.Control type="text" 
          placeholder="Enter last name" 
          value={lastname}
          onChange={handlelastname}/>
        </Col>
      </Form.Group>
      <Form.Group as={Row} className="mb-3" controlId="email">
        <Form.Label column sm="2">
          Email
        </Form.Label>
        <Col sm="10">
          <Form.Control type="email" 
          placeholder="Enter email"
          value={email}
          onChange={handleemail} />
        </Col>
      </Form.Group>
      <Form.Group as={Row} className="mb-3" controlId="password">
        <Form.Label column sm="2">
          Password
        </Form.Label>
        <Col sm="10">
          <Form.Control type="password" 
          placeholder="Enter password" 
          value={password}
          onChange={handlepassword}/>
        </Col>
      </Form.Group>
      <Button type='submit'>Submit</Button>
    </Form>
    <Footerone/>
    </>
  );
}

export default Registerform;