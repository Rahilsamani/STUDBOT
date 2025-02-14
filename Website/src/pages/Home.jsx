import Footer from "../components/common/Footer";
import CTAButton from "../components/core/HomePage/Button";
import HighlightText from "../components/core/HomePage/HighlightText";
import ChatBot1Image from "../assets/Images/Chat bot-amico.svg";
import ChatBot2Image from "../assets/Images/Chat bot-cuate.svg";
import ChatBot3Image from "../assets/Images/ImageChatbot.png";
import Atom from "../components/common/Atom";

const Home = () => {
  return (
    <div>
      {/*Section1  */}
      <div className="relative mx-auto flex flex-col w-11/12 max-w-maxContent items-center text-white justify-between gap-8">
        {/* Section 1 */}
        <div className="flex flex-col sm:flex-row justify-center items-center mt-10">
          {/* left part */}
          <div className="w-full sm:w-1/2 flex flex-col gap-6">
            <div className="text-4xl font-semibold mt-10">
              Empower Your Future with
              <HighlightText text={" STUDBOT"} />
            </div>

            <div className="w-[95%] text-lg font-bold text-richblack-300">
              Empower your future with STUDBOT's AI-enhanced capabilities,
              driving innovation and efficiency through collaboration. Unlock
              new opportunities and pave the way for a brighter future.
            </div>

            <div className="flex flex-row gap-7 mt-8">
              <CTAButton active={true} linkto={"https://mz5rnpttgzabr83qnu3buf.streamlit.app/"}>
                Explore
              </CTAButton>
            </div>
          </div>

          {/* right part */}
          <div className="mt-5 w-[70%] sm:w-[38%]">
            <img src={ChatBot1Image} alt="" />
          </div>
        </div>

        {/* Section 2 */}
        <div className="flex flex-col-reverse sm:flex-row justify-center items-center mt-10 gap-10 sm:gap-20">
          {/* left part */}
          <div className="w-[80%] sm:w-[38%]">
            <img src={ChatBot2Image} alt="" />
          </div>

          {/* left part */}
          <div className="w-full sm:w-1/2 flex flex-col gap-6">
            <div className="text-4xl font-semibold mt-10">
              Knowledge Extraction Made Easy with
              <HighlightText text={" ChatPDF"} />
            </div>

            <div className="w-[90%] text-lg font-bold text-richblack-300">
              Say goodbye to tedious manual document analysis. With ChatPDF,
              simply upload your PDF files and ask questions directly. Our
              AI-powered system extracts key information, enabling you to
              effortlessly glean insights and make informed decisions in record
              time.
            </div>

            <div className="flex flex-row gap-7 mt-8">
              <CTAButton active={true} linkto={"https://docchat-aehjsonnxwib6hxm9kmtic.streamlit.app/"}>
                Explore
              </CTAButton>
            </div>
          </div>
        </div>

        {/* Section 3 */}
        <div className="flex flex-col sm:flex-row justify-center items-center mt-10">
          {/* left part */}
          <div className="w-full sm:w-1/2 flex flex-col gap-6">
            <div className="text-4xl font-semibold mt-10">
              Visual Intelligence Unleashed with
              <HighlightText text={" ImageBot"} />
            </div>

            <div className="w-[90%] text-lg font-bold text-richblack-300">
              Curious about an object or landmark? Let ImageBot be your guide.
              Upload any image, and our advanced image recognition technology
              will identify it for you. Explore the world around you with
              confidence, all with just a click.
            </div>

            <div className="flex flex-row gap-7 mt-8">
              <CTAButton active={true} linkto={"http://localhost:8501/"}>
                Explore
              </CTAButton>
            </div>
          </div>

          {/* right part */}
          <div className="mt-5 w-[70%] sm:w-[38%]">
            <img src={ChatBot3Image} alt="" />
          </div>
        </div>

        {/* Section 4 */}
        <div className="flex flex-col-reverse md:flex-row justify-center items-center mt-10 mb-44 gap-20">
          {/* left part */}
          <Atom />

          {/* left part */}
          <div className="w-full sm:w-11/12 md:w-1/2 flex flex-col gap-6">
            <div className="text-3xl lg:text-4xl font-semibold mt-10">
              Accelerate Your Career with your Personalized
              <HighlightText text={" Intern"} />
            </div>

            <div className="w-[95%] text-md lg:text-lg font-bold text-richblack-300">
              In today's fast-paced world, time is precious. At STUDBOT, we
              maximize efficiency with personalized assistance, freeing you from
              routine tasks. Let our bot handle the small stuff while you focus
              on propelling your career forward. Save time, save money, and
              achieve your goals faster with STUDBOT.
            </div>

            <div className="flex flex-row gap-7 mt-8">
              <CTAButton active={true} linkto={"/signup"}>
                Explore
              </CTAButton>
            </div>
          </div>
        </div>
      </div>

      {/*Footer */}
      <Footer />
    </div>
  );
};

export default Home;
