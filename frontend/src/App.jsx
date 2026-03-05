import { useState } from "react";
import UploadPayslip from "./components/UploadPayslip";
import SalaryBreakdown from "./components/SalaryBreakdown";

function App() {
  const [data, setData] = useState(null);

  return (
    <div>
      <h1>PayGyaan – Explain My Payslip</h1>
      <UploadPayslip setData={setData} />
      <SalaryBreakdown data={data} />
    </div>
  );
}

export default App;