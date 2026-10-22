import "./KPICards.css";
import {
    Briefcase,
    DollarSign,
    Globe,
    TrendingUp
} from "lucide-react";

const cards = [
    {
        title: "Total Jobs",
        value: "50,000",
        change: "+12%",
        icon: Briefcase,
        color: "#5B5FEF"
    },
    {
        title: "Average Salary",
        value: "$110K",
        change: "+8%",
        icon: DollarSign,
        color: "#10B981"
    },
    {
        title: "Countries",
        value: "42",
        change: "+5",
        icon: Globe,
        color: "#F59E0B"
    },
    {
        title: "Hiring Growth",
        value: "18%",
        change: "+3%",
        icon: TrendingUp,
        color: "#EC4899"
    }
];

export default function KPICards() {

    return (

        <div className="kpiGrid">

            {cards.map((card, index) => {

                const Icon = card.icon;

                return (

                    <div className="kpiCard" key={index}>

                        <div className="top">

                            <div
                                className="icon"
                                style={{
                                    background: card.color
                                }}
                            >

                                <Icon size={22} />

                            </div>

                            <span>{card.change}</span>

                        </div>

                        <h4>{card.title}</h4>

                        <h2>{card.value}</h2>

                    </div>

                );

            })}

        </div>

    );

}