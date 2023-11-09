import React from "react";
import './Footer.css';
import facebook from '../assets/facebook.png';
import linkedin from '../assets/linkedin.png';
import instagrame from '../assets/instagrame.png';
import twitter from '../assets/twitter.png';

export const Footerone=()=>{
  return(
    <div className="footer">
      <div className="sb_footer section_padding">
        <div className="sb_footer-links">
          <div className="sb_footer-links_div">
            <h4>For Business</h4>
            <a href="/employer">
              <p>Employer</p>
            </a>
            <a href="/healthplan">
              <p>Health Plan</p>
            </a>
            <a href="/individual">
              <p>Individual</p>
            </a>
          </div>
          <div className="sb_footer-links_div">
            <h4>Resources</h4>
            <a href="/resource">
              <p>Resource center</p>
            </a>
            <a href="/resource">
              <p>Testimonials</p>
            </a>
            <a href="/resource">
              <p>STV</p>
            </a>
          </div>
          <div className="sb_footer-links_div">
            <h4>Partners</h4>
            <a href="/employer">
              <p>Swing Tech</p>
            </a>
          </div>
          <div className="sb_footer-links_div">
            <h4>Company</h4>
            <a href="/employer">
              <p>About</p>
            </a>
            <a href="/employer">
              <p>Press</p>
            </a>
            <a href="/employer">
              <p>Career</p>
            </a>
            <a href="/employer">
              <p>Contact</p>
            </a>
          </div>
          <div className="sb_footer-links_div">
            <h4>Coming soon on</h4>
            <div className="sacialmedia">
              <p><img src={facebook} alt="/" /></p>
              <p><img src={twitter} alt="/" /></p>
              <p><img src={linkedin} alt="/" /></p>
              <p><img src={instagrame} alt="/" /></p>
            </div>
          </div>
        </div>
        <hr className="sb_hr"></hr>
        <div className="sb_footer-below">
          <div className="sb_footer-copyright">
            <p>
              @{new Date().getFullYear()} CodeInn. All right reserved.
            </p>
          </div>
          <div className="sb_footer-below-links">
            <a href="/terms"><div><p>Terms & Conditions</p></div></a>
            <a href="/privacy"><div><p>Privacy</p></div></a>
            <a href="/security"><div><p>Security</p></div></a>
            <a href="/cookies"><div><p>Cookies Declaration</p></div></a>
          </div>
        </div>
      </div>
    </div>
  )
}


