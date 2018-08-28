'use strict';
const brojPodrucja=16;
var slide=0;
function definirajPodrucja(index){
    var mojiStilovi = document.getElementById("mojiStilovi");
    if(mojiStilovi!=undefined){
        document.getElementsByTagName('head')[0].removeChild(mojiStilovi);
    }
    var style = document.createElement('style');
    style.type = 'text/css';
    style.setAttribute("id","mojiStilovi");
    document.getElementsByTagName('head')[0].appendChild(style);
    var podrucje;
    var podrucja=Array();
    for(let i=0;i<brojPodrucja;i++){
        style.sheet.insertRule(".p"+i+"{" +
        "background-color: #" + (i%2==0 ? "7d3221" : "692f29") + ";"
        + "grid-column: auto / span " +  (Math.floor(Math.random() * 2) + 1)   + ";" + 
        " grid-row: auto / span " +   (Math.floor(Math.random() * 3) + 1)  + "; "
        + "}",0);
        podrucje = document.createElement("div");
        podrucje.setAttribute("class","podrucje p"+i);
        podrucje.setAttribute("id","p_"+i);
        podrucja.push(podrucje);
    }
    podrucja=shuffle(podrucja);
    let omotac = document.getElementById("omotac");
    while (omotac.firstChild) {
        omotac.removeChild(omotac.firstChild);
    }
    for(let i=0;i<podrucja.length;i++){
        omotac.appendChild(podrucja[i]);
    }
    popuniPodatke(slideovi[index]);
}
definirajPodrucja(0);
function popuniPodatke(podaci){
    for(let i=0;i<podaci.length;i++){
        if(i===0){
            document.getElementById("p_"+i).style.fontWeight="bold";  
            document.getElementById("p_"+i).style.textDecoration="underline";    
        }
        document.getElementById("p_"+i).appendChild(document.createTextNode(podaci[i]));
    }
}
//preuzeto s https://www.w3resource.com/javascript-exercises/javascript-array-exercise-17.php
function shuffle(arra1) {
    var ctr = arra1.length, temp, index;
    while (ctr > 0) {
        index = Math.floor(Math.random() * ctr);
        ctr--;
        temp = arra1[ctr];
        arra1[ctr] = arra1[index];
        arra1[index] = temp;
    }
    return arra1;
}
document.body.addEventListener("keydown", function(e){
    if (e.keyCode===37){
        if (slide===0){
            return false;
        }
        slide--;
        definirajPodrucja(slide);
        return false;
    }
    if (e.keyCode===39){
        if (slide===slideovi.length-1){
            return false;
        }
        slide++;
        definirajPodrucja(slide);
        return false;
    }
}, false);