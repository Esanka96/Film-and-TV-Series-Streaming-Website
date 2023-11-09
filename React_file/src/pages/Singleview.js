import React, { useEffect, useState } from "react";
import { Link, useParams,Outlet } from "react-router-dom";
import axios from "axios";
import Spinner from "react-bootstrap/Spinner";
import { Container, Row, Col, Button, Table,Nav,Navbar,Form } from "react-bootstrap";
import Carousel from "react-multi-carousel";
import { FcStart, FcDownload } from "react-icons/fc";
import { Footerone } from "../Footer/Footern";
import { Navbarcom } from "../Navbar/Navbar";


function Singleview() {
  const { id } = useParams();
  const [item, setItem] = useState({});
  const [loading, setLoading] = useState(true);
  const [downloadOptions, setDownloadOptions] = useState(null);

  const handleDownloadClick = () => {
    setDownloadOptions(
      <Container className="mt-2 d-flex justify-content-center">
        <Table className="text-center table table-borderless">
          <thead>
            <tr>
              <th
                style={{
                  fontSize: "18px",
                  background: "rgba(0, 0, 0, 0.4)",
                  color: "#83aaed",
                }}
              >
                Quality
              </th>
              <th
                style={{
                  fontSize: "18px",
                  background: "rgba(0, 0, 0, 0.4)",
                  color: "#83aaed",
                }}
              >
                Size
              </th>
            </tr>
          </thead>
          <hr></hr>
          <tbody>
            <tr>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                1080p
              </td>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                1.5 GB
              </td>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                <Link className="btn btn-danger">Download</Link>
              </td>
            </tr>
            <hr></hr>
            <tr>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                720p
              </td>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                900 MB
              </td>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                <Link className="btn btn-danger">Download</Link>
              </td>
            </tr>
            <hr></hr>
            <tr>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                480p
              </td>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                700 MB
              </td>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                <Link className="btn btn-danger">Download</Link>
              </td>
            </tr>
          </tbody>
        </Table>
      </Container>
    );
  };

  const handlewatchClick = () => {
    setDownloadOptions(
      <Container className="mt-2 d-flex justify-content-center">
        <Table className="text-center table table-borderless">
          <thead>
            <tr>
              <th
                style={{
                  fontSize: "18px",
                  background: "rgba(0, 0, 0, 0.4)",
                  color: "#83aaed",
                }}
              >
                Quality
              </th>
            </tr>
          </thead>
          <hr></hr>
          <tbody>
            <tr>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                1080p
              </td>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                <Link className="btn btn-success">Movie Link</Link>
              </td>
            </tr>
            <hr></hr>
            <tr>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                720p
              </td>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                <Link className="btn btn-success">Movie Link</Link>
              </td>
            </tr>
            <hr></hr>
            <tr>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                480p
              </td>
              <td style={{ color: "white", background: "rgba(0, 0, 0, 0.4)" }}>
                <Link className="btn btn-success">Movie Link</Link>
              </td>
            </tr>
          </tbody>
        </Table>
      </Container>
    );
  };

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/tasks/${id}/`)
      .then((response) => {
        setItem(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return (
      <div className="container text-center">
        <Spinner animation="border" variant="primary" />
      </div>
    );
  }

  const responsive = {
    superLargeDesktop: {
      breakpoint: { max: 4000, min: 3000 },
      items: 5,
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 5,
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
    <Navbarcom/>
    <div
      className="background-image"
      style={{ backgroundImage: `url("${item.photo}")` }}
    >
      <div className="background-layer">
        <Container className="bg-dark p-5 mt-2" style={{ color: "#D9E3F0" }}>
          <Row className="" bg="dark" data-bs-theme="dark">
            <Col xxl={2} lg={3} md={4}>
              <img src={item.photo} alt={item.name} />
            </Col>
            <Col xxl={10} lg={9} md={8}>
              <Row style={{ fontSize: "30px" }}>
                <strong>{item.name}</strong>
              </Row>
              <hr></hr>
              <div className="d-flex">
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
              </div>

              <Row style={{ fontSize: "15px" }}>
                <div style={{ fontSize: "12px" }}>{item.date}</div>
              </Row>
              <hr></hr>
              {item.persons.map((item) => (
                <h5 style={{ fontSize: "15px" }} key={item.id}>
                  <span style={{ textDecoration: "underline" }}>Director:</span>
                  <span> </span>
                  {item.name}
                </h5>
              ))}
              <h5 style={{ fontSize: "15px", textDecoration: "underline" }}>
                Cast:
              </h5>
              <Row>
                {item.actros.map((item) => (
                  <Col sm={6} md={4} lg={3} xl={2}>
                    <h5 style={{ fontSize: "14px" }} key={item.id}>
                      {item.name}
                    </h5>
                  </Col>
                ))}
              </Row>
            </Col>
          </Row>
        </Container>
        <Container className="mt-3 pb-4 ">
          <Row className="text-center">
            {item.filmnames.map((item) => (
              <h5
                style={{
                  fontSize: "25px",
                  color: "#8ed1fc",
                  textDecoration: "underline",
                }}
                key={item.id}
              >
                {item.name}
              </h5>
            ))}
          </Row>
          <Row className="mb-4 mt-1 px-5 text-center">
            <p
              className="card-text"
              style={{ color: "#dce775", fontSize: "20px" }}
            >
              {item.description}
            </p>
          </Row>
          <div className="mt-3">
            <Carousel responsive={responsive} autoPlay={true} infinite={true}>
              {item.filmphotos.map((item) => (
                <div>
                  <img
                    className="d-block w-40"
                    src={item.photo}
                    alt={`Photo ${item.id}`}
                  />
                </div>
              ))}
            </Carousel>
            ;
          </div>
          <Row className="d-flex justify-content-center mb-4">
            <Col
              className="d-flex justify-content-end mt-2"
              xxl={5}
              xl={5}
              lg={5}
              md={5}
              sm={6}
            >
              <Button
                className="d-flex align-items-center"
                variant="info"
                onClick={handleDownloadClick}
              >
                Download
                <FcDownload style={{ marginLeft: "10px" }} />
              </Button>
            </Col>
            <Col xxl={2} xl={2} lg={2} md={2} sm={0}></Col>
            <Col
              className="d-flex justify-content-start mt-2"
              xxl={5}
              xl={5}
              lg={5}
              md={5}
              sm={6}
            >
              <Button
                className="d-flex align-items-center"
                size="lg"
                variant="warning"
                onClick={handlewatchClick}
              >
                Online Watch <FcStart style={{ marginLeft: "10px" }} />
              </Button>
            </Col>
          </Row>
          {downloadOptions}
        </Container>
      </div>
    </div>
    <Footerone/>
    </>
  );
}

export default Singleview;
