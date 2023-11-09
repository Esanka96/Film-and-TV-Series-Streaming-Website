import {Button,Row,Col,Table,Form,Card,Container,Nav,Navbar} from "react-bootstrap"
import React,{useEffect,useState} from "react"
import { Link,Outlet } from "react-router-dom"
import LinesEllipsis from "react-lines-ellipsis"
import axios from "axios";
import { Footerone } from "../Footer/Footern";
import { Navbarcom } from "../Navbar/Navbar";


function TVseries(){

  const [fetchdata,setFetchData]=useState([]);

  useEffect(()=>{
    axios.get("http://127.0.0.1:8000/api/tvseries/")
      .then((response)=>{
        setFetchData(response.data);
      })
      .catch((error)=>{
        console.error("Error fetching data : ",error)
      });
  },[]);

  return(
    <>
   <Navbarcom/>
    <div className="container my-3">
      <Container>
        <Row bg="dark" data-bs-theme="dark">
          {fetchdata.map((post)=>(
            <Col key={post.id} xxl={2} xl={3} lg={3} md={4} sm={6} xs={6}>
              <Card className="my-2">
                <Card.Img
                  variant="top"
                  src={post.photo}
                />
                <Card.Body>
                  <Card.Title className="card-title" style={{fontSize:'14px',width:"100%"}}>
                    <LinesEllipsis
                      text={post.name}
                      maxLine="1"
                      ellipsis="..."
                      trimRight
                    />
                  </Card.Title>
                  <Card.Text style={{fontSize:"12px"}}>
                    {post.date}
                  </Card.Text>
                  <Link as={Link} to={`/singletv/${post.id}`} className="btn btn-primary" style={{width:"100%"}}>More</Link>
                </Card.Body>
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    </div>
    <Footerone/>
    </>
  )
}

export default TVseries;