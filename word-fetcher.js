// ==UserScript==
// @name         Duolingo words gatherer
// @namespace    github
// @version      0.1
// @description  It exports your Duolingo word page into a txt so you can use it in Anki
// @author       @Parnstermia
// @match        www.duolingo.com/words
// @copyright    none
// @grant        none
// @require      http://code.jquery.com/jquery-latest.js
// @require     https://raw.githubusercontent.com/eligrey/FileSaver.js/master/FileSaver.js
// ==/UserScript==
//Button
var input=document.createElement("input");
input.type="button";
input.value="Fetch Words";
input.onclick = showAlert;
input.setAttribute("style", "font-size:18px;position:absolute;top:80px;right:60px;");
document.body.appendChild(input);

//Fetching
function showAlert()
{
    var Rows = [];
    var Texts = [];
    var Words = [];
    //Takes the rows from the Matrix
    Rows = document.getElementsByClassName("word-cell");

    //We store just the hidden classes (store words)
    for(var i = 0; i < Rows.length ; i++){
        Texts.push(Rows[i].getElementsByClassName("hidden"));
    }
    //Storing barebone words without HTML
    for(i = 0; i < Texts.length;i++){
        Words.push(Texts[i][0].innerText);
        Words.push("\n");
    }
    //Saving Words into a File
    var file = new Blob(Words, {type: "text/plain;charset=utf-8"});
    saveAs(file, "Words.txt");
    document.body.removeChild(input); //remove button
}
