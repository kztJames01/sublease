import Authentication from "@/components/authentication";
import Footer from "@/components/footer";
import Navbar from "@/components/navbar";

const SignUpPage = () => {
    return (
        <div>
            <Navbar />
            <Authentication type="signup" />
            <Footer />
        </div>
    );
};

export default SignUpPage;
