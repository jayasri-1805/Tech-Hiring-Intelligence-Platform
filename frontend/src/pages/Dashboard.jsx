import "./Dashboard.css";
import KPICards from "../components/KPI/KPICards";

export default function Dashboard() {

    return (

        <div className="dashboard">

            {/* Hero Banner */}

            <div className="heroBanner">

                <div>

                    <h1>👋 Welcome Back, Jaya Sri</h1>

                    <p>
                        Monitor hiring trends, salary insights and AI predictions
                        from one place.
                    </p>

                </div>

                <button className="heroButton">
                    View Report
                </button>

            </div>

            {/* KPI Cards */}

            <KPICards />

            {/* Charts */}

            <div className="placeholderGrid">

                <div className="chartPlaceholder">

                    📈 Salary Distribution Chart

                </div>

                <div className="chartPlaceholder">

                    🌍 Jobs by Country

                </div>

            </div>

        </div>

    );

}