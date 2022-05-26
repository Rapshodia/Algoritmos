const reverse = (palabra) =>{
    const newPalabra = palabra.split('').reverse().join('');
    return newPalabra;
}
console.log(reverse('hola'));
