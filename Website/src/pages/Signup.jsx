import signupImg from "../assets/Images/login.webp";
import Template from "../components/core/Auth/Template";

function Signup() {
  return (
    <Template
      title="Embark on Your Adventure with STUDBOT"
      description1="Discover the thrilling intersection of education and exploration on STUDBOT, "
      description2="where learning evolves into an adventure of innovation and growth."
      image={signupImg}
      formType="signup"
    />
  );
}

export default Signup;
