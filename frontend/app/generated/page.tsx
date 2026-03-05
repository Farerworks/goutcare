import React, { useEffect, useState } from 'react';
import { getHealth } from './api';

const HomePage: React.FC = () => {
  const [status, setStatus] = useState<string | null>(null);

  useEffect(() => {
    const fetchHealth = async () => {
      try {
        const result = await getHealth();
        setStatus(result.status);
      } catch (error) {
        setStatus('error');
      }
    };

    fetchHealth();
  }, []);

  return (
    <div>
      <h1>Health Check</h1>
      {status === 'ok' && <p>The backend is healthy.</p>}
      {status === 'error' && <p>There was an error reaching the backend.</p>}
    </div>
  );
};

export default HomePage;