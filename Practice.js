//ordenar numeros que te pasan por parametro los pares e impares ademas en orden ascendente y descendente

const orderedNumber = (number) => {
    
    const numberArray = number.toString().split("").map(item => parseInt(item));
    
    const odds = numberArray.filter(item => item % 2 !==0).sort((a,b) => b - a );
    const evens = numberArray.filter(item => item % 2 ===0).sort((a,b) => a - b );
    console.log(odds, evens);
    return null;
  }
  
  console.log(orderedNumber(540613788));
