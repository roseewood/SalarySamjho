function SalaryBreakdown({ data }) {
  if (!data) return null;

  return (
    <div>
      {Object.entries(data).map(([key, value]) => (
        <p key={key}><b>{key}</b>: ₹{value}</p>
      ))}
    </div>
  );
}

export default SalaryBreakdown;