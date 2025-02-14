import { Link } from "react-router-dom";
import { FaArrowRight } from "react-icons/fa";

const ServiceCard = ({ heading, description, whereToGo, imageUrl }) => {
  return (
    <div className="bg-blue-100 bgcard1 w-full max-h-[800px] cursor-pointer p-10 bg-no-repeat transition-all duration-200 hover:scale-105 z-50">
      <div className="h-[200px] w-full flex justify-center items-center">
        <img
          src={imageUrl}
          alt={imageUrl}
          className="bg-lightBlue rounded-full h-full"
        />
      </div>
      <h3 className="font-inherit text-lg font-bold pt-4">{heading}</h3>
      <p className="font-inherit py-3 text-grayText leading-normal">
        {description}
      </p>
      {/* <!-- hyperlink --> */}
      <div className="flex items-center flex-row cursor-pointer group">
        <Link
          to={whereToGo}
          target="blank"
          className="font-inherit font-bold text-lightBlue500 group-hover:text-lightBlue transition-all duration-300 flex gap-1 items-baseline hover:text-richblack-400 bg-white px-3 py-1 rounded-lg"
        >
          <p>Know More</p>
          <FaArrowRight size={13} className="group-hover:translate-x-1 transition-transform duration-300" />
        </Link>
      </div>
    </div>
  );
};

export default ServiceCard;
