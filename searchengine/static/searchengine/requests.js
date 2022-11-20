
/*Funktion*/
function sendSearchRequest() {
    /* referenzen zum input*/
    let abflughafen = document.querySelector("#abflughafen").value;
    let anzahlErwachsene = document.querySelector("#anzahlErwachsene").value;
    let anzahlKinder = document.querySelector("#anzahlKinder").value;
    let begin = document.querySelector("#begin").value;
    let ende = document.querySelector("#ende").value;
    let pension = document.querySelector("#pension").value;
    let oceanblick = document.querySelector("#oceanblick").value;
    let raumtyp = document.querySelector("#raumtyp").value;

    let values = new Map();
    values.set('abflughafen', abflughafen);
    values.set('anzahlErwachsene', anzahlErwachsene);
    values.set('anzahlKinder', anzahlKinder);
    values.set('begin', begin);
    values.set('ende', ende);
    values.set('pension', pension);
    values.set('oceanblick', oceanblick);
    values.set('raumtyp', raumtyp);

    let url = "/searchengine/results/";
    for (let [name, value] of values) {
        if (value != null && value != '') {
            url = url + name + "=" + value + "&";
        }
    }
    window.open(url)
}

function sendStart() {
    let abflughafen = document.querySelector('#abflughafen').value;
    let url ="/searchengine/results/-"; 
    console.log(abflughafen);
    if (abflughafen != null && abflughafen != ''){
        url = "/searchengine/results/abflughafen="+abflughafen;
    }

    window.open(url);
}

