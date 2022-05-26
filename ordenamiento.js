

//Object.freeze(p); //inmutabilidad de un objeto

//ordenar las ciudades que mas veces se repiten de mayor a menor
const citiesList = [
    "Santiago",
    "pto montt",
    "buenos aires",
    "sao paulo",
    "madrid",
    "barcelona",
    "santander",
    "san jose",
    "villarrica",
    "santo domingo",
    "padre hurtado",
    "maipu",
    "cerro navia",
    "san joaquin",
    "talagante",
    "sao paulo",
    "talagante",
    "barcelona",
    "sao paulo",
    "madrid"
];

function foo(numCities){
    const cities = {}
    citiesList.forEach(city => {
        
        cities[city] = !cities[city] ? 1 : cities[city] += 1
    });

    return Object.keys(cities).map(city => ({name: city, times: cities[city]}))
    .sort((a, b) => b.times -a.times ).slice(0, numCities).map(city => city.name);
}


console.log(foo(5));