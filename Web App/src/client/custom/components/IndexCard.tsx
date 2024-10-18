import {Card, CardContent, CardHeader, CardTitle} from "@/components/ui/card"
import {ChevronDown, ChevronUp,Minus, ArrowUp, ArrowDown} from "lucide-react"


const IndexCard = ({ date, curindex, cardColor, delta}: { date: string, curindex: number, cardColor: string, delta: number}) => {
    
   const getDeltaIcon = (delta: number) => {
       switch(delta) {
           case 0:
               return <Minus className="w-[3vw] h-[3vw] sm:w-[2vw] sm:h-[2vw] md:w-[1.5vw] md:h-[1.5vw] mr-[1vw]"/>
           case 1:
               return <ArrowUp className="w-[3vw] h-[3vw] sm:w-[2vw] sm:h-[2vw] md:w-[1.5vw] md:h-[1.5vw] mr-[1vw]"/>
           case 2:
               return <ArrowDown className="w-[3vw] h-[3vw] sm:w-[2vw] sm:h-[2vw] md:w-[1.5vw] md:h-[1.5vw] mr-[1vw]"/>
       }
   } 
    return(
        <Card key={date} className={`w-full ${cardColor} border border-gray-200`}>
            <CardContent className="p-[2vh]">
                <div className="flex justify-between items-center mb-[1vh]">
                    <div className="font-semibold text-[2.5vw] sm:text-[2vw] md:text-[1.5vw] text-gray-700">{date}</div>
                </div>
                <div className="flex justify-between items-center mb-[1vh]">
                    <div className="txt-3xl text-left"> Index: {curindex}</div>
                    <div >
                        {getDeltaIcon(delta)} 
                    </div>
                    
                </div>

            </CardContent>
        </Card>
    )
}

export default IndexCard
// const Card = ({ date, index }: { date: string, index: number}) => {
//     return(
//     <div className="index-card">
//         <div className="index-card-date">{date}</div>
//         <div className="index-card-index">{index}</div>
//     </div>
// )
// }

// export default Card

