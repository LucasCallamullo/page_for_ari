(function () {
    const second = 1000,
          minute = second * 60,
          hour = minute * 60,
          day = hour * 24;

    let today = new Date(),
        dd = String(today.getDate()).padStart(2, "0"),
        mm = String(today.getMonth() + 1).padStart(2, "0"),
        yyyy = today.getFullYear(),
        nextYear = yyyy + 1,
        dayMonth = "03/01/",  // Puedes cambiar esta fecha si es necesario
        birthday = dayMonth + yyyy;

    today = mm + "/" + dd + "/" + yyyy;
    if (today > birthday) {
        birthday = dayMonth + nextYear;
    }

    const countDown = new Date(birthday).getTime();
    const x = setInterval(function() {    
        const now = new Date().getTime(),
              distance = countDown - now;

        // Actualizar los valores en el HTML
        document.getElementById("days").innerText = Math.floor(distance / day);
        document.getElementById("hours").innerText = Math.floor((distance % day) / hour);
        document.getElementById("minutes").innerText = Math.floor((distance % hour) / minute);
        document.getElementById("seconds").innerText = Math.floor((distance % minute) / second);

        // Cuando se llega a la fecha de cumpleaños
        if (distance < 0) {
            document.getElementById("headline").innerText = "Holaaa Hermosaaa";
            document.getElementById("countdown").style.display = "none";
            // document.getElementById("content").style.display = "block";
            clearInterval(x); // Detener el intervalo
        }
    }, 1000); // Ejecutar cada segundo
})();


// Todo del cumple ari
(function () {
    const second = 1000,
          minute = second * 60,
          hour = minute * 60,
          day = hour * 24;

    let today = new Date(),
        dd = String(today.getDate()).padStart(2, "0"),
        mm = String(today.getMonth() + 1).padStart(2, "0"),
        yyyy = today.getFullYear(),
        nextYear = yyyy + 1,
        // dayMonth = "01/03/",  // Puedes cambiar esta fecha si es necesario
        dayMonth = "1/1/",  // Puedes cambiar esta fecha si es necesario
        birthday = dayMonth + yyyy;

    today = mm + "/" + dd + "/" + yyyy;
    if (today > birthday) {
        birthday = dayMonth + nextYear;
    }

    const countDown = new Date(birthday).getTime();
    const x = setInterval(function() {    
        const now = new Date().getTime(),
              distance = countDown - now;

        // Actualizar los valores en el HTML
        document.getElementById("days_ari").innerText = Math.floor(distance / day);
        document.getElementById("hours_ari").innerText = Math.floor((distance % day) / hour);
        document.getElementById("minutes_ari").innerText = Math.floor((distance % hour) / minute);
        document.getElementById("seconds_ari").innerText = Math.floor((distance % minute) / second);

        // Cuando se llega a la fecha de cumpleaños
        if (distance < 0) {
            document.getElementById("headline_ari").innerText = "Feliz Cumplee Ari";
            document.getElementById("cumple_ari").style.display = "none";

            // para aparecer los emojis centrados
            const contentAri = document.getElementById("content-ari");
            contentAri.style.display = "flex"; // Cambia el display a flex para centrar los emojis
            contentAri.style.justifyContent = "center"; // Centrado horizontal
            contentAri.style.alignItems = "center"; // Centrado vertical
            clearInterval(x); // Detener el intervalo

            // para aparecer el boton
            const btnAri = document.getElementById("btn-ari");
            btnAri.style.display = "flex"; // Cambia el display a flex para centrar los emojis
            btnAri.style.justifyContent = "center"; // Centrado horizontal
            btnAri.style.alignItems = "center"; // Centrado vertical
        }
    }, 1000); // Ejecutar cada segundo
})();