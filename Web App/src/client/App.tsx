import "./App.css";
import { useEffect, useState } from "react";
import React from 'react'
import IndexCard from "./custom/components/IndexCard";
import { Card, CardTitle, CardHeader, CardContent } from "@/components/ui/card";


interface RiskDataItem {
  date: string;
  risk_index: number;
}

function App() {
  const getCardColor = (currentIndex: number, prevIndex: number| null) => {
    //let tuple: [number, string] = [0,'w-full max-w-4xl mx-auto bg-gradient-to-b from-blue-600 to-blue-800 text-white'];
    let tuple: [number, string] = [0,'bg-gray-50'];

    if (prevIndex === null) {
      return tuple;
    } else if (currentIndex === prevIndex) {
      return tuple;
    }
      else if (currentIndex > prevIndex) {
        const num = 600;
        const coloval = 'w-full max-w-4xl mx-auto bg-gradient-to-b from-red-' + num.toString() + ' to-purple-800 text-white';
        console.log(coloval);
        tuple = [1,coloval]; 
        return tuple;
    } else {
      tuple= [2,'w-full max-w-4xl mx-auto bg-gradient-to-b from-blue-600 to-blue-800 text-white'];;
      return tuple;
    }
  }
  const getPrevIndex = (index: number) => {
    if (index > 0) {
      return riskData[index - 1].risk_index;
    }
    return null;
    
  }

  
  const [riskData, setRiskData] = useState<RiskDataItem[]>([]);
  // const arrayItems = riskData.map((item,index) => (
  //   <IndexCard date={item.date} curindex={item.risk_index} cardColor={getCardColor(item.risk_index, getPrevIndex(index))}/>
  // ));
  const arrayItems = riskData.map((item,index) => {
    const prevIndex = index > 0 ? riskData[index - 1].risk_index : null;
    const [delta,cardColor] = (getCardColor(item.risk_index, prevIndex));
    return <IndexCard key={item.date} date={item.date} curindex={item.risk_index} cardColor={cardColor} delta={delta}/>
  });
  const highestIndex = Math.max(...riskData.map((item) => item.risk_index));
  
  
  
  
  useEffect(() => {
    fetch('/hello')
    .then(res => res.json())
    .then(data => setRiskData(data))
  },[])

  return (
    
    <>
      {riskData.length > 0 && 
      
      <Card className="w-full max-w-[90vw] mx-auto bg-white shadow-lg">
        <CardHeader>
          <CardTitle className="text-[4vw] sm:text-[3vw] md:text-[2vw] font-bold text-white">Risk Index</CardTitle>
        </CardHeader>
        <CardContent className='p-[2vh] sm:p-[3vh]'>
          <div className="mb-[3vh]">
            <div className="text-[6vw] sm:text-[4vw] md:text-[3vw] font-bold mb-[1vh] text-blue-600">Max Risk Index: {highestIndex}</div>
            <div className="text-sm">Highest index value for the next two weeks</div>
          </div>        
        <div className="grid gap-[2vh]">{arrayItems}</div>
        </CardContent>
      </Card>
      
      }
   
    </>
    
  )
}

export default App
