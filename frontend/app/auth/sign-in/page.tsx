import Authentication from "@/components/authentication";
import Footer from "@/components/footer";
import Navbar from "@/components/navbar";

const SignInPage = () => {
    return (
        <div>
            <Navbar />
            <Authentication type="login" />
            <Footer />
        </div>
    );
};

export default SignInPage;