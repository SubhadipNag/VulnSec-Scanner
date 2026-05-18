import { useState } from "react";
import API from "../services/api";

function ScanForm() {

    const [target, setTarget] = useState("");
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    const startScan = async () => {

        if (!target) {
            alert("Please enter target URL");
            return;
        }

        try {

            setLoading(true);

            const response = await API.post("/scan", {
                target
            });

            setResults(response.data);

        } catch (error) {

            console.error(error);

            alert(error.response?.data?.error || "Scan failed");

        } finally {

            setLoading(false);
        }
    };

    return (

        <div className="scan-container">

            <h2>Linux Vulnerability Scanner</h2>

            <input
                type="text"
                placeholder="Enter target URL"
                value={target}
                onChange={(e) => setTarget(e.target.value)}
            />

            <button onClick={startScan}>
                Start Scan
            </button>

            {loading && (
                <p>Scanning Target...</p>
            )}

            {results && (

                <div className="results">

                    <h3>Scan Results</h3>

                    <pre>
                        {JSON.stringify(results, null, 2)}
                    </pre>

                </div>
            )}

            {/* Footer */}

            <footer className="footer">

                <p>
                    -- Made with {"❤️"} by Subhadip Nag
                </p>

            </footer>

        </div>
    );
}

export default ScanForm;
