const operations = (a, b, callback)=>{
    return setTimeout(()=>{
        callback(a, b)
    }, 2000) 
}
operations(5, 6, (a, b) => console.log(a + b) )
operations(5, 6, (a, b) => a * b )
operations(5, 6, (a, b) => a - b )