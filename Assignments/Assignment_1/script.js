//Saketh Lakshmanan Sathiskumar
//UCID: sl778 
//Date submitted: 02/08/2023 

// first button to hide
document.getElementById("hide").addEventListener("click", function()
{
    document.querySelector(".container").style.display = "none";
});

// second button to show
document.getElementById("show").addEventListener("click", function()
{
    document.querySelector(".container").style.display = "block";
    document.querySelector(".container").style.textAlign = "center";
});