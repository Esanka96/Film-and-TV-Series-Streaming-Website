import React, { useEffect, useState } from "react";
import { Link, useParams,Outlet } from "react-router-dom";
import axios from "axios";
import Spinner from "react-bootstrap/Spinner";
import { Container, Row, Col, Button, Table,Form,Nav,Navbar } from "react-bootstrap";
import Carousel from "react-multi-carousel";
import { FcStart, FcDownload } from "react-icons/fc";
import { Footerone } from "../Footer/Footern";
import { Navbarcom } from "../Navbar/Navbar";


function Singletv() {
  const { id } = useParams();
  const [item, setItem] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/tvseries/${id}/`)
      .then((response) => {
        setItem(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data", error);
      });
  }, [id]);

  if (loading) {
    return (
      <div className="container text-center">
        <Spinner animation="border" variant="primary" />
      </div>
    );
  }

  return (
    <>
    <Navbarcom/>
    <div
      className="background-image"
      style={{ backgroundImage: `url("${item.photo}")` }}
    >
      <div className="background-layer">
        <Container className="bg-dark p-5 mt-2" style={{ color: "#D9E3F0" }}>
          <Row className="" bg="dark" data-bs-theme="dark">
            <Col xxl={2} lg={3} md={4}>
              <img src={item.photo} />
            </Col>
            <Col xxl={10} lg={9} md={8}>
              <Row style={{ fontSize: "30px" }}>
                <strong>{item.name}</strong>
              </Row>
              <hr></hr>
              {/* <div className="d-flex">
                {item.item.map((item) => (
                  <div
                    style={{
                      marginRight: "10px",
                      fontSize: "15px",
                      fontWeight: "bold",
                    }}
                    key={item.id}
                  >
                    {item.name}
                  </div>
                ))}
              </div> */}
              </Col>
          </Row>
        </Container>
      </div>
    </div>
    <Footerone/>
    </>
  );
}

export default Singletv;
