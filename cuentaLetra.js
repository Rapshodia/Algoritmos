// Funcion que retorne la cantidad de cada palabra de una frase

const cuentaPalabra = (palabra) =>{
    palabra = [...palabra]
  	cantidad = {}
    palabra.forEach(e => {
        cantidad[e] = !cantidad[e] ? 1 : cantidad[e] += 1
        
    });
    return cantidad
}
console.table(cuentaPalabra("hola que tal"))