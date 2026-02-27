import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [patients, setPatients] = useState([]);
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [gender, setGender] = useState("");

  const API = "http://localhost:5000";

  useEffect(() => {
    fetchPatients();
  }, []);

  const fetchPatients = async () => {
    const res = await axios.get(`${API}/patients`);
    setPatients(res.data);
  };

  const addPatient = async () => {
    await axios.post(`${API}/patients`, {
      name,
      age,
      gender,
    });

    setName("");
    setAge("");
    setGender("");
    fetchPatients();
  };

  const deletePatient = async (id) => {
    await axios.delete(`${API}/patients/${id}`);
    fetchPatients();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>🏥 Hospital Management System</h2>

      <h3>Add Patient</h3>
      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        placeholder="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
      />
      <input
        placeholder="Gender"
        value={gender}
        onChange={(e) => setGender(e.target.value)}
      />
      <button onClick={addPatient}>Add</button>

      <h3>Patient List</h3>
      <ul>
        {patients.map((p) => (
          <li key={p.patient_id}>
            {p.name} ({p.age}, {p.gender})
            <button onClick={() => deletePatient(p.patient_id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;