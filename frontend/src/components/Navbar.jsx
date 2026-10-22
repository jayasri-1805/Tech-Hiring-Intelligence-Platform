import "./Navbar.css";
import {
    Bell,
    Search,
    Moon,
    UserCircle2
} from "lucide-react";

export default function Navbar() {

    return (

        <div className="navbar">

            <div className="searchBox">

                <Search size={18} />

                <input
                    placeholder="Search jobs, companies..."
                />

            </div>

            <div className="navRight">

                <Moon />

                <Bell />

                <div className="avatar">

                    <UserCircle2 size={34} />

                    <div>

                        <h4>Jaya Sri</h4>

                        <span>Data Analyst</span>

                    </div>

                </div>

            </div>

        </div>

    )

}