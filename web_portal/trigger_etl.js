import React, { useState } from 'react';

const TriggerETL = () => {
  const [status, setStatus] = useState('');

  const triggerETL = async () => {
    try {
      const response = await fetch('http://localhost:5000/trigger_etl');
      const data = await response.json();
      setStatus(data.status);
    } catch (error) {
      setStatus('Error triggering ETL job');
    }
  };

  return (
    <div>
      <button onClick={triggerETL}>Trigger ETL Job</button>
      <p>Status: {status}</p>
    </div>
  );
};

export default TriggerETL;
