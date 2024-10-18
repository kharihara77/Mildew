import express from "express";
import dayjs from "dayjs";
import ViteExpress from "vite-express";
import { spawn } from 'node:child_process';
import { R } from "node_modules/tsx/dist/types-Cxp8y2TL.js";
const app = express();


interface RiskDataItem {
  risk_index: number;
  date: string;
}
function changeDateFormat(date: string) {
  const formattedDate = dayjs(date, 'YYYY-MM-DD');
  console.log(formattedDate.day()); 

 
}

app.get("/hello", (_, res) => {
  const pythonProcess = spawn('/Users/karthikharihara/Documents/coding_projects/Mildew/.venv/bin/python', ['/Users/karthikharihara/Documents/coding_projects/Mildew/main.py']);
  let dataToSend:string = "";

  pythonProcess.stdout.on('data',  function (data: any)   {
    console.log('Pipe data from python script ...');
    dataToSend += data.toString();
    
  });

  pythonProcess.on('close', (code: any) => {
    console.log(`child process close all stdio with code ${code}`);
    
    const riskData: RiskDataItem[] = JSON.parse(dataToSend).map((item: [number, string]) => ({
      risk_index: Math.round(item[0]), // Convert to integer
      date: item[1] // Keep as string
    }));

    res.send(riskData);
  });

});
ViteExpress.listen(app, 3000, () =>
  console.log("Server is listening on port 3000..."),
);
