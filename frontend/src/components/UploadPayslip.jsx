import api from "../api/axios";

function UploadPayslip({ setData }) {
  const upload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const res = await api.post("/payslip/upload", formData);
    setData(res.data.components);
  };

  return <input type="file" onChange={upload} />;
}

export default UploadPayslip;