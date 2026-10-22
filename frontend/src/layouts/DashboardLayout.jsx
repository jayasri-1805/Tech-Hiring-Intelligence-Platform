import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import Dashboard from "../pages/Dashboard";

import "./DashboardLayout.css";

export default function DashboardLayout() {

    return (

        <div className="layout">

            <Sidebar />

            <div className="content">

                <Navbar />

                <Dashboard />

            </div>

        </div>

    )

}