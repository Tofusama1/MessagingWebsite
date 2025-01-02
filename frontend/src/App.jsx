import { useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState([])

  useEffect(() => {
    async function fetchData(){
      console.log(import.meta.env.VITE_API_URL)
      try{
        const response = await fetch(`${import.meta.env.VITE_API_URL}posts/`, {
          method: 'GET',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
          },
          mode: 'cors',
        });
        
        if (!response.ok){
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const result = await response.json();
        console.log(result)
        setData(result);
      } catch (error){
        console.log('Error fetching data:', error);
      }
    }
    fetchData();
  }, []);

  return (
    <>
    hello world
    </>
  )
}

export default App