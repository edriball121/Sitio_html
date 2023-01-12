//introduccion
//https://www.w3schools.com/js/js_whereto.asp
//document.getElementById("holaMundo").innerHTML = "Este titulo fue afectado por javascript"
//document.getElementById("descripcion").style.fontSize = "55px";
//document.getElementById("descripcion").style.display = "none";


//Tipos de salida de JS
//https://www.w3schools.com/js/js_output.asp
//document.getElementById("descripcion").innerHTML = "Salida de prueba";
//document.write("Prueba");
//window.alert("Estas usando JavaScript");
//console.log("prueba JS ok");
//window.print("prueba");

//declaracion de variables 
//https://www.w3schools.com/js/js_statements.asp

/*let x,y,z;//declaracion de las variables
x = 5;//asignacion de valor a la variable
y = 6;
z = x + y;
console.log(z);

//del mismo modo en una linea

a = 1; b = 2; c = 3;
console.log(a, b, c);*/

//longitud de la linea
//para mejor legibilidad del codigo es comun no usar mas de 80 caracteres por lines

//document.getElementById("descripcion").innerHTML = 
//"Prueba salto de linea";

//bloques de codigo

/*function firtFuncion(){
    document.getElementById("descripcion").innerHTML = "funcion bloque";
    document.getElementById("holaMundo").innerHTML = "Titulo bloque funcional";
    window.alert(firtFuncion)
}*/

//Realizar una función que reciba por parámetro dicho arreglo y retorne un nuevo array con los objetos
// cuyo año de creación sea mayor a 1800.
let fechaCreacion = 1800;
const firstArrary = [
    {
        nombre: "Mona Lisa",
        creador: "Leonardo Da Vinci",
        creacion: 1503
    },
    {
        nombre: "La ultima cena",
        creador: "Leonardo Da Vinci",
        creacion: 1495
    },
    {
        nombre: "La noche estrellada",
        creador: "Vincent van Gogh",
        creacion: 1889
    },
    {
        nombre: "El grito",
        creador: "Edvard Munch",
        creacion: 1893
    },
    {
        nombre: "Trigal con cuervos",
        creador: "Vincent van Gogh",
        creacion: 1890
    },
    {
        nombre: "Maria Magdalena",
        creador: "Leonardo Da Vinci",
        creacion: 1495
    }

];
console.log(firstArrary);


for (let i = 0; i < firstArrary.length; i++) {
    console.log(firstArrary[i].creacion);
    if (firstArrary[i].creacion = fechaCreacion){
        console.log("Prueba")
    }
}




