document.getElementById("selectvalue")
    .onchange = function () {
        var b = {
            1: "moscow",
            2: "saintPetersburg",
            3: "maldives"
        }, c = this.value,
            a;
        for (a in b) document.getElementById(b[a])
            .style.display = 0 == c || c == a ? "block" : "none"
};

console.log("fffffff")