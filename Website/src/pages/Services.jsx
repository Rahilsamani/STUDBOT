import ServiceCard from "../components/core/ServicePage/ServiceCard";
import Service1 from "../assets/Images/service1.png";
import Service2 from "../assets/Images/service2.png";
import Service3 from "../assets/Images/ImageChatbot.png";
import Service6 from "../assets/Images/service6.png";
import Service7 from "../assets/Images/service7.png";
import Footer from "../components/common/Footer";

const Services = () => {
  const cardsData = [
    {
      heading: "Conversational AI Assistance",
      description:
        "Engage in natural conversations and seek instant assistance with our Chatbot feature, designed to provide helpful responses and guidance similar to ChatGPT, tailored to your needs and queries.",
      whereToGo: "https://mz5rnpttgzabr83qnu3buf.streamlit.app/",
      imageUrl: Service1,
    },
    {
      heading: "PDF Query Assistance",
      description:
        "Simplify your document analysis process with ChatPDF, where you can upload PDF files and ask questions related to the content, allowing for quick extraction of key information and insights.",
      whereToGo: "https://docchat-aehjsonnxwib6hxm9kmtic.streamlit.app/",
      imageUrl: Service2,
    },
    {
      heading: "Visual Intelligence",
      description:
        "Explore the world through images with our Image Identification Chatbot, capable of recognizing and providing details about various objects and landmarks, enhancing your visual understanding",
      whereToGo: "http://localhost:8501/",
      imageUrl: Service3,
    },
    {
      heading: "Smart Expense Management",
      description:
        "Manage your finances effortlessly with our Expense Tracking service. Monitor expenses and gain insights into your spending habits. Perfect for businesses, freelancers, and individuals alike.",
      whereToGo:
        "https://student-expense-tracker-eihchlnimamngnzl7zqmfj.streamlit.app/",
      imageUrl: Service6,
    },
    {
      heading: "Generate Youtube Script",
      description:
        "Convert YouTube transcripts into detailed notes effortlessly. Perfect for studying, research, or reference, our tool streamlines your note-taking process.",
      whereToGo: "https://ytranscriber-fxdybzxkxb6ahmemvmkzx6.streamlit.app/",
      imageUrl: Service7,
    },
  ];

  return (
    <div className="bg-richblack-800">
      <section className="relative pb-32">
        <div className="max-w-[1080px] w-11/12 mx-auto relative pt-4 mt-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 w-full gap-x-4 gap-y-10 z-[100] relative">
            {cardsData.map((card, index) => (
              <ServiceCard
                key={index}
                heading={card.heading}
                description={card.description}
                whereToGo={card.whereToGo}
                imageUrl={card.imageUrl}
              />
            ))}
          </div>
        </div>
      </section>
      <Footer />
    </div>
  );
};

export default Services;
