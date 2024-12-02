function gratis(){
    const gratis_btn = document.getElementById("gratis");
    gratis_btn.classList.add("active");
    const premium_btn = document.getElementById("premium");
    premium_btn.classList.remove("active");
    const all_btn = document.getElementById("all"); 
    all_btn.classList.remove("active");
}