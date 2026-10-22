import "./Sidebar.css";
import {
    LayoutDashboard,
    BarChart3,
    BrainCircuit,
    Activity,
    Globe,
    Briefcase,
    Settings
} from "lucide-react";

const menu = [
    { icon: <LayoutDashboard size={20} />, label: "Dashboard" },
    { icon: <BrainCircuit size={20} />, label: "Salary Prediction" },
    { icon: <BarChart3 size={20} />, label: "Analytics" },
    { icon: <Globe size={20} />, label: "Market Insights" },
    { icon: <Briefcase size={20} />, label: "Companies" },
    { icon: <Activity size={20} />, label: "API Status" },
    { icon: <Settings size={20} />, label: "Settings" }
];

export default function Sidebar() {

    return (

        <aside className="sidebar">

            <div className="logo">

                <div className="logoIcon">
                    📊
                </div>

                <div>

                    <h2>THIP</h2>

                    <span>
                        AI Analytics
                    </span>

                </div>

            </div>

            <div className="menu">

                {menu.map((item, index) => (

                    <div
                        className={`menuItem ${index === 0 ? "active" : ""}`}
                        key={index}
                    >

                        {item.icon}

                        <span>{item.label}</span>

                    </div>

                ))}

            </div>

            <div className="upgradeCard">

                <h3>🚀 AI Insights</h3>

                <p>
                    ML Powered Hiring Analytics
                </p>

                <button>
                    Explore
                </button>

            </div>

        </aside>

    );

}